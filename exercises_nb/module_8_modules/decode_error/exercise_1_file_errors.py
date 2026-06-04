# %% [markdown]
# {{CONTEXT_DECODE_ERROR_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לזהות ולתקן שגיאות נפוצות שקשורות לקבצים:
# `FileNotFoundError`, `PermissionError`, ועוד.
#
# נושא: פענוח שגיאות קבצים (File I/O)
# רמת קושי: 2-3
#
# ## {{ERROR_1_TITLE}}
# {{CONTEXT_ERROR_1_NARRATIVE}}
#
# השגיאה הנפוצה ביותר: מנסים לקרוא קובץ שלא קיים.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "read_data.py", line 3, in <module>
#     with open("nonexistent_file.txt", "r") as f:
# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'

# %%
# Trying to read a file that doesn't exist
with open("nonexistent_file.txt", "r") as f:
    content = f.read()
print(content)

# %% [markdown]
# קודם כל, הסבירי מה גרם לשגיאה:
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_1}}
#
# אפשרות תיקון 1: בדקי אם הקובץ קיים לפני הפתיחה
#   import os
#   if os.path.exists("data.txt"):
#       with open("data.txt", "r") as f:
#           content = f.read()
#
# אפשרות תיקון 2: השתמשי ב-`try/except` כדי לטפל בשגיאה
#   try:
#       with open("data.txt", "r") as f:
#           content = f.read()
#   except FileNotFoundError:
#       content = "File not found, using default"
#
# בחרי גישה אחת וכתבי את הקוד המתוקן:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_2_TITLE}}
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# שוכחים לטפל במצב שבו תיקייה לא קיימת.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "save_data.py", line 2, in <module>
#     with open("data/output.txt", "w") as f:
# FileNotFoundError: [Errno 2] No such file or directory: 'data/output.txt'

# %%
# Trying to write to a file in a directory that doesn't exist
with open("data/output.txt", "w") as f:
    f.write("Some data")

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_2}}
#
# התיקייה `"data"` לא קיימת! פייתון לא יוצרת תיקיות באופן אוטומטי כשכותבים קבצים.
#
# תיקון: צרי את התיקייה קודם (אם צריך)
#   import os
#   os.makedirs("data", exist_ok=True)  # exist_ok prevents error if exists
#   with open("data/output.txt", "w") as f:
#       f.write("Some data")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_3_TITLE}}
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# פותחים קובץ במצב לא נכון.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "update_data.py", line 3, in <module>
#     f.write("New line
# ")
# io.UnsupportedOperation: not writable

# %%
# Opened file for reading but trying to write
with open("data.txt", "r") as f:  # "r" = read mode!
    f.write("New line\n")

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_3}}
#
# הקובץ נפתח במצב קריאה (`"r"`) אבל ניסינו לכתוב לתוכו.
#
# תיקון: השתמשי במצב הנכון
#   `"w"` - כתיבה (מוחקת את תוכן הקובץ)
#   `"a"` - הוספה לסוף
#   `"r+"` - קריאה וכתיבה
#
# אם רוצים להוסיף לסוף הקובץ:
#   with open("data.txt", "a") as f:
#       f.write("New line\n")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_4_TITLE}}
# {{CONTEXT_ERROR_4_NARRATIVE}}
#
# משתמשים באובייקט הקובץ אחרי שבלוק ה-`with` סגר אותו.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "read_later.py", line 5, in <module>
#     content = f.read()
# ValueError: I/O operation on closed file.

# %%
with open("data.txt", "r") as f:
    first_line = f.readline()
# File is closed here!
content = f.read()  # Error: file is closed
print(content)

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_4}}
#
# כשבלוק ה-`with` מסתיים, הקובץ נסגר אוטומטית.
# כל פעולות הקובץ חייבות להתרחש בתוך בלוק ה-`with`.
#
# תיקון: בצעי את כל פעולות הקובץ בתוך בלוק ה-`with`
#   with open("data.txt", "r") as f:
#       first_line = f.readline()
#       content = f.read()  # Still inside the block!
#   print(content)  # Can print outside, just can't read more

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_5_TITLE}}
# {{CONTEXT_ERROR_5_NARRATIVE}}
#
# שוכחים להשתמש בקידוד הנכון.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "read_unicode.py", line 2, in <module>
#     content = f.read()
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 123: character maps to <undefined>

# %%
# File contains UTF-8 text but default encoding is different
with open("unicode_file.txt", "r") as f:
    content = f.read()

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_5}}
#
# הקובץ מכיל תווים מיוחדים (כמו אמוג'ים או אותיות עם ניקוד)
# שמקודדים ב-UTF-8, אבל פייתון ניסתה לקרוא אותו עם קידוד שונה.
#
# תיקון: ציינו את קידוד UTF-8 במפורש
#   with open("unicode_file.txt", "r", encoding="utf-8") as f:
#       content = f.read()
#
# > רמז: תמיד ציינו `encoding="utf-8"` לקבצי טקסט — זה חוסך הרבה כאבי ראש!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_DECODE_ERROR_INTRO}}")
print("=" * 50)
print()
print("For each exercise:")
print("1. Read the error message carefully")
print("2. Identify what caused the error")
print("3. Fix the code in the fix_code_X function")
print()

print("=== {{ERROR_1_TITLE}} ===")
print("FileNotFoundError - file doesn't exist")
# Uncomment to test after fixing:
# fix_code_a()

print("\n=== {{ERROR_2_TITLE}} ===")
print("FileNotFoundError - directory doesn't exist")
# fix_code_b()

print("\n=== {{ERROR_3_TITLE}} ===")
print("UnsupportedOperation - wrong file mode")
# fix_code_c()

print("\n=== {{ERROR_4_TITLE}} ===")
print("ValueError - file already closed")
# fix_code_d()

print("\n=== {{ERROR_5_TITLE}} ===")
print("UnicodeDecodeError - encoding mismatch")
# fix_code_e()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
print()
print("Key takeaways:")
print("  1. Always handle FileNotFoundError for reads")
print("  2. Create directories before writing to them")
print("  3. Use correct mode: 'r', 'w', 'a', 'r+'")
print("  4. Do all I/O inside the 'with' block")
print("  5. Use encoding='utf-8' for text files")
