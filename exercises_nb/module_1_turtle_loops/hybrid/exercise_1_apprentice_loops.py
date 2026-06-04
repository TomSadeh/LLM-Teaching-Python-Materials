# =============================================================================
# Hybrid Exercise: The Apprentice - Learning Loops
# =============================================================================
# Difficulty: 3
# Arc: The Apprentice
# Parts: DISCOVERY -> GUIDANCE -> GROWTH
# Concepts: for loops, range(), turtle graphics, loop patterns
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגילה מרובת-חלקים. השלימי כל חלק לפי הסדר.

# %%
import turtle

# %% [markdown]
# ## חלק 1: גילוי - לומדים מעבודת המאסטר
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# שימי לב כיצד {{mentor}} משתמשת בלולאות כדי לצייר צורות.
# נסי לנחש את הפלט לפני שתריצי את הקוד.

# %% locked
# The master draws a simple shape
t = turtle.Turtle()
t.speed(0)  # Fastest drawing
for i in range(3):
    t.forward(80)
    t.left(120)

# %% locked
# The master draws another shape
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(150, 0)  # Move to a new position
t.pendown()
for i in range(4):
    t.forward(60)
    t.right(90)

# %% locked
# The master draws a series of marks
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, 0)
t.pendown()
for count in range(1, 6):
    t.forward(count * 15)
    t.penup()
    t.forward(10)
    t.pendown()

# %% [markdown]
# תארי מה תצייר כל לולאה.
#
# הלולאה הראשונה מציירת: _______________ (רמז: 3 צלעות, פניות שמאלה)
#     צורה: _______________
#     מספר צלעות: ___
#     זווית פנייה: ___ מעלות
#
# הלולאה השנייה מציירת: _______________ (רמז: 4 צלעות, פניות ימינה)
#     צורה: _______________
#     מספר צלעות: ___
#     זווית פנייה: ___ מעלות
#
# הלולאה השלישית מציירת: _______________ (רמז: הקווים מתארכים)
#     כמה קווים: ___
#     אורך הקו הראשון: ___ יחידות
#     אורך הקו האחרון: ___ יחידות
#
# > רמז: הזווית החיצונית של צורה עם N צלעות היא 360/N מעלות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: הדרכה - תרגול עם עזרה
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# עכשיו נתרגלי עם קצת פיגום שיעזור לך.
#
# השלימי את הרווחים החסרים כדי לצייר מחומש (5 צלעות).
# מחומש זקוק לזוויות חיצוניות של 72 מעלות (360/5 = 72).
#
# t = turtle.Turtle()
# t.speed(0)
# t.penup()
# t.goto(-100, 150)
# t.pendown()
# for i in range(___):           # כמה צלעות?
#     t.forward(50)
#     t.right(___)               # איזו זווית?
#
# > רמז: למחומש יש 5 צלעות ופונים 72 מעלות בכל פעם.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השלימי את הרווחים החסרים כדי לצייר משושה (6 צלעות).
# משושה זקוק לזוויות חיצוניות של 60 מעלות (360/6 = 60).
#
# t = turtle.Turtle()
# t.speed(0)
# t.penup()
# t.goto(100, 150)
# t.pendown()
# ___ i in ___(6):               # השלימי את מילות המפתח של הלולאה
#     t.forward(40)
#     t.___(60)                  # השלימי את שיטת הפנייה
#
# > רמז: השתמשי ב-`for` וב-`range` כדי ליצור את הלולאה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - צרי משלך
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# עכשיו צרי צורות משלך עם מה שלמדת!
#
# צייר מתומן (8 צלעות) עבור {{hero}}.
#
# 1. צרי צב
# 2. מקמי אותו בנקודה (-200, -100) עם `penup`/`goto`/`pendown`
# 3. השתמשי בלולאת `for` שחוזרת 8 פעמים
# 4. בכל סיבוב: `forward` 35 יחידות, `left` 45 מעלות
#
# > רמז: 360/8 = 45 מעלות לכל פנייה
#
# פלט צפוי: מתומן (צורה בת 8 צלעות).

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# צייר דפוס מדרגות ספירלי עבור {{creature}}.
# כל מדרגה קצת ארוכה מהקודמת.
#
# 1. צרי צב
# 2. מקמי אותו בנקודה (0, -150)
# 3. השתמשי בלולאת `for` עם `range(1, 13)` לציור 12 קווים
# 4. בכל סיבוב:
#    - `forward(step * 8)` כאשר `step` הוא משתנה הלולאה
#    - `right(30)`
#
# פלט צפוי: דפוס ספירלי שבו כל קו ארוך מהקודם.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# צרי צורה משלך ב{{school}}!
# נסי מספר צלעות שונה, או דפוס כוכב.
#
# רעיונות:
# - צייר צורה בת 10 צלעות (עשרון) עם פניות של 36 מעלות
# - צייר כוכב בן 5 קצוות עם פניות של 144 מעלות
# - צייר כוכב בן 7 קצוות עם פניות של כ-154 מעלות
#
# היי יצירתית!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("PART 1: DISCOVERY - Study the Master's Work")
print("=" * 50)

print("\n--- master_code_1 ---")
master_code_1()

print("\n--- master_code_2 ---")
master_code_2()

print("\n--- master_code_3 ---")
master_code_3()

print("\n--- Your Predictions ---")
your_predictions()

print("\n" + "=" * 50)
print("PART 2: GUIDANCE - Practice with Support")
print("=" * 50)

print("\n--- guided_exercise_a ---")
# guided_exercise_a()  # Uncomment when blanks are filled

print("\n--- guided_exercise_b ---")
# guided_exercise_b()

print("\n" + "=" * 50)
print("PART 3: GROWTH - Create Your Own")
print("=" * 50)

print("\n--- your_creation_a ---")
your_creation_a()

print("\n--- your_creation_b ---")
your_creation_b()

print("\n--- your_creation_c ---")
your_creation_c()

print("\n" + "=" * 50)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
turtle.done()
