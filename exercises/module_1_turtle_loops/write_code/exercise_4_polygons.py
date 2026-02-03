# =============================================================================
# Write Code: Polygons
# =============================================================================
# Difficulty: 3-4
# Concepts: regular polygons, exterior angles, loop patterns for shapes
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
    # Draw a regular pentagon (5 sides) for {{hero}}.
    #
    # Step 1: Create a turtle
    # Step 2: Use a for loop with range(5)
    # Step 3: Inside the loop:
    #         - t.forward(70)
    #         - t.right(72)  # 360/5 = 72 degrees
    #
    # Key formula: exterior angle = 360 / number_of_sides
    # Pentagon: 360 / 5 = 72 degrees
    #
    # Expected: A regular 5-sided shape.
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a regular hexagon (6 sides) at {{school}}.
    #
    # Step 1: Create a turtle
    # Step 2: Position it at (100, 0) using penup/goto/pendown
    # Step 3: Use a for loop with range(6)
    # Step 4: Inside the loop:
    #         - forward(60)
    #         - right(60)  # 360/6 = 60 degrees
    #
    # Expected: A regular 6-sided shape.
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a regular octagon (8 sides) for {{creature}}.
    #
    # Step 1: Create a turtle
    # Step 2: Position it at (-100, 0)
    # Step 3: Use a for loop with range(8)
    # Step 4: Inside the loop:
    #         - forward(50)
    #         - right(45)  # 360/8 = 45 degrees
    #
    # Expected: A regular 8-sided shape.
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a regular decagon (10 sides) at {{location}}.
    #
    # Step 1: Create a turtle
    # Step 2: Position it at (0, -150)
    # Step 3: Use a for loop with range(10)
    # Step 4: Inside the loop:
    #         - forward(40)
    #         - right(36)  # 360/10 = 36 degrees
    #
    # Expected: A regular 10-sided shape (almost a circle!).
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw multiple polygons in a row at {{place}}.
    # Draw: triangle, square, pentagon, hexagon from left to right.
    #
    # Step 1: Create a turtle and set t.speed(0)
    # Step 2: Start at position (-250, 100)
    # Step 3: For each shape:
    #         - Draw the polygon using a loop
    #         - Move right to the next position (penup, forward 150, pendown)
    #
    # Shapes to draw:
    #   Triangle: 3 sides, 120 degree turns, 50 forward
    #   Square: 4 sides, 90 degree turns, 40 forward
    #   Pentagon: 5 sides, 72 degree turns, 35 forward
    #   Hexagon: 6 sides, 60 degree turns, 30 forward
    #
    # Hint: After drawing each shape, move right before starting the next.
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
