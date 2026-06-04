# =============================================================================
# Decode the Error: Input Errors
# =============================================================================
# Difficulty: 3-4
# Concepts: TypeError with input, ValueError, type conversion
# =============================================================================

# %% [markdown]
# {{CONTEXT_DECODE_ERROR_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{ERROR_1_TITLE}}
# {{CONTEXT_ERROR_1_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "program.py", line 3, in <module>
#     total = price + 10
# TypeError: can only concatenate str (not "int") to str

# %%
price = input("Enter price: ")
total = price + 10
print("With tax:", total)

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# > רמז: איזה סוג מחזירה `input()`? איזה סוג אנחנו צריכות לחשבון?
#
# כתבי את הקוד המתוקן למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_2_TITLE}}
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "program.py", line 2, in <module>
#     age = int(age_text)
# ValueError: invalid literal for int() with base 10: 'twenty'

# %%
age_text = "twenty"  # Simulating user typing "twenty"
age = int(age_text)
print("Age:", age)

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# > רמז: `int()` יכולה להמיר רק מחרוזות שמכילות ספרות כמו `"20"`.
# > המילה `"twenty"` לא יכולה להתמיר למספר.
#
# שימי לב: השגיאה הזו קורית כשמשתמש מקליד טקסט במקום מספרים.
# לצורך התרגיל הזה, שני את הקלט למחרוזת מספר תקינה.
#
# כתבי את הקוד המתוקן למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_3_TITLE}}
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "program.py", line 4, in <module>
#     result = num1 + num2
# TypeError: can only concatenate str (not "str") to str

# %%
num1 = input("First number: ")
num2 = input("Second number: ")
result = num1 + num2
print("Sum:", result)

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# > רמז: אם המשתמשת מקלידה 5 ו-3, הקוד הנוכחי ידפיס `"53"`
# > כי הוא מחבר מחרוזות במקום לחבור מספרים!
#
# כתבי את הקוד המתוקן למטה:

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
# Uncomment to test after fixing:
# fix_code_a()

print("\n=== {{ERROR_2_TITLE}} ===")
# fix_code_b()

print("\n=== {{ERROR_3_TITLE}} ===")
# fix_code_c()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
