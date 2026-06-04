# %% [markdown]
# {{CONTEXT_ERROR_HANDLING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: טיפול ב-`AttributeError` ממודולים מיובאים
# רמת קושי: 3
#
# גם כשמודול מיובא בהצלחה, ניסיון להשתמש בפונקציה
# או במאפיין שלא קיים גורם ל-`AttributeError`. נלמד
# להתמודד עם זה בצורה חכמה.
#
# ## {{HANDLING_1_TITLE}}
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# הפונקציה הזו קורסת אם הפונקציה לא קיימת במודול.

# %%
import math
return math.fake_function(42)  # AttributeError!

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_1}}
#
# 1. נסי לייבא את המודול
# 2. קבלי את הפונקציה בעזרת `getattr(module, function_name)`
# 3. קראי לפונקציה עם `*args`
# 4. טפלי ב-`ModuleNotFoundError` וב-`AttributeError`
#
# דוגמה:
#   try:
#       module = __import__(module_name)
#       func = getattr(module, function_name)
#       return func(*args)
#   except ModuleNotFoundError:
#       print(f"Module '{module_name}' not found")
#       return None
#   except AttributeError:
#       print(f"Function '{function_name}' not found in {module_name}")
#       return None

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_2_TITLE}}
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# בדקי אם פונקציה קיימת לפני שמשתמשים בה.

# %%
import math
return math.nonexistent()  # Crashes!

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_2}}
#
# אפשרות 1: השתמשי ב-`hasattr()`
#   return hasattr(module, function_name)
#
# אפשרות 2: השתמשי ב-`try/except` עם `getattr()`
#   try:
#       getattr(module, function_name)
#       return True
#   except AttributeError:
#       return False

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_2}}
#
# 1. נסי לייבא את המודול
# 2. נסי לקבל את המאפיין עם `getattr(module, constant_name, default)` —
#    הארגומנט השלישי של `getattr` הוא ערך ברירת מחדל!
# 3. טפלי ב-`ModuleNotFoundError`
#
# דוגמה:
#   try:
#       module = __import__(module_name)
#       return getattr(module, constant_name, default)
#   except ModuleNotFoundError:
#       return default

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_3_TITLE}}
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# בני פונקציה גמישה לקריאת פונקציות עבור {{school}}.

# %%
import math
func = getattr(math, operation)
return func(value)

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_3}}
#
# 1. ייבאי את `math`
# 2. נסי לקבל ולקרוא לפונקציה
# 3. טפלי במספר סוגי שגיאות:
#         except AttributeError:
#             print(f"Unknown operation: {operation}")
#         except ValueError as e:
#             print(f"Invalid value: {e}")
#         except TypeError as e:
#             print(f"Wrong type: {e}")
# 4. החזירי ערך ברירת מחדל בכל שגיאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_4_TITLE}}
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# צרי סייר מודולים שמציג בצורה בטוחה את הפונקציות הזמינות.
#
# {{CONTEXT_HANDLING_HINT_4}}
#
# 1. נסי לייבא את המודול
# 2. קבלי את כל השמות עם `dir(module)`
# 3. סנני רק פריטים שניתן לקרוא להם:
#         functions = []
#         for name in dir(module):
#             if not name.startswith('_'):  # Skip private
#                 attr = getattr(module, name)
#                 if callable(attr):
#                     functions.append(name)
# 4. החזירי את הרשימה
# 5. טפלי ב-`ModuleNotFoundError`, החזירי רשימה ריקה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
print("=" * 50)

print("\n=== {{HANDLING_1_TITLE}} ===")
print("Testing safe function call:")
# Uncomment to test:
# result = safe_use_module_function("math", "sqrt", 16)
# print(f"  math.sqrt(16) = {result}")
# result = safe_use_module_function("math", "fake_func", 16)
# print(f"  math.fake_func(16) = {result}")
# result = safe_use_module_function("fake_module", "sqrt", 16)
# print(f"  fake_module.sqrt(16) = {result}")

print("\n=== {{HANDLING_2_TITLE}} ===")
print("Testing function existence check:")
# Uncomment to test:
# import math
# print(f"  math has sqrt: {has_function(math, 'sqrt')}")
# print(f"  math has fake: {has_function(math, 'fake')}")
# print(f"  Pi value: {safe_get_constant('math', 'pi', 3.14)}")
# print(f"  Fake constant: {safe_get_constant('math', 'fake', 'N/A')}")

print("\n=== {{HANDLING_3_TITLE}} ===")
print("Testing safe math operations:")
# Uncomment to test:
# print(f"  sqrt(16): {safe_math_operation('sqrt', 16)}")
# print(f"  floor(3.7): {safe_math_operation('floor', 3.7)}")
# print(f"  fake(16): {safe_math_operation('fake', 16, 'N/A')}")
# print(f"  sqrt(-1): {safe_math_operation('sqrt', -1, 'N/A')}")

print("\n=== {{HANDLING_4_TITLE}} ===")
print("Listing module functions:")
# Uncomment to test:
# functions = list_module_functions("math")
# print(f"  math has {len(functions)} functions")
# print(f"  First 5: {functions[:5]}")
# functions = list_module_functions("fake_module")
# print(f"  fake_module: {functions}")

print("\n" + "=" * 50)
print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")
