#!/usr/bin/env python
"""
Convert exercise Python files to JSON format for remote sync.

Usage:
    python scripts/convert_exercises.py <source_dir>

Example:
    python scripts/convert_exercises.py ../maya-chat/data/exercises
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

# Map module folders to topic IDs
MODULE_TO_TOPIC = {
    "module_0_basics": "basics.print",
    "module_1_turtle_loops": "loops.for",
    "module_2_decisions": "control.if",
    "module_3_lists": "collections.lists",
    "module_4_games": "loops.while",
    "module_5_functions": "functions.basic",
    "module_6_final_project": "project.final",
}

# Module to difficulty mapping
MODULE_TO_DIFFICULTY = {
    "module_0_basics": 1,
    "module_1_turtle_loops": 1,
    "module_2_decisions": 2,
    "module_3_lists": 2,
    "module_4_games": 2,
    "module_5_functions": 3,
    "module_6_final_project": 3,
}

# Hebrew module names
MODULE_NAMES_HE = {
    "module_0_basics": "יסודות",
    "module_1_turtle_loops": "צב ולולאות",
    "module_2_decisions": "תנאים והחלטות",
    "module_3_lists": "רשימות",
    "module_4_games": "משחקים",
    "module_5_functions": "פונקציות",
    "module_6_final_project": "פרויקט מסכם",
}

# Hebrew title mapping
TITLE_HE_MAP = {
    "hello": "שלום עולם",
    "variables": "משתנים",
    "math": "חישובים",
    "input": "קלט",
    "calculator": "מחשבון",
    "madlib simple": "סיפור משוגע",
    "counting": "ספירה",
    "patterns": "דפוסים",
    "sum": "סכום",
    "functions basic": "פונקציות בסיסיות",
    "functions params": "פונקציות עם פרמטרים",
    "functions return": "פונקציות עם החזרה",
    "fizzbuzz": "פיזבאז",
    "multiplication table": "לוח הכפל",
    "mini project": "פרויקט מיני",
    "turtle intro": "הכרות עם צב",
    "turtle shapes": "צורות עם צב",
    "turtle colors": "צבעים עם צב",
    "square": "ריבוע",
    "triangle": "משולש",
    "star": "כוכב",
    "creative": "יצירתי",
    "hexagon": "משושה",
    "circle": "עיגול",
    "rainbow": "קשת",
    "nested squares": "ריבועים מקוננים",
    "flower": "פרח",
    "password": "סיסמה",
    "grades": "ציונים",
    "number game": "משחק מספרים",
    "quiz": "חידון",
    "age checker": "בודק גיל",
    "time greeter": "ברכת שעה",
    "even odd": "זוגי אי-זוגי",
    "leap year": "שנה מעוברת",
    "favorites": "מועדפים",
    "loop list": "לולאה על רשימה",
    "magic 8ball": "כדור קסם",
    "madlibs": "סיפור משוגע",
    "todo list": "רשימת מטלות",
    "name picker": "בוחר שמות",
    "shopping total": "סכום קניות",
    "playlist shuffler": "מערבל פלייליסט",
    "word collector": "אוסף מילים",
    "guess number": "נחש את המספר",
    "rock paper scissors": "אבן נייר ומספריים",
    "dice game": "משחק קוביות",
    "your game": "המשחק שלך",
    "coin flip streak": "רצף מטבע",
    "higher lower": "גבוה נמוך",
    "trivia": "טריוויה",
    "word scramble": "מילים מבולבלות",
    "adventure": "הרפתקה",
    "shapes": "צורות",
    "helper functions": "פונקציות עזר",
    "turtle art": "אומנות צב",
    "temperature": "טמפרטורה",
    "tip calculator": "מחשבון טיפ",
    "password generator": "מחולל סיסמאות",
    "greeting card": "כרטיס ברכה",
    "turtle scene": "סצנת צב",
    "template game": "תבנית משחק",
    "template art": "תבנית אומנות",
    "template app": "תבנית אפליקציה",
    "bonus example spiral": "בונוס: ספירלה",
}


def extract_title_from_filename(filename: str) -> tuple[str, str]:
    """Extract English and Hebrew title from filename."""
    name = filename.replace(".py", "")

    # Remove exercise_XX_ or template_ prefix
    match = re.match(r"(exercise_\d+_|template_)(.+)", name)
    if match:
        name = match.group(2)

    # Convert underscore to space and title case
    title = name.replace("_", " ").title()
    title_he = TITLE_HE_MAP.get(title.lower(), title)

    return title, title_he


def extract_description_from_content(content: str) -> str:
    """Extract description from the first comment in the file."""
    lines = content.split("\n")
    description_lines = []

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            comment = line.lstrip("#").strip()
            if comment:
                description_lines.append(comment)
        elif line and not line.startswith("#"):
            break

    return "\n".join(description_lines) if description_lines else ""


def parse_exercise_file(filepath: Path) -> dict:
    """Parse a single exercise file into JSON format."""
    content = filepath.read_text(encoding="utf-8")
    module_name = filepath.parent.name
    filename = filepath.name

    title, title_he = extract_title_from_filename(filename)
    description = extract_description_from_content(content)

    # Build Hebrew description
    module_he = MODULE_NAMES_HE.get(module_name, module_name)
    if description:
        description_he = f"{module_he}: {title_he}\n\n{description}"
    else:
        description_he = f"{module_he}: {title_he}\n\nהשלימי את הקוד בפונקציות המסומנות ב-pass"

    # Generate a stable ID from module and filename
    exercise_id = f"{module_name}.{filename.replace('.py', '')}"

    return {
        "id": exercise_id,
        "topic_id": MODULE_TO_TOPIC.get(module_name, "basics.print"),
        "title": title,
        "title_he": title_he,
        "description_he": description_he,
        "difficulty": MODULE_TO_DIFFICULTY.get(module_name, 1),
        "starter_code": content,
        "solution_code": None,
        "hints": [],
        "tags": module_name,
        "source_file": f"{module_name}/{filename}",
    }


def get_exercise_files(exercises_dir: Path) -> list[Path]:
    """Get all exercise Python files from the exercises directory."""
    files = []
    for module_dir in sorted(exercises_dir.iterdir()):
        if module_dir.is_dir() and module_dir.name.startswith("module_"):
            for py_file in sorted(module_dir.glob("*.py")):
                files.append(py_file)
    return files


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/convert_exercises.py <source_exercises_dir>")
        print("Example: python scripts/convert_exercises.py ../maya-chat/data/exercises")
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    if not source_dir.exists():
        print(f"Error: Source directory not found: {source_dir}")
        sys.exit(1)

    # Output directory (repo root)
    output_dir = Path(__file__).parent.parent

    # Get all exercise files
    files = get_exercise_files(source_dir)
    print(f"Found {len(files)} exercise files")

    # Convert to JSON
    exercises = []
    for filepath in files:
        try:
            exercise = parse_exercise_file(filepath)
            exercises.append(exercise)
            print(f"  [OK] {exercise['id']}")
        except Exception as e:
            print(f"  [ERROR] {filepath}: {e}")

    # Group by module for summary
    by_module = {}
    for ex in exercises:
        module = ex["tags"]
        by_module.setdefault(module, []).append(ex)

    # Write exercises.json
    exercises_data = {
        "version": "1.0.0",
        "generated_at": datetime.now().isoformat(),
        "total_count": len(exercises),
        "by_module": {k: len(v) for k, v in by_module.items()},
        "exercises": exercises,
    }

    exercises_path = output_dir / "exercises.json"
    with open(exercises_path, "w", encoding="utf-8") as f:
        json.dump(exercises_data, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {exercises_path}")

    # Write version.json
    version_data = {
        "exercises": "1.0.0",
        "prompts": "1.0.0",
        "updated_at": datetime.now().isoformat(),
    }

    version_path = output_dir / "version.json"
    with open(version_path, "w", encoding="utf-8") as f:
        json.dump(version_data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {version_path}")

    # Write empty prompts.json
    prompts_data = {
        "version": "1.0.0",
        "prompts": [],
    }

    prompts_path = output_dir / "prompts.json"
    with open(prompts_path, "w", encoding="utf-8") as f:
        json.dump(prompts_data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {prompts_path}")

    # Summary
    print("\nSummary:")
    print(f"  Total exercises: {len(exercises)}")
    for module, exs in sorted(by_module.items()):
        print(f"  {module}: {len(exs)}")


if __name__ == "__main__":
    main()
