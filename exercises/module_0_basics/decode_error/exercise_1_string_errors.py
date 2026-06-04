# =============================================================================
# Decode the Error: String Errors
# =============================================================================
# Difficulty: 3
# Concepts: TypeError, quote matching, string + number errors
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
#     message = "Welcome to " + school_name + ", " + hero_name
# TypeError: can only concatenate str (not "int") to str

# %%
school_name = 42
hero_name = "{{hero}}"
message = "Welcome to " + school_name + ", " + hero_name
print(message)

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# > רמז: שימי לב לסוג של `school_name`. האם אפשר לחבר (`+`) מחרוזת עם מספר ישירות?
#
# כתבי את הקוד המתוקן כאן למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_2_TITLE}}
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
#   File "program.py", line 2
#     greeting = "Hello, {{hero}}!
#                                 ^
# SyntaxError: unterminated string literal

# %%
# The actual buggy code would be:
# greeting = "Hello, {{hero}}!
# print(greeting)
pass

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# > רמז: מחרוזות חייבות להיפתח ולהיסגר עם מרכאות — גם בהתחלה וגם בסוף.
#
# כתבי את הקוד המתוקן כאן למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_3_TITLE}}
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "program.py", line 3, in <module>
#     print("Score: " + score)
# TypeError: can only concatenate str (not "int") to str

# %%
score = 100
print("Score: " + score)

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# > רמז: יש שתי דרכים לתקן את זה:
# > 1. המירי את `score` למחרוזת בעזרת `str()`
# > 2. השתמשי בפסיק במקום `+` בתוך `print()`
#
# כתבי את הקוד המתוקן כאן למטה (נסי את שתי הפתרונות!):

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
