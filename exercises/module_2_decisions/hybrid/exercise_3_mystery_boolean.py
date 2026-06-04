# =============================================================================
# Hybrid Exercise: The Mystery - Boolean Confusion
# =============================================================================
# Difficulty: 4
# Arc: The Mystery
# Parts: DISCOVERY -> INVESTIGATION -> IMPROVEMENT
# Concepts: and/or/not debugging, tracing boolean expressions
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגיל בן מספר חלקים. השלימי כל חלק לפי הסדר.
#
# ## חלק 1: גילוי - מה קורה פה?
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{hero}} מצאה קוד בקרת גישה ב-{{school}}.
# הקוד נראה מכניס את האנשים הלא נכונים פנימה!

# %%
# Only VIP members with valid tickets should enter
# Expected: Non-VIP with ticket should NOT enter
is_vip = False
has_ticket = True

if is_vip or has_ticket:
    print("Welcome to the {{location}}!")
else:
    print("Access denied.")

# %%
# {{hero}} should NOT go outside if it's raining AND cold
# Expected: Raining alone should be fine
is_raining = True
is_cold = False

if not is_raining and is_cold:  # Something's wrong here
    print("{{hero}} goes outside.")
else:
    print("{{hero}} stays inside.")

# %%
# {{hero}} needs EITHER a primary {{item}} OR (a backup {{item}} AND supplies) to fight
# Expected: Having only backup only (no supplies) should NOT work
has_primary = False
has_backup = True
has_supplies = False

if has_primary or has_backup or has_supplies:  # Logic is wrong
    print("{{hero}} is ready to fight!")
else:
    print("{{hero}} cannot fight without weapons.")

# %% [markdown]
# **הרשמי את התצפיות שלך:**
#
# mystery_code_1:
#   ציפינו: מי שאינה VIP לא אמורה להיכנס גם עם כרטיס
#   בפועל: ________________________________
#   האם `or` נכון עבור "חברות VIP עם כרטיס תקף"? _____
#
# mystery_code_2:
#   ציפינו: גשם בלבד (ללא קור) אמור לאפשר יציאה החוצה
#   בפועל: ________________________________
#   מה בודקת בעצם `not is_raining and is_cold`? ____________
#
# mystery_code_3:
#   ציפינו: גיבוי בלי ציוד לא אמור לעבוד
#   בפועל: ________________________________
#   האם `has_primary or has_backup or has_supplies` תואמת את הדרישה? _____

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: חקירה - עקבי אחרי ההיגיון הבוליאני
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# עקבי אחרי כל תעלומה כדי להבין את הביטויים הבוליאניים.
#
# **עקבי אחרי הקוד:**
#
# תנאי: `is_vip or has_ticket`
# ערכים: `False or True`
#
# `False or True` = _____ (`True`/`False`)
#
# הבעיה: "חברות VIP עם כרטיס תקף" פירושו שצריך את שניהם.
# `or` פירושו שמספיק אחד מהם.
#
# האופרטור הנכון צריך להיות: _____

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# **עקבי אחרי הקוד:**
#
# תנאי: `not is_raining and is_cold`
# ערכים: `not True and False`
#
# 1. `not True` = _____
# 2. `_____ and False` = _____
#
# זה בודק: "לא גשום וקר"
# אבל רצינו: "לא (גשום וקר)"
#
# ההבדל:
# - `not is_raining and is_cold` = יוצאים אם לא גשום, אבל קר
# - `not (is_raining and is_cold)` = יוצאים אלא אם גשום וקר גם יחד
#
# ההיגיון הנוכחי יוצא החוצה כש: _______________________
# ההיגיון הנכון אמור לצאת החוצה כש: _______________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# **עקבי אחרי הקוד:**
#
# תנאי: `has_primary or has_backup or has_supplies`
# ערכים: `False or True or False`
#
# `False or True` = _____
# `_____ or False` = _____
#
# זה בודק: "יש לפחות אחד משלושת הפריטים"
# אבל רצינו: "יש נשק ראשי, או (נשק גיבוי וציוד)"
#
# הביטוי הנכון עם סוגריים:
# `has_primary or (has_backup and has_supplies)`
#
# בואי נאמת: `False or (True and False)`
# 1. `True and False` = _____
# 2. `False or _____` = _____
#
# עכשיו הקוד מסרב נכון לאפשר כניסה!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: שיפור - תקני את הביטויים הבוליאניים
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# תקני כל ביטוי בוליאני שגוי!
#
# **תקני את הבאג:**
#
# דרישה: חברות VIP עם כרטיס תקף (צריך את שניהם)
# המקורי (שגוי): `is_vip or has_ticket`
#
# התיקון שלך:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
is_vip = False
has_ticket = True

# Fix: Change 'or' to 'and'
pass

# %% [markdown]
# **תקני את הבאג:**
#
# דרישה: לא לצאת החוצה אם גשום וקר גם יחד
#         (כל אחד בנפרד - בסדר גמור)
# המקורי (שגוי): `not is_raining and is_cold`
#
# התיקון שלך:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
is_raining = True
is_cold = False

# Fix: Add parentheses: not (is_raining and is_cold)
pass

# %% [markdown]
# **תקני את הבאג:**
#
# דרישה: צריך נשק ראשי, או (נשק גיבוי וציוד)
# המקורי (שגוי): `has_primary or has_backup or has_supplies`
#
# התיקון שלך:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
has_primary = False
has_backup = True
has_supplies = False

# Fix: Use parentheses to group: has_primary or (has_backup and has_supplies)
pass

# %%
print("\n--- Testing Fixed Code 1 ---")
# Test: VIP without ticket
is_vip = True
has_ticket = False
# Should deny entry (missing ticket)

# Test: Non-VIP with ticket
is_vip = False
has_ticket = True
# Should deny entry (not VIP)

# Test: VIP with ticket
is_vip = True
has_ticket = True
# Should allow entry

print("\n--- Testing Fixed Code 2 ---")
# Test: Raining only
is_raining = True
is_cold = False
# Should allow outside (only one condition, not both)

# Test: Raining AND cold
is_raining = True
is_cold = True
# Should stay inside (both conditions)

print("\n--- Testing Fixed Code 3 ---")
# Test: Only bow
has_primary = False
has_backup = True
has_supplies = False
# Should deny (bow needs arrows)

# Test: Bow with arrows
has_primary = False
has_backup = True
has_supplies = True
# Should allow

print("If all tests pass, your fixes are correct!")

# %%
print("=" * 50)
print("PART 1: DISCOVERY - Observe Confusing Behavior")
print("=" * 50)

print("\n--- mystery_code_1 ---")
print("Expected: 'Access denied' for non-VIP")
print("Actual:")
mystery_code_1()

print("\n--- mystery_code_2 ---")
print("Expected: 'goes outside' when only raining")
print("Actual:")
mystery_code_2()

print("\n--- mystery_code_3 ---")
print("Expected: 'cannot fight' with only bow (no arrows)")
print("Actual:")
mystery_code_3()

print("\n--- Your Observations ---")
your_observations()

print("\n" + "=" * 50)
print("PART 2: INVESTIGATION - Trace the Boolean Logic")
print("=" * 50)

print("\n--- trace_mystery_1 ---")
trace_mystery_1()

print("\n--- trace_mystery_2 ---")
trace_mystery_2()

print("\n--- trace_mystery_3 ---")
trace_mystery_3()

print("\n" + "=" * 50)
print("PART 3: IMPROVEMENT - Fix the Boolean Expressions")
print("=" * 50)

print("\n--- fixed_code_1 ---")
# fixed_code_1()  # Uncomment after fixing

print("\n--- fixed_code_2 ---")
# fixed_code_2()

print("\n--- fixed_code_3 ---")
# fixed_code_3()

# test_fixed_code()  # Uncomment to test your fixes

print("\n" + "=" * 50)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
