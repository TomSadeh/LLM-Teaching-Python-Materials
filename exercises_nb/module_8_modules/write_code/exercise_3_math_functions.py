# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תכירי את הפונקציות השימושיות ביותר של מודול `math`.
# הן חיוניות לחישובים במשחקים, מדע וניתוח נתונים.
#
# נושא: פונקציות מודול math (`sqrt`, `floor`, `ceil`, `pow`, `fabs`)
# Difficulty: 2

# %%
import math

# %% [markdown]
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# תרגלי פונקציות math בסיסיות.
#
# 1. חשבי את הערכים הבאים באמצעות פונקציות math:
#         - `square_root = math.sqrt(256)`
#         - `power_result = math.pow(3, 4)`  # 3 בחזקת 4
#         - `absolute = math.fabs(-42.5)`    # ערך מוחלט
#
# 2. הדפיסי כל תוצאה עם תיאור:
#         `"Square root of 256: [value]"`
#         `"3 to the power of 4: [value]"`
#         `"Absolute value of -42.5: [value]"`
#
# > רמז: `math.fabs()` מחזירה float, ואילו `abs()` היא פונקציה מובנית למספרים שלמים

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# למדי פונקציות עיגול לחישובי {{school}}.
#
# 1. צרי משתנה: `value = 7.6`
#
# 2. חשבי:
#         - `floor_result = math.floor(value)`   # מעגל כלפי מטה
#         - `ceil_result = math.ceil(value)`     # מעגל כלפי מעלה
#         - `trunc_result = math.trunc(-7.6)`    # מסיר את החלק העשרוני
#
# 3. הדפיסי כל תוצאה:
#         `"Floor of 7.6: [value]"`     (צריך להיות 7)
#         `"Ceiling of 7.6: [value]"`   (צריך להיות 8)
#         `"Truncate -7.6: [value]"`    (צריך להיות -7)
#
# 4. נסי עם המספר השלילי 7.6-:
#         הדפיסי `floor` ו-`ceil` של 7.6- כדי לראות את ההבדל
#
# > רמז: `floor(-7.6) = -8`, ‏`ceil(-7.6) = -7` (לכיוון אפס / הרחק מאפס)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# בני מחשבון מרחקים באמצעות משפט פיתגורס.
# חשבי את המרחק ש-{{hero}} צריכה לעבור.
#
# 1. צרי קואורדינטות התחלה:
#         `start_x = 0`
#         `start_y = 0`
#
# 2. צרי קואורדינטות סיום:
#         `end_x = 3`
#         `end_y = 4`
#
# 3. חשבי מרחק לפי משפט פיתגורס:
#         `distance = sqrt((end_x - start_x)^2 + (end_y - start_y)^2)`
#
#         בפייתון:
#         `dx = end_x - start_x`
#         `dy = end_y - start_y`
#         `distance = math.sqrt(dx**2 + dy**2)`
#         # או: `distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))`
#
# 4. הדפיסי: `"Distance from (0,0) to (3,4): [distance]"`
#         התשובה צריכה להיות `5.0`
#
# 5. נסי עם קואורדינטות (0,0) עד (5,12) — התשובה צריכה להיות `13.0`

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
