# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# ## תרגיל מרובה-חלקים: {{hero}} בונה מערכת שמירת נתונים עבור {{school}}.
# # תלמדי לשמור ולטעון נתוני התקדמות בקבצי טקסט,
# # להבין שגיאות נפוצות ולהוסיף טיפול נכון בשגיאות.
#
# # מושגי תכנות: קריאה וכתיבה לקבצים, מנהלי הקשר, טיפול בשגיאות
# # רמת קושי: 2-3
#
# ## חלק 1: צמיחה — שמירת נתונים לקבצים
# # {{CONTEXT_GROWTH_INTRO}}
# # {{CONTEXT_GROWTH_NARRATIVE}}
#
# # למדי לשמור סוגים שונים של נתונים לקבצי טקסט.
#
# 1. פתחי קובץ לכתיבה:
#    `with open(filename, "w") as f:`
#
# 2. כתבי כל שדה בשורה נפרדת:
#    `f.write(f"NAME: {name}\n")`
#    `f.write(f"LEVEL: {level}\n")`
#    `f.write(f"ABILITIES: {', '.join(abilities)}\n")`
#
# 3. הדפיסי הודעת אישור

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. פתחי קובץ לכתיבה
#
# 2. עברי על מילון הציונים:
#    `for name, score in scores.items():`
#        `f.write(f"{name}: {score}\n")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה — טעינת נתונים מקבצים
# # {{CONTEXT_GROWTH_INTRO}}
# # {{CONTEXT_GROWTH_NARRATIVE}}
#
# # למדי לקרוא ולנתח נתונים מקבצי טקסט.
#
# 1. אתחלי מילון פרופיל ריק
#
# 2. פתחי וקראי את הקובץ:
#    `with open(filename, "r") as f:`
#        `for line in f:`
#            `# נתחי כל שורה`
#
# 3. נתחי את שורת ה-NAME:
#    `if line.startswith("NAME:"):`
#        `profile["name"] = line.replace("NAME:", "").strip()`
#
# 4. נתחי את שורת ה-LEVEL (המירי ל-`int`):
#    `if line.startswith("LEVEL:"):`
#        `profile["level"] = int(line.replace("LEVEL:", "").strip())`
#
# 5. נתחי את שורת ה-ABILITIES (פצלי לרשימה):
#    `if line.startswith("ABILITIES:"):`
#        `abilities_str = line.replace("ABILITIES:", "").strip()`
#        `profile["abilities"] = [a.strip() for a in abilities_str.split(",")]`
#
# 6. החזירי את מילון הפרופיל

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. אתחלי מילון ציונים ריק
#
# 2. פתחי וקראי את הקובץ
#
# 3. נתחי כל שורה:
#    `for line in f:`
#        `if ":" in line:`
#            `name, score = line.split(":")`
#            `scores[name.strip()] = int(score.strip())`
#
# 4. החזירי את מילון הציונים

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: חקירה — הבנת שגיאות קבצים
# # {{CONTEXT_INVESTIGATION_INTRO}}
# # {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# # מה קורה כשדברים משתבשים?
#
# # הודעת שגיאה 1:
# # ----------------
# # Traceback (most recent call last):
# #   File "load_game.py", line 2, in <module>
# #     with open("save_data.txt", "r") as f:
# # FileNotFoundError: [Errno 2] No such file or directory: 'save_data.txt'
#
# # הודעת שגיאה 2:
# # ----------------
# # Traceback (most recent call last):
# #   File "parse_score.py", line 5, in <module>
# #     score = int(line.strip())
# # ValueError: invalid literal for int() with base 10: 'not_a_number'
#
# 1. הסבירי את `FileNotFoundError`:
#    `print("FileNotFoundError occurs when:")`
#    `print("  - The file path is wrong")`
#    `print("  - The file was deleted")`
#    `print("  - The file was never created")`
#
# 2. הסבירי את `ValueError` בעת ניתוח הנתונים:
#    `print("\nValueError during int() occurs when:")`
#    `print("  - The file format is corrupted")`
#    `print("  - The data isn't what we expected")`
#    `print("  - Extra whitespace or characters")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: שיפור — טעינה בטוחה עם טיפול בשגיאות
# # {{CONTEXT_IMPROVEMENT_INTRO}}
# # {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# # הוסיפי טיפול בשגיאות כדי להפוך את המערכת לאמינה.
#
# 1. קבעי ברירת מחדל אם לא סופקה:
#    `if default is None:`
#        `default = {"name": "Unknown", "level": 1, "abilities": []}`
#
# 2. נסי לטעון:
#    `try:`
#        `profile = load_profile(filename)`
#        `return profile`
#    `except FileNotFoundError:`
#        `print(f"No save file found: {filename}")`
#        `return default`
#    `except ValueError as e:`
#        `print(f"Save file corrupted: {e}")`
#        `return default`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# # טפלי ב-`FileNotFoundError` והחזירי `{}` כברירת מחדל

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. אם `backup` הוא `True`, שנמי שם לקובץ הישן:
#    `import os`
#    `if os.path.exists(filename) and backup:`
#        `os.rename(filename, filename + ".backup")`
#
# 2. שמרי את הפרופיל החדש
#
# 3. הדפיסי הודעת אישור

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Data Persistence for {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Saving Data")
print("-" * 40)
# Uncomment to test:
# save_profile(
#     "hero_save.txt",
#     "{{hero}}",
#     5,
#     ["{{spell1}}", "{{spell2}}"]
# )
# save_high_scores(
#     "scores.txt",
#     {"{{hero}}": 1000, "{{heroine}}": 1200, "{{friend}}": 800}
# )
print()

print(">>> PART 2: Loading Data")
print("-" * 40)
# Uncomment to test:
# profile = load_profile("hero_save.txt")
# print(f"Loaded profile: {profile}")
# scores = load_high_scores("scores.txt")
# print(f"Loaded scores: {scores}")
print()

print(">>> PART 3: Understanding Errors")
print("-" * 40)
explain_file_errors()
print()

print(">>> PART 4: Safe Loading")
print("-" * 40)
# Uncomment to test:
# profile = safe_load_profile("nonexistent.txt")
# print(f"Safe load result: {profile}")
# profile = safe_load_profile("hero_save.txt")
# print(f"Safe load result: {profile}")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
