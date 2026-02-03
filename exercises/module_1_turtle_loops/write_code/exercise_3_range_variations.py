# =============================================================================
# Write Code: Range Variations
# =============================================================================
# Difficulty: 3
# Concepts: range(start, stop), range(start, stop, step), counting patterns
# =============================================================================

"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

import turtle

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Print numbers 5 through 9 for {{hero}}'s countdown.
    #
    # Step 1: Use a for loop with range(5, 10)
    # Step 2: Print each number inside the loop
    #
    # Expected output:
    # 5
    # 6
    # 7
    # 8
    # 9
    #
    # Hint: range(5, 10) gives 5, 6, 7, 8, 9 - it stops BEFORE 10.
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Print even numbers from 2 to 10 for {{creature}}'s training.
    #
    # Step 1: Use a for loop with range(2, 11, 2)
    # Step 2: Print each number
    #
    # Expected output:
    # 2
    # 4
    # 6
    # 8
    # 10
    #
    # Hint: The step of 2 skips every other number.
    # We use 11 as stop because we WANT to include 10.
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a countdown from 10 to 1 for {{hero}}'s challenge.
    #
    # Step 1: Use a for loop with range(10, 0, -1)
    # Step 2: Print each number
    #
    # Expected output:
    # 10
    # 9
    # 8
    # 7
    # 6
    # 5
    # 4
    # 3
    # 2
    # 1
    #
    # Hint: A negative step (-1) counts backwards.
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a series of lines with increasing lengths at {{location}}.
    # Each line should be 20, 40, 60, 80, and 100 units long.
    #
    # Step 1: Create a turtle
    # Step 2: Use a for loop with range(20, 101, 20)
    # Step 3: Inside the loop:
    #         - t.forward(length) where length is the loop variable
    #         - t.penup()
    #         - t.backward(length)  # Return to start
    #         - t.right(90)
    #         - t.forward(15)       # Move down
    #         - t.left(90)
    #         - t.pendown()
    #
    # Expected: 5 horizontal lines of increasing length, stacked vertically.
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a star pattern at {{school}} by drawing lines at every 144 degrees.
    # A 5-pointed star requires turning 144 degrees after each line.
    #
    # Step 1: Create a turtle
    # Step 2: Use a for loop with range(5) to draw 5 lines
    # Step 3: Inside the loop:
    #         - t.forward(100)
    #         - t.right(144)
    #
    # Expected: A 5-pointed star shape.
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
    turtle.done()


main()
