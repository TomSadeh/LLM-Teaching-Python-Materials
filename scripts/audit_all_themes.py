#!/usr/bin/env python3
"""
Comprehensive Theme-Specific Content Audit

Searches for hardcoded content from ALL themes:
- Harry Potter (dumblecode)
- Percy Jackson (chirthon)
- Hunger Games (compile-games)
- Keeper of Lost Cities (pyfire)
- Generic real-world references

Usage: python scripts/audit_all_themes.py
"""

import re
from pathlib import Path
from collections import defaultdict

# Define theme-specific patterns to detect
THEME_PATTERNS = {
    "Harry Potter (dumblecode)": {
        "houses": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"],
        "characters": ["Harry", "Hermione", "Ron", "Dumbledore", "Snape", "Voldemort", "Luna", "Neville"],
        "locations": ["Hogwarts", "Diagon Alley", "Hogsmeade", "Forbidden Forest"],
        "items": ["Invisibility Cloak", "Elder Wand", "Philosopher's Stone"],
        "spells": ["Expelliarmus", "Lumos", "Wingardium Leviosa", "Patronus", "Protego", "Avada Kedavra"],
    },
    "Percy Jackson (chirthon)": {
        "locations": ["Camp Half-Blood", "Olympus", "Tartarus"],
        "characters": ["Percy", "Annabeth", "Grover", "Luke", "Chiron", "Clarisse"],
        "gods": ["Zeus", "Poseidon", "Athena", "Apollo", "Hermes", "Ares", "Hades"],
        "items": ["Riptide", "Golden Fleece", "Aegis"],
        "creatures": ["Minotaur", "Medusa", "Cyclops", "Hellhound"],
    },
    "Hunger Games (compile-games)": {
        "locations": ["Panem", "Capitol", "District 12", "Arena"],
        "characters": ["Katniss", "Peeta", "Gale", "Rue", "Finnick", "Haymitch", "Effie"],
        "items": ["Mockingjay", "Tracker Jacker"],
    },
    "Keeper of Lost Cities (pyfire)": {
        "locations": ["Foxfire", "Lost Cities", "Havenfield", "Atlantis"],
        "characters": ["Sophie", "Keefe", "Fitz", "Biana", "Dex", "Marella"],
        "items": ["Pathfinder", "Leaping Crystal"],
        "abilities": ["Telepath", "Empath", "Vanisher", "Pyrokinetic"],
    },
    "Generic/Real-world": {
        "real_places": ["New York", "London", "Paris", "Tokyo", "California"],
        "real_people": ["Einstein", "Shakespeare", "Mozart"],
        "brands": ["Apple", "Google", "Microsoft", "Nike", "McDonald"],
    }
}

def create_pattern_dict():
    """Convert theme patterns to regex patterns."""
    all_patterns = {}
    for theme, categories in THEME_PATTERNS.items():
        for category, terms in categories.items():
            for term in terms:
                # Word boundary regex to avoid false positives
                pattern = r'\b' + re.escape(term) + r'\b'
                all_patterns[term] = {
                    "theme": theme,
                    "category": category,
                    "pattern": pattern
                }
    return all_patterns

def is_in_comment_or_docstring(line):
    """Check if content is in a comment or docstring."""
    stripped = line.strip()
    # Single line comment
    if stripped.startswith('#'):
        return True
    # In docstring (approximate check)
    if '"""' in line or "'''" in line:
        return True
    return False

def scan_file(filepath, patterns):
    """Scan a file for hardcoded theme content."""
    violations = defaultdict(list)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except:
        return violations

    in_docstring = False
    docstring_char = None

    for line_num, line in enumerate(lines, 1):
        # Track docstrings
        if '"""' in line:
            in_docstring = not in_docstring
            docstring_char = '"""'
        elif "'''" in line:
            in_docstring = not in_docstring
            docstring_char = "'''"

        # Skip comments and docstrings
        if is_in_comment_or_docstring(line) or in_docstring:
            continue

        # Check each pattern
        for term, info in patterns.items():
            match = re.search(info["pattern"], line, re.IGNORECASE)
            if match:
                violations[term].append({
                    "line_num": line_num,
                    "line": line.strip(),
                    "theme": info["theme"],
                    "category": info["category"]
                })

    return violations

def main():
    print("=" * 80)
    print("COMPREHENSIVE THEME-SPECIFIC CONTENT AUDIT")
    print("=" * 80)
    print()

    patterns = create_pattern_dict()
    print(f"Searching for {len(patterns)} theme-specific terms...")
    print()

    all_violations = defaultdict(lambda: defaultdict(list))
    total_files_scanned = 0

    # Scan all Python files
    exercises = Path("exercises")
    if not exercises.exists():
        print("ERROR: exercises directory not found!")
        print("Run this from repository root.")
        return

    for py_file in sorted(exercises.rglob("*.py")):
        total_files_scanned += 1
        violations = scan_file(py_file, patterns)

        if violations:
            for term, occurrences in violations.items():
                for occ in occurrences:
                    all_violations[occ["theme"]][py_file].append({
                        "term": term,
                        "category": occ["category"],
                        "line_num": occ["line_num"],
                        "line": occ["line"]
                    })

    # Display results by theme
    print(f"Files scanned: {total_files_scanned}")
    print()

    if not all_violations:
        print("=" * 80)
        print("SUCCESS: No hardcoded theme-specific content found!")
        print("All exercises are theme-agnostic.")
        print("=" * 80)
        return

    total_violations = 0
    total_files_affected = set()

    for theme in sorted(all_violations.keys()):
        print("=" * 80)
        print(f"THEME: {theme}")
        print("=" * 80)
        print()

        files_with_violations = all_violations[theme]
        theme_violation_count = sum(len(v) for v in files_with_violations.values())
        total_violations += theme_violation_count

        print(f"Files with violations: {len(files_with_violations)}")
        print(f"Total violations: {theme_violation_count}")
        print()

        for filepath in sorted(files_with_violations.keys()):
            total_files_affected.add(filepath)
            violations = files_with_violations[filepath]

            print(f"  {filepath}")

            # Group by term
            by_term = defaultdict(list)
            for v in violations:
                by_term[v["term"]].append(v)

            for term, occurrences in sorted(by_term.items()):
                category = occurrences[0]["category"]
                print(f"    - {term} ({category}): {len(occurrences)} instance(s)")
                for occ in occurrences[:2]:  # Show first 2 lines
                    print(f"        Line {occ['line_num']}: {occ['line'][:60]}...")
                if len(occurrences) > 2:
                    print(f"        ... and {len(occurrences) - 2} more")
            print()

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total files scanned: {total_files_scanned}")
    print(f"Files with violations: {len(total_files_affected)}")
    print(f"Total violations: {total_violations}")
    print(f"Themes affected: {len(all_violations)}")
    print()
    print("RECOMMENDATION:")
    print("Replace all hardcoded references with appropriate placeholders.")
    print("See docs/THEME_AGNOSTIC_SOLUTION.md for details.")
    print("=" * 80)

if __name__ == "__main__":
    main()
