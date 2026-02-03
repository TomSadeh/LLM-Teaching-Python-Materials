# =============================================================================
# Write Code: List Creation
# =============================================================================
# Difficulty: 1
# Concepts: List literals, creating lists with different element types
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
    # {{hero}} is making a list of supplies for {{school}}.
    # Create a simple list of strings.
    #
    # Step 1: Create a list called supplies with three items:
    #         "{{item}}", "book", "pen"
    # Step 2: Print the list using: print(supplies)
    #
    # Hint: Use square brackets [] to create a list.
    #       Items are separated by commas.
    #
    # Expected output:
    #   ['{{item}}', 'book', 'pen']
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
    # {{heroine}} is tracking {{creature}} stats.
    # Create a list of numbers.
    #
    # Step 1: Create a list called stats with four numbers:
    #         100, 75, 50, 25
    # Step 2: Print the list
    #
    # Hint: Numbers in lists don't need quotes.
    #
    # Expected output:
    #   [100, 75, 50, 25]
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
    # {{mentor}} explains that lists can hold different types.
    # Create a mixed list with strings and numbers.
    #
    # Step 1: Create a list called profile with these items:
    #         "{{hero}}", 100, "{{house}}", 42
    # Step 2: Print f"Profile: {profile}"
    #
    # Hint: A list can contain strings AND numbers together.
    #
    # Expected output:
    #   Profile: ['{{hero}}', 100, '{{house}}', 42]
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
    # {{hero}} starts with an empty inventory and then
    # creates a list using the list() function.
    #
    # Step 1: Create an empty list called inventory using []
    # Step 2: Print f"Empty inventory: {inventory}"
    # Step 3: Create a list called letters using list("abc")
    # Step 4: Print f"Letters: {letters}"
    #
    # Hint: list() can convert strings into lists of characters.
    #
    # Expected output:
    #   Empty inventory: []
    #   Letters: ['a', 'b', 'c']
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
