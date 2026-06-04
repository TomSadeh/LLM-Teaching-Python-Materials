# =============================================================================
# Write Code: Variables
# =============================================================================
# Difficulty: 2
# Concepts: variable creation, assignment, using variables in print
# =============================================================================

# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# צרי משתנה בשם `hero_name` ושמרי בו את "{{hero}}".
# אחר כך הדפיסי את המשתנה.
#
# 1. צרי את המשתנה: `hero_name = "{{hero}}"`
# 2. הדפיסי אותו: `print(hero_name)`
#
# פלט מצופה: `{{hero}}`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# צרי שני משתנים והדפיסי אותם יחד.
#
# 1. צרי משתנה `location` עם הערך `"{{school}}"`
# 2. צרי משתנה `activity` עם הערך `"learning Python"`
# 3. הדפיסי את שניהם כך: `print(location, "-", activity)`
#
# פלט מצופה: `{{school}} - learning Python`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# צרי משתנים עבור המלאי של {{hero}}.
#
# 1. צרי `item_name` עם הערך `"{{item}}"`
# 2. צרי `item_count` עם הערך `3` (מספר, בלי מרכאות!)
# 3. הדפיסי הודעה כמו: `"{{hero}} has 3 {{item}}s"`
#    השתמשי ב: `print("{{hero}} has", item_count, item_name + "s")`
#
# פלט מצופה: `{{hero}} has 3 {{item}}s`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# עדכני את הערך של משתנה.
#
# 1. צרי `level` עם הערך `1`
# 2. הדפיסי `"Starting level:"` ואחריו את המשתנה `level`
# 3. שני את `level` ל-`2` (השבי ערך חדש)
# 4. הדפיסי `"New level:"` ואחריו את המשתנה `level`
#
# פלט מצופה:
# `Starting level: 1`
# `New level: 2`

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
