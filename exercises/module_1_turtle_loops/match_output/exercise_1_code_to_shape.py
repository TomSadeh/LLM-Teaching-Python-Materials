# =============================================================================
# Match the Output: Code to Shape
# =============================================================================
# Difficulty: 3-4
# Concepts: loop count to sides, turn angles to shape type
# =============================================================================

"""
{{CONTEXT_MATCH_OUTPUT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

import turtle


# ============================================================
# {{MATCH_SET_1_TITLE}}
# ============================================================
# {{CONTEXT_MATCH_SET_1_NARRATIVE}}
#
# Match each code snippet to the shape it draws.

# --- CODE SNIPPETS ---


def snippet_1():
    """What shape does this draw?"""
    t = turtle.Turtle()
    t.speed(0)
    for i in range(3):
        t.forward(80)
        t.right(120)


def snippet_2():
    """What shape does this draw?"""
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(150, 0)
    t.pendown()
    for i in range(4):
        t.forward(60)
        t.right(90)


def snippet_3():
    """What shape does this draw?"""
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    for i in range(6):
        t.forward(40)
        t.right(60)


# --- POSSIBLE OUTPUTS ---
"""
OUTPUT A: Triangle
---------
A 3-sided closed shape with equal sides.
The turtle turns 120 degrees at each corner.

OUTPUT B: Square
---------
A 4-sided closed shape with equal sides.
The turtle turns 90 degrees at each corner.

OUTPUT C: Hexagon
---------
A 6-sided closed shape with equal sides.
The turtle turns 60 degrees at each corner.
"""


# --- YOUR ANSWERS ---


def your_matches_set1():
    # ✏️ MATCH SNIPPETS TO OUTPUTS ✏️
    #
    # Write the letter (A, B, or C) that matches each snippet.
    #
    # Hint: Look at range(N) to find the number of sides.
    # The turn angle determines what shape it is:
    # - Triangle: 120 degrees (360 / 3)
    # - Square: 90 degrees (360 / 4)
    # - Hexagon: 60 degrees (360 / 6)

    matches = {
        "snippet_1": "?",
        "snippet_2": "?",
        "snippet_3": "?",
    }

    return matches


# ============================================================
# {{MATCH_SET_2_TITLE}}
# ============================================================
# {{CONTEXT_MATCH_SET_2_NARRATIVE}}
#
# These snippets look similar but produce different results!
# {{hero}} must identify each pattern.

# --- CODE SNIPPETS ---


def snippet_4():
    """What does this code draw?"""
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, -100)
    t.pendown()
    for i in range(5):
        t.forward(80)
        t.right(72)


def snippet_5():
    """What does this code draw?"""
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    for i in range(5):
        t.forward(80)
        t.right(144)


def snippet_6():
    """What does this code draw?"""
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(200, -100)
    t.pendown()
    for i in range(5):
        t.forward(80)
        t.left(72)


# --- POSSIBLE OUTPUTS ---
"""
OUTPUT D: Pentagon (5-sided polygon)
---------
A regular 5-sided closed shape.
Turn angle: 72 degrees (360/5).
Turns RIGHT at each corner.

OUTPUT E: 5-Pointed Star
---------
A star shape with 5 points.
Turn angle: 144 degrees (larger than polygon).
Lines cross through the center.

OUTPUT F: Pentagon (counterclockwise)
---------
A regular 5-sided closed shape.
Turn angle: 72 degrees.
Turns LEFT at each corner (draws in opposite direction).
"""


# --- YOUR ANSWERS ---


def your_matches_set2():
    # ✏️ MATCH SNIPPETS TO OUTPUTS ✏️
    #
    # Hint: Compare the turn angles and directions!
    # - 72 degrees = 360/5, creates a regular pentagon
    # - 144 degrees = 2 * 72, creates a star pattern
    # - left vs right affects which way the shape is drawn

    matches = {
        "snippet_4": "?",
        "snippet_5": "?",
        "snippet_6": "?",
    }

    return matches


def main():
    print("{{CONTEXT_MATCH_OUTPUT_INTRO}}")
    print("=" * 50)

    print("\n=== {{MATCH_SET_1_TITLE}} ===")
    print("\nRunning all snippets...")
    snippet_1()
    snippet_2()
    snippet_3()
    print("\nYour matches:", your_matches_set1())

    print("\n=== {{MATCH_SET_2_TITLE}} ===")
    snippet_4()
    snippet_5()
    snippet_6()
    print("\nYour matches:", your_matches_set2())

    print("\n" + "=" * 50)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")
    turtle.done()


main()
