# =============================================================================
# Write Code: Pattern Angles
# =============================================================================
# Difficulty: 4
# Concepts: calculated angles, star patterns, geometric patterns
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
    # Draw a 5-pointed star for {{hero}}.
    #
    # Step 1: Create a turtle
    # Step 2: Use a for loop with range(5)
    # Step 3: Inside the loop:
    #         - t.forward(100)
    #         - t.right(144)  # Star angle: 144 degrees
    #
    # Why 144? A 5-pointed star skips vertices, creating a 144-degree turn.
    # Formula: 180 - (180 / 5) = 180 - 36 = 144
    # Or think of it as: 2 * (360/5) = 2 * 72 = 144
    #
    # Expected: A classic 5-pointed star shape.
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a 6-pointed star (Star of David pattern) at {{school}}.
    # This is made of two overlapping triangles!
    #
    # Step 1: Create a turtle and position at (150, 0)
    # Step 2: Draw first triangle (3 sides, 120 degree right turns)
    # Step 3: Turn right 60 degrees to prepare for second triangle
    # Step 4: Draw second triangle (3 sides, 120 degree right turns)
    #
    # Hint: Each triangle is a regular triangle.
    # The second triangle is rotated 60 degrees from the first.
    #
    # Expected: Two overlapping triangles forming a 6-pointed star.
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a spiral square pattern for {{creature}}.
    # Each side gets longer as you go around!
    #
    # Step 1: Create a turtle and position at (-100, 100)
    # Step 2: Use a for loop with range(1, 21) for 20 lines
    # Step 3: Inside the loop:
    #         - t.forward(i * 5)  where i is the loop variable
    #         - t.right(90)
    #
    # Expected: A spiral that grows outward in a square pattern.
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a circular pattern of triangles at {{location}}.
    # Draw 12 small triangles arranged in a circle.
    #
    # Step 1: Create a turtle and position at (0, -100)
    # Step 2: Use an outer loop with range(12) for 12 triangles
    # Step 3: Inside the outer loop:
    #         a) Use an inner... wait, NO NESTED LOOPS YET!
    #         b) Instead: draw 3 forward/right(120) commands for triangle
    #         c) Then turn right 30 degrees to position for next triangle
    #
    # Actually, let's simplify - draw 12 lines radiating from center:
    # Step 3: Inside the loop:
    #         - t.forward(60)
    #         - t.backward(60)
    #         - t.right(30)  # 360/12 = 30 degrees
    #
    # Expected: 12 lines radiating outward like spokes of a wheel.
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a "flower" pattern at {{place}} for {{hero}}.
    # Draw 36 small lines in a circular pattern, each rotated 10 degrees.
    #
    # Step 1: Create a turtle
    # Step 2: Use a for loop with range(36)
    # Step 3: Inside the loop:
    #         - t.forward(80)
    #         - t.backward(80)
    #         - t.right(10)  # 360/36 = 10 degrees
    #
    # Optional challenge: Make every other line a different length!
    # (Check if i is even or odd... but we can't use if yet!)
    #
    # Expected: A circular sunburst pattern with 36 rays.
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
