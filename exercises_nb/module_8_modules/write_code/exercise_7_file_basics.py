# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לקרוא מקבצים ולכתוב אליהם
# באמצעות הכלים המובנים של Python לטיפול בקבצים.
# זה חיוני לשמירת נתונים, טעינת הגדרות ועבודה עם מידע חיצוני.
#
# נושא: קלט/פלט קבצים עם מנהלי הקשר
# רמת קושי: 2-3
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# למדי את משפט `with` (מנהל הקשר) לטיפול בטוח בקבצים.
#
# כתבי טקסט לקובץ באמצעות מנהל הקשר.
#
# 1. השתמשי ב-`with open()` כדי לפתוח קובץ לכתיבה:
#         with open("greeting.txt", "w") as f:
#             # פעולות על הקובץ כאן
#
# 2. כתבי הודעת ברכה:
#         f.write("Welcome to {{school}}!\n")
#         f.write("Greetings, {{hero}}.\n")
#
# 3. הקובץ נסגר אוטומטית כשבלוק ה-`with` מסתיים!
#
# 4. הדפיסי: `"File 'greeting.txt' created successfully!"`
#
# מצבי פתיחת קובץ:
#   `"w"` = כתיבה (יוצר קובץ חדש או מחליף קיים)
#   `"r"` = קריאה (ברירת מחדל)
#   `"a"` = הוספה לסוף

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# קראי טקסט מהקובץ שיצרת זה עתה.
#
# 1. פתחי את הקובץ לקריאה:
#         with open("greeting.txt", "r") as f:
#
# 2. קראי את כל התוכן בבת אחת:
#         content = f.read()
#
# 3. הדפיסי את התוכן:
#         print("File content:")
#         print(content)
#
# > רמז: אחרי בלוק ה-`with`, הקובץ נסגר אוטומטית

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# למדי דרכים שונות לקריאת קבצים.
#
# ראשית, צרי קובץ עם כמה שורות.
#
# 1. צרי קובץ עם שורות ממוספרות:
#         with open("lines.txt", "w") as f:
#             for i in range(1, 6):
#                 f.write(f"Line {i}: {{spell1}}\n")
#
# 2. קראי והדפיסי באמצעות `readlines()`:
#         with open("lines.txt", "r") as f:
#             lines = f.readlines()  # מחזירה רשימה של שורות
#
# 3. הדפיסי כל שורה עם האינדקס שלה:
#         for i, line in enumerate(lines):
#             print(f"{i}: {line.strip()}")  # strip() מסיר את \n
#
# > רמז: `readlines()` כוללת את תו השורה החדשה `\n`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# קראי קובץ שורה אחר שורה (יעיל יותר בזיכרון לקבצים גדולים).
#
# 1. פתחי את הקובץ:
#         with open("lines.txt", "r") as f:
#
# 2. עברי ישירות על אובייקט הקובץ:
#             for line in f:
#                 print(line.strip())
#
# זו הדרך הכי פייתונית לקרוא קבצים שורה אחר שורה.
# היא לא טוענת את כל הקובץ לזיכרון בבת אחת.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# למדי להוסיף לקבצים קיימים ולעבוד עם נתיבי קבצים.
#
# הוסיפי תוכן לקובץ קיים.
#
# 1. פתחי במצב הוספה `"a"`:
#         with open("greeting.txt", "a") as f:
#             f.write("\nNew message added!\n")
#             f.write("From {{heroine}}.\n")
#
# 2. קראי את הקובץ כדי לוודא:
#         with open("greeting.txt", "r") as f:
#             print(f.read())
#
# > רמז: מצב `"a"` מוסיף לסוף, מצב `"w"` מחליף את כל התוכן!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# צרי פונקציה לשמירת רשימה בקובץ.
#
# 1. צרי רשימת פריטים:
#         inventory = ["{{item}}", "potion", "scroll", "gem", "key"]
#
# 2. כתבי כל פריט לקובץ (אחד בכל שורה):
#         with open("inventory.txt", "w") as f:
#             for item in inventory:
#                 f.write(item + "\n")
#
# 3. קראי את הקובץ בחזרה לרשימה:
#         with open("inventory.txt", "r") as f:
#             loaded = []
#             for line in f:
#                 loaded.append(line.strip())
#
# 4. הדפיסי את שתי הרשימות כדי לוודא שהן זהות:
#         print(f"Original: {inventory}")
#         print(f"Loaded: {loaded}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print("Writing and reading files with 'with' statement")
exercise_a()
exercise_b()

print("\n=== {{PHASE_2_TITLE}} ===")
print("Different ways to read files")
exercise_c()
exercise_d()

print("\n=== {{PHASE_3_TITLE}} ===")
print("Appending and saving lists")
exercise_e()
exercise_f()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print()
print("File I/O Summary:")
print("  with open(file, 'w') as f:  # Write (overwrite)")
print("  with open(file, 'r') as f:  # Read")
print("  with open(file, 'a') as f:  # Append")
print("  f.read()       # Read all content")
print("  f.readlines()  # Read as list of lines")
print("  f.write(text)  # Write text")
