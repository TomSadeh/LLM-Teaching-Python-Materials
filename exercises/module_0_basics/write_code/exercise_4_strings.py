# =============================================================================
# Write Code: Strings
# =============================================================================
# Difficulty: 3
# Concepts: string creation, concatenation, combining with print
# =============================================================================

# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# צרי הודעת ברוכה הבאה עבור {{school}}.
#
# 1. צרי משתנה `school` עם הערך "{{school}}"
# 2. צרי משתנה `message` שמחבר את "Welcome to " עם school
#    השתמשי באופרטור +: message = "Welcome to " + school
# 3. הדפיסי את ההודעה
#
# פלט צפוי: Welcome to {{school}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# צרי ברכה עבור {{hero}} ב-{{school}}.
#
# 1. צרי `hero` עם הערך "{{hero}}"
# 2. צרי `location` עם הערך "{{school}}"
# 3. הדפיסי עם פסיקים: print(hero, "is studying at", location)
#
# > רמז: פסיקים בתוך `print()` מוסיפים רווחים אוטומטית בין הפריטים.
#
# פלט צפוי: {{hero}} is studying at {{school}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# בני תיאור של ה-{{item}} של {{hero}}.
#
# 1. צרי `item` עם הערך "{{item}}"
# 2. צרי `color` עם הערך "golden"
# 3. צרי `description` על ידי חיבור: "a " + color + " " + item
# 4. הדפיסי: "{{hero}} found" ואחריו description
#
# פלט צפוי: {{hero}} found a golden {{item}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# ערבבי מחרוזות ומספרים בפלט.
#
# 1. צרי `hero` עם הערך "{{hero}}"
# 2. צרי `level` עם הערך 5 (מספר, בלי גרשיים!)
# 3. הדפיסי עם פסיקים: print(hero, "reached level", level)
#
# > רמז: שימוש בפסיקים בתוך `print()` מטפל במספר אוטומטית — אין צורך להמיר אותו למחרוזת!
#
# פלט צפוי: {{hero}} reached level 5

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
