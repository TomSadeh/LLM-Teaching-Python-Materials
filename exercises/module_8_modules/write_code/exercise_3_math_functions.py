"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll explore the math module's most useful functions.
These are essential for calculations in games, science, and data analysis.

Topic: Math module functions (sqrt, floor, ceil, pow, fabs)
Difficulty: 2
"""

import math


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Practice with basic math functions.
    #
    # Step 1: Calculate these values using math functions:
    #         - square_root = math.sqrt(256)
    #         - power_result = math.pow(3, 4)  # 3 to the power of 4
    #         - absolute = math.fabs(-42.5)    # absolute value
    #
    # Step 2: Print each result with a description:
    #         "Square root of 256: [value]"
    #         "3 to the power of 4: [value]"
    #         "Absolute value of -42.5: [value]"
    #
    # Note: math.fabs() returns a float, abs() is built-in for integers
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn rounding functions for {{school}} calculations.
    #
    # Step 1: Create a variable: value = 7.6
    #
    # Step 2: Calculate:
    #         - floor_result = math.floor(value)   # rounds DOWN
    #         - ceil_result = math.ceil(value)     # rounds UP
    #         - trunc_result = math.trunc(-7.6)    # removes decimal part
    #
    # Step 3: Print each result:
    #         "Floor of 7.6: [value]"     (should be 7)
    #         "Ceiling of 7.6: [value]"   (should be 8)
    #         "Truncate -7.6: [value]"    (should be -7)
    #
    # Step 4: Try with negative number -7.6:
    #         Print floor and ceil of -7.6 to see the difference
    #
    # Note: floor(-7.6) = -8, ceil(-7.6) = -7 (toward/away from zero)
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Build a distance calculator using the Pythagorean theorem.
    # Calculate the distance {{hero}} must travel.
    #
    # Step 1: Create starting coordinates:
    #         start_x = 0
    #         start_y = 0
    #
    # Step 2: Create ending coordinates:
    #         end_x = 3
    #         end_y = 4
    #
    # Step 3: Calculate distance using Pythagorean theorem:
    #         distance = sqrt((end_x - start_x)^2 + (end_y - start_y)^2)
    #
    #         In Python:
    #         dx = end_x - start_x
    #         dy = end_y - start_y
    #         distance = math.sqrt(dx**2 + dy**2)
    #         # Or: distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
    #
    # Step 4: Print: "Distance from (0,0) to (3,4): [distance]"
    #         The answer should be 5.0
    #
    # Step 5: Try with coordinates (0,0) to (5,12) - answer should be 13.0
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
