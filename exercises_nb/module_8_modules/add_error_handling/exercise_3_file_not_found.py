# %% [markdown]
# {{CONTEXT_ERROR_HANDLING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: טיפול בשגיאת FileNotFoundError בצורה מסודרת
# רמת קושי: 3
#
# לפעמים הקבצים שמנסים לפתוח פשוט לא קיימים. כאן נלמד להתמודד עם זה
# בצורה חכמה — להחזיר ברירת מחדל, ליצור את הקובץ, או להודיע למשתמשת.
#
# {{HANDLING_1_TITLE}}
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# הפונקציה הזו קורסת אם הקובץ לא קיים.

# %%
with open("config.txt", "r") as f:
    return f.read()

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_1}}
#
# 1. נסי לפתוח ולקרוא את הקובץ
#
# 2. אם מתקבלת שגיאת `FileNotFoundError`, החזירי את `default_content`
#
# תבנית:
#   try:
#       with open(filename, "r") as f:
#           return f.read()
#   except FileNotFoundError:
#       return default_content

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_2_TITLE}}
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# הפונקציה הזו לא מטפלת בקבצים חסרים.

# %%
with open("items.txt", "r") as f:
    return [line.strip() for line in f]

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_2}}
#
# 1. טפלי ב-`None` כברירת מחדל (השתמשי ברשימה ריקה):
#         if default_list is None:
#             default_list = []
#
# 2. נסי לטעון את הקובץ
#
# 3. טפלי בשגיאת `FileNotFoundError`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_3_TITLE}}
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# יש ליצור את הקובץ עם ברירות מחדל אם הוא לא קיים.

# %%
with open("settings.txt", "r") as f:
    return f.read()

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_3}}
#
# 1. נסי לקרוא את הקובץ הקיים
#
# 2. אם מתקבלת שגיאת `FileNotFoundError`:
#         - צרי את הקובץ עם `default_config`
#         - הדפיסי הודעה על יצירת הקובץ החדש
#         - החזירי את `default_config`
#
# תבנית:
#   try:
#       with open(filename, "r") as f:
#           return f.read()
#   except FileNotFoundError:
#       with open(filename, "w") as f:
#           f.write(default_config)
#       print(f"Created new config: {filename}")
#       return default_config

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_4_TITLE}}
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# יש לטפל בכמה פעולות על קבצים בצורה בטוחה.

# %%
with open("source.txt", "r") as src:
    content = src.read()
with open("dest.txt", "w") as dst:
    dst.write(content)

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_4}}
#
# 1. נסי לקרוא את קובץ המקור
#
# 2. נסי לכתוב לקובץ היעד
#
# 3. טפלי בשגיאת `FileNotFoundError` עבור קובץ המקור
#
# 4. טפלי בשגיאת `PermissionError` עבור קובץ היעד
#
# 5. החזירי `True` בהצלחה ו-`False` בכישלון

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_5_TITLE}}
# {{CONTEXT_HANDLING_5_NARRATIVE}}
#
# בני טוען קבצים חזק ל-{{school}}.
#
# {{CONTEXT_HANDLING_HINT_5}}
#
# 1. עברי בלולאה על שמות הקבצים
#
# 2. נסי לקרוא כל קובץ
#
# 3. אם הצלחת, החזירי את התוכן מיד
#
# 4. אם קיבלת `FileNotFoundError`, המשיכי לקובץ הבא
#
# 5. אחרי הלולאה (כולם נכשלו), החזירי את ברירת המחדל
#
# תבנית:
#   for filename in filenames:
#       try:
#           with open(filename, "r") as f:
#               return f.read()
#       except FileNotFoundError:
#           continue
#   return default

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
print("=" * 50)

print("\n=== {{HANDLING_1_TITLE}} ===")
print("Reading with default:")
# content = safe_read_config("nonexistent.txt", "default value")
# print(f"  Result: {content}")

print("\n=== {{HANDLING_2_TITLE}} ===")
print("Loading list with default:")
# items = safe_load_list("nonexistent.txt", ["default1", "default2"])
# print(f"  Items: {items}")

print("\n=== {{HANDLING_3_TITLE}} ===")
print("Ensuring config exists:")
# config = ensure_config_exists("test_config.txt", "setting=value")
# print(f"  Config: {config}")

print("\n=== {{HANDLING_4_TITLE}} ===")
print("Safe file copy:")
# success = safe_copy_file("source.txt", "dest.txt")
# print(f"  Copy successful: {success}")

print("\n=== {{HANDLING_5_TITLE}} ===")
print("Loading with fallbacks:")
# content = load_with_fallbacks(["primary.txt", "backup.txt"], "default")
# print(f"  Content: {content}")

print("\n" + "=" * 50)
print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")
