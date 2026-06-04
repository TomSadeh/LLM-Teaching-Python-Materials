# =============================================================================
# Write Code: Boolean Operators (and/or/not)
# =============================================================================
# Difficulty: 4
# Concepts: and, or, not, compound conditions
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
# ל-{{hero}} דרושים גם {{primary_stat}} גבוה וגם {{item}} כדי להמשיך.
# השתמשי ב-`and` כדי לבדוק את שני התנאים יחד.
#
# 1. צרי משתנה `stat_value = 80`
# 2. צרי משתנה `has_item = True`
# 3. כתבי משפט `if/else` עם `and`:
#         if stat_value >= 50 and has_item:
#             print "{{hero}} is ready to proceed!"
#         else:
#             print "{{hero}} needs to prepare more."
#
# פלט צפוי:
#   {{hero}} is ready to proceed!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{hero}} יכולה להיכנס ל-{{location}} עם מפתח או עם הסיסמה — מספיק אחד מהשניים.
# השתמשי ב-`or` כדי לבדוק שלפחות תנאי אחד מתקיים.
#
# 1. צרי משתנה `has_key = False`
# 2. צרי משתנה `knows_password = True`
# 3. כתבי משפט `if/else` עם `or`:
#         if has_key or knows_password:
#             print "{{hero}} enters {{location}}!"
#         else:
#             print "{{hero}} cannot enter."
#
# פלט צפוי:
#   {{hero}} enters {{location}}!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{hero}} יוצאת לחקור רק אם אין אויבים בקרבת מקום.
# השתמשי ב-`not` כדי לבדוק את ההיפך של תנאי.
#
# 1. צרי משתנה `enemy_nearby = False`
# 2. כתבי משפט `if/else` עם `not`:
#         if not enemy_nearby:
#             print "{{hero}} explores safely."
#         else:
#             print "{{hero}} stays hidden."
#
# פלט צפוי:
#   {{hero}} explores safely.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{hero}} יכולה להשתמש ב-{{spell3}} אם יש לה מספיק {{secondary_stat}}
# וגם היכולה אינה בקולדאון.
# שלבי `and` עם `not`.
#
# 1. צרי משתנה `power = 100`
# 2. צרי משתנה `on_cooldown = False`
# 3. צרי משתנה `required_power = 50`
# 4. כתבי משפט `if/else`:
#         if power >= required_power and not on_cooldown:
#             print "{{hero}} uses {{spell3}}!"
#         else:
#             print "Cannot use {{spell3}} right now."
#
# פלט צפוי:
#   {{hero}} uses {{spell3}}!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{mentor}} קובעת אם {{hero}} יכולה להצטרף לשיעור מתקדם.
# דרישות: (level >= 10 AND passed_exam) OR has_special_permission
#
# 1. צרי משתנה `level = 8`
# 2. צרי משתנה `passed_exam = True`
# 3. צרי משתנה `has_special_permission = False`
# 4. כתבי משפט `if/else` עם סוגריים לבהירות:
#         if (level >= 10 and passed_exam) or has_special_permission:
#             print "{{hero}} can take the advanced class!"
#         else:
#             print "{{hero}} must meet the requirements first."
#
# פלט צפוי (הרמה היא רק 8, ואין הרשאה מיוחדת):
#   {{hero}} must meet the requirements first.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_6_TITLE}}
# {{CONTEXT_PHASE_6}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# צרי בודקת כשירות לאתגר של {{school}}.
# לאתגר יש מספר דרישות שאפשר לעמוד בהן בדרכים שונות.
#
# 1. צרי את המשתנים:
#         hero_level = 15
#         hero_gold = 200
#         is_guild_member = True
# 2. הדפיסי `f"Level: {hero_level}, Gold: {hero_gold}, Guild Member: {is_guild_member}"`
# 3. דרישות האתגר — צריך לעמוד באחת מאלה:
#         - רמה גבוהה (level >= 20)
#         - עשירה (gold >= 500)
#         - חברת גילד עם רמה בינונית (is_guild_member and level >= 10)
# 4. כתבי את משפט `if/else`:
#         if hero_level >= 20 or hero_gold >= 500 or (is_guild_member and hero_level >= 10):
#             print "{{hero}} qualifies for the challenge!"
#         else:
#             print "{{hero}} doesn't meet any requirement."
#
# פלט צפוי (חברת גילד ברמה 15 כשירה):
#   Level: 15, Gold: 200, Guild Member: True
#   {{hero}} qualifies for the challenge!

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

print("\n=== {{PHASE_6_TITLE}} ===")
exercise_f()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
