# =============================================================================
# Write Code: Basic Functions
# =============================================================================
# Difficulty: 1
# Concepts: def keyword, function definition, function calls, simple print output
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
    # Create a function that prints a greeting.
    #
    # Step 1: Define a function called say_hello that takes no parameters
    # Step 2: Inside the function, print "Hello, {{school}}!"
    # Step 3: Call the function
    #
    # Hint: Functions start with 'def', have a name, parentheses, and colon.
    #       The body is indented.
    #
    # Expected output:
    #   Hello, {{school}}!
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
    # Create a function that prints multiple lines.
    #
    # Step 1: Define a function called introduce_hero
    # Step 2: Inside the function:
    #         - Print "Meet {{hero}}!"
    #         - Print "From {{house}}"
    #         - Print "Ready for adventure!"
    # Step 3: Call the function
    #
    # Expected output:
    #   Meet {{hero}}!
    #   From {{house}}
    #   Ready for adventure!
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
    # Create two functions and call them in sequence.
    #
    # Step 1: Define a function called show_header that prints:
    #         "===== {{school}} Report ====="
    # Step 2: Define a function called show_footer that prints:
    #         "===== End of Report ====="
    # Step 3: Call show_header
    # Step 4: Print "Status: Active"
    # Step 5: Call show_footer
    #
    # Expected output:
    #   ===== {{school}} Report =====
    #   Status: Active
    #   ===== End of Report =====
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
    # Create a function that uses variables defined inside it.
    #
    # Step 1: Define a function called display_stats
    # Step 2: Inside the function:
    #         - Create a variable: name = "{{hero}}"
    #         - Create a variable: level = 1
    #         - Print f"{name} is at level {level}"
    # Step 3: Call display_stats
    #
    # Hint: Variables inside a function are local to that function.
    #
    # Expected output:
    #   {{hero}} is at level 1
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
