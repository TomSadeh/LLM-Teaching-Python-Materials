# =============================================================================
# Write Code: First Loop
# =============================================================================
# Difficulty: 2
# Concepts: for loop, range(n), repeating turtle commands
# =============================================================================

# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}

# %%
import turtle

# %% [markdown]
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# השתמשי בלולאה כדי להדפיסי "Hello, {{school}}!" שלוש פעמים.
#
# 1. כתבי: `for i in range(3):`
# 2. בשורה הבאה, עם הזחה (indentation), כתבי: `print("Hello, {{school}}!")`
#
# פלט צפוי:
# Hello, {{school}}!
# Hello, {{school}}!
# Hello, {{school}}!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# צייר ריבוע עבור {{hero}} בעזרת לולאה.
# לריבוע יש 4 צלעות, עם פנייה של 90 מעלות בכל פינה.
#
# 1. צרי צב בעזרת `t = turtle.Turtle()`
# 2. כתבי לולאה שחוזרת 4 פעמים
# 3. בתוך הלולאה (עם הזחה):
#    - `t.forward(100)`
#    - `t.right(90)`
#
# > רמז: כל צלע היא: התקדמי קדימה, אחר כך פני ימינה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# צייר משולש עבור {{creature}} בעזרת לולאה.
# למשולש יש 3 צלעות עם פניות של 120 מעלות.
#
# 1. צרי צב
# 2. כתבי לולאה שחוזרת 3 פעמים
# 3. בתוך הלולאה:
#    - התקדמי 80 יחידות קדימה
#    - פני שמאלה 120 מעלות
#
# > רמז: הזווית החיצונית של משולש שווה צלעות היא 120 מעלות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# צרי קו מקווקו ב-{{location}} על ידי חזרה על הפעולות:
# שרטטי, הרימי את העט, התקדמי, הורידי את העט.
#
# 1. צרי צב
# 2. השתמשי בלולאה שחוזרת 5 פעמים
# 3. בתוך הלולאה:
#    - `t.forward(20)`      # שרטטי קו קצר
#    - `t.penup()`          # הרימי את העט
#    - `t.forward(10)`      # התקדמי בלי לצייר
#    - `t.pendown()`        # הורידי את העט
#
# פלט צפוי: קו מקווקו עם 5 קווים ו-4 רווחים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
exercise_a()

print("\n=== {{PHASE_2_TITLE}} ===")
exercise_b()

print("\n=== {{PHASE_3_TITLE}} ===")
exercise_c()

print("\n=== {{PHASE_4_TITLE}} ===")
exercise_d()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
turtle.done()
