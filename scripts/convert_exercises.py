#!/usr/bin/env python
"""
Convert exercise Python files to per-module JSON format.

Reads configuration from:
- exercises_config.json (modules, exercise types, i18n)
- templates/exercise_types_metadata.json (skills, estimated times, etc.)

Usage:
    python scripts/convert_exercises.py [exercises_dir]
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

VERSION = "3.0.0"


def load_json_file(path: Path) -> dict:
    """Load a JSON file, return empty dict if not found."""
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def extract_title_from_filename(filename: str) -> str:
    """Extract human-readable title from filename.

    exercise_1_hello_world.py -> Hello World
    exercise_2_bug_hunt.py -> Bug Hunt
    """
    name = filename.replace(".py", "")

    # Remove exercise_N_ prefix
    match = re.match(r"exercise_\d+_(.+)", name)
    if match:
        name = match.group(1)

    # Convert underscore to space and title case
    return name.replace("_", " ").title()


def extract_docstring(content: str) -> str:
    """Extract the module docstring from file content."""
    # Match triple-quoted docstring at start
    match = re.match(r'^"""(.*?)"""', content, re.DOTALL)
    if match:
        return match.group(1).strip()

    match = re.match(r"^'''(.*?)'''", content, re.DOTALL)
    if match:
        return match.group(1).strip()

    return ""


def parse_exercise_file(
    filepath: Path,
    module_name: str,
    exercise_type: str,
    module_config: dict,
    type_metadata: dict,
) -> dict:
    """Parse a single exercise file into JSON format."""
    content = filepath.read_text(encoding="utf-8")
    filename = filepath.name

    # Extract title from filename
    title = extract_title_from_filename(filename)

    # Get docstring for description
    docstring = extract_docstring(content)

    # Generate stable ID
    exercise_id = f"{module_name}.{exercise_type}.{filename.replace('.py', '')}"

    # Get module metadata (with fallbacks)
    topic_id = module_config.get("topic_id", "basics.print")
    difficulty = module_config.get("difficulty", 1)
    module_name_en = module_config.get("name_en", module_name.replace("_", " ").title())
    module_name_he = module_config.get("name_he", module_name_en)

    # Get exercise type metadata (with fallbacks)
    type_info = type_metadata.get(exercise_type, {})
    category = type_info.get("category", "free_writing")
    requires_running = type_info.get("requires_running", True)
    estimated_time = type_info.get("estimated_time_minutes", 10)
    skills = type_info.get("skills", [])
    type_name_en = type_info.get("name", exercise_type.replace("_", " ").title())
    type_name_he = type_info.get("name_he", type_name_en)

    # Build descriptions
    if docstring:
        description_en = f"{module_name_en}: {title}\n\n{docstring}"
        description_he = f"{module_name_he}: {title}\n\n{docstring}"
    else:
        description_en = f"{module_name_en}: {title}\n\nComplete the code in the functions marked with pass"
        description_he = f"{module_name_he}: {title}\n\nהשלימי את הקוד בפונקציות המסומנות ב-pass"

    # Check for solution file
    solution_path = filepath.parent / f"{filepath.stem}_solution.py"
    solution_code = None
    if solution_path.exists():
        solution_code = solution_path.read_text(encoding="utf-8")

    # Check for hints file
    hints = []
    hints_path = filepath.parent.parent / "hints.json"
    if hints_path.exists():
        hints_data = load_json_file(hints_path)
        exercise_key = filepath.stem
        if exercise_key in hints_data:
            hint_entry = hints_data[exercise_key]
            if isinstance(hint_entry, list):
                hints = hint_entry
            elif isinstance(hint_entry, dict):
                hints = hint_entry.get("hints", [])

    return {
        "id": exercise_id,
        "topic_id": topic_id,
        "exercise_type": exercise_type,
        "category": category,
        "title": title,
        "title_en": title,
        "title_he": title,  # Could be translated via lookup table
        "description_en": description_en,
        "description_he": description_he,
        "difficulty": difficulty,
        "requires_running": requires_running,
        "estimated_time_minutes": estimated_time,
        "skills": skills,
        "starter_code": content,
        "solution_code": solution_code,
        "hints": hints,
        "tags": [module_name, exercise_type],
        "source_file": f"{module_name}/{exercise_type}/{filename}",
    }


def main():
    # Determine paths
    root = Path(__file__).parent.parent

    if len(sys.argv) >= 2:
        exercises_dir = Path(sys.argv[1])
    else:
        exercises_dir = root / "exercises"

    if not exercises_dir.exists():
        print(f"Error: Exercises directory not found: {exercises_dir}")
        sys.exit(1)

    # Load configuration files
    exercises_config = load_json_file(root / "exercises_config.json")
    types_metadata_file = load_json_file(root / "templates" / "exercise_types_metadata.json")

    modules_config = exercises_config.get("modules", {})
    types_metadata = types_metadata_file.get("exercise_types", {})

    if modules_config:
        print(f"Loaded config for {len(modules_config)} modules")
    else:
        print("Warning: No module config found in exercises_config.json")

    if types_metadata:
        print(f"Loaded metadata for {len(types_metadata)} exercise types")
    else:
        print("Warning: No exercise type metadata found")

    # Discover modules from filesystem
    module_dirs = sorted([
        d for d in exercises_dir.iterdir()
        if d.is_dir() and d.name.startswith("module_")
    ])

    print(f"Found {len(module_dirs)} modules on disk")

    # Check for mismatches
    disk_modules = {d.name for d in module_dirs}
    config_modules = set(modules_config.keys())

    missing_in_config = disk_modules - config_modules
    if missing_in_config:
        print(f"Warning: Modules on disk but not in config: {missing_in_config}")

    missing_on_disk = config_modules - disk_modules
    if missing_on_disk:
        print(f"Note: Modules in config but not on disk: {missing_on_disk}")

    total_exercises = 0
    module_names = []

    for module_dir in module_dirs:
        module_name = module_dir.name
        module_names.append(module_name)

        # Get module config (use empty dict if not found)
        module_config = modules_config.get(module_name, {})

        exercises = []
        type_counts = {}

        # Get all type subdirectories
        type_dirs = sorted([
            d for d in module_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".")
        ])

        # Warn about legacy files in module root
        legacy_files = list(module_dir.glob("*.py"))
        if legacy_files:
            print(f"  Warning: {module_name} has {len(legacy_files)} .py files not in subdirectories")

        for type_dir in type_dirs:
            exercise_type = type_dir.name
            py_files = sorted(type_dir.glob("*.py"))

            # Skip solution files
            py_files = [f for f in py_files if not f.name.endswith("_solution.py")]

            for filepath in py_files:
                try:
                    exercise = parse_exercise_file(
                        filepath,
                        module_name,
                        exercise_type,
                        module_config,
                        types_metadata,
                    )
                    exercises.append(exercise)
                    type_counts[exercise_type] = type_counts.get(exercise_type, 0) + 1
                except Exception as e:
                    print(f"  Error parsing {filepath}: {e}")

        if not exercises:
            print(f"  {module_name}: no exercises found")
            continue

        # Write module's exercises.json
        module_data = {
            "version": VERSION,
            "theme_support": True,
            "generated_at": datetime.now().isoformat(),
            "module": module_name,
            "count": len(exercises),
            "exercise_types": sorted(type_counts.keys()),
            "exercises": exercises,
        }

        output_path = module_dir / "exercises.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(module_data, f, indent=2, ensure_ascii=False)

        # Format summary
        type_summary = ", ".join(f"{t}:{c}" for t, c in sorted(type_counts.items()))
        print(f"  {module_name}: {len(exercises)} exercises ({type_summary})")
        total_exercises += len(exercises)

    # Write manifest.json
    manifest = {
        "version": VERSION,
        "modules": module_names,
    }
    manifest_path = root / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {manifest_path}")

    # Write version.json
    version_data = {
        "exercises": VERSION,
        "prompts": "1.0.0",
        "updated_at": datetime.now().isoformat(),
        "i18n_supported": True,
        "languages": ["he", "en"],
    }
    version_path = root / "version.json"
    with open(version_path, "w", encoding="utf-8") as f:
        json.dump(version_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {version_path}")

    print(f"\nTotal: {total_exercises} exercises in {len(module_names)} modules")


if __name__ == "__main__":
    main()
