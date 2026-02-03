# =============================================================================
# Write Code: Turtle Basics
# =============================================================================
# Difficulty: 1
# Concepts: turtle movement, forward(), backward(), right(), left(), penup(), pendown()
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
    # Draw a straight line 100 units long for {{hero}}.
    #
    # Step 1: Create a turtle with t = turtle.Turtle()
    # Step 2: Use t.forward(100) to draw the line
    #
    # Expected: A horizontal line from the center going right.
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Help {{hero}} draw an L-shape on the map of {{school}}.
    #
    # Step 1: Create a turtle
    # Step 2: Move forward 80 units
    # Step 3: Turn left 90 degrees (use t.left(90))
    # Step 4: Move forward 60 units
    #
    # Expected: An L-shape (horizontal line, then vertical line going up).
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a staircase pattern with 3 steps for {{creature}}.
    # Each step is: forward 30, turn right 90, forward 30, turn left 90
    #
    # Step 1: Create a turtle
    # Step 2: For each of the 3 steps:
    #         - forward(30), right(90), forward(30), left(90)
    #
    # Hint: You can write out all 12 commands for now.
    # Later you'll learn to use loops to repeat patterns!
    #
    # Expected: A staircase going right and down.
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use penup() and pendown() to draw two separate lines
    # representing paths in {{location}}.
    #
    # Step 1: Create a turtle
    # Step 2: Draw a line forward 50 units
    # Step 3: Lift the pen with t.penup()
    # Step 4: Move forward 30 units (no line drawn)
    # Step 5: Put the pen down with t.pendown()
    # Step 6: Draw another line forward 50 units
    #
    # Expected: Two horizontal lines with a gap between them.
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
    turtle.done()


main()
