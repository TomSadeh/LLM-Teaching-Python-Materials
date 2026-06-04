# =============================================================================
# Write Code: if/else Statements
# =============================================================================
# Difficulty: 2
# Concepts: if/else, two-branch decisions, mutual exclusion
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
# {{hero}} צריכה לבדוק אם היא יכולה להיכנס ל-{{location}}.
# הכניסה דורשת לפחות 100 זהב.
#
# 1. צרי משתנה בשם `gold` עם הערך 150
# 2. כתבי משפט `if`: `if gold >= 100:`
# 3. בתוך בלוק ה-`if`, הדפיסי `"{{hero}} enters {{location}}"`
# 4. הוסיפי פסוקית `else`
# 5. בתוך בלוק ה-`else`, הדפיסי `"{{hero}} cannot afford entry"`
#
# פלט צפוי כש-`gold` שווה 150:
#   {{hero}} enters {{location}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{mentor}} בודקת את המבחן של {{hero}}.
# ציון של 60 ומעלה נחשב לעובר.
#
# 1. צרי משתנה בשם `score` עם הערך 55
# 2. הדפיסי `f"{{hero}}'s score: {score}"`
# 3. כתבי `if/else` שבודק אם `score >= 60`
# 4. אם נכון, הדפיסי `"Congratulations! You passed!"`
# 5. אחרת, הדפיסי `"Keep practicing. You'll get it next time!"`
# 6. אחרי ה-`if/else`, הדפיסי `"{{mentor}} records the result."`
#
# פלט צפוי כש-`score` שווה 55:
#   {{hero}}'s score: 55
#   Keep practicing. You'll get it next time!
#   {{mentor}} records the result.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# בדקי אם {{hero}} יודעת את הסיסמה כדי להיכנס ל-{{school}}.
# השתמשי ב-`==` כדי להשוות מחרוזות.
#
# 1. צרי משתנה בשם `secret` עם הערך `"{{password}}"`
# 2. צרי משתנה בשם `attempt` עם הערך `"{{password}}"`
# 3. כתבי `if/else` שבודק אם `attempt == secret`
# 4. אם נכון, הדפיסי `"{{greeting}}"`
# 5. אחרת, הדפיסי `"Access denied. Incorrect password."`
#
# פלט צפוי כשהסיסמאות תואמות:
#   {{greeting}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# {{CONTEXT_STUDENT_TASK}}
#
# {{hero}} רוצה לקנות {{item}} שעולה 80 זהב.
# עדכני את `gold` אם הרכישה מצליחה.
#
# 1. צרי משתנה בשם `gold` עם הערך 100
# 2. צרי משתנה בשם `price` עם הערך 80
# 3. הדפיסי `f"{{hero}} has {gold} gold"`
# 4. כתבי `if/else` שבודק אם `gold >= price`
# 5. אם נכון:
#    - חסרי את `price` מ-`gold`: `gold = gold - price`
#    - הדפיסי `"Purchased {{item}}!"`
# 6. אחרת:
#    - הדפיסי `"Not enough gold!"`
# 7. אחרי ה-`if/else`, הדפיסי `f"Remaining gold: {gold}"`
#
# פלט צפוי כש-`gold` שווה 100 ו-`price` שווה 80:
#   {{hero}} has 100 gold
#   Purchased {{item}}!
#   Remaining gold: 20

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
