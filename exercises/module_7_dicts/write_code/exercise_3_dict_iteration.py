# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לעבור על מילונים בעזרת המתודות
# `.keys()`, `.values()` ו-`.items()`.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# תרגלי מעבר על מפתחות המילון.
#
# 1. צרי את מילון הרשימה הבא:
#    roster = {
#        "{{hero}}": "active",
#        "{{heroine}}": "active",
#        "{{mentor}}": "retired",
#        "{{friend}}": "training"
#    }
#
# 2. הדפיסי את כל השמות (המפתחות) ברשימה.
#    השתמשי בלולאה: `for name in roster.keys():`
#
# 3. ספרי כמה אנשים יש ברשימה.
#    > רמז: השתמשי ב-`len(roster)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# תרגלי מעבר על ערכי המילון.
#
# 1. צרי את מילון הציונים הבא:
#    scores = {
#        "{{hero}}": 85,
#        "{{heroine}}": 92,
#        "{{friend}}": 78
#    }
#
# 2. חשבי את סכום כל הציונים.
#    השתמשי בלולאה: `for score in scores.values():`
#
# 3. חשבי את הציון הממוצע.
#
# 4. הדפיסי: `"Total: [total], Average: [average]"`
#
# אפשר גם להשתמש ב-`sum(scores.values())` ישירות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# תרגלי מעבר על זוגות מפתח-ערך עם `.items()`.
#
# 1. צרי את מילון המלאי הבא:
#    inventory = {
#        "{{item}}": 5,
#        "{{spell1}}": 3,
#        "{{spell2}}": 1
#    }
#
# 2. הדפיסי כל פריט וכמות שלו בעזרת `.items()`.
#    השתמשי בלולאה: `for item_name, quantity in inventory.items():`
#    פורמט: `"[item_name]: [quantity]"`
#
# 3. מצאי והדפיסי את הפריט עם הכמות הגבוהה ביותר.
#    > רמז: עקבי אחרי הערך המקסימלי במהלך הלולאה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# השתמשי בלולאות כדי לסנן ולעבד נתוני מילון.
#
# 1. צרי את מילון הסטטוס הבא:
#    status = {
#        "{{hero}}": "healthy",
#        "{{heroine}}": "{{harmful_status}}",
#        "{{friend}}": "healthy",
#        "{{mentor}}": "{{harmful_status}}"
#    }
#
# 2. צרי רשימה של כל הדמויות שהן `"healthy"`.
#    השתמשי בלולאה עם `.items()` ובתנאי `if`.
#
# 3. הדפיסי: `"Healthy characters: [list]"`
#
# 4. ספרי כמה דמויות נמצאות במצב `"{{harmful_status}}"`.

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
