"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn alternative import syntax that lets
you import specific items directly, avoiding the need for dot notation.

Topic: from module import syntax and aliases
Difficulty: 2
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Import specific functions directly from a module.
    #
    # Step 1: Use this syntax: from math import sqrt, pi
    #         This imports sqrt and pi directly (no dot notation needed)
    #
    # Step 2: Calculate the square root of 225 using sqrt() directly
    #         (not math.sqrt(), just sqrt())
    #
    # Step 3: Print: "Square root of 225 is [result]"
    #
    # Step 4: Print: "Pi is approximately [pi value]"
    #
    # Note: With 'from import', you use the name directly
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use aliases to rename imports for convenience or to avoid conflicts.
    #
    # Step 1: Import with alias: import math as m
    #         Now you use m.sqrt() instead of math.sqrt()
    #
    # Step 2: Calculate: m.pow(2, 10)  (2 to the power of 10)
    #         Store in a variable called `result`
    #
    # Step 3: Print: "2 to the power of 10 is [result]"
    #
    # Step 4: Also try: from math import factorial as fact
    #         Calculate fact(5) and print "5 factorial is [result]"
    #
    # Note: Aliases are useful for long module names or avoiding conflicts
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Practice importing multiple items and using them together.
    # Help {{hero}} calculate some statistics.
    #
    # Step 1: From math, import: sqrt, floor, ceil, pi
    #         Use: from math import sqrt, floor, ceil, pi
    #
    # Step 2: Create a list of values: values = [10, 15, 20, 25, 30]
    #
    # Step 3: Calculate:
    #         - total = sum of all values (use Python's built-in sum())
    #         - average = total / len(values)
    #         - root_of_average = sqrt(average)
    #
    # Step 4: Print:
    #         "Total: [total]"
    #         "Average: [average]"
    #         "Square root of average: [root_of_average]"
    #         "Rounded down: [floor(root_of_average)]"
    #         "Rounded up: [ceil(root_of_average)]"
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
