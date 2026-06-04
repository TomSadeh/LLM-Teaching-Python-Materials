# =============================================================================
# Write Code: Comparison Operators
# =============================================================================
# Difficulty: 2-3
# Concepts: ==, !=, <, >, <=, >= operators
# =============================================================================

# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# בדקי אם הרמה של {{hero}} תואמת בדיוק לדרישת האתגר.
# השתמשי ב-`==` להשוואת שוויון.
#
# 1. צרי משתנה בשם `hero_level` עם הערך `10`
# 2. צרי משתנה בשם `challenge_level` עם הערך `10`
# 3. כתבי משפט `if/else` עם `==`
# 4. אם `hero_level == challenge_level`, הדפיסי `"Challenge unlocked for {{hero}}!"`
# 5. אחרת, הדפיסי `"Level mismatch."`
#
# פלט צפוי:
#   `Challenge unlocked for {{hero}}!`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# בדקי אם היצור המתקרב הוא לא חבר/ה.
# השתמשי ב-`!=` להשוואת אי-שוויון.
#
# 1. צרי משתנה בשם `approaching` עם הערך `"{{villain}}"`
# 2. צרי משתנה בשם `friend_name` עם הערך `"{{friend}}"`
# 3. כתבי משפט `if/else` עם `!=`
# 4. אם `approaching != friend_name`, הדפיסי `"{{hero}} prepares for action!"`
# 5. אחרת, הדפיסי `"{{hero}} waves hello."`
#
# פלט צפוי:
#   `{{hero}} prepares for action!`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# בדקי אם נקודות החיים של {{hero}} נמצאות ברמה קריטית עם `<`.
# אחר כך בדקי אם הן נמוכות מרמת האזהרה או שוות לה עם `<=`.
#
# 1. צרי משתנה בשם `health` עם הערך `25`
# 2. צרי משתנה בשם `critical` עם הערך `20`
# 3. צרי משתנה בשם `warning` עם הערך `50`
#
# 4. כתבי `if/else` עם `<` לבדיקה קריטית:
#    אם `health < critical`, הדפיסי `"CRITICAL: Find healing immediately!"`
#    אחרת, הדפיסי `"Health above critical level."`
#
# 5. כתבי `if/else` נוסף עם `<=` לבדיקת אזהרה:
#    אם `health <= warning`, הדפיסי `"WARNING: Health getting low."`
#    אחרת, הדפיסי `"Health is acceptable."`
#
# פלט צפוי כאשר `health` הוא `25`:
#   `Health above critical level.`
#   `WARNING: Health getting low.`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# בדקי אם {{hero}} יכולה להרשות לעצמה פריט, עם `>=` להשוואת "לפחות".
#
# 1. צרי משתנה בשם `gold` עם הערך `100`
# 2. צרי משתנה בשם `price` עם הערך `100`
# 3. הדפיסי `f"{{item}} costs {price} gold. {{hero}} has {gold} gold."`
# 4. כתבי `if/else` עם `>=`:
#    אם `gold >= price`, הדפיסי `"{{hero}} can buy the {{item}}!"`
#    אחרת, הדפיסי `"Not enough gold."`
#
# פלט צפוי:
#   `{{item}} costs 100 gold. {{hero}} has 100 gold.`
#   `{{hero}} can buy the {{item}}!`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# סווגי ציון באמצעות השוואות מרובות.
# השתמשי ב-`>`, `<` ו-`==` בבדיקות שונות.
#
# 1. צרי משתנה בשם `score` עם הערך `85`
# 2. צרי משתנה בשם `average` עם הערך `70`
#
# 3. בדקי אם `score > average` והדפיסי `"Above average!"`
# 4. בדקי אם `score < average` והדפיסי `"Below average."`
# 5. בדקי אם `score == average` והדפיסי `"Exactly average."`
#
# > רמז: אלה שלושה משפטי `if` נפרדים (לא `if/elif/else`).
#         רק אחד מהם אמור להתפעל עבור `score = 85`.
#
# פלט צפוי:
#   `Above average!`

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
