# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי איך לייבא מודולים ולגשת לתוכנם
# באמצעות סימון הנקודה. זוהי הבסיס לשימוש בספרייה
# הסטנדרטית העוצמתית של Python.
#
# נושא: תחביר ייבוא בסיסי וסימון נקודה
# רמת קושי: 1
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# למדי לייבא מודול ולהשתמש בפונקציות שלו.
#
# 1. יבאי את מודול `math` באמצעות: `import math`
# 2. השתמשי ב-`math.sqrt()` כדי לחשב את השורש הריבועי של 144 — שמרי את התוצאה במשתנה בשם `root`
# 3. הדפיסי: `"The square root of 144 is [result]"`
#
# > רמז: אחרי הייבוא, גישה לפונקציות עם `module_name.function_name`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# השתמשי בקבועים של מודול (ערכים מיוחדים השמורים במודולים).
#
# 1. יבאי את מודול `math` (אם עוד לא יובא למעלה)
# 2. גשי ל-`math.pi` ושמרי אותו במשתנה בשם `pi_value`
# 3. חשבי את שטח עיגול עם רדיוס 5 — הנוסחה: `area = pi * radius * radius`
# 4. הדפיסי: `"A circle with radius 5 has area [result]"`
#
# > רמז: `math.pi` נותן לך את ערך פאי (3.14159...)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# שלבי מספר פונקציות מאותו מודול.
# חשבי את רמת הכוח של {{hero}} באמצעות פעולות מתמטיות.
#
# 1. יבאי את מודול `math`
# 2. צרי את המשתנים האלה:
#    - `base_power = 64`
#    - `multiplier = 2.7`
# 3. חשבי:
#    - `root_power = math.sqrt(base_power)`
#    - `floor_multiplier = math.floor(multiplier)`
#    - `ceiling_multiplier = math.ceil(multiplier)`
# 4. הדפיסי כל ערך מחושב עם תיאור, לדוגמה:
#    `"Square root of 64: [value]"`
#    `"Floor of 2.7: [value]"`
#    `"Ceiling of 2.7: [value]"`
#
# > רמז: `floor()` מעגל למטה, `ceil()` מעגל למעלה

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

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
