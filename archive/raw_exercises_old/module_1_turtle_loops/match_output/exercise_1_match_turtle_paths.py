# Exercise 1: Match the Output - Turtle Paths
#
# Match each code snippet to the shape it draws.
# Don't run the code - visualize the turtle's movement!
#
# Theme: {{hero}} learns magical drawing


# ============================================================
# CODE SNIPPETS - Study these carefully
# ============================================================

# Note: Assume turtle starts at center, facing right (East)

def snippet_1():
    """What shape does this draw?"""
    import turtle
    t = turtle.Turtle()
    for i in range(4):
        t.forward(100)
        t.right(90)


def snippet_2():
    """What shape does this draw?"""
    import turtle
    t = turtle.Turtle()
    for i in range(3):
        t.forward(100)
        t.right(120)


def snippet_3():
    """What shape does this draw?"""
    import turtle
    t = turtle.Turtle()
    t.forward(100)
    t.right(90)
    t.forward(100)


def snippet_4():
    """What shape does this draw?"""
    import turtle
    t = turtle.Turtle()
    for i in range(6):
        t.forward(50)
        t.right(60)


# ============================================================
# POSSIBLE OUTPUTS - Which goes with which snippet?
# ============================================================

"""
SHAPE A: Triangle
---------
A closed three-sided shape.
Turtle turns 120° at each corner.

SHAPE B: Square
---------
A closed four-sided shape.
All sides equal length.

SHAPE C: L-Shape (two lines meeting at right angle)
---------
Two lines connected at a 90° angle.
Not a closed shape.

SHAPE D: Hexagon
---------
A closed six-sided shape.
Turtle turns 60° at each corner.
"""


# ============================================================
# YOUR ANSWERS
# ============================================================

def your_matches():
    # ✏️ MATCH SNIPPETS TO SHAPES ✏️
    #
    # Write the letter (A, B, C, or D) that matches each snippet.
    # Think about:
    # - How many times does the loop run?
    # - What angle does the turtle turn?
    # - Does the shape close (connect back to start)?

    matches = {
        "snippet_1": "?",  # Hint: 4 sides, 90° turns
        "snippet_2": "?",  # Hint: 3 sides, 120° turns
        "snippet_3": "?",  # Hint: Only 2 lines, no loop
        "snippet_4": "?",  # Hint: 6 sides, 60° turns
    }

    return matches


def shape_reasoning():
    # ✏️ OPTIONAL: EXPLAIN YOUR REASONING ✏️
    #
    # For each snippet, explain:
    # 1. How many lines are drawn?
    # 2. What angle is turned?
    # 3. Does it make a complete shape?

    explanations = {
        "snippet_1": "Because...",
        "snippet_2": "Because...",
        "snippet_3": "Because...",
        "snippet_4": "Because...",
    }

    return explanations


def main():
    print("=== Match the Output: Turtle Paths ===")
    print()
    print("Match each snippet to the shape it draws (A, B, C, or D)")
    print("Think about loops, angles, and number of sides!")
    print()
    print("Fill in your answers in your_matches()")
    print()
    print("="*50)
    print()
    print("HINT: For a closed shape with N sides:")
    print("  - The loop runs N times")
    print("  - Total turning = 360°")
    print("  - Each turn = 360° ÷ N")
    print()
    print("="*50)
    print("\nYour matches:", your_matches())

    # Uncomment below to see shapes (requires turtle graphics)
    # print("\nRunning snippet_1...")
    # snippet_1()


main()
