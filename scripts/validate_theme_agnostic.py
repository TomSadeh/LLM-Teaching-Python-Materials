#!/usr/bin/env python3
"""
Theme Agnostic Validation Script

Checks all Python exercises for hardcoded theme-specific content.
Ensures exercises work across all themes (dumblecode, chirthon, compile-games, pymentor).

Usage:
    python scripts/validate_theme_agnostic.py

Exit codes:
    0 - All exercises are theme-agnostic
    1 - Hardcoded theme references found
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

# Hardcoded theme-specific patterns to detect
HARDCODED_PATTERNS = {
    # Harry Potter specific
    "Gryffindor": r'\bGryffindor\b',
    "Hufflepuff": r'\bHufflepuff\b',
    "Ravenclaw": r'\bRavenclaw\b',
    "Slytherin": r'\bSlytherin\b',
    "Hogwarts": r'\bHogwarts\b',
    "Dumbledore": r'\bDumbledore\b',
    "Harry": r'\bHarry\b',
    "Hermione": r'\bHermione\b',
    "Ron": r'\bRon\b',

    # Specific spells (should use {{spell1}} etc.)
    "Expelliarmus": r'\bExpelliarmus\b',
    "Lumos": r'\bLumos\b',
    "Patronus": r'\bPatronus\b',
    "Protego": r'\bProtego\b',

    # Percy Jackson specific (add if found)
    "Camp Half-Blood": r'Camp Half-Blood',
    "Poseidon": r'\bPoseidon\b',
    "Athena": r'\bAthena\b',

    # Hunger Games specific
    "Panem": r'\bPanem\b',
    "Katniss": r'\bKatniss\b',
}

# Exceptions - cases where hardcoded content is OK
EXCEPTION_PATTERNS = [
    r'#.*',  # Comments (documentation references are OK)
    r'""".*"""',  # Docstrings
    r"'''.*'''",  # Docstrings
]


def is_exception(line, match_pos):
    """Check if match is in an exception context (comment/docstring)."""
    # Check if match is in a comment
    if '#' in line[:match_pos]:
        return True
    return False


def check_file(filepath):
    """
    Check if file contains hardcoded theme references.

    Returns:
        dict: {pattern_name: [(line_num, line_content), ...]}
    """
    violations = defaultdict(list)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        return violations  # Skip binary files

    for line_num, line in enumerate(lines, 1):
        for pattern_name, pattern_regex in HARDCODED_PATTERNS.items():
            matches = re.finditer(pattern_regex, line)
            for match in matches:
                # Check if it's in a comment or string (exception)
                if is_exception(line, match.start()):
                    continue

                violations[pattern_name].append((line_num, line.strip()))

    return violations


def format_file_violations(filepath, violations):
    """Format violations for display."""
    output = [f"\n❌ {filepath}"]

    for pattern_name, occurrences in sorted(violations.items()):
        output.append(f"   📍 {pattern_name}: {len(occurrences)} instance(s)")
        for line_num, line_content in occurrences:
            output.append(f"      Line {line_num}: {line_content[:80]}")

    return "\n".join(output)


def main():
    """Run validation on all Python exercises."""
    print("🔍 Scanning exercises for hardcoded theme content...\n")

    exercises_dir = Path("exercises")
    if not exercises_dir.exists():
        print(f"❌ Error: {exercises_dir} not found!")
        print("   Run this script from the repository root.")
        sys.exit(1)

    all_violations = {}
    total_files_scanned = 0
    total_files_with_violations = 0
    total_violations = 0

    # Scan all Python files
    for py_file in sorted(exercises_dir.rglob("*.py")):
        total_files_scanned += 1
        violations = check_file(py_file)

        if violations:
            all_violations[py_file] = violations
            total_files_with_violations += 1
            total_violations += sum(len(v) for v in violations.values())

    # Display results
    if all_violations:
        print("⚠️  HARDCODED THEME REFERENCES FOUND\n")
        print("=" * 70)

        for filepath, violations in sorted(all_violations.items()):
            print(format_file_violations(filepath, violations))

        print("\n" + "=" * 70)
        print(f"\n📊 Summary:")
        print(f"   Files scanned: {total_files_scanned}")
        print(f"   Files with violations: {total_files_with_violations}")
        print(f"   Total violations: {total_violations}")
        print(f"\n💡 Fix these by replacing with placeholders:")
        print(f"   'Gryffindor' → '{{{{house_1}}}}'")
        print(f"   'Hufflepuff' → '{{{{house_2}}}}'")
        print(f"   'Ravenclaw' → '{{{{house_3}}}}'")
        print(f"   'Slytherin' → '{{{{house_4}}}}'")
        print(f"\n📖 See docs/THEME_AGNOSTIC_SOLUTION.md for details\n")

        sys.exit(1)
    else:
        print("✅ All exercises are theme-agnostic!")
        print(f"   Scanned {total_files_scanned} Python files")
        print(f"   No hardcoded theme references found")
        print(f"\n🎉 Exercises can be used with any theme!\n")

        sys.exit(0)


if __name__ == "__main__":
    main()
