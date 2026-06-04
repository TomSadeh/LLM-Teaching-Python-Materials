# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי את היסודות של מילונים:
# יצירתם, גישה לערכים, והבנת זוגות מפתח-ערך.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# צרי מילון שמאחסן מידע על {{hero}}.
#
# 1. צרי מילון בשם `profile` עם המפתחות והערכים הבאים:
#    - "name" -> המחרוזת "{{hero}}"
#    - "skill" -> המחרוזת "{{spell1}}"
#    - "level" -> המספר השלם 1
#
# 2. הדפיסי את המילון כולו
#
# 3. הדפיסי רק את הערך המשויך למפתח "name"
#
# דוגמה לפורמט הפלט:
#   {'name': '...', 'skill': '...', 'level': 1}
#   ...

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# צרי מילון שמאחסן ניקוד עבור כמה דמויות.
#
# 1. צרי מילון בשם `scores` עם:
#    - "{{hero}}" -> 100
#    - "{{heroine}}" -> 150
#    - "{{friend}}" -> 75
#
# 2. הדפיסי את הניקוד של כל דמות בעזרת f-string
#    פורמט: "[name] has [score] points"
#
# 3. חשבי והדפיסי את סכום כל הניקודים
#
# > רמז: גישה לערכים עם scores["key_name"]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# צרי מילון שמייצג את המאפיינים של {{item}}.
#
# 1. צרי מילון בשם `item_stats` עם:
#    - "name" -> "{{item}}"
#    - "power" -> 50
#    - "durability" -> 100
#    - "rarity" -> "uncommon"
#
# 2. בדקי אם הכוח גדול מ-30
#    אם כן, הדפיסי: "[item name] is powerful!"
#    אם לא, הדפיסי: "[item name] needs upgrading."
#
# 3. הדפיסי את כל המפתחות במילון
# > רמז: השתמשי במתודה `.keys()`

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
