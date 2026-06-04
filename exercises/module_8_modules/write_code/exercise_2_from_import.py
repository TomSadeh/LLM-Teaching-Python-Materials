# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי דרך חלופית לייבא פריטים ממודול —
# ישירות, בלי צורך בסימון הנקודה.
#
# נושא: תחביר `from module import` וכינויים (aliases)
# רמת קושי: 2
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# ייבאי פונקציות ספציפיות ישירות ממודול.
#
# 1. השתמשי בתחביר הזה: `from math import sqrt, pi`
#    כך מייבאים את `sqrt` ואת `pi` ישירות (ללא סימן נקודה)
#
# 2. חשבי את השורש הריבועי של 225 באמצעות `sqrt()` ישירות
#    (לא `math.sqrt()`, פשוט `sqrt()`)
#
# 3. הדפיסי: `"Square root of 225 is [result]"`
#
# 4. הדפיסי: `"Pi is approximately [pi value]"`
#
# > רמז: עם `from import`, משתמשים בשם ישירות — ללא קידומת שם המודול

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# השתמשי בכינויים (aliases) כדי לתת שמות קצרים יותר לייבואים.
#
# 1. ייבאי עם כינוי: `import math as m`
#    עכשיו תשתמשי ב-`m.sqrt()` במקום `math.sqrt()`
#
# 2. חשבי: `m.pow(2, 10)` (2 בחזקת 10)
#    שמרי את התוצאה במשתנה בשם `result`
#
# 3. הדפיסי: `"2 to the power of 10 is [result]"`
#
# 4. נסי גם: `from math import factorial as fact`
#    חשבי `fact(5)` והדפיסי `"5 factorial is [result]"`
#
# > רמז: כינויים שימושיים כשיש שמות מודול ארוכים, או כדי למנוע התנגשות בין שמות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# תרגלי ייבוא של מספר פריטים ושימוש בהם יחד.
# עזרי ל-{{hero}} לחשב כמה סטטיסטיקות.
#
# 1. מ-`math`, ייבאי: `sqrt`, `floor`, `ceil`, `pi`
#    השתמשי ב: `from math import sqrt, floor, ceil, pi`
#
# 2. צרי רשימת ערכים: `values = [10, 15, 20, 25, 30]`
#
# 3. חשבי:
#    - `total` = סכום כל הערכים (השתמשי ב-`sum()` המובנה של Python)
#    - `average` = `total / len(values)`
#    - `root_of_average` = `sqrt(average)`
#
# 4. הדפיסי:
#    `"Total: [total]"`
#    `"Average: [average]"`
#    `"Square root of average: [root_of_average]"`
#    `"Rounded down: [floor(root_of_average)]"`
#    `"Rounded up: [ceil(root_of_average)]"`

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
