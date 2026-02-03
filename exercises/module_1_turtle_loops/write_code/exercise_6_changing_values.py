# =============================================================================
# Write Code: Changing Values
# =============================================================================
# Difficulty: 4
# Concepts: loop variables in calculations, accumulators, changing patterns
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
    # Calculate and print the sum of 1 + 2 + 3 + 4 + 5 for {{hero}}.
    #
    # Step 1: Create a variable `total` and set it to 0
    # Step 2: Use a for loop with range(1, 6)
    # Step 3: Inside the loop: total = total + i (where i is loop variable)
    # Step 4: After the loop, print "Sum:", total
    #
    # Expected output: Sum: 15
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Print a multiplication table for 3 at {{school}}.
    #
    # Step 1: Use a for loop with range(1, 6)
    # Step 2: Inside the loop:
    #         - result = 3 * i (where i is the loop variable)
    #         - print(f"3 x {i} = {result}")
    #
    # Expected output:
    # 3 x 1 = 3
    # 3 x 2 = 6
    # 3 x 3 = 9
    # 3 x 4 = 12
    # 3 x 5 = 15
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a growing staircase for {{creature}}.
    # Each step is taller than the previous.
    #
    # Step 1: Create a turtle and position at (-200, 100)
    # Step 2: Use a for loop with range(1, 8)
    # Step 3: Inside the loop:
    #         - height = i * 15  (step height grows)
    #         - t.forward(30)    (horizontal part)
    #         - t.right(90)
    #         - t.forward(height)  (vertical part - varies!)
    #         - t.left(90)
    #
    # Expected: A staircase where each step is taller.
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a spiral at {{location}} where line length increases.
    #
    # Step 1: Create a turtle
    # Step 2: Use a for loop with range(1, 25)
    # Step 3: Inside the loop:
    #         - length = i * 5  (length grows each iteration)
    #         - t.forward(length)
    #         - t.right(90)
    #
    # Expected: A square spiral that grows outward.
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Track and print total distance traveled at {{place}}.
    #
    # Step 1: Create a turtle and position at (100, 0)
    # Step 2: Create total_distance = 0
    # Step 3: Use a for loop with range(1, 6)
    # Step 4: Inside the loop:
    #         - distance = i * 20
    #         - t.forward(distance)
    #         - total_distance = total_distance + distance
    #         - t.right(144)  (star pattern)
    #         - print(f"Moved {distance}, total: {total_distance}")
    #
    # Expected: A star shape with increasing line lengths,
    # and a printed report of distances.
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
