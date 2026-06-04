# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לשנות מילונים:
# להוסיף ערכים חדשים, לעדכן ערכים קיימים ולמחוק ערכים.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# למדי להוסיף ולעדכן ערכים במילון.
#
# 1. צרי מילון ריק בשם `stats`
#
# 2. הוסיפי את הערכים האלה אחד אחד:
#         stats["name"] = "{{hero}}"
#         stats["health"] = 100
#         stats["strength"] = 10
#
# 3. הדפיסי את המילון
#
# 4. עדכני את ה-health ל-150 (השתמשי באותו מפתח)
#
# 5. הדפיסי את המילון שוב כדי לראות את השינוי

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# תרגלי הגדלה והקטנה של ערכים במילון.
#
# 1. צרי את מילון המלאי הזה:
#         inventory = {"{{item}}": 5, "{{spell1}}": 3, "{{spell2}}": 1}
#
# 2. הוסיפי עוד 2 יחידות של "{{item}}" (הגדילי את הערך)
# > רמז: inventory["{{item}}"] = inventory["{{item}}"] + 2
#
# 3. השתמשי ב-1 יחידה של "{{spell1}}" (הקטיני את הערך)
#
# 4. הוסיפי פריט חדש "{{spell3}}" עם כמות 1
#
# 5. הדפיסי את המלאי הסופי
#
# 6. הדפיסי את סך כל הפריטים
# > רמז: השתמשי ב-`sum()` עם `inventory.values()`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# תרגלי מחיקת ערכים ממילונים.
#
# 1. צרי את מילון הרישום הזה:
#         registry = {
#             "active": ["{{hero}}", "{{heroine}}"],
#             "retired": ["{{mentor}}"],
#             "temporary": ["visitor"]
#         }
#
# 2. הדפיסי את כל המפתחות לפני השינוי
#
# 3. מחקי את המפתח "temporary" באמצעות: del registry["temporary"]
#
# 4. הדפיסי את כל המפתחות אחרי השינוי
#
# 5. הוסיפי את {{friend}} לרשימה "active"
# > רמז: registry["active"].append("{{friend}}")
#
# 6. הדפיסי את הרישום הסופי

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
