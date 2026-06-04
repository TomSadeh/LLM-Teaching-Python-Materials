# =============================================================================
# Fill in the Blanks: Loop Syntax
# =============================================================================
# Difficulty: 2
# Concepts: for loop keyword, range() function, in keyword, loop variable
# =============================================================================

# %% [markdown]
# {{CONTEXT_FILL_BLANKS_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}

# %%
import turtle

# %% [markdown]
# ## {{EXERCISE_1_TITLE}}
# {{CONTEXT_EXERCISE_1_NARRATIVE}}
#
# השלימי את לולאת ה-`for` כדי לחזור 4 פעמים עבור {{hero}}.
#
# > רמז: לולאת `for` מתחילה במילת המפתח `for`.
#
# ___ i in range(4):              # Fill in the loop keyword
#     print("Step", i)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_2_TITLE}}
# {{CONTEXT_EXERCISE_2_NARRATIVE}}
#
# השלימי את הלולאה כדי לעבור על טווח עבור {{creature}}.
#
# > רמז: מילת המפתח `in` מחברת בין המשתנה לבין מה שעוברים עליו בלולאה.
#
# for step ___ range(3):          # Fill in the connecting keyword
#     print("{{creature}} takes step", step)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_3_TITLE}}
# {{CONTEXT_EXERCISE_3_NARRATIVE}}
#
# השלימי את הטווח כדי לחזור 5 פעמים ב-{{school}}.
#
# > רמז: `range(n)` יוצרת מספרים מ-0 עד n-1.
# > כדי לחזור 5 פעמים, מה צריך להיות n?
#
# for i in ___(5):                # Fill in the function name
#     print("Repeat number", i)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_4_TITLE}}
# {{CONTEXT_EXERCISE_4_NARRATIVE}}
#
# השלימי את הלולאה שמציירת ריבוע ב-{{location}}.
#
# > רמז: לריבוע יש 4 צלעות, אז חוזרים 4 פעמים.
#
# t = turtle.Turtle()
# ___ side ___ range(___):        # Fill in: keyword, keyword, number
#     t.forward(50)
#     t.right(90)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_5_TITLE}}
# {{CONTEXT_EXERCISE_5_NARRATIVE}}
#
# השלימי את ההזחה של גוף הלולאה למסע של {{hero}}.
#
# > רמז: קוד שנמצא בתוך לולאה חייב להיות מוזח (4 רווחים או טאב אחד).
#
# t = turtle.Turtle()
# for i in range(3):
# ___t.forward(30)                # Add proper indentation
# ___t.right(120)                 # Add proper indentation

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

print("\n=== {{EXERCISE_5_TITLE}} ===")
# exercise_e()

print("\nFill in all the blanks, then uncomment to test!")
print("{{CONTEXT_ROLE_COMPLETE}}")
turtle.done()
