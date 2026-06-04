# =============================================================================
# Bug Hunt: Basics Bugs
# =============================================================================
# Difficulty: 5
# Concepts: All Module 0 concepts - integration debugging
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# התנהגות צפויה:
# אמורה להדפיס `{{hero}} has 75 gold` (100 - 25 = 75)
#
# התנהגות בפועל:
# מדפיסה `{{hero}} has 10025 gold` (חיבור כמחרוזות!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
gold = "100"
spent = 25
remaining = gold - spent
print("{{hero}} has", remaining, "gold")

# %% [markdown]
# מה מצאתי: ________________________________
#
# > רמז: שימי לב איך `gold` מוגדר. האם זה מספר או מחרוזת?
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# התנהגות צפויה:
# אמורה להדפיס את שם הגיבורה השמור במשתנה
#
# התנהגות בפועל:
# מדפיסה את המילה `hero_name` במקום השם האמיתי
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
hero_name = "{{hero}}"
print("Welcome,", "hero_name")

# %% [markdown]
# מה מצאתי: ________________________________
#
# > רמז: מתי שמים גרשיים סביב שם משתנה?
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# התנהגות צפויה:
# אמורה לחשב כפל הניקוד: 50 * 2 = 100
#
# התנהגות בפועל:
# המשתנה `doubled` לא נמצא בשימוש בכלל!
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
score = 50
doubled = score * 2
print("Double score:", score)

# %% [markdown]
# מה מצאתי: ________________________________
#
# > רמז: בדקי איזה משתנה מודפס בפועל.
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# התנהגות צפויה:
# אמורה לברך את {{hero}} ב-{{school}} בשורה אחת
#
# התנהגות בפועל:
# שגיאה: `can only concatenate str (not "int") to str`
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
name = "{{hero}}"
level = 5
message = name + " is level " + level + " at {{school}}"
print(message)

# %% [markdown]
# מה מצאתי: ________________________________
#
# > רמז: אי אפשר להשתמש ב-`+` כדי לחבר מחרוזת עם מספר ישירות.
# > אפשר להמיר את המספר למחרוזת, או להשתמש בגישה אחרת.
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Buggy version:")
# buggy_a()  # This would cause an error!
print("(Error: can't subtract from string)")
print("\nFixed version:")
fix_a()

print("\n=== {{CASE_2_TITLE}} ===")
print("Buggy version:")
buggy_b()
print("\nFixed version:")
fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Buggy version:")
buggy_c()
print("\nFixed version:")
fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Buggy version:")
# buggy_d()  # This would cause an error!
print("(Error: can't concatenate str and int)")
print("\nFixed version:")
fix_d()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
