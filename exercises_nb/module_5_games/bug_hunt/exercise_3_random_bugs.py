# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# נושא: מציאת באגים בשימוש במודול `random`
# רמת קושי: 2-3
#
# כמה מלכודות נפוצות במודול `random`:
# - `randint` כולל את שני הקצוות (שלא כמו `range`)
# - שכחה לייבא את `random`
# - שימוש בפונקציה הלא-נכונה למשימה

# %%
import random

# %% [markdown]
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# קוביה זו אמורה להטיל ערכים בין 1 ל-6, אבל משהו לא בסדר.
#
# התנהגות צפויה:
# מחזירה ערכים מ-1 עד 6 (כולל)
#
# התנהגות בפועל:
# מחזירה ערכים מ-0 עד 5 (לעולם לא מחזירה 6!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
return random.randint(0, 5)  # BUG: Range should be 1 to 6

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# הבוחרת הזו אמורה לבחור פריט מרשימה, אבל היא בוחרת אינדקסים במקום.
#
# התנהגות צפויה:
# מחזירה אחד מהם: `"{{hero}}"`, `"{{villain}}"`, `"{{friend}}"`
#
# התנהגות בפועל:
# מחזירה 0, 1 או 2 (האינדקסים, לא השמות!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
characters = ["{{hero}}", "{{villain}}", "{{friend}}"]
return random.randint(0, len(characters) - 1)  # BUG: Returns index, not item

# %% [markdown]
# מה מצאתי: ________________________________
#
# > רמז: השתמשי ב-`random.choice()` במקום `randint` כדי לבחור מרשימה
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# פונקציית ההסתברות הזו אמורה להחזיר `True` בכ-70% מהמקרים.
#
# התנהגות צפויה:
# מחזירה `True` בערך ב-70% מהפעמים
#
# התנהגות בפועל:
# מחזירה `True` בערך ב-30% מהפעמים (הפוך!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
roll = random.random()
return roll > 0.7  # BUG: Condition is inverted! Should be < 0.7

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# מחשבון הנזק הזה סובל משגיאת off-by-one בטווח שלו.
#
# התנהגות צפויה:
# מחלק נזק בסיס ועוד בונוס של 1-5 (כלומר 11-15 אם הבסיס הוא 10)
#
# התנהגות בפועל:
# מחלק נזק בסיס ועוד בונוס של 1-6 (כולל 6, שהוא גבוה מדי)
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
bonus = random.randint(1, 6)  # BUG: Should be 1-5, not 1-6
return base_damage + bonus

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_5_TITLE}}
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# מטיל המטבע הזה אמור להחזיר `"heads"` או `"tails"` באופן אקראי.
#
# התנהגות צפויה:
# מחזירה `"heads"` או `"tails"` בהסתברות שווה
#
# התנהגות בפועל:
# תמיד מחזירה `"heads"` (המשתנה מוגדר אבל לא נעשה בו שימוש)
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

# %%
result = random.choice(["heads", "tails"])
return "heads"  # BUG: Ignores the random result, always returns "heads"

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_6_TITLE}}
# {{CONTEXT_CASE_6_NARRATIVE}}
#
# מחולל הסטטיסטיקות הזה אמור ליצור ערכים מאוזנים (סך-הכל בסביבות 30).
#
# התנהגות צפויה:
# מייצר שלושה ערכים של 8-12 כל אחד, סך-הכל 24-36
#
# התנהגות בפועל:
# כל שלושת הערכים זהים (הגלגול בוצע פעם אחת ושימש שלוש פעמים)
#
# {{CONTEXT_INVESTIGATION_PROMPT_6}}

# %%
roll = random.randint(8, 12)
return {
    "strength": roll,  # BUG: Same roll used for all three!
    "agility": roll,
    "wisdom": roll
}

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Testing die roller (should be 1-6):")
results = [buggy_roll_die() for _ in range(10)]
print(f"Buggy rolls: {results}")
print("Notice: never gets 6, sometimes gets 0!")

print("\n=== {{CASE_2_TITLE}} ===")
print("Testing character picker:")
print(f"Buggy result: {buggy_pick_character()} (should be a name, not number)")

print("\n=== {{CASE_3_TITLE}} ===")
print("Testing 70% chance (100 trials):")
successes = sum(1 for _ in range(100) if buggy_seventy_percent_chance())
print(f"Buggy successes: {successes}/100 (should be ~70)")

print("\n=== {{CASE_4_TITLE}} ===")
print("Testing damage calculator (base 10):")
damages = [buggy_calculate_damage(10) for _ in range(10)]
print(f"Buggy damages: {damages}")
print("Notice: might include 16 (10+6), which shouldn't be possible!")

print("\n=== {{CASE_5_TITLE}} ===")
print("Testing coin flipper (10 flips):")
flips = [buggy_flip_coin() for _ in range(10)]
print(f"Buggy flips: {flips}")
print("Notice: always heads!")

print("\n=== {{CASE_6_TITLE}} ===")
print("Testing stat generator:")
stats = buggy_generate_balanced_stats()
print(f"Buggy stats: {stats}")
print("Notice: all stats are identical!")

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
