# =============================================================================
# Bug Hunt: General Conditional Bugs
# =============================================================================
# Difficulty: 5
# Concepts: Common conditional mistakes across all types
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# {{hero}} בודקת אם הניקוד שלה מזכה אותה בבונוס.
# ניקוד של בדיוק 100 אמור גם הוא לזכות בבונוס!
#
# התנהגות צפויה:
# כאשר score=100, אמורה להודפס ההודעה "Bonus earned!"
#
# התנהגות בפועל:
# כאשר score=100, מודפסת ההודעה "No bonus."
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
score = 100
if score > 100:  # BUG: Wrong operator
    print("{{hero}} earned a bonus!")
else:
    print("No bonus this time.")

# %% [markdown]
# מה מצאתי: שימוש ב-`>` במקום ב-`>=`
# הבאג: `>` פירושו "גדול מ-" ולא כולל שוויון.
#        ‏score=100 אינו `> 100`, ולכן התנאי נכשל.
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
score = 100
pass

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# {{mentor}} רוצה לתת הודעות שונות לפי הציון, אבל הסדר של התנאים לא נכון!
#
# התנהגות צפויה:
# כאשר score=95, אמורה להודפס ההודעה "Excellent!" (הדרגה הגבוהה ביותר)
#
# התנהגות בפועל:
# כאשר score=95, מודפסת ההודעה "Good job!" (דרגה שגויה)
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
score = 95
# BUG: Conditions in wrong order - first match wins!
if score >= 60:
    print("Good job!")
elif score >= 80:
    print("Great work!")
elif score >= 90:
    print("Excellent!")
else:
    print("Keep practicing.")

# %% [markdown]
# מה מצאתי: יש לבדוק את הסף הגבוה ביותר ראשון.
# הבאג: ‏score=95 מתאים לתנאי `score >= 60` ראשון, ולכן הקוד עוצר שם.
#        תנאי ה-`elif` לא נבדקים בכלל.
#
# התיקון (יש לבדוק את הסף הגבוה ביותר ראשון):

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
score = 95
pass

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# {{hero}} מנסה לעדכן את הזהב שלה אחרי רכישה, אבל הזהב לא משתנה בכלל!
#
# התנהגות צפויה:
# אחרי הרכישה, הזהב אמור להיות 70 (100 - 30)
#
# התנהגות בפועל:
# אחרי הרכישה, הזהב עדיין 100
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
gold = 100
item_price = 30

if gold >= item_price:
    print("{{hero}} buys the {{item}}!")
    # BUG: Forgot to actually subtract!
    # gold - item_price  # This calculates but doesn't save!

print(f"Gold remaining: {gold}")

# %% [markdown]
# מה מצאתי: החישוב לא שומר את התוצאה.
# הבאג: `gold - item_price` מחשב אבל לא שומר,
#        צריך לכתוב `gold = gold - item_price` כדי לשמור את התוצאה.
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
gold = 100
item_price = 30
pass

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# ל-{{hero}} יש קוד שבודק אם שתי סיסמאות תואמות, אבל יש בו בעיית תחביר בהשוואה!
#
# התנהגות צפויה:
# סיסמה נכונה אמורה להדפיס "Access granted!"
#
# התנהגות בפועל:
# הקוד לא רץ בכלל — שגיאת תחביר!
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
# NOTE: This code is commented because it would cause a syntax error
#
# password = "{{password}}"
# attempt = "{{password}}"
#
# if attempt = password:  # BUG: = instead of ==
#     print("Access granted to {{location}}!")
# else:
#     print("Access denied!")

# The bug is using = (assignment) instead of == (comparison)
print("(This function shows a common bug - see comments)")

# %% [markdown]
# מה מצאתי: שימוש ב-`=` במקום ב-`==`.
# הבאג: `=` הוא השמה (קביעת ערך), `==` הוא השוואה (בדיקת שוויון).
#        בתנאי צריך להשוות, לא להשים.
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
password = "{{password}}"
attempt = "{{password}}"
pass

# %% [markdown]
# ## {{CASE_5_TITLE}}
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# קוד ה-level-up של {{hero}} אמור לפעול כשמגיעים לרמה 10, אבל הודעת ה-level-up לא מודפסת!
#
# התנהגות צפויה:
# כשה-level מגיע ל-10, אמורה להודפס ההודעה "Level up!"
#
# התנהגות בפועל:
# ההודעה לא מופיעה בכלל
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

# %%
level = 9

# {{hero}} gains experience...
level = level + 1  # Now level is 10

# BUG: Checking wrong variable/value
if level == 9:
    print("{{hero}} leveled up! Now level 10!")

print(f"Current level: {level}")

# %% [markdown]
# מה מצאתי: בדיקה אם `level == 9` אחרי שכבר הוסיפו 1.
# הבאג: אחרי `level + 1`, הרמה היא 10, לא 9.
#        התנאי צריך לבדוק `== 10`.
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
level = 9
level = level + 1
pass

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Expected: 'Bonus earned' when score is 100")
print("Buggy version:")
buggy_a()
print("\nFixed version:")
# fix_a()

print("\n=== {{CASE_2_TITLE}} ===")
print("Expected: 'Excellent' for score of 95")
print("Buggy version:")
buggy_b()
print("\nFixed version:")
# fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Expected: Gold should be 70 after purchase")
print("Buggy version:")
buggy_c()
print("\nFixed version:")
# fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Expected: Working password comparison")
print("Buggy version:")
buggy_d()
print("\nFixed version:")
# fix_d()

print("\n=== {{CASE_5_TITLE}} ===")
print("Expected: 'Level up' message when reaching level 10")
print("Buggy version:")
buggy_e()
print("\nFixed version:")
# fix_e()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
