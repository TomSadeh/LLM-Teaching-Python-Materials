"""
Script to replace hardcoded theme references with {{placeholders}}.

Reads replacement patterns from replacements.json.

Usage:
    python apply_theme_placeholders.py              # Update exercises.json
    python apply_theme_placeholders.py --raw        # Update raw .py files in raw_exercises/
    python apply_theme_placeholders.py --all        # Update both raw files and exercises.json
"""

import json
import re
import sys
from pathlib import Path


def load_replacements():
    """Load replacement patterns from replacements.json."""
    replacements_path = Path(__file__).parent.parent / "replacements.json"

    with open(replacements_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Build the replacements list from the data file
    replacements = []

    # Add comment patterns first (more specific)
    for item in data.get('comment_patterns', []):
        replacements.append((item['pattern'], item['replacement']))

    # Add trivia replacements
    for item in data.get('trivia_replacements', []):
        replacements.append((re.escape(item['pattern']), item['replacement']))

    # Add character suggestions
    for item in data.get('character_suggestions', []):
        replacements.append((re.escape(item['pattern']), item['replacement']))

    # Add simple word replacements from dictionaries
    # Order: characters, locations, spells, creatures, passwords, gods
    for category in ['characters', 'locations', 'spells_and_abilities',
                     'creatures_and_items', 'passwords_and_phrases', 'gods_and_mentors']:
        items = data.get(category, {})
        # Sort by length (longest first) to avoid partial replacements
        sorted_items = sorted(items.items(), key=lambda x: len(x[0]), reverse=True)
        for original, placeholder in sorted_items:
            escaped = re.escape(original)
            # For short words (<=5 chars), use word boundaries to avoid partial matches
            # e.g., "Ron" shouldn't match inside "Patronum" or "Wrong"
            if len(original) <= 5:
                # Only quoted version for short names to be safe
                replacements.append((f'"{escaped}"', f'"{placeholder}"'))
            else:
                # Add both quoted and unquoted versions for longer terms
                replacements.append((f'"{escaped}"', f'"{placeholder}"'))
                replacements.append((rf'\b{escaped}\b', placeholder))

    return replacements


def apply_replacements(text: str, replacements: list) -> str:
    """Apply all replacements to the text."""
    result = text
    for pattern, replacement in replacements:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE | re.MULTILINE)
    return result


def update_exercises_json(replacements: list):
    """Update exercises.json with theme placeholders."""
    exercises_path = Path(__file__).parent.parent / "exercises.json"

    with open(exercises_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Apply replacements to each exercise
    for exercise in data['exercises']:
        if exercise.get('starter_code'):
            exercise['starter_code'] = apply_replacements(exercise['starter_code'], replacements)
        if exercise.get('description_he'):
            exercise['description_he'] = apply_replacements(exercise['description_he'], replacements)
        if exercise.get('hints'):
            exercise['hints'] = [apply_replacements(h, replacements) for h in exercise['hints']]
        if exercise.get('solution_code'):
            exercise['solution_code'] = apply_replacements(exercise['solution_code'], replacements)

    # Update version
    data['version'] = '1.2.0'
    data['theme_support'] = True

    # Save back
    with open(exercises_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated {len(data['exercises'])} exercises in exercises.json")
    print("Version updated to 1.2.0")


def update_raw_files(replacements: list):
    """Update raw .py files in raw_exercises/ with theme placeholders."""
    raw_exercises_path = Path(__file__).parent.parent / "raw_exercises"

    if not raw_exercises_path.exists():
        print(f"Error: raw_exercises directory not found at {raw_exercises_path}")
        return 0

    updated_count = 0

    # Process all module directories
    for module_dir in sorted(raw_exercises_path.iterdir()):
        if not module_dir.is_dir() or not module_dir.name.startswith("module_"):
            continue

        # Process all .py files in the module
        for py_file in sorted(module_dir.glob("*.py")):
            original_content = py_file.read_text(encoding='utf-8')
            updated_content = apply_replacements(original_content, replacements)

            if original_content != updated_content:
                py_file.write_text(updated_content, encoding='utf-8')
                print(f"  [UPDATED] {module_dir.name}/{py_file.name}")
                updated_count += 1
            else:
                print(f"  [no change] {module_dir.name}/{py_file.name}")

    print(f"\nUpdated {updated_count} raw exercise files")
    return updated_count


def main():
    args = sys.argv[1:]

    # Load replacements from data file
    print("Loading replacements from replacements.json...")
    replacements = load_replacements()
    print(f"Loaded {len(replacements)} replacement patterns")

    if '--raw' in args:
        print("\nUpdating raw exercise files...")
        update_raw_files(replacements)
    elif '--all' in args:
        print("\nUpdating raw exercise files...")
        update_raw_files(replacements)
        print("\nUpdating exercises.json...")
        update_exercises_json(replacements)
    else:
        print("\nUpdating exercises.json...")
        update_exercises_json(replacements)
        print("\nTip: Use --raw to update raw .py files, or --all for both")


if __name__ == "__main__":
    main()
