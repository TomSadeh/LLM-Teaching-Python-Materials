# =============================================================================
# Fill in the Blanks: Input
# =============================================================================
# Difficulty: 3-4
# Concepts: input() function, type conversion, int(), str()
# =============================================================================

# %% [markdown]
# {{CONTEXT_FILL_BLANKS_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{EXERCISE_1_TITLE}}
# {{CONTEXT_EXERCISE_1_NARRATIVE}}
#
# קבלי את השם של {{hero}} מהמשתמשת.
#
# > רמז: השתמשי בפונקציה `input()` כדי לקבל טקסט מהמשתמשת.
#
# name = ___("What is your name? ")    # Fill in the function name
# print("Hello,", name)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_2_TITLE}}
# {{CONTEXT_EXERCISE_2_NARRATIVE}}
#
# קבלי את הגיל של {{hero}} ושמרי אותו כמספר.
#
# > רמז: `input()` תמיד מחזירה מחרוזת. השתמשי ב-`int()` כדי להמיר למספר.
#
# age_text = input("How old are you? ")
# age = ___(age_text)                  # Convert string to integer
# print("Next year you will be", age + 1)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_3_TITLE}}
# {{CONTEXT_EXERCISE_3_NARRATIVE}}
#
# קבלי את המחיר של {{item}} וחשבי את הסכום הכולל.
#
# > רמז: אפשר לעטוף את `input()` ישירות בתוך `int()`.
#
# price = ___(input("Enter the price: "))    # Convert input directly
# quantity = 3
# total = price ___ quantity                  # Multiply price by quantity
# print("Total:", total)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_4_TITLE}}
# {{CONTEXT_EXERCISE_4_NARRATIVE}}
#
# צרי ברכת ברוכה הבאה אישית ל-{{school}}.
#
# > רמז: שלבי בין `input()` לבין חיבור מחרוזות.
#
# name = input("Enter your name: ")
# print("Welcome to {{school}}, " ___ name ___ "!")    # Join strings

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_FILL_BLANKS_INTRO}}")
print("=" * 50)

print("\n=== {{EXERCISE_1_TITLE}} ===")
# exercise_a()  # Uncomment when you've filled the blanks

print("\n=== {{EXERCISE_2_TITLE}} ===")
# exercise_b()

print("\n=== {{EXERCISE_3_TITLE}} ===")
# exercise_c()

print("\n=== {{EXERCISE_4_TITLE}} ===")
# exercise_d()

print("\nFill in all the blanks, then uncomment to test!")
print("{{CONTEXT_ROLE_COMPLETE}}")
