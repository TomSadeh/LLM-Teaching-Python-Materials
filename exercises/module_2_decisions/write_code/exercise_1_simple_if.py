# =============================================================================
# Write Code: Simple if Statements
# =============================================================================
# Difficulty: 1
# Concepts: Basic if statement, conditional execution, indentation
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
# {{hero}} מתאמנת ב-{{school}}.
# כתבי משפט `if` שבודק אם רמת האנרגיה שלה גבוהה מ-50.
#
# 1. צרי משתנה בשם `energy` עם הערך 75
# 2. כתבי משפט `if`: `if energy > 50:`
# 3. בתוך בלוק ה-`if`, הדפיסי `"{{hero}} is ready to train!"`
#
# > רמז: זכרי לשים נקודתיים אחרי התנאי ולהזיח את ה-`print`.
#
# פלט צפוי כאשר `energy` שווה 75:
#   {{hero}} is ready to train!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{hero}} מצאה {{item}} עם ערך מסוים.
# בדקי אם הערך גבוה מספיק כדי לשמור אותו.
#
# 1. צרי משתנה בשם `item_value` עם הערך 120
# 2. הדפיסי `f"Found {{item}} worth {item_value} gold"`
# 3. כתבי משפט `if`: `if item_value > 100:`
# 4. בתוך בלוק ה-`if`, הדפיסי `"This {{item}} is valuable!"`
# 5. אחרי בלוק ה-`if` (ללא הזחה), הדפיסי `"Search complete."`
#
# פלט צפוי כאשר `item_value` שווה 120:
#   Found {{item}} worth 120 gold
#   This {{item}} is valuable!
#   Search complete.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{hero}} בודקת את בריאותה לפני משימה.
# כמה פעולות יכולות לקרות כאשר תנאי מתקיים.
#
# 1. צרי משתנה בשם `health` עם הערך 80
# 2. צרי משתנה בשם `min_health` עם הערך 60
# 3. כתבי משפט `if`: `if health > min_health:`
# 4. בתוך בלוק ה-`if`, הדפיסי שתי שורות:
#    `"Health check passed!"`
#    `"{{hero}} can proceed to {{location}}."`
# 5. אחרי בלוק ה-`if`, הדפיסי `f"Current health: {health}"`
#
# > רמז: שתי הוראות ה-`print` שבתוך ה-`if` צריכות להיות מוזחות.
#
# פלט צפוי כאשר `health` שווה 80:
#   Health check passed!
#   {{hero}} can proceed to {{location}}.
#   Current health: 80

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{mentor}} בודק/ת את הידע של {{hero}}.
# בדקי אם התשובה נכונה באמצעות `==` (שוויון).
#
# 1. צרי משתנה בשם `answer` עם הערך 42
# 2. צרי משתנה בשם `correct_answer` עם הערך 42
# 3. הדפיסי `"Checking your answer..."`
# 4. כתבי משפט `if`: `if answer == correct_answer:`
# 5. בתוך בלוק ה-`if`, הדפיסי `"{{exclamation}} Correct!"`
#
# > רמז: השתמשי ב-`==` כדי לבדוק אם שני ערכים שווים (לא `=`).
#
# פלט צפוי כאשר שניהם שווים ל-42:
#   Checking your answer...
#   {{exclamation}} Correct!

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

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
