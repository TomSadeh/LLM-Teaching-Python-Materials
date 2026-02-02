# =============================================================================
# Write Code: Hello World
# =============================================================================
# Difficulty: 1
# Concepts: print() function, string literals, printing multiple values
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
    # Print the message: Hello, world!
    #
    # Step 1: Use the print() function
    # Step 2: Put your message inside quotes within the parentheses
    #
    # Example output: Hello, world!
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Print a greeting for {{hero}}.
    #
    # Step 1: Print "Welcome, {{hero}}!"
    # Step 2: Print "You are now at {{school}}."
    #
    # Expected output (2 lines):
    # Welcome, {{hero}}!
    # You are now at {{school}}.
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use print() with multiple items separated by commas.
    #
    # Step 1: Print three items in one print statement: "{{hero}}", "has a", "{{item}}"
    #
    # Hint: When you use commas in print(), Python adds spaces between items.
    # Example: print("Hello", "World") outputs: Hello World
    #
    # Expected output: {{hero}} has a {{item}}
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

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
