# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי את יסודות המחלקות (classes):
# הגדרת מחלקה, כתיבת מתודת `__init__`, ושימוש ב-`self`
# כדי ליצור תכונות של אובייקט.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# צרי את המחלקה הראשונה שלך כדי לייצג דמות ב-{{school}}.
#
# 1. הגדירי מחלקה בשם `Character` באמצעות:
#    `class Character:`
#
# 2. בתוך המחלקה, הגדירי את מתודת `__init__`:
#    `def __init__(self, name, level):`
#
# 3. בתוך `__init__`, שמרי את הפרמטרים כתכונות של האובייקט:
#    `self.name = name`
#    `self.level = level`
#
# 4. צרי אובייקט מסוג `Character` עבור {{hero}}:
#    `hero = Character("{{hero}}", 1)`
#
# 5. הדפיסי את שם הגיבורה ורמתה באמצעות סימון הנקודה:
#    `print(f"Name: {hero.name}, Level: {hero.level}")`
#
# > רמז: המילה השמורה `class` פותחת הגדרת מחלקה, בדיוק כמו ש-`def` פותחת פונקציה. `self` מתייחס לאובייקט הספציפי שנוצר.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# צרי מחלקה עם יותר תכונות.
#
# 1. הגדירי מחלקה בשם `Item` עם `__init__` שמקבלת:
#    - `self` (תמיד ראשון!)
#    - `name` (שם הפריט)
#    - `power` (מספר שלם לדירוג עוצמה)
#    - `rarity` (מחרוזת כמו `"common"` או `"rare"`)
#
# 2. שמרי את שלושת הפרמטרים כתכונות של האובייקט באמצעות `self`
#
# 3. צרי שני אובייקטים:
#    `item1 = Item("{{item}}", 50, "uncommon")`
#    `item2 = Item("{{spell1}}", 25, "common")`
#
# 4. הדפיסי את התכונות של שני הפריטים:
#    `"[name] - Power: [power], Rarity: [rarity]"`
#
# שימי לב: לכל אובייקט יש ערכים משלו הנפרדים לחלוטין!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# צרי מחלקה עם ערכי ברירת מחדל לפרמטרים.
#
# 1. הגדירי מחלקה בשם `Student` עם `__init__` שמקבלת:
#    - `self`
#    - `name`
#    - `house` (ברירת מחדל: `"{{house}}"`)
#    - `year` (ברירת מחדל: `1`)
#
# 2. שמרי את כולן כתכונות של האובייקט
#
# 3. צרי שלוש תלמידות:
#    `student1 = Student("{{hero}}")  # משתמשת בברירות המחדל`
#    `student2 = Student("{{heroine}}", "{{house}}", 2)`
#    `student3 = Student("{{friend}}", year=3)  # ארגומנט בשם`
#
# 4. הדפיסי את הפרטים של כל תלמידה:
#    `"[name] is in [house], year [year]"`
#
# > רמז: פרמטרים עם ברירת מחדל עובדים בדיוק אותו הדבר כמו בפונקציות רגילות!

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
