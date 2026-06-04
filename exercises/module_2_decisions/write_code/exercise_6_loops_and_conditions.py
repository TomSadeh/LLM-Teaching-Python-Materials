# =============================================================================
# Write Code: Loops with Conditionals
# =============================================================================
# Difficulty: 5
# Concepts: Combining for loops with if/elif/else statements
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
# ספרי כמה מספרים בין 1 ל-10 גדולים מ-5.
#
# 1. צרי משתנה בשם `count` עם הערך 0
# 2. השתמשי בלולאה: `for num in range(1, 11):`
# 3. בתוך הלולאה, כתבי תנאי:
#         `if num > 5:`
#             `count = count + 1`
# 4. אחרי הלולאה, הדפיסי `f"Numbers greater than 5: {count}"`
#
# פלט צפוי:
#   Numbers greater than 5: 5

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# הדפיסי האם כל מספר בין 1 ל-5 הוא זוגי או אי-זוגי.
#
# 1. השתמשי בלולאה: `for num in range(1, 6):`
# 2. בתוך הלולאה, בדקי אם `num % 2 == 0` (זוגי)
# 3. אם זוגי, הדפיסי `f"{num} is even"`
# 4. אחרת, הדפיסי `f"{num} is odd"`
#
# > רמז: `%` הוא אופרטור המודולו (שארית החלוקה).
# >       אם `num % 2 == 0`, המספר מתחלק ב-2 בדיוק (זוגי).
#
# פלט צפוי:
#   1 is odd
#   2 is even
#   3 is odd
#   4 is even
#   5 is odd

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{hero}} בודקת את המלאי. ספרי פריטים יקרי ערך (שווים יותר מ-50).
# השתמשי בסכום מצטבר כדי לעקוב אחר הערך הכולל.
#
# 1. צרי משתנים:
#         `item_values = [20, 75, 30, 100, 45, 80]`  # שימי לב: זו רשימה!
#         `valuable_count = 0`
#         `total_valuable = 0`
#
# 2. השתמשי בלולאה: `for value in item_values:`
# 3. בתוך הלולאה, בדקי אם `value > 50`
# 4. אם כן:
#         - הוסיפי 1 ל-`valuable_count`
#         - הוסיפי את `value` ל-`total_valuable`
#
# 5. אחרי הלולאה, הדפיסי:
#         `f"Found {valuable_count} valuable items"`
#         `f"Total value: {total_valuable} gold"`
#
# > רמז: כאן אנחנו עוברות על רשימה של מספרים — זו הצצה למודול 3 (רשימות)!
#
# פלט צפוי:
#   Found 3 valuable items
#   Total value: 255 gold

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# סווגי ציונים באמצעות `if`/`elif`/`else` בתוך לולאה.
# ספרי כמה A, B, C ו-F יש.
#
# 1. צרי רשימת ציונים:
#         `scores = [95, 82, 67, 73, 88, 91, 55, 78]`
#
# 2. צרי מונים:
#         `count_a = 0`
#         `count_b = 0`
#         `count_c = 0`
#         `count_f = 0`
#
# 3. השתמשי בלולאה: `for score in scores:`
# 4. בתוך הלולאה, השתמשי ב-`if`/`elif`/`elif`/`else`:
#         - `if score >= 90: count_a += 1`
#         - `elif score >= 80: count_b += 1`
#         - `elif score >= 70: count_c += 1`
#         - `else: count_f += 1`
#
# 5. אחרי הלולאה, הדפיסי את המונים:
#         `f"A grades: {count_a}"`
#         `f"B grades: {count_b}"`
#         `f"C grades: {count_c}"`
#         `f"F grades: {count_f}"`
#
# פלט צפוי:
#   A grades: 2
#   B grades: 2
#   C grades: 2
#   F grades: 2

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{hero}} מתאמנת ב-{{school}}. בכל יום, בדקי תנאים ופעלי בהתאם.
# השתמשי במספר תנאים בתוך לולאה.
#
# 1. צרי ערכי התחלה:
#         `energy = 100`
#         `skill = 0`
#
# 2. השתמשי בלולאה: `for day in range(1, 6):  # 5 ימים`
# 3. הדפיסי `f"Day {day}: Energy={energy}, Skill={skill}"`
#
# 4. בתוך הלולאה, בדקי אנרגיה והתאמני:
#         `if energy >= 30:`
#             `# אימון: צוברת כישורים, מאבדת אנרגיה`
#             `skill = skill + 10`
#             `energy = energy - 25`
#             `print "  {{hero}} trains hard!"`
#         `else:`
#             `# מנוחה: מחזירה אנרגיה`
#             `energy = energy + 20`
#             `print "  {{hero}} rests."`
#
# 5. אחרי הלולאה, הדפיסי את הנתונים הסופיים:
#         `f"Final: Energy={energy}, Skill={skill}"`
#
# פלט צפוי (האנרגיה מתחילה ב-100):
#   Day 1: Energy=100, Skill=0
#     {{hero}} trains hard!
#   Day 2: Energy=75, Skill=10
#     {{hero}} trains hard!
#   Day 3: Energy=50, Skill=20
#     {{hero}} trains hard!
#   Day 4: Energy=25, Skill=30
#     {{hero}} rests.
#   Day 5: Energy=45, Skill=30
#     {{hero}} trains hard!
#   Final: Energy=20, Skill=40

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
