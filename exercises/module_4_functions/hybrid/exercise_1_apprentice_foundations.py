# =============================================================================
# Hybrid Exercise: The Apprentice - Function Foundations
# =============================================================================
# Difficulty: 1-2
# Arc: Apprentice (GUIDANCE -> GUIDANCE -> GROWTH)
# Concepts: Function definition, calling functions, basic structure
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: GUIDANCE - Study Function Syntax
# ============================================================
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# {{mentor}} demonstrates how functions work. Study these examples
# and fill in the blanks.


def study_example_1():
    """Study this function - notice the structure."""
    print("Welcome to {{school}}!")
    print("Let's learn about functions.")


def study_example_2():
    """Another function example."""
    message = "{{hero}} is practicing"
    print(message)
    print("Functions group code together!")


def part_1_fill_blanks():
    # FILL IN THE BLANKS
    #
    # Complete the function definition below.
    # Look at the examples above for the pattern.

    # ___ display_greeting():        # Hint: What keyword defines a function?
    #     print("{{exclamation}}")
    #     print("{{hero}} says hello!")

    # Call the function:
    # ___()                          # Hint: Use the function name with ()

    pass


# ============================================================
# PART 2: GUIDANCE - Practice with Scaffolding
# ============================================================
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# Complete the function following the provided structure.


def show_character_info():
    """
    Display information about a character.

    This function should print:
    - The character's name
    - Their location
    - A status message
    """
    # Started for you:
    print("Character Profile:")
    print("-" * 20)

    # COMPLETE THIS FUNCTION
    #
    # Add three more print statements:
    # 1. Print f"Name: {{hero}}"
    # 2. Print f"Location: {{location}}"
    # 3. Print "Status: Ready"
    #
    # Hint: Just add three print statements below.

    pass  # Replace with implementation


# ============================================================
# PART 3: GROWTH - Create Your Own
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now create functions on your own.


def exercise_create_greeting():
    # YOUR CODE HERE
    #
    # Create and call a function that prints a greeting.
    #
    # Step 1: Define a function called custom_greeting
    # Step 2: Inside, print f"Greetings from {{school}}!"
    # Step 3: Inside, print f"{{hero}} welcomes you."
    # Step 4: Call the function
    #
    # Expected output:
    #   Greetings from {{school}}!
    #   {{hero}} welcomes you.
    pass


def exercise_create_report():
    # YOUR CODE HERE
    #
    # Create a function that displays a formatted report.
    #
    # Step 1: Define a function called show_report
    # Step 2: Inside, print "=" * 30
    # Step 3: Inside, print "Daily Report"
    # Step 4: Inside, print "=" * 30
    # Step 5: Inside, print f"Location: {{location}}"
    # Step 6: Inside, print f"Leader: {{mentor}}"
    # Step 7: Call show_report
    #
    # Expected output:
    #   ==============================
    #   Daily Report
    #   ==============================
    #   Location: {{location}}
    #   Leader: {{mentor}}
    pass


def exercise_multiple_functions():
    # YOUR CODE HERE
    #
    # Create two functions and use them together.
    #
    # Step 1: Define a function called start_sequence that prints:
    #         ">>> Starting {{spell1}} sequence..."
    # Step 2: Define a function called end_sequence that prints:
    #         ">>> {{spell1}} sequence complete!"
    # Step 3: Call start_sequence
    # Step 4: Print "Processing..."
    # Step 5: Call end_sequence
    #
    # Expected output:
    #   >>> Starting {{spell1}} sequence...
    #   Processing...
    #   >>> {{spell1}} sequence complete!
    pass


def main():
    print("=" * 60)
    print("THE APPRENTICE: Function Foundations")
    print("=" * 60)

    print("\n--- PART 1: GUIDANCE - Study Syntax ---")
    print("{{CONTEXT_GUIDANCE_INTRO}}")
    print("\nStudy Example 1:")
    study_example_1()
    print("\nStudy Example 2:")
    study_example_2()
    print("\nNow fill in the blanks:")
    part_1_fill_blanks()

    print("\n--- PART 2: GUIDANCE - Practice ---")
    print("{{CONTEXT_GUIDANCE_INTRO}}")
    print("\nTesting show_character_info:")
    show_character_info()

    print("\n--- PART 3: GROWTH - Your Turn ---")
    print("{{CONTEXT_GROWTH_INTRO}}")
    print("\nCustom greeting:")
    exercise_create_greeting()
    print("\nShow report:")
    exercise_create_report()
    print("\nMultiple functions:")
    exercise_multiple_functions()

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
