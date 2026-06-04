# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# תרגיל מסכם: בני מערכת ניהול נתונים מלאה עבור {{school}}.
#
# הפרויקט הזה משלב את כל מה שלמדנו במודול 8:
# - מודולים מהספרייה הסטנדרטית (`datetime`, `random`)
# - קריאה וכתיבה לקבצים עם context managers
# - `JSON` לאחסון נתונים מובנים
# - `CSV` לייצוא נתונים
# - טיפול בשגיאות לאורך כל הקוד
#
# מושגי תכנות: שילוב מלא של מודולים, קבצים, JSON ו-CSV
# רמת קושי: 5 (מסכם)

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
# ## חלק 1: צמיחה - עיצוב מבנה הנתונים
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# עצבי את מודל הנתונים עבור מערכת ניהול הסטודנטים של {{school}}.
#
# צרי מילון סטודנט עם השדות הבאים:
# ```
# {
#     "id": generate_id(),  # מזהה ייחודי
#     "name": name,
#     "house": house,
#     "year": year,
#     "enrolled_date": str(date.today()),
#     "abilities": [],
#     "grades": {},
#     "achievements": [],
#     "status": "active"
# }
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי במודולים `random` ו-`string`:
# ```
# letters = ''.join(random.choices(string.ascii_uppercase, k=3))
# numbers = ''.join(random.choices(string.digits, k=3))
# return f"STU-{letters}{numbers}"
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# צרי מילון קורס עם השדות הבאים:
# ```
# {
#     "id": f"CRS-{...}",
#     "name": name,
#     "instructor": instructor,
#     "max_students": max_students,
#     "enrolled_students": [],
#     "schedule": {}
# }
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - פעולות CRUD
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# מימשי פעולות יצירה, קריאה, עדכון ומחיקה עבור סטודנטים.
#
# 1. וודאי שקיימת רשימת `"students"` במסד הנתונים:
#    `if "students" not in database: database["students"] = []`
# 2. בדקי שאין מזהה כפול
# 3. הוסיפי את הסטודנט להחזירי את המזהה שלו

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# עברי בלולאה על `database["students"]` והחזירי את הסטודנט שה-`id` שלו תואם.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. מצאי את הסטודנט
# 2. אם נמצא, עדכני את השדות: `student.update(updates)`
# 3. החזירי אם הפעולה הצליחה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# מצאי את הסטודנט והסירי אותו מהרשימה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# אם אין פילטרים — החזירי את כל הסטודנטים. אם יש פילטרים — החזירי רק את אלה שמתאימים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - שמירת נתונים ב-JSON
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# שמרי וטעני את מסד הנתונים בעזרת `JSON`.
#
# 1. הוסיפי מטא-דאטה:
#    ```
#    database["_metadata"] = {
#        "last_saved": str(datetime.now()),
#        "version": "1.0"
#    }
#    ```
# 2. שמרי עם טיפול בשגיאות:
#    ```
#    try:
#        with open(filename, "w") as f:
#            json.dump(database, f, indent=2)
#        return True
#    except Exception as e:
#        print(f"Save error: {e}")
#        return False
#    ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# נסי לטעון את הקובץ. אם נכשל — החזירי מסד נתונים ריק:
# `{"students": [], "courses": [], "_metadata": {}}`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. צרי שם לקובץ הגיבוי: `backup_name = f"{filename}.{date.today()}.backup"`
# 2. קראי את הקובץ המקורי וכתבי אותו לגיבוי

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: צמיחה - ייצוא ל-CSV
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# ייצאי נתונים לקובץ `CSV` לצורך דוחות.
#
# 1. קבלי את רשימת הסטודנטים
# 2. הגדירי את שמות העמודות לייצוא:
#    `fieldnames = ["id", "name", "house", "year", "status", "enrolled_date"]`
# 3. כתבי את ה-`CSV` עם `DictWriter`
#    > רמז: `extrasaction='ignore'` מדלג על שדות שאינם ב-`fieldnames`
# 4. החזירי את מספר השורות שנוצרו

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# צרי שורה לכל סטודנט עם הציונים שלו.
# פורמט: `name`, `course1`, `course2`, `average`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חשבי ואספי את הנתונים הבאים:
# - סה"כ סטודנטים
# - סטודנטים לפי בית/קבוצה
# - סטודנטים לפי שנת לימוד
# - פעילים מול לא פעילים
# - סה"כ קורסים

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 5: שיפור - טיפול מקצועי בשגיאות
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# הוסיפי טיפול מקיף בשגיאות.
#
# עטפי פעולה ב-`try/except`:
# ```
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
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# בדקי שדות חובה: `id`, `name`, `house`, `year`
# - אם תקין: החזירי `(True, [])`
# - אם חסר שדה: החזירי `(False, ["Missing field: name"])`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. נסי לטעון את קובץ הגיבוי
# 2. אמתי את תקינות הנתונים
# 3. שמרי לקובץ הראשי
# 4. טפלי בשגיאות בצורה נאותה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## הרצת המערכת - הדגמה

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
