# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# בתרגיל הזה תבני מערכת הגדרות עבור {{school}}
# ששומרת את ההגדרות בין סשנים בעזרת JSON.
#
# מושגי תכנות: JSON, קריאה וכתיבה לקבצים, טיפול בשגיאות, ערכי ברירת מחדל
# רמת קושי: 3-4

# %%
import json

# %% [markdown]
# ## PART 1: Growth - Save Settings to JSON
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# למדי לשמור הגדרות תצורה לקובץ JSON.
#
# 1. פתחי את הקובץ לכתיבה:
#    `with open(filename, "w") as f:`
#
# 2. שמרי עם עיצוב מסודר:
#    `json.dump(settings, f, indent=2)`
#
# 3. החזירי `True`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# החזירי `dict` עם ערכי ברירת המחדל הבאים:
# ```
# {
#     "player_name": "{{hero}}",
#     "difficulty": "normal",
#     "music_enabled": True,
#     "volume": 80,
#     "language": "en",
#     "theme": "default",
#     "last_save": None,
#     "high_score": 0
# }
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## PART 2: Growth - Load Settings with Defaults
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# טעיני הגדרות ומלאי ערכים חסרים בברירות המחדל.
#
# 1. קבלי ברירות מחדל אם לא סופקו:
#    `if defaults is None:`
#    `    defaults = create_default_settings()`
#
# 2. התחילי עם עותק של ברירות המחדל:
#    `settings = defaults.copy()`
#
# 3. נסי לטעון את הקובץ ולעדכן את ההגדרות:
#    `try:`
#    `    with open(filename, "r") as f:`
#    `        loaded = json.load(f)`
#    `        settings.update(loaded)`
#    `except FileNotFoundError:`
#    `    pass  # Use defaults`
#    `except json.JSONDecodeError:`
#    `    print("Settings file corrupt, using defaults")`
#
# 4. החזירי את `settings`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי במתודה `dict.get()`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## PART 3: Investigation - Handling Corrupt Files
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# מה קורה כשקובץ ההגדרות פגום?
#
# הודעת שגיאה:
# ```
# Traceback (most recent call last):
#   File "load_config.py", line 3, in <module>
#     settings = json.load(f)
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
# ```
#
# זה קורה כאשר:
# 1. הקובץ ריק
# 2. הקובץ מכיל JSON לא תקין
# 3. הקובץ נפגם בזמן הכתיבה
#
# 1. נסי לפתוח את הקובץ.
#    אם `FileNotFoundError`: החזירי `("missing", "File not found")`
#
# 2. קראי את התוכן.
#    אם ריק: החזירי `("empty", "File is empty")`
#
# 3. נסי לנתח את ה-JSON.
#    אם `JSONDecodeError`: החזירי `("corrupt", "Invalid JSON")`
#
# 4. החזירי `("ok", "Settings file is valid")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## PART 4: Growth - Complete Settings Manager
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# בני מנהל הגדרות שלם עם כל הפיצ'רים.
#
# 1. צרי `dict` לאחסון:
#    `manager = {`
#    `    "filename": filename,`
#    `    "settings": load_settings(filename),`
#    `    "dirty": False  # Track unsaved changes`
#    `}`
#
# 2. צרי פונקציות עזר (מקוננות בתוך הפונקציה):
#
#    `def get(key, default=None):`
#    `    return manager["settings"].get(key, default)`
#
#    `def set_value(key, value):`
#    `    manager["settings"][key] = value`
#    `    manager["dirty"] = True`
#
#    `def save():`
#    `    save_settings(manager["filename"], manager["settings"])`
#    `    manager["dirty"] = False`
#
#    `def has_unsaved():`
#    `    return manager["dirty"]`
#
#    `def reset_to_defaults():`
#    `    manager["settings"] = create_default_settings()`
#    `    manager["dirty"] = True`
#
# 3. הוסיפי את הפונקציות ל-manager:
#    `manager["get"] = get`
#    `manager["set"] = set_value`
#    `manager["save"] = save`
#    `manager["has_unsaved"] = has_unsaved`
#    `manager["reset"] = reset_to_defaults`
#
# 4. החזירי את `manager`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# הדפיסי כל הגדרה בצורה מסודרת:
# `print("Current Settings:")`
# `print("-" * 30)`
# `for key, value in settings.items():`
# `    print(f"  {key}: {value}")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Settings Manager for {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Saving Settings")
print("-" * 40)
# Uncomment to test:
# defaults = create_default_settings()
# print("Default settings:")
# display_settings(defaults)
# save_settings("test_settings.json", defaults)
# print("\nSaved to test_settings.json")
print()

print(">>> PART 2: Loading Settings")
print("-" * 40)
# Uncomment to test:
# settings = load_settings("test_settings.json")
# print("Loaded settings:")
# display_settings(settings)
# print()
# # Test with missing file
# settings = load_settings("nonexistent.json")
# print("From missing file (defaults):")
# display_settings(settings)
print()

print(">>> PART 3: Diagnosing Files")
print("-" * 40)
# Uncomment to test:
# status, message = diagnose_settings_file("test_settings.json")
# print(f"test_settings.json: {status} - {message}")
# status, message = diagnose_settings_file("nonexistent.json")
# print(f"nonexistent.json: {status} - {message}")
print()

print(">>> PART 4: Settings Manager")
print("-" * 40)
# Uncomment to test:
# manager = create_settings_manager("game_settings.json")
# print(f"Current difficulty: {manager['get']('difficulty')}")
# print(f"Current volume: {manager['get']('volume')}")
# manager['set']('difficulty', 'hard')
# manager['set']('volume', 100)
# print(f"Has unsaved changes: {manager['has_unsaved']()}")
# manager['save']()
# print("Settings saved!")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
