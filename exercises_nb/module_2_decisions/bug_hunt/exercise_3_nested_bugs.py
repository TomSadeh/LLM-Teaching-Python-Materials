# =============================================================================
# Bug Hunt: Nested Conditional Bugs
# =============================================================================
# Difficulty: 5
# Concepts: Nested if statements, complex conditional logic
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# {{hero}} צריכה לעמוד במספר תנאים כדי להיכנס לאזור מוגבל.
# צריך להיות ברמה 10+ ועם תעודת מעבר, **או** להיות VIP.
#
# **התנהגות מצופה:**
# VIP אמורה להיכנס ללא קשר לרמה
#
# **התנהגות בפועל:**
# VIP ברמה 5 נדחית מהכניסה
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
level = 5
has_pass = False
is_vip = True

# BUG: VIP check is nested inside level check
if level >= 10:
    if has_pass:
        print("{{hero}} enters with pass!")
    elif is_vip:
        print("{{hero}} enters as VIP!")
    else:
        print("Access denied - no pass.")
else:
    print("Access denied - level too low.")

# %% [markdown]
# **מה מצאתי:** בדיקת VIP צריכה להיות עצמאית, ללא קשר לרמה
# **הבאג:** בדיקת `is_vip` נמצאת בתוך הבלוק של `level >= 10`
#          כך שמי שהיא VIP ברמה נמוכה לא נבדקת בכלל
#
# **התיקון:** לבדוק VIP קודם, או לשנות את מבנה הלוגיקה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
level = 5
has_pass = False
is_vip = True

# Better structure:
# if is_vip:
#     enter as VIP
# elif level >= 10 and has_pass:
#     enter with pass
# else:
#     denied
pass

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# למחשבון הציונים של {{mentor}} יש תנאים מקוננים.
# אבל משהו לא בסדר עם לוגיקת ההזחה!
#
# **התנהגות מצופה:**
# ציון 75 אמור להדפיס `"C"` ו-`"Needs improvement"`
#
# **התנהגות בפועל:**
# ציון 75 מדפיס `"C"` אבל גם `"Excellent work!"` (שגוי!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")

# BUG: Wrong indentation - this should be inside an if
if grade == "A":
    print("{{exclamation}} Excellent work!")
print("Needs improvement.")  # This always runs!

# %% [markdown]
# **מה מצאתי:** `"Needs improvement"` רץ לכולם
# **הבאג:** ההודעה השנייה לא נמצאת בתוך בלוק `else`
#          היא אמורה להדפיס רק אם הציון הוא לא `"A"`
#
# **התיקון:**

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
score = 75
# ... grade assignment ...
# if grade == "A":
#     print("Excellent!")
# else:
#     print("Needs improvement.")
pass

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# {{hero}} בודקת אם היא יכולה להשלים אתגר.
# יש לבדוק מספר דרישות בסדר הנכון.
#
# **התנהגות מצופה:**
# לבדוק קודם רמה, אחר כך זהב, ואז פריט
# חוסר בזהב (רמה בסדר, אין פריט) אמור להציג `"Need more gold"`
#
# **התנהגות בפועל:**
# מציג `"Need the {{item}}"` גם כשהבעיה היא בזהב
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
level = 10
gold = 30  # Not enough gold!
has_challenge_item = True

if level >= 5:
    # BUG: Wrong nesting - checking item before gold
    if has_challenge_item:
        if gold >= 50:
            print("{{hero}} completes the challenge!")
        else:
            print("Need more gold!")
    else:
        print("Need the {{item}}!")
else:
    print("Level too low for this challenge.")

# %% [markdown]
# **מה מצאתי:** סדר הקינון הלא נכון מביא להודעות שגיאה לא נכונות
# **הבאג:** עם `gold=30` ו-`has_challenge_item=True`:
#          - נכנסת לבדיקת הרמה (בסדר)
#          - נכנסת לבדיקת `has_challenge_item` (נכון)
#          - נכשלת בבדיקת הזהב -> `"Need more gold!"` (נכון במקרה הזה!)
#
# רגע, נקראי שוב... למעשה הקוד עובד לקלט הזה.
# נסי: `level=10`, `gold=100`, `has_challenge_item=False`
#          - נכנסת לבדיקת הרמה (בסדר)
#          - נכשלת בבדיקת `has_challenge_item` (שקר)
#          - מדפיסה `"Need the item!"` לפני שבדקה את הזהב
#
# בעיית הלוגיקה: צריך לבדוק מה חסר בפועל
# גישה טובה יותר: לבדוק כל דרישה ולדווח מה חסר

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
level = 10
gold = 30
has_challenge_item = True
pass

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# מערכת הפעולות של {{hero}} בוחרת מה לעשות לפי {{primary_stat}} ו-{{secondary_stat}}.
# אבל לתנאים המקוננים יש פגם לוגי!
#
# **התנהגות מצופה:**
# {{primary_stat}} נמוך **וגם** {{secondary_stat}} נמוך — צריך `"{{retreat_action}}"`
# {{primary_stat}} נמוך **או** {{secondary_stat}} נמוך (אבל לא שניהם) — צריך `"{{basic_action}}"`
#
# **התנהגות בפועל:**
# {{primary_stat}} נמוך תמיד מוביל ל-`"{{retreat_action}}"` ללא קשר ל-{{secondary_stat}}
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
primary = 20
secondary = 80  # Plenty of {{secondary_stat}}!

if primary < 30:
    # BUG: Always retreats when {{primary_stat}} is low, ignoring {{secondary_stat}}
    print("{{hero}} must {{retreat_action}}!")
elif secondary < 20:
    print("{{hero}} must {{basic_action}}!")
else:
    print("{{hero}} uses {{spell2}}!")

# %% [markdown]
# **מה מצאתי:** `{{retreat_action}}` צריך לדרוש גם {{primary_stat}} נמוך וגם {{secondary_stat}} נמוך
# **הבאג:** הקוד הנוכחי מבצע נסיגה על {{primary_stat}} נמוך לבד
#          צריך `{{retreat_action}}` רק אם `primary < 30` **ו-**`secondary < 20`
#
# **התיקון:**

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
primary = 20
secondary = 80

# Better logic:
# if primary < 30 and secondary < 20:
#     {{retreat_action}}
# elif primary < 30:
#     recover {{primary_stat}}
# elif secondary < 20:
#     {{basic_action}}
# else:
#     use special ability
pass

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Expected: VIP enters regardless of level")
print("Buggy version:")
buggy_a()
print("\nFixed version:")
# fix_a()

print("\n=== {{CASE_2_TITLE}} ===")
print("Expected: C grade says 'Needs improvement' only")
print("Buggy version:")
buggy_b()
print("\nFixed version:")
# fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Expected: Correct error message for missing requirement")
print("Buggy version:")
buggy_c()
print("\nFixed version:")
# fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Expected: Only {{retreat_action}} if BOTH stats are low")
print("Buggy version:")
buggy_d()
print("\nFixed version:")
# fix_d()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
