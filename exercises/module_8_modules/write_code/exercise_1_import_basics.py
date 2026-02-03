"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn how to import modules and access
their contents using dot notation. This is the foundation of
using Python's powerful standard library.

Topic: Basic import syntax and dot notation
Difficulty: 1
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn to import a module and use its functions.
    #
    # Step 1: Import the math module using: import math
    #
    # Step 2: Use math.sqrt() to calculate the square root of 144
    #         Store the result in a variable called `root`
    #
    # Step 3: Print: "The square root of 144 is [result]"
    #
    # Hint: After importing, access functions with module_name.function_name
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use module constants (special values stored in modules).
    #
    # Step 1: Import the math module (if not already imported above)
    #
    # Step 2: Access math.pi and store it in a variable called `pi_value`
    #
    # Step 3: Calculate the area of a circle with radius 5
    #         Formula: area = pi * radius * radius
    #
    # Step 4: Print: "A circle with radius 5 has area [result]"
    #
    # Hint: math.pi gives you the value of pi (3.14159...)
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Combine multiple functions from the same module.
    # Calculate {{hero}}'s power level using math operations.
    #
    # Step 1: Import the math module
    #
    # Step 2: Create these variables:
    #         - base_power = 64
    #         - multiplier = 2.7
    #
    # Step 3: Calculate:
    #         - root_power = math.sqrt(base_power)
    #         - floor_multiplier = math.floor(multiplier)
    #         - ceiling_multiplier = math.ceil(multiplier)
    #
    # Step 4: Print each calculated value with a description
    #         Example: "Square root of 64: [value]"
    #                  "Floor of 2.7: [value]"
    #                  "Ceiling of 2.7: [value]"
    #
    # Hint: floor() rounds down, ceil() rounds up
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
