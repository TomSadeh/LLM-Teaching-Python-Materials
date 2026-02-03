# =============================================================================
# Write Code: Indexing Access
# =============================================================================
# Difficulty: 2
# Concepts: Positive indexing, accessing elements, using indexed values
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
    # {{hero}} has a list of items to study.
    # Access specific elements by their index.
    #
    # Step 1: Create a list called items with:
    #         "{{item}}", "{{spell1}}", "{{spell2}}"
    # Step 2: Print the first item using index 0
    # Step 3: Print the third item using index 2
    #
    # Hint: Index 0 is the first element, index 2 is the third.
    #
    # Expected output:
    #   {{item}}
    #   {{spell2}}
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
    # {{heroine}} is tracking scores for {{house}} members.
    # Use indexed values in calculations.
    #
    # Step 1: Create a list called scores: [85, 92, 78, 95]
    # Step 2: Print f"First score: {scores[0]}"
    # Step 3: Print f"Last score: {scores[3]}"
    # Step 4: Calculate and print the average of first and last:
    #         average = (scores[0] + scores[3]) / 2
    #         Print f"Average: {average}"
    #
    # Expected output:
    #   First score: 85
    #   Last score: 95
    #   Average: 90.0
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
    # {{mentor}} shows how to use len() with indexing.
    # The last valid index is always len(list) - 1.
    #
    # Step 1: Create a list called team:
    #         ["{{hero}}", "{{heroine}}", "{{friend}}"]
    # Step 2: Get the length: team_size = len(team)
    # Step 3: Print f"Team has {team_size} members"
    # Step 4: Calculate last_index = team_size - 1
    # Step 5: Print f"Last member: {team[last_index]}"
    #
    # Expected output:
    #   Team has 3 members
    #   Last member: {{friend}}
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
    # {{hero}} builds a greeting using indexed elements.
    # Combine multiple list accesses in one statement.
    #
    # Step 1: Create a list called parts:
    #         ["Hello", "{{hero}}", "welcome to", "{{school}}"]
    # Step 2: Build a message using f-string and indices:
    #         message = f"{parts[0]} {parts[1]}, {parts[2]} {parts[3]}!"
    # Step 3: Print the message
    #
    # Expected output:
    #   Hello {{hero}}, welcome to {{school}}!
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

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
