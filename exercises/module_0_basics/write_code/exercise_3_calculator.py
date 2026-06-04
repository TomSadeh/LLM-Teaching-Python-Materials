# =============================================================================
# Write Code: Calculator
# =============================================================================
# Difficulty: 2-3
# Concepts: arithmetic operators (+, -, *, /, //, %, **)
# =============================================================================

# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# חשבי את העלות הכוללת של {{item}}ים ב{{school}}.
#
# 1. צרי משתנה `price` עם הערך 15
# 2. צרי משתנה `quantity` עם הערך 4
# 3. צרי משתנה `total` שמכפיל את price ב-quantity
# 4. הדפיסי `Total cost:` ואחריו את המשתנה total
#
# פלט צפוי: `Total cost: 60`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# חשבי איך לחלק {{item}}ים בין החברים של {{hero}}.
#
# 1. צרי `items` עם הערך 17
# 2. צרי `friends` עם הערך 5
# 3. צרי `each_gets` באמצעות `//` (חילוק שלם)
# 4. צרי `leftover` באמצעות `%` (שארית)
# 5. הדפיסי `Each friend gets:` ואחריו את each_gets
# 6. הדפיסי `Leftover:` ואחריו את leftover
#
# פלט צפוי:
# `Each friend gets: 3`
# `Leftover: 2`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# חשבי את רמת הכוח של {{hero}} ב{{school}}.
#
# 1. צרי `base_power` עם הערך 2
# 2. צרי `level` עם הערך 5
# 3. צרי `total_power` באמצעות `**` (חזקה): `base_power ** level`
# 4. הדפיסי `Power level:` ואחריו את total_power
#
# > רמז: `2 ** 5` פירושו `2 * 2 * 2 * 2 * 2`
#
# פלט צפוי: `Power level: 32`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# חשבי את הניקוד של {{hero}} עם הבונוסים.
#
# 1. צרי `base_score` עם הערך 100
# 2. צרי `bonus` עם הערך 25
# 3. צרי `penalty` עם הערך 10
# 4. צרי `final_score` = `base_score + bonus - penalty`
# 5. הדפיסי `Final score:` ואחריו את final_score
#
# פלט צפוי: `Final score: 115`

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
