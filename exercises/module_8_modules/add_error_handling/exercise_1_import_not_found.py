# %% [markdown]
# {{CONTEXT_ERROR_HANDLING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Handling ModuleNotFoundError
# Difficulty: 3
#
# כשמייבאים מודולים, יכולות לקרות טעויות: המודול אולי לא קיים,
# נכתב בצורה שגויה, או לא מותקן. נלמד לטפל בזה בצורה נאותה.
#
# ## {{HANDLING_1_TITLE}}
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# הפונקציה הזו קורסת אם המודול לא קיים.

# %%
import nonexistent_module  # This will crash!
return nonexistent_module.some_function()

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_1}}
#
# 1. השתמשי ב-`try/except` כדי לתפוס `ModuleNotFoundError`
#
# 2. בתוך `try`:
#    השתמשי ב-`__import__(module_name)` כדי לייבא באופן דינמי —
#    זה שקול ל-`import module_name`
#
# 3. אם הייבוא הצליח, החזירי את המודול
#
# 4. בבלוק `except`:
#    הדפיסי: `f"Module '{module_name}' not found"`
#    החזירי `None`
#
# דוגמה:
#   try:
#       module = __import__(module_name)
#       return module
#   except ModuleNotFoundError:
#       print(f"Module '{module_name}' not found")
#       return None

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_2_TITLE}}
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# לפעמים רוצים להשתמש ביכולות אופציונליות אם הן זמינות.

# %%
import colorama  # Optional third-party module
colorama.init()
return colorama.Fore.RED + "Error!" + colorama.Style.RESET_ALL

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_2}}
#
# 1. נסי לייבא את `colorama`
#
# 2. אם הייבוא הצליח, השתמשי בו כדי לצבוע את הטקסט
#
# 3. אם קיבלת `ModuleNotFoundError`, פשוט החזירי את הטקסט הרגיל
#
# תבנית:
#   try:
#       import colorama
#       colorama.init()
#       # ... use colorama ...
#   except ModuleNotFoundError:
#       return text  # Return plain text

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_3_TITLE}}
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# טפלי בטעויות כתיב בשמות מודולים בצורה נאותה.

# %%
import maht  # Typo! Should be 'math'
return maht.sqrt(16)

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_3}}
#
# 1. נסי לייבא את `math` ולחשב `sqrt`
#
# 2. טפלי ב-`ModuleNotFoundError` (לא אמור לקרות עם `math`,
#    אבל זה מדגים את התבנית)
#
# 3. טפלי ב-`ValueError` עבור מספרים שליליים
#
# דוגמה:
#   try:
#       import math
#       return math.sqrt(value)
#   except ModuleNotFoundError:
#       print("Math module not available")
#       return None
#   except ValueError:
#       print("Cannot calculate square root of negative number")
#       return None

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_4_TITLE}}
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# צרי פונקציית ייבוא גמישה עבור {{school}}.
#
# {{CONTEXT_HANDLING_HINT_4}}
#
# 1. עברי בלולאה על `module_names`
#
# 2. לכל שם, נסי לייבא אותו
#
# 3. אם הייבוא הצליח, החזירי את המודול מיד
#
# 4. אם הייבוא נכשל (`ModuleNotFoundError`), המשיכי לבא
#
# 5. אחרי הלולאה, החזירי את `fallback_value`
#
# דוגמה:
#   for name in module_names:
#       try:
#           return __import__(name)
#       except ModuleNotFoundError:
#           continue
#   return fallback_value

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
print("=" * 50)

print("\n=== {{HANDLING_1_TITLE}} ===")
print("Testing optional module import:")
# Uncomment to test:
# result = safe_import_optional_module("math")
# if result:
#     print(f"  math imported: sqrt(16) = {result.sqrt(16)}")
# result = safe_import_optional_module("fake_module")
# print(f"  fake_module result: {result}")

print("\n=== {{HANDLING_2_TITLE}} ===")
print("Testing optional colors:")
# Uncomment to test:
# text = use_colors_if_available("Warning message", "yellow")
# print(f"  Result: {text}")

print("\n=== {{HANDLING_3_TITLE}} ===")
print("Testing safe sqrt:")
# Uncomment to test:
# print(f"  sqrt(16) = {safe_math_sqrt(16)}")
# print(f"  sqrt(-4) = {safe_math_sqrt(-4)}")

print("\n=== {{HANDLING_4_TITLE}} ===")
print("Testing flexible import:")
# Uncomment to test:
# modules_to_try = ["fake1", "fake2", "math", "fake3"]
# result = try_import_modules(modules_to_try)
# if result:
#     print(f"  Found module: {result.__name__}")

print("\n" + "=" * 50)
print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")
