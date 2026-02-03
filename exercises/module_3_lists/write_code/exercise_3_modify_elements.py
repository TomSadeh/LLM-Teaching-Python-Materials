# =============================================================================
# Write Code: Modify List Elements
# =============================================================================
# Difficulty: 2-3
# Concepts: Element modification by index, list mutability
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
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} updates a team roster.
    # Modify an element by assigning to its index.
    #
    # Step 1: Create roster = ["{{hero}}", "{{friend}}", "trainee"]
    # Step 2: Print f"Before: {roster}"
    # Step 3: Change the third element: roster[2] = "{{heroine}}"
    # Step 4: Print f"After: {roster}"
    #
    # Expected output:
    #   Before: ['{{hero}}', '{{friend}}', 'trainee']
    #   After: ['{{hero}}', '{{friend}}', '{{heroine}}']
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{heroine}} corrects a {{creature}} health record.
    # Use negative indexing to modify the last element.
    #
    # Step 1: Create health = [100, 85, 70, 50]
    # Step 2: Print f"Original: {health}"
    # Step 3: Update the last value: health[-1] = 75
    # Step 4: Print f"Corrected: {health}"
    #
    # Expected output:
    #   Original: [100, 85, 70, 50]
    #   Corrected: [100, 85, 70, 75]
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{mentor}} shows how to swap two elements.
    # Use a temporary variable to hold one value.
    #
    # Step 1: Create order = ["first", "second", "third"]
    # Step 2: Print f"Before swap: {order}"
    # Step 3: Save the first element: temp = order[0]
    # Step 4: Set first to last: order[0] = order[2]
    # Step 5: Set last to saved: order[2] = temp
    # Step 6: Print f"After swap: {order}"
    #
    # Expected output:
    #   Before swap: ['first', 'second', 'third']
    #   After swap: ['third', 'second', 'first']
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} modifies scores based on calculations.
    # Update elements using their current values.
    #
    # Step 1: Create scores = [80, 75, 90, 85]
    # Step 2: Print f"Original: {scores}"
    # Step 3: Add bonus to first score: scores[0] = scores[0] + 10
    # Step 4: Double the last score: scores[-1] = scores[-1] * 2
    # Step 5: Print f"Modified: {scores}"
    # Step 6: Print f"Total: {scores[0] + scores[1] + scores[2] + scores[3]}"
    #
    # Expected output:
    #   Original: [80, 75, 90, 85]
    #   Modified: [90, 75, 90, 170]
    #   Total: 425
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Update multiple elements in sequence.
    #
    # Step 1: Create inventory = ["old sword", "broken shield", "torn cloak"]
    # Step 2: Print f"Old inventory: {inventory}"
    # Step 3: Upgrade first item: inventory[0] = "{{item}}"
    # Step 4: Upgrade second item: inventory[1] = "steel shield"
    # Step 5: Upgrade third item: inventory[2] = "magic cloak"
    # Step 6: Print f"Upgraded: {inventory}"
    #
    # Expected output:
    #   Old inventory: ['old sword', 'broken shield', 'torn cloak']
    #   Upgraded: ['{{item}}', 'steel shield', 'magic cloak']
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
