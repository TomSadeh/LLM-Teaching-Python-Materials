# %% [markdown]
# {{CONTEXT_DECODE_ERROR_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי להבין ולתקן שגיאות הקשורות ל-JSON,
# ובמיוחד את `JSONDecodeError` שמופיעה כשמנסים לפרסר JSON לא תקין.
#
# נושא: פירוש שגיאות JSON
# רמת קושי: 3

# %%
import json

# %% [markdown]
# ## {{ERROR_1_TITLE}}
# {{CONTEXT_ERROR_1_NARRATIVE}}
#
# שגיאת JSON הנפוצה ביותר: תחביר JSON שגוי.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "load_config.py", line 3, in <module>
#     config = json.load(f)
# json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 2 column 5 (char 6)

# %%
# The file "config.json" contains:
# {
#     name: "{{hero}}"
# }
# Notice: 'name' should be "name" (double quotes required!)

with open("config.json", "r") as f:
    config = json.load(f)

# %% [markdown]
# {{CONTEXT_ERROR_HINT_1}}
#
# JSON דורשת גרשיים כפולים לכל המחרוזות והמפתחות!
# שלא כמו Python, אי אפשר להשתמש בגרשיים בודדים או במפתחות ללא גרשיים.
#
# שגוי: `{name: "value"}` — מפתח ללא גרשיים
# שגוי: `{"name": 'value'}` — גרשיים בודדים
# נכון: `{"name": "value"}` — גרשיים כפולים בכל מקום
#
# קודם, הסבירי מה גרם לשגיאה:
# השגיאה קרתה כי: _______________
#
# תיקון: תקני את תוכן קובץ ה-JSON, או טפלי בשגיאה:
#   try:
#       with open("config.json", "r") as f:
#           config = json.load(f)
#   except json.JSONDecodeError as e:
#       print(f"Invalid JSON: {e}")
#       config = {"default": "settings"}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_2_TITLE}}
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# פסיק עודף בסוף גורם לשגיאות JSON (שלא כמו ב-Python).
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "load_list.py", line 3, in <module>
#     data = json.load(f)
# json.decoder.JSONDecodeError: Expecting value: line 5 column 1 (char 42)

# %%
# The file "items.json" contains:
# {
#     "items": [
#         "{{spell1}}",
#         "{{spell2}}",
#     ]
# }
# Notice: Trailing comma after "{{spell2}}" is not allowed!

with open("items.json", "r") as f:
    data = json.load(f)

# %% [markdown]
# {{CONTEXT_ERROR_HINT_2}}
#
# JSON לא מאפשרת פסיק עודף בסוף (Python כן מאפשרת).
#
# שגוי: `["a", "b", "c",]` — פסיק עודף
# נכון: `["a", "b", "c"]` — ללא פסיק עודף
#
# זו טעות נפוצה כשמעתיקים קוד מ-Python!
#
# השגיאה קרתה כי: _______________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_3_TITLE}}
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# קבצים ריקים או קטועים גורמים לשגיאות JSON.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "load_save.py", line 3, in <module>
#     save_data = json.load(f)
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

# %%
# The file "save.json" is empty or corrupted (incomplete write)

with open("save.json", "r") as f:
    save_data = json.load(f)

# %% [markdown]
# {{CONTEXT_ERROR_HINT_3}}
#
# הקובץ ריק או לא מכיל JSON תקין.
# זה יכול לקרות אם:
# - לא נכתב כלום לקובץ
# - פעולת הכתיבה הופסקה באמצע
# - הקובץ נמחק בטעות
#
# השגיאה קרתה כי: _______________
#
# תיקון: בדקי אם הקובץ ריק, או טפלי בשגיאה:
#   try:
#       with open("save.json", "r") as f:
#           content = f.read()
#           if not content.strip():
#               save_data = {}  # Default for empty file
#           else:
#               save_data = json.loads(content)
#   except json.JSONDecodeError:
#       save_data = {}  # Default for corrupt file

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_4_TITLE}}
# {{CONTEXT_ERROR_4_NARRATIVE}}
#
# שגיאות טיפוס כשעובדים עם נתוני JSON.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "process_data.py", line 6, in <module>
#     level = data["level"] + 1
# TypeError: can only concatenate str (not "int") to str

# %%
json_string = '{"name": "{{hero}}", "level": "5"}'  # Note: "5" is a string!

data = json.loads(json_string)
level = data["level"] + 1  # Error: "5" + 1 doesn't work

# %% [markdown]
# {{CONTEXT_ERROR_HINT_4}}
#
# ה-JSON הכיל `"5"` (מחרוזת) במקום `5` (מספר).
# JSON שומרת על הטיפוסים — אם זו מחרוזת ב-JSON, היא תישאר מחרוזת ב-Python.
#
# השגיאה קרתה כי: _______________
#
# 1. אפשרות תיקון — תקני את מקור ה-JSON:
#    `json_string = '{"name": "{{hero}}", "level": 5}'` — ללא גרשיים סביב 5
#
# 2. אפשרות תיקון — המירי בעת השימוש:
#    `level = int(data["level"]) + 1`

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
print("JSONDecodeError - missing quotes on keys")
# Uncomment to test after fixing:
# fix_code_a()

print("\n=== {{ERROR_2_TITLE}} ===")
print("JSONDecodeError - trailing comma")
# fix_code_b()

print("\n=== {{ERROR_3_TITLE}} ===")
print("JSONDecodeError - empty/corrupt file")
# fix_code_c()

print("\n=== {{ERROR_4_TITLE}} ===")
print("TypeError - wrong data type from JSON")
# fix_code_d()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
print()
print("Key differences between JSON and Python:")
print("  1. JSON keys MUST be double-quoted strings")
print("  2. JSON strings MUST use double quotes")
print("  3. JSON does NOT allow trailing commas")
print("  4. JSON has: true, false, null (not True, False, None)")
print("  5. JSON numbers can be strings - watch for type issues!")
