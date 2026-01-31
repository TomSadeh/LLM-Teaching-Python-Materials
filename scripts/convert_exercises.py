#!/usr/bin/env python
"""
Convert exercise Python files to per-module JSON format.

Usage:
    python scripts/convert_exercises.py [source_dir]

If source_dir is not provided, defaults to raw_exercises in the repo root.
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime

VERSION = "2.0.0"

# Map module folders to topic IDs
MODULE_TO_TOPIC = {
    "module_0_basics": "basics.print",
    "module_1_turtle_loops": "loops.for",
    "module_2_decisions": "control.if",
    "module_3_lists": "collections.lists",
    "module_4_games": "loops.while",
    "module_5_functions": "functions.basic",
    "module_6_final_project": "project.final",
    "module_7_dictionaries": "collections.dict",
    "module_8_modules": "modules.stdlib",
    "module_9_oop": "oop.classes",
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
    "module_7_dictionaries": 2,
    "module_8_modules": 3,
    "module_9_oop": 3,
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
    "module_7_dictionaries": "מילונים",
    "module_8_modules": "מודולים",
    "module_9_oop": "תכנות מונחה עצמים",
}

# English module names
MODULE_NAMES_EN = {
    "module_0_basics": "Basics",
    "module_1_turtle_loops": "Turtle and Loops",
    "module_2_decisions": "Conditions and Decisions",
    "module_3_lists": "Lists",
    "module_4_games": "Games",
    "module_5_functions": "Functions",
    "module_6_final_project": "Final Project",
    "module_7_dictionaries": "Dictionaries",
    "module_8_modules": "Modules",
    "module_9_oop": "Object-Oriented Programming",
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
    # Module 7: Dictionaries
    "spellbook": "ספר כישופים",
    "character stats": "נתוני דמות",
    "loop dictionaries": "לולאות על מילונים",
    "nested data": "מידע מקונן",
    "dict methods": "מתודות מילון",
    "quiz game": "משחק חידון",
    "secret codes": "קודים סודיים",
    "rpg inventory": "מלאי RPG",
    "contact book": "ספר אנשי קשר",
    # Module 8: Modules
    "datetime basics": "יסודות תאריך ושעה",
    "random advanced": "אקראיות מתקדם",
    "json basics": "יסודות JSON",
    "time module": "מודול זמן",
    "math module": "מודול מתמטיקה",
    "string module": "מודול מחרוזות",
    "os path": "נתיבי מערכת",
    "collections": "אוספים",
    "create module": "יצירת מודול",
    # Module 9: OOP
    "first class": "מחלקה ראשונה",
    "init method": "מתודת אתחול",
    "methods": "מתודות",
    "str repr": "ייצוג טקסטואלי",
    "interaction": "אינטראקציה",
    "inheritance": "הורשה",
    "composition": "הרכבה",
    "text adventure": "הרפתקת טקסט",
    "rpg battle": "קרב RPG",
}

# English title mapping (keys match TITLE_HE_MAP)
TITLE_EN_MAP = {
    "hello": "Hello World",
    "variables": "Variables",
    "math": "Math Operations",
    "input": "Input",
    "calculator": "Calculator",
    "madlib simple": "Mad Lib Story",
    "counting": "Counting",
    "patterns": "Patterns",
    "sum": "Sum",
    "functions basic": "Basic Functions",
    "functions params": "Functions with Parameters",
    "functions return": "Functions with Return",
    "fizzbuzz": "FizzBuzz",
    "multiplication table": "Multiplication Table",
    "mini project": "Mini Project",
    "turtle intro": "Turtle Introduction",
    "turtle shapes": "Turtle Shapes",
    "turtle colors": "Turtle Colors",
    "square": "Square",
    "triangle": "Triangle",
    "star": "Star",
    "creative": "Creative",
    "hexagon": "Hexagon",
    "circle": "Circle",
    "rainbow": "Rainbow",
    "nested squares": "Nested Squares",
    "flower": "Flower",
    "password": "Password",
    "grades": "Grades",
    "number game": "Number Game",
    "quiz": "Quiz",
    "age checker": "Age Checker",
    "time greeter": "Time Greeter",
    "even odd": "Even or Odd",
    "leap year": "Leap Year",
    "favorites": "Favorites",
    "loop list": "Loop Through List",
    "magic 8ball": "Magic 8 Ball",
    "madlibs": "Mad Libs",
    "todo list": "Todo List",
    "name picker": "Name Picker",
    "shopping total": "Shopping Total",
    "playlist shuffler": "Playlist Shuffler",
    "word collector": "Word Collector",
    "guess number": "Guess the Number",
    "rock paper scissors": "Rock Paper Scissors",
    "dice game": "Dice Game",
    "your game": "Your Own Game",
    "coin flip streak": "Coin Flip Streak",
    "higher lower": "Higher or Lower",
    "trivia": "Trivia",
    "word scramble": "Word Scramble",
    "adventure": "Adventure",
    "shapes": "Shapes",
    "helper functions": "Helper Functions",
    "turtle art": "Turtle Art",
    "temperature": "Temperature",
    "tip calculator": "Tip Calculator",
    "password generator": "Password Generator",
    "greeting card": "Greeting Card",
    "turtle scene": "Turtle Scene",
    "template game": "Game Template",
    "template art": "Art Generator",
    "template app": "App Template",
    "bonus example spiral": "Bonus: Spiral",
    # Module 7: Dictionaries
    "spellbook": "Spellbook",
    "character stats": "Character Stats",
    "loop dictionaries": "Looping Dictionaries",
    "nested data": "Nested Data",
    "dict methods": "Dictionary Methods",
    "quiz game": "Quiz Game",
    "secret codes": "Secret Codes",
    "rpg inventory": "RPG Inventory",
    "contact book": "Contact Book",
    # Module 8: Modules
    "datetime basics": "Date and Time Basics",
    "random advanced": "Advanced Random",
    "json basics": "JSON Basics",
    "time module": "Time Module",
    "math module": "Math Module",
    "string module": "String Module",
    "os path": "OS and Paths",
    "collections": "Collections",
    "create module": "Create Your Module",
    # Module 9: OOP
    "first class": "First Class",
    "init method": "Init Method",
    "methods": "Methods",
    "str repr": "String Representation",
    "interaction": "Object Interaction",
    "inheritance": "Inheritance",
    "composition": "Composition",
    "text adventure": "Text Adventure",
    "rpg battle": "RPG Battle",
}


def extract_title_from_filename(filename: str) -> tuple[str, str, str]:
    """Extract base title, English title, and Hebrew title from filename."""
    name = filename.replace(".py", "")

    # Remove exercise_XX_ or template_ prefix
    match = re.match(r"(exercise_\d+_|template_)(.+)", name)
    if match:
        name = match.group(2)

    # Convert underscore to space and title case
    title = name.replace("_", " ").title()
    key = title.lower()
    title_en = TITLE_EN_MAP.get(key, title)
    title_he = TITLE_HE_MAP.get(key, title)

    return title, title_en, title_he


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

    title, title_en, title_he = extract_title_from_filename(filename)
    description = extract_description_from_content(content)

    # Build Hebrew description
    module_he = MODULE_NAMES_HE.get(module_name, module_name)
    if description:
        description_he = f"{module_he}: {title_he}\n\n{description}"
    else:
        description_he = f"{module_he}: {title_he}\n\nהשלימי את הקוד בפונקציות המסומנות ב-pass"

    # Build English description
    module_en = MODULE_NAMES_EN.get(module_name, module_name)
    if description:
        description_en = f"{module_en}: {title_en}\n\n{description}"
    else:
        description_en = f"{module_en}: {title_en}\n\nComplete the code in the functions marked with pass"

    # Generate a stable ID from module and filename
    exercise_id = f"{module_name}.{filename.replace('.py', '')}"

    # Use full path as title to match local migration format
    full_title = f"{module_name}/{filename}"

    return {
        "id": exercise_id,
        "topic_id": MODULE_TO_TOPIC.get(module_name, "basics.print"),
        "title": full_title,
        "title_he": title_he,
        "title_en": title_en,
        "description_he": description_he,
        "description_en": description_en,
        "difficulty": MODULE_TO_DIFFICULTY.get(module_name, 1),
        "starter_code": content,
        "solution_code": None,
        "hints": [],
        "tags": module_name,
        "source_file": f"{module_name}/{filename}",
    }


def main():
    # Determine source directory
    root = Path(__file__).parent.parent

    if len(sys.argv) >= 2:
        source_dir = Path(sys.argv[1])
    else:
        source_dir = root / "raw_exercises"

    if not source_dir.exists():
        print(f"Error: Source directory not found: {source_dir}")
        sys.exit(1)

    # Get all module directories
    modules = sorted([
        d for d in source_dir.iterdir()
        if d.is_dir() and d.name.startswith("module_")
    ])

    print(f"Found {len(modules)} modules")

    total_exercises = 0
    module_names = []

    for module_dir in modules:
        module_name = module_dir.name
        module_names.append(module_name)

        # Get all exercise files in this module
        py_files = sorted(module_dir.glob("*.py"))
        exercises = []

        for filepath in py_files:
            try:
                exercise = parse_exercise_file(filepath)
                exercises.append(exercise)
            except Exception as e:
                print(f"  [ERROR] {filepath}: {e}")

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
            "exercises": exercises,
        }

        output_path = module_dir / "exercises.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(module_data, f, indent=2, ensure_ascii=False)

        print(f"  {module_name}: {len(exercises)} exercises")
        total_exercises += len(exercises)

    # Write manifest.json
    manifest_data = {
        "version": VERSION,
        "modules": module_names,
    }
    manifest_path = root / "manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {manifest_path}")

    # Write version.json with i18n metadata
    version_data = {
        "exercises": VERSION,
        "prompts": "1.0.0",
        "updated_at": datetime.now().isoformat(),
        "i18n_supported": True,
        "languages": ["he", "en"],
    }
    version_path = root / "version.json"
    with open(version_path, "w", encoding="utf-8") as f:
        json.dump(version_data, f, ensure_ascii=False, indent=2)
    print(f"Wrote {version_path}")

    print(f"\nTotal: {total_exercises} exercises in {len(module_names)} modules")


if __name__ == "__main__":
    main()
