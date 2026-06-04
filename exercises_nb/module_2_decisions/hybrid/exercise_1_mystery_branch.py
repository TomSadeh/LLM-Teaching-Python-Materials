# =============================================================================
# Hybrid Exercise: The Mystery - Unexpected Branch
# =============================================================================
# Difficulty: 2-3
# Arc: The Mystery
# Parts: DISCOVERY -> INVESTIGATION -> IMPROVEMENT
# Concepts: if/else debugging, tracing, conditional logic
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגילה בכמה חלקים. השלימי כל חלק לפי הסדר.
#
# ## חלק 1: גילוי - שימי לב למשהו לא צפוי
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{hero}} כתבה קוד ב-{{school}}, אבל הוא מתנהג בצורה מוזרה!
# הריצי כל קטע קוד ושימי לב למה לא עובד כמו שצריך.

# %%
# {{hero}} wants to check if they have enough energy to train.
# Expected: Should say "Ready to train!" when energy is 75
# But something is wrong...
energy = 75
if energy > 75:
    print("{{hero}} is ready to train!")
else:
    print("{{hero}} needs to rest.")

# %%
# {{mentor}} is checking if {{hero}} passed the exam.
# Expected: Score of 60 should say "Passed!"
# But something is wrong...
score = 60
required = 60
if score > required:
    print("{{hero}} passed!")
else:
    print("{{hero}} failed.")

# %%
# {{hero}} is trying to enter {{location}} with a password.
# Expected: Correct password should grant access.
# But something is wrong...
secret = "{{password}}"
entered = "{{password}} "  # Notice the extra space!
if secret == entered:
    print("Access granted to {{location}}!")
else:
    print("Access denied!")

# %% [markdown]
# ## התצפיות שלי
#
# mystery_code_1:
#   פלט צפוי: "{{hero}} is ready to train!"
#   פלט בפועל: ________________________________
#   מה מוזר? ________________________________
#
# mystery_code_2:
#   פלט צפוי: "{{hero}} passed!"
#   פלט בפועל: ________________________________
#   מה מוזר? ________________________________
#
# mystery_code_3:
#   פלט צפוי: "Access granted to {{location}}!"
#   פלט בפועל: ________________________________
#   מה מוזר? ________________________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: חקירה - עקבי אחרי הקוד
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# עכשיו עקבי אחרי כל תעלומה כדי למצוא את הסיבה המדויקת.
#
# ## עקבי אחרי הקוד
#
# mystery_code_1 משתמשת ב: `if energy > 75`
#
# energy = 75
# תנאי: 75 > 75 = _______ (True או False?)
#
# הבעיה: `>` אומר "גדול מ-" אבל 75 אינו גדול מ-75.
#
# > רמז: באיזה אופרטור להשתמש במקום? _______ (רמז: `>=`)
#
# הבאג: שימוש ב-`>` כשצריך ___

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## עקבי אחרי הקוד
#
# mystery_code_2 משתמשת ב: `if score > required`
#
# score = 60
# required = 60
# תנאי: 60 > 60 = _______ (True או False?)
#
# הבעיה: ציון השווה ל-required אמור להיחשב כעובר.
#
# > רמז: באיזה אופרטור להשתמש במקום? _______ (רמז: `>=`)
#
# הבאג: שימוש ב-`>` כשצריך ___

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## עקבי אחרי הקוד
#
# mystery_code_3 משווה בין המחרוזות האלה:
# secret = "{{password}}"
# entered = "{{password}} "
#
# האם הן שוות? _______ (True או False?)
#
# ספרי את התווים בכל אחת:
# ל-secret יש ___ תווים
# ל-entered יש ___ תווים (ספרי בזהירות!)
#
# הבאג: ________________________________
#
# לקח: מחרוזות חייבות להתאים בדיוק, כולל רווחים!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: שיפור - תקני את הבעיות
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# עכשיו תקני כל באג שמצאת!
#
# ## תקני את הבאג
#
# תקני את בדיקת האנרגיה כך ש-75 אנרגיה ייחשב כ-"מוכנה לאימון".
#
# מה שמצאתי: שימוש ב-`>` במקום `>=` גורם ל-75 לא לעבור את הבדיקה
#
# התיקון שלי:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
energy = 75
pass

# %% [markdown]
# ## תקני את הבאג
#
# תקני את בדיקת המבחן כך שציון השווה ל-required ייחשב כעובר.
#
# מה שמצאתי: שימוש ב-`>` במקום `>=` גורם לציונים שווים להיכשל
#
# התיקון שלי:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
score = 60
required = 60
pass

# %% [markdown]
# ## תקני את הבאג
#
# תקני את הסיסמה כך שתתאים בדיוק (הסירי את הרווח המיותר).
#
# מה שמצאתי: הסיסמה שהוזנה הכילה רווח נוסף בסוף
#
# התיקון שלי:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
secret = "{{password}}"
pass

# %%
print("=" * 50)
print("PART 1: DISCOVERY - Observe the Unexpected")
print("=" * 50)

print("\n--- mystery_code_1 ---")
print("Expected: '{{hero}} is ready to train!'")
print("Actual:")
mystery_code_1()

print("\n--- mystery_code_2 ---")
print("Expected: '{{hero}} passed!'")
print("Actual:")
mystery_code_2()

print("\n--- mystery_code_3 ---")
print("Expected: 'Access granted to {{location}}!'")
print("Actual:")
mystery_code_3()

print("\n--- Your Observations ---")
your_observations()

print("\n" + "=" * 50)
print("PART 2: INVESTIGATION - Trace the Code")
print("=" * 50)

print("\n--- trace_mystery_1 ---")
trace_mystery_1()

print("\n--- trace_mystery_2 ---")
trace_mystery_2()

print("\n--- trace_mystery_3 ---")
trace_mystery_3()

print("\n" + "=" * 50)
print("PART 3: IMPROVEMENT - Fix the Issues")
print("=" * 50)

print("\n--- fixed_code_1 ---")
# fixed_code_1()  # Uncomment after fixing

print("\n--- fixed_code_2 ---")
# fixed_code_2()

print("\n--- fixed_code_3 ---")
# fixed_code_3()

print("\n" + "=" * 50)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
