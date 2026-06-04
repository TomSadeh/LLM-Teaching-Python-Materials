# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# CAPSTONE EXERCISE: Build a complete data management system for {{school}}.
#
# This comprehensive project combines everything from Module 8:
# - Standard library modules (datetime, random)
# - File I/O with context managers
# - JSON for structured data storage
# - CSV for data export
# - Error handling throughout
#
# Programming concepts: Full integration of modules, files, JSON, CSV
# Difficulty: 5 (Capstone)

# %%
import json

# %%
import csv

# %%
from datetime import date, datetime

# %%
import random

# %%
import string

# %% [markdown]
# PART 1: Growth - Design Data Structure
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Design the data model for {{school}}'s student management system.
#
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

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Use random and string modules:
# letters = ''.join(random.choices(string.ascii_uppercase, k=3))
# numbers = ''.join(random.choices(string.digits, k=3))
# return f"STU-{letters}{numbers}"

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
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

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 2: Growth - Implement CRUD Operations
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Create, Read, Update, Delete operations for students.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Ensure "students" list exists:
#         if "students" not in database:
#             database["students"] = []
#
# Step 2: Check for duplicate ID
#
# Step 3: Append student and return ID

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Loop through database["students"]
# Return student if id matches

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Find the student
#
# Step 2: If found, update fields:
#         student.update(updates)
#
# Step 3: Return success status

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Find and remove the student from the list

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# If no filters, return all students
# If filters, return matching students

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Growth - JSON Persistence
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Save and load the database using JSON.
#
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

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Try to load, return empty database on error:
# {"students": [], "courses": [], "_metadata": {}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Generate backup filename:
#         backup_name = f"{filename}.{date.today()}.backup"
#
# Step 2: Read original and write backup

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 4: Growth - CSV Export
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Export data to CSV for reporting.
#
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

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Create a row per student with their grades
# Format: name, course1, course2, average

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Calculate:
# - Total students
# - Students per house
# - Students per year
# - Active vs inactive
# - Total courses

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 5: Improvement - Production Error Handling
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Add comprehensive error handling for production use.
#
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

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Check required fields: id, name, house, year
# Return (True, []) if valid
# Return (False, ["Missing field: name"]) if invalid

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Try to load backup
# Step 2: Validate backup data
# Step 3: Save to primary file
# Step 4: Handle errors gracefully

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN - System Demo

# %%
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

# %%
run_demo()
