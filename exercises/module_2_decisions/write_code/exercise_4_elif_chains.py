# =============================================================================
# Write Code: if/elif/else Chains
# =============================================================================
# Difficulty: 3
# Concepts: if/elif/else, multiple branches, first match wins
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
# {{mentor}} מחלקת ציונים לפי תוצאות.
# השתמשי ב-`if/elif/else` כדי לקבוע את הציון.
#
# 1. צרי משתנה בשם `score` עם הערך `78`
# 2. כתבי שרשרת `if/elif/else`:
#    - אם `score >= 90`: הדפיסי `"Grade: A"`
#    - אם `score >= 80`: הדפיסי `"Grade: B"`
#    - אם `score >= 70`: הדפיסי `"Grade: C"`
#    - אחרת: הדפיסי `"Grade: F"`
#
# פלט צפוי כאשר score הוא 78:
#   `Grade: C`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# מיינו את {{hero}} ל-{{house}} לפי התכונה החזקה ביותר שלה.
#
# 1. צרי משתנה בשם `trait` עם הערך `"courage"`
# 2. כתבי שרשרת `if/elif/else`:
#    - אם `trait == "courage"`: הדפיסי `"{{hero}} joins the Warriors"`
#    - אם `trait == "wisdom"`: הדפיסי `"{{hero}} joins the Scholars"`
#    - אם `trait == "kindness"`: הדפיסי `"{{hero}} joins the Healers"`
#    - אחרת: הדפיסי `"{{hero}} joins the Explorers"`
#
# פלט צפוי כאשר trait הוא "courage":
#   `{{hero}} joins the Warriors`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# קבעי את הדרגה של {{hero}} לפי הרמה שלה.
# הדפיסי את הסטטוס המלא שלה.
#
# 1. צרי משתנה בשם `level` עם הערך `15`
# 2. צרי משתנה בשם `rank` (יקבל ערך בתוך שרשרת ה-`if/elif/else`)
# 3. כתבי שרשרת `if/elif/else` להגדרת `rank`:
#    - אם `level >= 20`: `rank = "Master"`
#    - אם `level >= 15`: `rank = "Expert"`
#    - אם `level >= 10`: `rank = "Intermediate"`
#    - אם `level >= 5`: `rank = "Apprentice"`
#    - אחרת: `rank = "Novice"`
# 4. הדפיסי `f"{{hero}} - Level {level} - Rank: {rank}"`
#
# פלט צפוי כאשר level הוא 15:
#   `{{hero}} - Level 15 - Rank: Expert`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# קבעי מה {{hero}} יכולה לקנות בחנות עם הזהב שלה.
# השתמשי ב-`if/elif/else` כדי למצוא את הפריט הכי יקר שהיא יכולה להרשות לעצמה.
#
# 1. צרי משתנה בשם `gold` עם הערך `75`
# 2. הדפיסי `f"{{hero}} has {gold} gold"`
# 3. כתבי שרשרת `if/elif/else`:
#    - אם `gold >= 100`: הדפיסי `"You can buy the {{spell3}} scroll!"`
#    - אם `gold >= 50`: הדפיסי `"You can buy the {{spell2}} scroll!"`
#    - אם `gold >= 20`: הדפיסי `"You can buy the {{spell1}} scroll!"`
#    - אחרת: הדפיסי `"You can't afford any scrolls."`
#
# פלט צפוי כאשר gold הוא 75:
#   `{{hero}} has 75 gold`
#   `You can buy the {{spell2}} scroll!`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# צרי מערכת תגובה למזג האוויר עבור {{school}}.
# טמפרטורות שונות מובילות לפעילויות שונות.
#
# 1. צרי משתנה בשם `temperature` עם הערך `22`
# 2. צרי משתנה בשם `activity` (יקבל ערך בתוך שרשרת ה-`if/elif/else`)
# 3. כתבי שרשרת `if/elif/else`:
#    - אם `temperature >= 30`: `activity = "indoor study"`
#    - אם `temperature >= 20`: `activity = "outdoor training"`
#    - אם `temperature >= 10`: `activity = "warm-up exercises"`
#    - אחרת: `activity = "rest by the fire"`
# 4. הדפיסי `f"At {temperature} degrees, {{school}} recommends: {activity}"`
#
# פלט צפוי כאשר temperature הוא 22:
#   `At 22 degrees, {{school}} recommends: outdoor training`

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
