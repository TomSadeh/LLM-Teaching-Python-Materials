"""
{{CONTEXT_DECODE_ERROR_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to understand and handle common CSV-related
errors and data issues.

Topic: CSV error interpretation
Difficulty: 3
"""

import csv


# ============================================================
# {{ERROR_1_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_1_NARRATIVE}}
#
# Trying to read a CSV file that doesn't exist.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "read_data.py", line 2, in <module>
    with open("data.csv", "r") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
"""


def buggy_code_a():
    """The code that caused the error."""
    with open("nonexistent_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_1}}
    #
    # Fix: Handle FileNotFoundError
    #   try:
    #       with open("data.csv", "r") as f:
    #           reader = csv.reader(f)
    #           for row in reader:
    #               print(row)
    #   except FileNotFoundError:
    #       print("Data file not found, using defaults")
    #       # Use default data

    pass


# ============================================================
# {{ERROR_2_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# Index error from assuming wrong number of columns.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "parse_row.py", line 6, in <module>
    score = int(row[2])
IndexError: list index out of range
"""


def buggy_code_b():
    """The code that caused the error."""
    # CSV file has some rows with missing columns:
    # Name,Level,Score
    # {{hero}},5,100
    # {{heroine}},7        <-- Missing score!
    # {{friend}},3,75

    with open("incomplete.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            name = row[0]
            level = row[1]
            score = int(row[2])  # IndexError on incomplete row!


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_2}}
    #
    # A row had fewer columns than expected (missing data).
    #
    # Fix: Check row length before accessing
    #   for row in reader:
    #       if len(row) >= 3:
    #           name = row[0]
    #           level = row[1]
    #           score = int(row[2])
    #       else:
    #           print(f"Skipping incomplete row: {row}")

    pass


# ============================================================
# {{ERROR_3_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# ValueError when converting CSV string to number.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "parse_score.py", line 7, in <module>
    score = int(row[2])
ValueError: invalid literal for int() with base 10: 'N/A'
"""


def buggy_code_c():
    """The code that caused the error."""
    # CSV file has non-numeric values where numbers expected:
    # Name,Level,Score
    # {{hero}},5,100
    # {{heroine}},7,N/A    <-- Not a number!
    # {{friend}},3,75

    with open("mixed_data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            score = int(row[2])  # ValueError on "N/A"!


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_3}}
    #
    # The CSV had "N/A" where a number was expected.
    #
    # Fix: Handle conversion errors
    #   for row in reader:
    #       try:
    #           score = int(row[2])
    #       except ValueError:
    #           score = 0  # Default for invalid values
    #           print(f"Invalid score for {row[0]}, using 0")

    pass


# ============================================================
# {{ERROR_4_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_4_NARRATIVE}}
#
# KeyError when using DictReader with missing columns.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "dict_reader.py", line 5, in <module>
    print(row["Score"])
KeyError: 'Score'
"""


def buggy_code_d():
    """The code that caused the error."""
    # Header has different column name than expected:
    # Name,Level,Points     <-- "Points" not "Score"!
    # {{hero}},5,100

    with open("different_headers.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row["Score"])  # KeyError: column is "Points"!


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_4}}
    #
    # The column header in the file doesn't match the expected key.
    #
    # Fix option 1: Use the correct column name
    #   print(row["Points"])
    #
    # Fix option 2: Check available columns first
    #   with open("data.csv", "r") as f:
    #       reader = csv.DictReader(f)
    #       print(f"Available columns: {reader.fieldnames}")
    #
    # Fix option 3: Use .get() with default
    #   score = row.get("Score", row.get("Points", 0))

    pass


# ============================================================
# {{ERROR_5_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_5_NARRATIVE}}
#
# Extra blank lines in CSV causing empty rows.

"""
UNEXPECTED BEHAVIOR:
-------------------
Reading CSV returns rows like:
['{{hero}}', '5', '100']
[]
['{{heroine}}', '7', '150']
[]
"""


def buggy_code_e():
    """The code that shows the problem."""
    # Windows issue: not using newline="" causes extra blank rows

    with open("data.csv", "r") as f:  # Missing newline=""
        reader = csv.reader(f)
        for row in reader:
            name = row[0]  # Crashes on empty row!


def fix_code_e():
    # ✏️ FIX THE CODE ✏️
    #
    # The problem occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_5}}
    #
    # On Windows, opening CSV without newline="" can cause issues.
    # Or the file genuinely has blank lines.
    #
    # Fix 1: Use newline="" when opening
    #   with open("data.csv", "r", newline="") as f:
    #
    # Fix 2: Skip empty rows
    #   for row in reader:
    #       if row:  # Skip empty rows
    #           name = row[0]

    pass


def main():
    print("{{CONTEXT_DECODE_ERROR_INTRO}}")
    print("=" * 50)
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()

    print("=== {{ERROR_1_TITLE}} ===")
    print("FileNotFoundError - CSV file doesn't exist")

    print("\n=== {{ERROR_2_TITLE}} ===")
    print("IndexError - row has fewer columns than expected")

    print("\n=== {{ERROR_3_TITLE}} ===")
    print("ValueError - can't convert value to number")

    print("\n=== {{ERROR_4_TITLE}} ===")
    print("KeyError - column name doesn't match")

    print("\n=== {{ERROR_5_TITLE}} ===")
    print("Empty rows - blank lines in data")

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
    print()
    print("CSV error handling tips:")
    print("  1. Always use newline='' on Windows")
    print("  2. Check row length before accessing by index")
    print("  3. Handle ValueError for type conversions")
    print("  4. Use .get() or check fieldnames with DictReader")
    print("  5. Skip empty rows: if row:")


main()
