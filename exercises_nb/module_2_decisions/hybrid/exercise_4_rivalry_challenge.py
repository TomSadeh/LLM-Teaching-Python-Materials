# =============================================================================
# Hybrid Exercise: The Rivalry - Conditional Challenge
# =============================================================================
# Difficulty: 5
# Arc: The Rivalry
# Parts: SETBACK -> GROWTH -> CONFRONTATION
# Concepts: Bug hunting, writing conditionals, building a complete system
# =============================================================================

# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# זוהי תרגילה בכמה חלקים. השלימי כל חלק לפי הסדר.
#
# ## חלק 1: נפילה — ניתוח הקוד הכושל
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{hero}} הפסידה אתגר תכנות מול {{villain}}!
# הבודק של {{villain}} מצא 3 באגים בהגשה של {{hero}}.
# מצאי והבני כל באג.

# %%
# BUG 1: Score classifier
score = 85
if score > 90:  # Wrong: should be >= 90 for A
    grade = "A"
elif score > 80:  # Wrong: should be >= 80 for B
    grade = "B"
else:
    grade = "F"
print(f"Bug 1 - Grade for 85: {grade}")  # Should be B, not F!

# BUG 2: Access checker
age = 18
has_id = True
if age > 18 and has_id:  # Wrong: should be >= 18
    print("Bug 2 - Access: Granted")
else:
    print("Bug 2 - Access: Denied")  # Wrong output!

# BUG 3: Range checker
value = 50
if value >= 0 or value <= 100:  # Wrong: should be 'and' not 'or'
    print(f"Bug 3 - {value} is in range [0, 100]: True")
else:
    print(f"Bug 3 - {value} is in range [0, 100]: False")

# %% [markdown]
# ## זה תמיד מדפיס True, אפילו עבור value = 500!
#
# ## באג 1: מסווג ציונים
# מה הבאג? _____________________________________
# צפוי עבור score=85: _____ בפועל: _____
# תיקון: שני `>` ל־___
#
# ## באג 2: בודק גישה
# מה הבאג? _____________________________________
# צפוי עבור age=18: _____ בפועל: _____
# תיקון: שני `>` ל־___
#
# ## באג 3: בודק טווח
# מה הבאג? _____________________________________
# למה `or` לא עובד כאן? _____________________________
# תיקון: שני `or` ל־___

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה — בני לוגיקה תנאית נכונה
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# תרגלי כתיבת לוגיקה תנאית נכונה.
# השלימי כל פונקציה כדי לחזק את הכישורים שלך.
#
# כתבי מסווג ציונים נכון.
# A: 90 ומעלה, B: 80–89, C: 70–79, D: 60–69, F: מתחת ל־60
#
# בדיקה: score = 75 (אמורה לקבל C)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
score = 75
pass

# %% [markdown]
# כתבי בודק גיל/הרשאה נכון.
# מותר להיכנס אם: (age >= 18) OR (age >= 13 AND has_parent_permission)
#
# בדיקה: age=15, has_parent_permission=True (אמורה להיות מורשית)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
age = 15
has_parent_permission = True
pass

# %% [markdown]
# כתבי בודק טווח נכון.
# ערך נמצא בטווח אם: value >= min_val AND value <= max_val
#
# בדיקה: value=50, min_val=0, max_val=100 (אמורה להיות בטווח)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
value = 50
min_val = 0
max_val = 100
pass

# %% [markdown]
# ## חלק 3: עימות — בני מערכת החלטות שלמה
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# עכשיו בני מערכת החלטות שלמה כדי להביס את {{villain}}!
# צרי מעריך סטטוס משחק שמטפל נכון בכל המקרים.
#
# בני מעריך סטטוס משחק שלם עבור {{school}}.
#
# משתני קלט:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
player_primary = 45
player_secondary = 80
player_level = 12
boss_defeated = False
has_key = True

# Requirements:
# 1. First, check game over conditions:
#    - If primary <= 0: status = "Game Over"
#
# 2. If not game over, check victory conditions:
#    - If boss_defeated AND has_key: status = "Victory!"
#
# 3. If neither, determine current state:
#    - If primary < 30 AND secondary < 30: status = "Critical - Must {{retreat_action}}!"
#    - Elif primary < 50 OR secondary < 50: status = "Caution - Recover"
#    - Elif level >= 15: status = "Ready for {{villain}}!"
#    - Else: status = "Keep training"
#
# 4. Print the status and explain why:
#    f"{{hero}} Status: {status}"
#    f"{{primary_stat}}: {player_primary}, {{secondary_stat}}: {player_secondary}, Level: {player_level}"
#
# Expected output for the given values:
#   {{hero}} Status: Caution - Recover
#   {{primary_stat}}: 45, {{secondary_stat}}: 80, Level: 12
#   (Because primary < 50)

pass

# %%
print("\n--- Test Cases ---")

# Test 1: Game Over
print("Test 1: primary=0 -> Should be 'Game Over'")

# Test 2: Victory
print("Test 2: boss_defeated=True, has_key=True -> Should be 'Victory!'")

# Test 3: Critical
print("Test 3: primary=20, secondary=15 -> Should be 'Critical - Must {{retreat_action}}!'")

# Test 4: Caution (low primary)
print("Test 4: primary=40, secondary=100 -> Should be 'Caution - Recover'")

# Test 5: Ready for {{villain}}
print("Test 5: primary=100, secondary=100, level=15 -> Should be 'Ready for {{villain}}!'")

# Test 6: Keep training
print("Test 6: primary=100, secondary=100, level=10 -> Should be 'Keep training'")

print("\nIf all tests pass, you've defeated {{villain}}!")

# %%
print("=" * 50)
print("PART 1: SETBACK - Analyze the Failed Code")
print("=" * 50)

print("\n--- Failed Submission (3 bugs) ---")
failed_submission()

print("\n--- Your Bug Analysis ---")
analyze_bugs()

print("\n" + "=" * 50)
print("PART 2: GROWTH - Build Better Conditional Logic")
print("=" * 50)

print("\n--- growth_exercise_1: Grade Classifier ---")
growth_exercise_1()

print("\n--- growth_exercise_2: Permission Checker ---")
growth_exercise_2()

print("\n--- growth_exercise_3: Range Checker ---")
growth_exercise_3()

print("\n" + "=" * 50)
print("PART 3: CONFRONTATION - Build a Complete System")
print("=" * 50)

print("\n--- Your Final Solution ---")
your_final_solution()

# test_your_solution()  # Uncomment to run tests

print("\n" + "=" * 50)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
