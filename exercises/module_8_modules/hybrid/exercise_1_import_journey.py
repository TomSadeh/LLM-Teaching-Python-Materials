# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זו תרגילה מרובת-חלקים שבה תשלטי בכל הדרכים לייבא מודולים,
# תוך כדי בניית מחשבון סטטיסטיקות עבור {{school}}.
#
# מושגי תכנות: תחביר ייבוא, כתיב נקודה, from import, כינויים
# רמת קושי: 1-2
#
# ## חלק 1: הכוונה - ייבוא בסיסי עם כתיב נקודה
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# התחילי בשימוש בתחביר הייבוא הבסיסי. זו הדרך הכי
# ברורה לשימוש במודולים - תמיד רואים מאיפה הדברים מגיעים.
#
# השתמשי בתחביר ייבוא בסיסי כדי לגשת לפונקציות המתמטיות.
#
# 1. יבאי את מודול ה-math בעזרת: `import math`
#
# 2. צרי מילון סטטיסטיקות לדמות:
#         stats = {
#             "name": "{{hero}}",
#             "base_power": 100,
#             "multiplier": 1.5
#         }
#
# 3. חשבי תוך שימוש בכתיב נקודה:
#         - `power_root = math.sqrt(stats["base_power"])`
#         - `rounded_mult = math.floor(stats["multiplier"])`
#
# 4. הדפיסי את התוצאות:
#         `"[name]'s power root: [power_root]"`
#         `"Rounded multiplier: [rounded_mult]"`
#
# > רמז: עם `import math`, תמיד השתמשי בצורה `math.שם_הפונקציה`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - שדרוג עם from import
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# עכשיו שדרגי לשימוש בייבוא ישיר. זה הופך את הקוד לנקי יותר
# כשמשתמשים באותן פונקציות הרבה פעמים.
#
# שדרגי לשימוש בתחביר `from...import`.
#
# 1. יבאי פונקציות ספציפיות:
#         `from math import sqrt, floor, ceil, pow`
#
# 2. צרי סטטיסטיקות עבור מספר דמויות:
#         hero_power = 144
#         ally_power = 81
#         mentor_power = 225
#
# 3. חשבי רמות כוח (בלי קידומת `math.`!):
#         hero_level = sqrt(hero_power)
#         ally_level = sqrt(ally_power)
#         mentor_level = sqrt(mentor_power)
#
# 4. חשבי כוח מוגבר בעזרת `pow()`:
#         boosted = pow(hero_level, 2)
#
# 5. הדפיסי את כל התוצאות:
#         `"{{hero}} level: [value]"`
#         `"{{friend}} level: [value]"`
#         `"{{mentor}} level: [value]"`
#         `"Boosted power: [value]"`
#
# > שימי לב: הקוד נקי יותר בלי קידומת `math.` בכל מקום

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - שימוש בכינויים
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# למדי מתי כינויים שימושיים: כדי למנוע התנגשות בין שמות,
# או כדי לקצר שמות מודולים ארוכים.
#
# השתמשי בכינויים לקוד נקי ונטול התנגשויות.
#
# 1. מה קורה אם יש לנו פונקציית `sqrt` משלנו?
#         ראשית, יבאי את math עם כינוי:
#         `import math as m`
#
# 2. צרי פונקציה מקומית שמשתמשת במודול:
#         def calculate_stat(value):
#             """Calculate a derived stat."""
#             return m.floor(m.sqrt(value))
#
# 3. בדקי עם מספר ערכים:
#         values = [100, 144, 200, 256]
#         for value in values:
#             result = calculate_stat(value)
#             print(f"Stat from {value}: {result}")
#
# 4. נסי גם לתת כינוי לפונקציה ספציפית:
#         `from math import factorial as fact`
#         הדפיסי: `"5! = [fact(5)]"`
#         הדפיסי: `"7! = [fact(7)]"`
#
# > רמז: כינויים נפוצים: `import numpy as np`, `import pandas as pd`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_DISCOVERY_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Basic Import with Dot Notation")
print("(Using import math and math.function())")
print()
exercise_part1()

print()
print(">>> PART 2: Refactoring with from...import")
print("(Using from math import function)")
print()
exercise_part2()

print()
print(">>> PART 3: Using Aliases")
print("(Using import math as m)")
print()
exercise_part3()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print()
print("Import Syntax Summary:")
print("  import math          -> math.sqrt()")
print("  from math import sqrt -> sqrt()")
print("  import math as m     -> m.sqrt()")
print("=" * 60)
