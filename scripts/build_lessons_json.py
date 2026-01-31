#!/usr/bin/env python
"""
Build lessons.json from markdown lesson files.

Reads lesson markdown files from en/lessons/ and he/lessons/,
parses their metadata and content, and outputs a combined lessons.json.

Usage:
    python scripts/build_lessons_json.py

The output lessons.json is written to the repository root.
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

VERSION = "1.0.0"


def parse_lesson_metadata(content: str, lang: str = "en") -> dict:
    """
    Parse lesson metadata from markdown content.

    Extracts metadata from blockquote format:
    > **Module**: module_X_name
    > **Difficulty**: 1
    > **Duration**: 15-20 minutes

    Also handles Hebrew format:
    > **מודול**: module_X_name
    > **רמת קושי**: 1
    > **משך**: 15-20 דקות
    """
    metadata = {
        "module": None,
        "difficulty": 1,
        "duration": None,
    }

    # Pattern for English
    module_pattern_en = r'>\s*\*\*Module\*\*:\s*(\S+)'
    difficulty_pattern_en = r'>\s*\*\*Difficulty\*\*:\s*(\d+)'
    duration_pattern_en = r'>\s*\*\*Duration\*\*:\s*(.+)'

    # Pattern for Hebrew
    module_pattern_he = r'>\s*\*\*מודול\*\*:\s*(\S+)'
    difficulty_pattern_he = r'>\s*\*\*רמת קושי\*\*:\s*(\d+)'
    duration_pattern_he = r'>\s*\*\*משך\*\*:\s*(.+)'

    # Try English patterns first, then Hebrew
    module_match = re.search(module_pattern_en, content) or re.search(module_pattern_he, content)
    difficulty_match = re.search(difficulty_pattern_en, content) or re.search(difficulty_pattern_he, content)
    duration_match = re.search(duration_pattern_en, content) or re.search(duration_pattern_he, content)

    if module_match:
        metadata["module"] = module_match.group(1)
    if difficulty_match:
        metadata["difficulty"] = int(difficulty_match.group(1))
    if duration_match:
        metadata["duration"] = duration_match.group(1).strip()

    return metadata


def extract_title(content: str) -> str:
    """Extract title from the first H1 heading."""
    match = re.search(r'^#\s+(?:Lesson:\s*|שיעור:\s*)?(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Untitled"


def get_module_order(module_name: str) -> int:
    """Extract order index from module name (e.g., module_0_basics -> 0)."""
    match = re.search(r'module_(\d+)', module_name)
    if match:
        return int(match.group(1))
    return 0


def load_module_config(root: Path) -> dict:
    """Load exercises_config.json for module metadata."""
    config_path = root / "exercises_config.json"
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"modules": {}}


def parse_lesson_file(filepath: Path, config: dict, lang: str) -> dict | None:
    """Parse a single lesson markdown file."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  [ERROR] Reading {filepath}: {e}")
        return None

    # Extract metadata
    metadata = parse_lesson_metadata(content, lang)
    title = extract_title(content)

    if not metadata["module"]:
        print(f"  [WARN] No module found in {filepath.name}, skipping")
        return None

    module_name = metadata["module"]
    module_config = config.get("modules", {}).get(module_name, {})

    # Build source_id from filename
    source_id = filepath.stem  # e.g., "lesson_module_0_basics"

    # Get titles and descriptions from config or derive from content
    if lang == "en":
        lesson_title = title
        title_he = module_config.get("name_he", title)
        description = module_config.get("description_en", "")
        description_he = module_config.get("description_he", "")
    else:
        lesson_title = module_config.get("name_en", title)
        title_he = title
        description = module_config.get("description_en", "")
        description_he = module_config.get("description_he", "")

    return {
        "source_id": source_id,
        "title": lesson_title,
        "title_he": title_he,
        "description": description,
        "description_he": description_he,
        "module": module_name,
        "order_index": get_module_order(module_name),
        "difficulty": metadata["difficulty"],
        "duration": metadata.get("duration"),
        "content_md": content,
        "lang": lang,
    }


def main():
    root = Path(__file__).parent.parent

    # Load module configuration
    config = load_module_config(root)

    # Find lesson directories
    en_lessons_dir = root / "en" / "lessons"
    he_lessons_dir = root / "he" / "lessons"

    lessons = []
    seen_sources = set()

    # Process English lessons (primary)
    if en_lessons_dir.exists():
        print(f"Processing English lessons from {en_lessons_dir}")
        for filepath in sorted(en_lessons_dir.glob("lesson_*.md")):
            lesson = parse_lesson_file(filepath, config, "en")
            if lesson:
                lessons.append(lesson)
                seen_sources.add(lesson["source_id"])
                print(f"  + {lesson['source_id']}: {lesson['title']}")
    else:
        print(f"[WARN] English lessons directory not found: {en_lessons_dir}")

    # Process Hebrew lessons - merge content_md_he if English exists
    he_lessons_map = {}
    if he_lessons_dir.exists():
        print(f"\nProcessing Hebrew lessons from {he_lessons_dir}")
        for filepath in sorted(he_lessons_dir.glob("lesson_*.md")):
            lesson = parse_lesson_file(filepath, config, "he")
            if lesson:
                he_lessons_map[lesson["source_id"]] = lesson
                print(f"  + {lesson['source_id']}: {lesson.get('title_he', lesson['title'])}")

    # Merge Hebrew content into English lessons
    for lesson in lessons:
        source_id = lesson["source_id"]
        if source_id in he_lessons_map:
            he_lesson = he_lessons_map[source_id]
            lesson["content_md_he"] = he_lesson["content_md"]
            # Use Hebrew title from Hebrew file if available
            he_title = extract_title(he_lesson["content_md"])
            if he_title and he_title != "Untitled":
                lesson["title_he"] = he_title

    # Add Hebrew-only lessons (not in English)
    for source_id, he_lesson in he_lessons_map.items():
        if source_id not in seen_sources:
            # Hebrew-only lesson
            he_lesson["content_md_he"] = he_lesson.pop("content_md")
            he_lesson["content_md"] = ""  # No English content
            lessons.append(he_lesson)
            print(f"  + {source_id} (Hebrew only)")

    # Sort by order_index
    lessons.sort(key=lambda x: x["order_index"])

    # Remove internal fields before output
    for lesson in lessons:
        lesson.pop("lang", None)

    # Build output
    output = {
        "version": VERSION,
        "generated_at": datetime.now().isoformat(),
        "lessons": lessons,
    }

    # Write lessons.json
    output_path = root / "lessons.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {output_path}")
    print(f"Total: {len(lessons)} lessons")

    return 0


if __name__ == "__main__":
    sys.exit(main())
