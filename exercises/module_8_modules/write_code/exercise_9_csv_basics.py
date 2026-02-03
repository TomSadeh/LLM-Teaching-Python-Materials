"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to work with CSV (Comma-Separated Values)
files using Python's csv module. CSV is perfect for spreadsheet-style
tabular data with rows and columns.

Topic: CSV module basics (reader, writer, DictReader, DictWriter)
Difficulty: 3
"""

import csv


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Learn to write data to CSV files.


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Write data to a CSV file using csv.writer.
    #
    # Step 1: Prepare data as a list of lists (rows):
    #         data = [
    #             ["Name", "Level", "Ability"],  # Header row
    #             ["{{hero}}", 5, "{{spell1}}"],
    #             ["{{heroine}}", 7, "{{spell2}}"],
    #             ["{{friend}}", 3, "{{spell1}}"]
    #         ]
    #
    # Step 2: Write to CSV:
    #         with open("characters.csv", "w", newline="") as f:
    #             writer = csv.writer(f)
    #             writer.writerows(data)  # Write all rows at once
    #
    # Step 3: Print confirmation
    #
    # Note: newline="" is important on Windows to prevent blank lines!
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Write rows one at a time using writerow (singular).
    #
    # Step 1: Create the file and write header:
    #         with open("scores.csv", "w", newline="") as f:
    #             writer = csv.writer(f)
    #             writer.writerow(["Player", "Score", "Date"])
    #
    # Step 2: Write individual rows:
    #             writer.writerow(["{{hero}}", 1000, "2024-01-15"])
    #             writer.writerow(["{{heroine}}", 1500, "2024-01-16"])
    #             writer.writerow(["{{friend}}", 750, "2024-01-14"])
    #
    # Note: writerow() for one row, writerows() for multiple
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Learn to read data from CSV files.


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Read CSV data using csv.reader.
    #
    # Step 1: Open and read the CSV:
    #         with open("characters.csv", "r") as f:
    #             reader = csv.reader(f)
    #
    # Step 2: Iterate through rows:
    #             for row in reader:
    #                 print(row)  # Each row is a list
    #
    # Step 3: Access specific columns:
    #             # Reset to beginning
    #         with open("characters.csv", "r") as f:
    #             reader = csv.reader(f)
    #             next(reader)  # Skip header row
    #             for row in reader:
    #                 name = row[0]
    #                 level = int(row[1])  # CSV values are strings!
    #                 print(f"{name} is level {level}")
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Read CSV as list of lists.
    #
    # Step 1: Load entire CSV into memory:
    #         with open("characters.csv", "r") as f:
    #             reader = csv.reader(f)
    #             all_rows = list(reader)
    #
    # Step 2: Access by index:
    #         header = all_rows[0]
    #         data_rows = all_rows[1:]
    #
    #         print(f"Columns: {header}")
    #         print(f"Number of records: {len(data_rows)}")
    #
    # Step 3: Find a specific row:
    #         for row in data_rows:
    #             if row[0] == "{{hero}}":
    #                 print(f"Found: {row}")
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Learn DictReader and DictWriter for easier column access.


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use DictWriter to write dicts as rows.
    #
    # Step 1: Define field names (column headers):
    #         fieldnames = ["name", "level", "ability", "active"]
    #
    # Step 2: Create list of dicts:
    #         records = [
    #             {"name": "{{hero}}", "level": 5, "ability": "{{spell1}}", "active": True},
    #             {"name": "{{heroine}}", "level": 7, "ability": "{{spell2}}", "active": True},
    #             {"name": "{{friend}}", "level": 3, "ability": "{{spell1}}", "active": False}
    #         ]
    #
    # Step 3: Write using DictWriter:
    #         with open("roster.csv", "w", newline="") as f:
    #             writer = csv.DictWriter(f, fieldnames=fieldnames)
    #             writer.writeheader()  # Write column names
    #             writer.writerows(records)
    #
    # Note: DictWriter needs fieldnames to know column order
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use DictReader to read rows as dicts.
    #
    # Step 1: Read with DictReader:
    #         with open("roster.csv", "r") as f:
    #             reader = csv.DictReader(f)
    #
    # Step 2: Access columns by name:
    #             for row in reader:
    #                 print(f"{row['name']} - Level {row['level']}")
    #
    # Step 3: DictReader uses first row as keys automatically!
    #         with open("roster.csv", "r") as f:
    #             reader = csv.DictReader(f)
    #             print(f"Columns: {reader.fieldnames}")
    #             # Convert to list of dicts
    #             all_records = list(reader)
    #             print(f"Records: {all_records}")
    #
    # Note: This is much cleaner than using indices!
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    print("Writing CSV files")
    exercise_a()
    exercise_b()

    print("\n=== {{PHASE_2_TITLE}} ===")
    print("Reading CSV files")
    exercise_c()
    exercise_d()

    print("\n=== {{PHASE_3_TITLE}} ===")
    print("DictReader and DictWriter")
    exercise_e()
    exercise_f()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print()
    print("CSV Summary:")
    print("  Basic:")
    print("    csv.writer(f).writerow(list)     # Write one row")
    print("    csv.writer(f).writerows(lists)   # Write many rows")
    print("    csv.reader(f)                    # Read rows as lists")
    print()
    print("  With dicts:")
    print("    csv.DictWriter(f, fieldnames)    # Write dicts as rows")
    print("    csv.DictReader(f)                # Read rows as dicts")
    print()
    print("  Remember: newline='' when opening for write on Windows!")


main()
