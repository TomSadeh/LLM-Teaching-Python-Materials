# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לעבוד עם קבצי CSV (Comma-Separated Values)
# באמצעות מודול `csv` של פייתון. CSV מתאים בצורה מושלמת לנתונים
# טבלאיים עם שורות ועמודות, כמו גיליון אלקטרוני.
#
# נושא: יסודות מודול csv (reader, writer, DictReader, DictWriter)
# רמת קושי: 3

# %%
import csv

# %% [markdown]
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# תלמדי לכתוב נתונים לקבצי CSV.
#
# כתבי נתונים לקובץ CSV באמצעות `csv.writer`.
#
# 1. הכיני את הנתונים כרשימה של רשימות (שורות):
#         data = [
#             ["Name", "Level", "Ability"],  # Header row
#             ["{{hero}}", 5, "{{spell1}}"],
#             ["{{heroine}}", 7, "{{spell2}}"],
#             ["{{friend}}", 3, "{{spell1}}"]
#         ]
#
# 2. כתבי לקובץ CSV:
#         with open("characters.csv", "w", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerows(data)  # Write all rows at once
#
# 3. הדפיסי אישור שהקובץ נוצר.
#
# > רמז: `newline=""` חשוב על Windows כדי למנוע שורות ריקות!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# כתבי שורות אחת אחת באמצעות `writerow`.
#
# 1. צרי את הקובץ וכתבי כותרת:
#         with open("scores.csv", "w", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow(["Player", "Score", "Date"])
#
# 2. כתבי שורות בנפרד:
#             writer.writerow(["{{hero}}", 1000, "2024-01-15"])
#             writer.writerow(["{{heroine}}", 1500, "2024-01-16"])
#             writer.writerow(["{{friend}}", 750, "2024-01-14"])
#
# > רמז: `writerow()` לשורה אחת, `writerows()` לכמה שורות יחד.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# תלמדי לקרוא נתונים מקבצי CSV.
#
# קראי נתוני CSV באמצעות `csv.reader`.
#
# 1. פתחי וקראי את הקובץ:
#         with open("characters.csv", "r") as f:
#             reader = csv.reader(f)
#
# 2. עברי על השורות:
#             for row in reader:
#                 print(row)  # Each row is a list
#
# 3. גשי לעמודות ספציפיות:
#             # Reset to beginning
#         with open("characters.csv", "r") as f:
#             reader = csv.reader(f)
#             next(reader)  # Skip header row
#             for row in reader:
#                 name = row[0]
#                 level = int(row[1])  # CSV values are strings!
#                 print(f"{name} is level {level}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# קראי קובץ CSV כרשימה של רשימות.
#
# 1. טעיני את כל הקובץ לזיכרון:
#         with open("characters.csv", "r") as f:
#             reader = csv.reader(f)
#             all_rows = list(reader)
#
# 2. גשי לפי אינדקס:
#         header = all_rows[0]
#         data_rows = all_rows[1:]
#
#         print(f"Columns: {header}")
#         print(f"Number of records: {len(data_rows)}")
#
# 3. חפשי שורה ספציפית:
#         for row in data_rows:
#             if row[0] == "{{hero}}":
#                 print(f"Found: {row}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# תלמדי להשתמש ב-`DictReader` וב-`DictWriter` לגישה נוחה יותר לעמודות.
#
# השתמשי ב-`DictWriter` כדי לכתוב מילונים כשורות.
#
# 1. הגדירי את שמות השדות (כותרות העמודות):
#         fieldnames = ["name", "level", "ability", "active"]
#
# 2. צרי רשימה של מילונים:
#         records = [
#             {"name": "{{hero}}", "level": 5, "ability": "{{spell1}}", "active": True},
#             {"name": "{{heroine}}", "level": 7, "ability": "{{spell2}}", "active": True},
#             {"name": "{{friend}}", "level": 3, "ability": "{{spell1}}", "active": False}
#         ]
#
# 3. כתבי באמצעות `DictWriter`:
#         with open("roster.csv", "w", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()  # Write column names
#             writer.writerows(records)
#
# > רמז: `DictWriter` צריך את `fieldnames` כדי לדעת את סדר העמודות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`DictReader` כדי לקרוא שורות כמילונים.
#
# 1. קראי עם `DictReader`:
#         with open("roster.csv", "r") as f:
#             reader = csv.DictReader(f)
#
# 2. גשי לעמודות לפי שם:
#             for row in reader:
#                 print(f"{row['name']} - Level {row['level']}")
#
# 3. `DictReader` משתמש בשורה הראשונה כמפתחות אוטומטית!
#         with open("roster.csv", "r") as f:
#             reader = csv.DictReader(f)
#             print(f"Columns: {reader.fieldnames}")
#             # Convert to list of dicts
#             all_records = list(reader)
#             print(f"Records: {all_records}")
#
# > רמז: זה הרבה יותר נקי מאשר שימוש באינדקסים!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
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
