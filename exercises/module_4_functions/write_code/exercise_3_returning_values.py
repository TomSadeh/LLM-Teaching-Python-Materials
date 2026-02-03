# =============================================================================
# Write Code: Returning Values
# =============================================================================
# Difficulty: 2-3
# Concepts: return statement, using returned values, return vs print
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
    # Create a function that returns a value.
    #
    # Step 1: Define a function called get_location that takes no parameters
    # Step 2: Inside, return the string "{{location}}"
    # Step 3: Call the function and store the result in a variable: place
    # Step 4: Print f"Current location: {place}"
    #
    # Hint: Use 'return' to send a value back from the function.
    #
    # Expected output:
    #   Current location: {{location}}
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
    # Create a function that returns a calculated value.
    #
    # Step 1: Define a function called add_numbers that takes two
    #         parameters: a and b
    # Step 2: Inside, return a + b
    # Step 3: Call the function with 10 and 20, store in result
    # Step 4: Print f"10 + 20 = {result}"
    # Step 5: Call the function with 5 and 3, store in result2
    # Step 6: Print f"5 + 3 = {result2}"
    #
    # Expected output:
    #   10 + 20 = 30
    #   5 + 3 = 8
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
    # Create a function that formats a string and returns it.
    #
    # Step 1: Define a function called create_title that takes one
    #         parameter: name
    # Step 2: Inside, return f"The Great {name}"
    # Step 3: Call create_title with "{{hero}}" and store in title1
    # Step 4: Call create_title with "{{heroine}}" and store in title2
    # Step 5: Print title1
    # Step 6: Print title2
    #
    # Expected output:
    #   The Great {{hero}}
    #   The Great {{heroine}}
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
    # Use a returned value in a calculation.
    #
    # Step 1: Define a function called get_base_score that takes no parameters
    #         and returns 100
    # Step 2: Define a function called apply_bonus that takes one parameter:
    #         score and returns score + 50
    # Step 3: Call get_base_score and store in base
    # Step 4: Call apply_bonus with base and store in final
    # Step 5: Print f"Base score: {base}"
    # Step 6: Print f"Final score: {final}"
    #
    # Expected output:
    #   Base score: 100
    #   Final score: 150
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
    # Use a returned value directly in a print statement.
    #
    # Step 1: Define a function called make_announcement that takes one
    #         parameter: message and returns f"[ANNOUNCEMENT] {message}"
    # Step 2: Print make_announcement("{{hero}} has arrived!")
    #         (Call the function inside the print)
    # Step 3: Store make_announcement("Training begins!") in notice
    # Step 4: Print notice
    #
    # Hint: You can use a function call directly inside print().
    #
    # Expected output:
    #   [ANNOUNCEMENT] {{hero}} has arrived!
    #   [ANNOUNCEMENT] Training begins!
    pass


# ============================================================
# {{PHASE_6_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_6}}


def exercise_f():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Chain function calls together.
    #
    # Step 1: Define multiply(a, b) that returns a * b
    # Step 2: Define add_ten(number) that returns number + 10
    # Step 3: Call multiply(5, 4) and store in product
    # Step 4: Call add_ten(product) and store in final
    # Step 5: Print f"5 * 4 = {product}"
    # Step 6: Print f"{product} + 10 = {final}"
    # Step 7: Bonus: Do it in one line: result = add_ten(multiply(3, 3))
    # Step 8: Print f"(3 * 3) + 10 = {result}"
    #
    # Expected output:
    #   5 * 4 = 20
    #   20 + 10 = 30
    #   (3 * 3) + 10 = 19
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

    print("\n=== {{PHASE_6_TITLE}} ===")
    exercise_f()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
