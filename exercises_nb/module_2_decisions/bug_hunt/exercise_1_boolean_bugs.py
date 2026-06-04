# =============================================================================
# Bug Hunt: Boolean Expression Bugs
# =============================================================================
# Difficulty: 4
# Concepts: and/or confusion, not placement, operator precedence
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# {{hero}} כתבה קוד שבודק אם אפשר לקנות פריט.
# צריך לפחות 100 זהב **וגם** לפחות 50 אבני חן.
#
# התנהגות צפויה:
# עם `gold=150` ו-`gems=30`, צריך להדפיס `"Cannot afford item"`
# (כי כמות אבני החן נמוכה מדי)
#
# התנהגות בפועל:
# מדפיס `"Buying item!"` למרות שיש רק 30 אבני חן
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
gold = 150
gems = 30

# Need BOTH resources to be sufficient
if gold >= 100 or gems >= 50:  # BUG: Wrong operator
    print(f"{{hero}} buys the {{item}}!")
else:
    print("Cannot afford the {{item}}.")

# %% [markdown]
# מה מצאתי: שימוש ב-`or` כשצריך `and`
# הבאג: `or` אומר שמספיק שתנאי **אחד** יהיה נכון
#       `and` אומר שה**שניים** חייבים להיות נכונים
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
gold = 150
gems = 30
pass

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# {{hero}} רוצה להיכנס ל-{{danger_location}} רק אם **אין** {{obstacle}}.
#
# התנהגות צפויה:
# עם `danger_detected=True`, צריך להדפיס `"Too dangerous!"`
#
# התנהגות בפועל:
# מדפיס `"Entering!"` גם כשסכנה מזוהה
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
danger_detected = True

if danger_detected == False:  # Awkward but works
    print("{{hero}} enters {{danger_location}}!")
else:
    print("Too dangerous! {{hero}} stays back.")

# Wait, the bug is actually in this version:
if not danger_detected == True:  # BUG: Operator precedence!
    print("Entering safely...")

# %% [markdown]
# מה מצאתי: `not danger_detected == True` מבלבל
# הבאג: `not` פועל על `danger_detected` קודם, ואז משווה ל-`True`
#       `not True` הוא `False`, ואז `False == True` הוא `False`
#       כלומר התנאי תמיד `False`!
#
# דרכים טובות יותר לכתוב "אם danger_detected הוא False":
# 1. `if not danger_detected:`
# 2. `if danger_detected == False:`
# 3. `if not (danger_detected == True):`  — עם סוגריים
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
danger_detected = True
pass

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# {{mentor}} מדרגת תלמידות: צריך ציון >= 60 **או** `extra_credit` כדי לעבור.
#
# התנהגות צפויה:
# עם `score=55` ו-`extra_credit=True`, צריך להדפיס `"Passed!"`
# (כי `extra_credit` הוא `True`)
#
# התנהגות בפועל:
# מדפיס `"Failed."` גם עם קרדיט נוסף
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
score = 55
extra_credit = True

if score >= 60 and extra_credit:  # BUG: Wrong operator
    print("{{hero}} passed!")
else:
    print("{{hero}} failed.")

# %% [markdown]
# מה מצאתי: שימוש ב-`and` כשצריך `or`
# הבאג: `and` דורש שה**שני** תנאים יהיו `True`
#       הדרישה אומרת ציון גבוה **או** קרדיט נוסף — מספיק אחד
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
score = 55
extra_credit = True
pass

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# {{hero}} יכולה לנוח אם **לא** {{busy_activity}} **וגם לא** {{harmful_status}}.
#
# התנהגות צפויה:
# עם `is_busy=False` ו-`is_harmed=True`, צריך להדפיס `"Cannot rest"`
# (כי היא פצועה, למרות שלא עסוקה)
#
# התנהגות בפועל:
# מדפיס `"Resting..."` גם כשהיא פצועה
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
is_busy = False
is_harmed = True

if not is_busy or is_harmed:  # BUG: Logic error
    print("{{hero}} rests and recovers.")
else:
    print("Cannot rest right now!")

# %% [markdown]
# מה מצאתי: התנאי הפוך
# הבאג: `not is_busy or is_harmed` אומר:
#       "יכולה לנוח אם לא עסוקה **או** אם פצועה"
#       אבל אנחנו רוצות: "יכולה לנוח אם לא עסוקה **וגם** לא פצועה"
#
# התיקון (צריך שני התנאים כדי לנוח):

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
is_busy = False
is_harmed = True
pass

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Expected: 'Cannot afford' (gems too low)")
print("Buggy version:")
buggy_a()
print("\nFixed version:")
# fix_a()

print("\n=== {{CASE_2_TITLE}} ===")
print("Expected: 'Too dangerous' when danger detected")
print("Buggy version:")
buggy_b()
print("\nFixed version:")
# fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Expected: 'Passed' with extra credit")
print("Buggy version:")
buggy_c()
print("\nFixed version:")
# fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Expected: 'Cannot rest' when harmed")
print("Buggy version:")
buggy_d()
print("\nFixed version:")
# fix_d()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
