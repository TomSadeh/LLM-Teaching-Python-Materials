# =============================================================================
# Write Code: Comparison Operators
# =============================================================================
# Difficulty: 2-3
# Concepts: ==, !=, <, >, <=, >= operators
# =============================================================================

"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Check if {{hero}}'s level exactly matches the challenge requirement.
    # Use == for equality comparison.
    #
    # Step 1: Create a variable called hero_level with the value 10
    # Step 2: Create a variable called challenge_level with the value 10
    # Step 3: Write an if/else using ==
    # Step 4: If hero_level == challenge_level, print "Challenge unlocked for {{hero}}!"
    # Step 5: Else, print "Level mismatch."
    #
    # Expected output:
    #   Challenge unlocked for {{hero}}!
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Check if the creature approaching is NOT a friend.
    # Use != for inequality comparison.
    #
    # Step 1: Create a variable called approaching with the value "{{villain}}"
    # Step 2: Create a variable called friend_name with the value "{{friend}}"
    # Step 3: Write an if/else using !=
    # Step 4: If approaching != friend_name, print "{{hero}} prepares for action!"
    # Step 5: Else, print "{{hero}} waves hello."
    #
    # Expected output:
    #   {{hero}} prepares for action!
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Check if {{hero}}'s health is critically low using <.
    # Then check if it's at or below warning level using <=.
    #
    # Step 1: Create a variable called health with the value 25
    # Step 2: Create a variable called critical with the value 20
    # Step 3: Create a variable called warning with the value 50
    #
    # Step 4: Write an if/else using < for critical check
    #         If health < critical, print "CRITICAL: Find healing immediately!"
    #         Else, print "Health above critical level."
    #
    # Step 5: Write another if/else using <= for warning check
    #         If health <= warning, print "WARNING: Health getting low."
    #         Else, print "Health is acceptable."
    #
    # Expected output when health is 25:
    #   Health above critical level.
    #   WARNING: Health getting low.
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Check if {{hero}} can afford an item using >= for "at least" comparison.
    #
    # Step 1: Create a variable called gold with the value 100
    # Step 2: Create a variable called price with the value 100
    # Step 3: Print f"{{item}} costs {price} gold. {{hero}} has {gold} gold."
    # Step 4: Write an if/else using >=
    #         If gold >= price, print "{{hero}} can buy the {{item}}!"
    #         Else, print "Not enough gold."
    #
    # Expected output:
    #   {{item}} costs 100 gold. {{hero}} has 100 gold.
    #   {{hero}} can buy the {{item}}!
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Classify a score using multiple comparisons.
    # Use >, <, and == in different checks.
    #
    # Step 1: Create a variable called score with the value 85
    # Step 2: Create a variable called average with the value 70
    #
    # Step 3: Check if score > average and print "Above average!"
    # Step 4: Check if score < average and print "Below average."
    # Step 5: Check if score == average and print "Exactly average."
    #
    # Note: These are three separate if statements (not if/elif/else).
    #       Only one should trigger for score = 85.
    #
    # Expected output:
    #   Above average!
    pass


def main():
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

    print("\n=== {{PHASE_5_TITLE}} ===")
    exercise_e()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
