# =============================================================================
# Write Code: if/elif/else Chains
# =============================================================================
# Difficulty: 3
# Concepts: if/elif/else, multiple branches, first match wins
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
    # {{mentor}} assigns grades based on scores.
    # Use if/elif/else to determine the grade.
    #
    # Step 1: Create a variable called score with the value 78
    # Step 2: Write an if/elif/else chain:
    #         - if score >= 90: print "Grade: A"
    #         - elif score >= 80: print "Grade: B"
    #         - elif score >= 70: print "Grade: C"
    #         - else: print "Grade: F"
    #
    # Expected output when score is 78:
    #   Grade: C
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
    # Sort {{hero}} into a {{house}} based on their strongest trait.
    # Use a numeric trait value.
    #
    # Step 1: Create a variable called trait with the value "courage"
    # Step 2: Write an if/elif/else chain:
    #         - if trait == "courage": print "{{hero}} joins the Warriors"
    #         - elif trait == "wisdom": print "{{hero}} joins the Scholars"
    #         - elif trait == "kindness": print "{{hero}} joins the Healers"
    #         - else: print "{{hero}} joins the Explorers"
    #
    # Expected output when trait is "courage":
    #   {{hero}} joins the Warriors
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
    # Determine {{hero}}'s rank based on their level.
    # Print their full status.
    #
    # Step 1: Create a variable called level with the value 15
    # Step 2: Create a variable called rank (will be assigned in the if/elif/else)
    # Step 3: Write an if/elif/else chain to assign rank:
    #         - if level >= 20: rank = "Master"
    #         - elif level >= 15: rank = "Expert"
    #         - elif level >= 10: rank = "Intermediate"
    #         - elif level >= 5: rank = "Apprentice"
    #         - else: rank = "Novice"
    # Step 4: Print f"{{hero}} - Level {level} - Rank: {rank}"
    #
    # Expected output when level is 15:
    #   {{hero}} - Level 15 - Rank: Expert
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
    # Determine what {{hero}} can buy at the shop with their gold.
    # Use if/elif/else to find the best affordable item.
    #
    # Step 1: Create a variable called gold with the value 75
    # Step 2: Print f"{{hero}} has {gold} gold"
    # Step 3: Write an if/elif/else chain:
    #         - if gold >= 100: print "You can buy the {{spell3}} scroll!"
    #         - elif gold >= 50: print "You can buy the {{spell2}} scroll!"
    #         - elif gold >= 20: print "You can buy the {{spell1}} scroll!"
    #         - else: print "You can't afford any scrolls."
    #
    # Expected output when gold is 75:
    #   {{hero}} has 75 gold
    #   You can buy the {{spell2}} scroll!
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
    # Create a weather response system for {{school}}.
    # Different temperatures mean different activities.
    #
    # Step 1: Create a variable called temperature with the value 22
    # Step 2: Create a variable called activity (assigned in if/elif/else)
    # Step 3: Write an if/elif/else chain:
    #         - if temperature >= 30: activity = "indoor study"
    #         - elif temperature >= 20: activity = "outdoor training"
    #         - elif temperature >= 10: activity = "warm-up exercises"
    #         - else: activity = "rest by the fire"
    # Step 4: Print f"At {temperature} degrees, {{school}} recommends: {activity}"
    #
    # Expected output when temperature is 22:
    #   At 22 degrees, {{school}} recommends: outdoor training
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
