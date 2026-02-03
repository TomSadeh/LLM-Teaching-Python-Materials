# =============================================================================
# Hybrid Exercise: The Apprentice - Learning Loops
# =============================================================================
# Difficulty: 3
# Arc: The Apprentice
# Parts: DISCOVERY -> GUIDANCE -> GROWTH
# Concepts: for loops, range(), turtle graphics, loop patterns
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""

import turtle


# ============================================================
# PART 1: DISCOVERY - Study the Master's Work
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Study how {{mentor}} uses loops to draw shapes.
# Predict the output before running the code.


def master_code_1():
    """DO NOT MODIFY - Study and predict"""
    # The master draws a simple shape
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing
    for i in range(3):
        t.forward(80)
        t.left(120)


def master_code_2():
    """DO NOT MODIFY - Study and predict"""
    # The master draws another shape
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(150, 0)  # Move to a new position
    t.pendown()
    for i in range(4):
        t.forward(60)
        t.right(90)


def master_code_3():
    """DO NOT MODIFY - Study and predict"""
    # The master draws a series of marks
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    for count in range(1, 6):
        t.forward(count * 15)
        t.penup()
        t.forward(10)
        t.pendown()


def your_predictions():
    # ✏️ YOUR PREDICTIONS HERE ✏️
    #
    # Describe what each master_code function will draw.
    #
    # master_code_1 draws: _______________ (hint: 3 sides, left turns)
    #     Shape: _______________
    #     Number of sides: ___
    #     Turn angle: ___ degrees
    #
    # master_code_2 draws: _______________ (hint: 4 sides, right turns)
    #     Shape: _______________
    #     Number of sides: ___
    #     Turn angle: ___ degrees
    #
    # master_code_3 draws: _______________ (hint: lines get longer)
    #     How many lines: ___
    #     First line length: ___ units
    #     Last line length: ___ units
    #
    # Hint: The exterior angle of a shape with N sides is 360/N degrees.
    pass


# ============================================================
# PART 2: GUIDANCE - Practice with Support
# ============================================================
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# Now practice with some scaffolding to help you.


def guided_exercise_a():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Complete the loop to draw a pentagon (5 sides).
    # A pentagon needs exterior angles of 72 degrees (360/5 = 72).
    #
    # t = turtle.Turtle()
    # t.speed(0)
    # t.penup()
    # t.goto(-100, 150)
    # t.pendown()
    # for i in range(___):           # How many sides?
    #     t.forward(50)
    #     t.right(___)               # What angle?
    #
    # Hint: A pentagon has 5 sides and turns 72 degrees each time.
    pass


def guided_exercise_b():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Complete the loop to draw a hexagon (6 sides).
    # A hexagon needs exterior angles of 60 degrees (360/6 = 60).
    #
    # t = turtle.Turtle()
    # t.speed(0)
    # t.penup()
    # t.goto(100, 150)
    # t.pendown()
    # ___ i in ___(6):               # Fill in the loop keywords
    #     t.forward(40)
    #     t.___(60)                  # Fill in the turn method
    #
    # Hint: Use "for" and "range" to create the loop.
    pass


# ============================================================
# PART 3: GROWTH - Create Your Own
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now create your own shapes using what you've learned!


def your_creation_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw an octagon (8 sides) for {{hero}}.
    #
    # Step 1: Create a turtle
    # Step 2: Position it at (-200, -100) using penup/goto/pendown
    # Step 3: Use a for loop to repeat 8 times
    # Step 4: Each iteration: forward 35 units, left 45 degrees
    #
    # Hint: 360/8 = 45 degrees per turn
    #
    # Expected: An octagon (8-sided shape).
    pass


def your_creation_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Draw a spiral staircase pattern for {{creature}}.
    # Each step is slightly longer than the previous.
    #
    # Step 1: Create a turtle
    # Step 2: Position it at (0, -150)
    # Step 3: Use a for loop with range(1, 13) to draw 12 lines
    # Step 4: Each iteration:
    #         - forward(step * 8) where step is the loop variable
    #         - right(30)
    #
    # Expected: A spiral pattern where each line is longer than the last.
    pass


def your_creation_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create your own shape at {{school}}!
    # Try a different number of sides, or a star pattern.
    #
    # Ideas:
    # - Draw a 10-sided shape (decagon) with 36-degree turns
    # - Draw a 5-pointed star with 144-degree turns
    # - Draw a 7-pointed star with 154-degree turns (approximately)
    #
    # Be creative!
    pass


def main():
    print("=" * 50)
    print("PART 1: DISCOVERY - Study the Master's Work")
    print("=" * 50)

    print("\n--- master_code_1 ---")
    master_code_1()

    print("\n--- master_code_2 ---")
    master_code_2()

    print("\n--- master_code_3 ---")
    master_code_3()

    print("\n--- Your Predictions ---")
    your_predictions()

    print("\n" + "=" * 50)
    print("PART 2: GUIDANCE - Practice with Support")
    print("=" * 50)

    print("\n--- guided_exercise_a ---")
    # guided_exercise_a()  # Uncomment when blanks are filled

    print("\n--- guided_exercise_b ---")
    # guided_exercise_b()

    print("\n" + "=" * 50)
    print("PART 3: GROWTH - Create Your Own")
    print("=" * 50)

    print("\n--- your_creation_a ---")
    your_creation_a()

    print("\n--- your_creation_b ---")
    your_creation_b()

    print("\n--- your_creation_c ---")
    your_creation_c()

    print("\n" + "=" * 50)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    turtle.done()


main()
