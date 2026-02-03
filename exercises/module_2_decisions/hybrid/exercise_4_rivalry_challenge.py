# =============================================================================
# Hybrid Exercise: The Rivalry - Conditional Challenge
# =============================================================================
# Difficulty: 5
# Arc: The Rivalry
# Parts: SETBACK -> GROWTH -> CONFRONTATION
# Concepts: Bug hunting, writing conditionals, building a complete system
# =============================================================================

"""
{{CONTEXT_SETBACK_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: SETBACK - Analyze the Failed Code
# ============================================================
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{hero}} lost a coding challenge to {{villain}}!
# {{villain}}'s validator found 3 bugs in {{hero}}'s submission.
# Find and understand each bug.


def failed_submission():
    """{{hero}}'s buggy code - find the 3 bugs!"""
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
    # This always prints True, even for value = 500!


def analyze_bugs():
    # ✏️ YOUR ANALYSIS HERE ✏️
    #
    # BUG 1: Score classifier
    # What's the bug? _____________________________________
    # Expected for score=85: _____ Actual: _____
    # Fix: Change > to ___
    #
    # BUG 2: Access checker
    # What's the bug? _____________________________________
    # Expected for age=18: _____ Actual: _____
    # Fix: Change > to ___
    #
    # BUG 3: Range checker
    # What's the bug? _____________________________________
    # Why does 'or' not work? _____________________________
    # Fix: Change or to ___
    pass


# ============================================================
# PART 2: GROWTH - Build Better Conditional Logic
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Practice writing correct conditional logic.
# Complete each function to build your skills.


def growth_exercise_1():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Write a correct grade classifier.
    # A: 90+, B: 80-89, C: 70-79, D: 60-69, F: below 60
    #
    # Test with score = 75 (should get C)
    score = 75
    pass


def growth_exercise_2():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Write a correct age/permission checker.
    # Can enter if: (age >= 18) OR (age >= 13 AND has_parent_permission)
    #
    # Test with age=15, has_parent_permission=True (should be allowed)
    age = 15
    has_parent_permission = True
    pass


def growth_exercise_3():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Write a correct range checker.
    # Value must be >= min_val AND <= max_val to be in range.
    #
    # Test with value=50, min_val=0, max_val=100 (should be in range)
    value = 50
    min_val = 0
    max_val = 100
    pass


# ============================================================
# PART 3: CONFRONTATION - Build a Complete Decision System
# ============================================================
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# Now build a complete decision system to defeat {{villain}}!
# Create a game status evaluator that correctly handles all cases.


def your_final_solution():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Build a complete game status evaluator for {{school}}.
    #
    # Input variables:
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


def test_your_solution():
    """Test cases to verify your solution works correctly"""
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


def main():
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


main()
