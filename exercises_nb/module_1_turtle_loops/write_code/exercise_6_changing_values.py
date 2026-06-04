# =============================================================================
# Write Code: Changing Values
# =============================================================================
# Difficulty: 4
# Concepts: loop variables in calculations, accumulators, changing patterns
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
# חשבי והדפיסי את הסכום של 1 + 2 + 3 + 4 + 5 עבור {{hero}}.
#
# 1. צרי משתנה בשם `total` והגדירי אותו ל-0
# 2. השתמשי בלולאת `for` עם `range(1, 6)`
# 3. בתוך הלולאה: `total = total + i` (כאשר `i` הוא משתנה הלולאה)
# 4. אחרי הלולאה, הדפיסי `"Sum:", total`
#
# פלט צפוי: `Sum: 15`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# הדפיסי לוח כפל של 3 ב-{{school}}.
#
# 1. השתמשי בלולאת `for` עם `range(1, 6)`
# 2. בתוך הלולאה:
#    - `result = 3 * i` (כאשר `i` הוא משתנה הלולאה)
#    - `print(f"3 x {i} = {result}")`
#
# פלט צפוי:
# `3 x 1 = 3`
# `3 x 2 = 6`
# `3 x 3 = 9`
# `3 x 4 = 12`
# `3 x 5 = 15`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# שרטטי מדרגות גדלות עבור {{creature}}.
# כל מדרגה גבוהה יותר מהקודמת.
#
# 1. צרי צב ומקמי אותו בנקודה `(-200, 100)`
# 2. השתמשי בלולאת `for` עם `range(1, 8)`
# 3. בתוך הלולאה:
#    - `height = i * 15`  (גובה המדרגה גדל)
#    - `t.forward(30)`    (החלק האופקי)
#    - `t.right(90)`
#    - `t.forward(height)`  (החלק האנכי - משתנה!)
#    - `t.left(90)`
#
# פלט צפוי: מדרגות שבהן כל שלב גבוה יותר מהקודם.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# שרטטי ספירלה ב-{{location}} שבה אורך הקו גדל.
#
# 1. צרי צב
# 2. השתמשי בלולאת `for` עם `range(1, 25)`
# 3. בתוך הלולאה:
#    - `length = i * 5`  (האורך גדל בכל איטרציה)
#    - `t.forward(length)`
#    - `t.right(90)`
#
# פלט צפוי: ספירלה מרובעת שגדלה כלפי חוץ.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# עקבי והדפיסי את המרחק הכולל שעברת ב-{{place}}.
#
# 1. צרי צב ומקמי אותו בנקודה `(100, 0)`
# 2. צרי משתנה `total_distance = 0`
# 3. השתמשי בלולאת `for` עם `range(1, 6)`
# 4. בתוך הלולאה:
#    - `distance = i * 20`
#    - `t.forward(distance)`
#    - `total_distance = total_distance + distance`
#    - `t.right(144)`  (דפוס כוכב)
#    - `print(f"Moved {distance}, total: {total_distance}")`
#
# פלט צפוי: צורת כוכב עם קווים שגדלים בהדרגה,
# ודוח מודפס של המרחקים.

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

print("\n=== {{PHASE_5_TITLE}} ===")
exercise_e()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
turtle.done()
