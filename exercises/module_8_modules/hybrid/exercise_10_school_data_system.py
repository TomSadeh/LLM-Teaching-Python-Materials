"""
{{CONTEXT_PROJECT_INTRO}}

CAPSTONE EXERCISE: Build a complete data management system for {{school}}.

This comprehensive project combines everything from Module 8:
- Standard library modules (datetime, random)
- File I/O with context managers
- JSON for structured data storage
- CSV for data export
- Error handling throughout

Programming concepts: Full integration of modules, files, JSON, CSV
Difficulty: 5 (Capstone)
"""

import json
import csv
from datetime import date, datetime
import random
import string


# ============================================================
# PART 1: Growth - Design Data Structure
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Design the data model for {{school}}'s student management system.


def create_student(name, house, year=1):
    """
    Create a new student record.

    Args:
        name: Student's name
        house: Student's house/team
        year: Academic year (1-7)

    Returns:
        dict: Complete student record with all fields
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a student dict with:
    # {
    #     "id": generate_id(),  # Unique identifier
    #     "name": name,
    #     "house": house,
    #     "year": year,
    #     "enrolled_date": str(date.today()),
    #     "abilities": [],
    #     "grades": {},
    #     "achievements": [],
    #     "status": "active"
    # }
    pass


def generate_id():
    """
    Generate a unique student ID.

    Returns:
        str: ID like "STU-ABC123"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use random and string modules:
    # letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    # numbers = ''.join(random.choices(string.digits, k=3))
    # return f"STU-{letters}{numbers}"
    pass


def create_course(name, instructor, max_students=30):
    """
    Create a course record.

    Args:
        name: Course name
        instructor: Instructor name
        max_students: Maximum enrollment

    Returns:
        dict: Course record
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # {
    #     "id": f"CRS-{...}",
    #     "name": name,
    #     "instructor": instructor,
    #     "max_students": max_students,
    #     "enrolled_students": [],
    #     "schedule": {}
    # }
    pass


# ============================================================
# PART 2: Growth - Implement CRUD Operations
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Create, Read, Update, Delete operations for students.


def add_student(database, student):
    """
    Add a student to the database.

    Args:
        database: Database dict with "students" key
        student: Student dict to add

    Returns:
        str: Student ID if successful, None if error
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Ensure "students" list exists:
    #         if "students" not in database:
    #             database["students"] = []
    #
    # Step 2: Check for duplicate ID
    #
    # Step 3: Append student and return ID
    pass


def find_student(database, student_id):
    """
    Find a student by ID.

    Args:
        database: Database dict
        student_id: ID to search for

    Returns:
        dict: Student record or None if not found
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Loop through database["students"]
    # Return student if id matches
    pass


def update_student(database, student_id, updates):
    """
    Update a student's information.

    Args:
        database: Database dict
        student_id: ID of student to update
        updates: Dict of fields to update

    Returns:
        bool: True if updated, False if not found
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Find the student
    #
    # Step 2: If found, update fields:
    #         student.update(updates)
    #
    # Step 3: Return success status
    pass


def delete_student(database, student_id):
    """
    Remove a student from the database.

    Args:
        database: Database dict
        student_id: ID of student to remove

    Returns:
        bool: True if deleted, False if not found
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Find and remove the student from the list
    pass


def list_students(database, filters=None):
    """
    List students, optionally filtered.

    Args:
        database: Database dict
        filters: Optional dict of {field: value} to filter by

    Returns:
        list: Matching students
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # If no filters, return all students
    # If filters, return matching students
    pass


# ============================================================
# PART 3: Growth - JSON Persistence
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Save and load the database using JSON.


def save_database(database, filename="school_data.json"):
    """
    Save the database to a JSON file.

    Args:
        database: Database dict
        filename: Output file path

    Returns:
        bool: True if successful
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Add metadata:
    #         database["_metadata"] = {
    #             "last_saved": str(datetime.now()),
    #             "version": "1.0"
    #         }
    #
    # Step 2: Save with error handling:
    #         try:
    #             with open(filename, "w") as f:
    #                 json.dump(database, f, indent=2)
    #             return True
    #         except Exception as e:
    #             print(f"Save error: {e}")
    #             return False
    pass


def load_database(filename="school_data.json"):
    """
    Load the database from a JSON file.

    Args:
        filename: Input file path

    Returns:
        dict: Database, or empty database if error
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Try to load, return empty database on error:
    # {"students": [], "courses": [], "_metadata": {}}
    pass


def create_backup(filename="school_data.json"):
    """
    Create a backup of the database file.

    Args:
        filename: File to backup

    Returns:
        str: Backup filename, or None if error
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Generate backup filename:
    #         backup_name = f"{filename}.{date.today()}.backup"
    #
    # Step 2: Read original and write backup
    pass


# ============================================================
# PART 4: Growth - CSV Export
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Export data to CSV for reporting.


def export_students_csv(database, filename="students_export.csv"):
    """
    Export student list to CSV.

    Args:
        database: Database dict
        filename: Output CSV path

    Returns:
        int: Number of records exported
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Get students
    #
    # Step 2: Define fieldnames for export:
    #         fieldnames = ["id", "name", "house", "year", "status", "enrolled_date"]
    #
    # Step 3: Write CSV with DictWriter
    #         Note: extrasaction='ignore' skips fields not in fieldnames
    #
    # Step 4: Return count
    pass


def export_grade_report(database, filename="grades_report.csv"):
    """
    Export a grade report to CSV.

    Args:
        database: Database dict
        filename: Output CSV path

    Returns:
        int: Number of records exported
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a row per student with their grades
    # Format: name, course1, course2, average
    pass


def generate_statistics_report(database):
    """
    Generate statistics about the database.

    Returns:
        dict: Statistics summary
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Calculate:
    # - Total students
    # - Students per house
    # - Students per year
    # - Active vs inactive
    # - Total courses
    pass


# ============================================================
# PART 5: Improvement - Production Error Handling
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Add comprehensive error handling for production use.


def safe_operation(operation, *args, default=None, **kwargs):
    """
    Wrapper to safely execute any database operation.

    Args:
        operation: Function to call
        *args: Arguments for the function
        default: Value to return on error
        **kwargs: Keyword arguments for the function

    Returns:
        Result of operation, or default if error
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Wrap operation in try/except:
    # try:
    #     return operation(*args, **kwargs)
    # except FileNotFoundError:
    #     print(f"File not found")
    #     return default
    # except json.JSONDecodeError:
    #     print("Data corruption detected")
    #     return default
    # except Exception as e:
    #     print(f"Operation failed: {e}")
    #     return default
    pass


def validate_student(student):
    """
    Validate a student record has required fields.

    Args:
        student: Student dict to validate

    Returns:
        tuple: (is_valid: bool, errors: list)
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Check required fields: id, name, house, year
    # Return (True, []) if valid
    # Return (False, ["Missing field: name"]) if invalid
    pass


def recover_from_backup(primary_file, backup_file):
    """
    Attempt to recover database from backup.

    Args:
        primary_file: Main database file
        backup_file: Backup file to restore from

    Returns:
        bool: True if recovery successful
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Try to load backup
    # Step 2: Validate backup data
    # Step 3: Save to primary file
    # Step 4: Handle errors gracefully
    pass


# ============================================================
# MAIN - System Demo
# ============================================================

def run_demo():
    """Run a demonstration of the complete system."""
    print("=" * 60)
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("{{school}} Data Management System - CAPSTONE")
    print("=" * 60)
    print()

    # Initialize database
    db = {"students": [], "courses": []}

    print(">>> Creating sample data...")
    # Uncomment to test:
    # student1 = create_student("{{hero}}", "{{house}}", 5)
    # student2 = create_student("{{heroine}}", "{{house}}", 5)
    # student3 = create_student("{{friend}}", "{{house}}", 4)
    # add_student(db, student1)
    # add_student(db, student2)
    # add_student(db, student3)
    # print(f"Added {len(db['students'])} students")
    print()

    print(">>> Testing CRUD operations...")
    # Uncomment to test:
    # found = find_student(db, student1["id"])
    # print(f"Found student: {found['name']}")
    # update_student(db, student1["id"], {"year": 6})
    # print(f"Updated year to: {find_student(db, student1['id'])['year']}")
    print()

    print(">>> Saving to JSON...")
    # Uncomment to test:
    # save_database(db, "demo_school.json")
    # print("Database saved!")
    print()

    print(">>> Exporting to CSV...")
    # Uncomment to test:
    # count = export_students_csv(db, "demo_students.csv")
    # print(f"Exported {count} students to CSV")
    print()

    print(">>> Generating statistics...")
    # Uncomment to test:
    # stats = generate_statistics_report(db)
    # print(f"Statistics: {stats}")
    print()

    print("=" * 60)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print()
    print("Capstone Complete! You've built a full data management system")
    print("using modules, file I/O, JSON, CSV, and error handling.")
    print("=" * 60)


def main():
    run_demo()


if __name__ == "__main__":
    main()
