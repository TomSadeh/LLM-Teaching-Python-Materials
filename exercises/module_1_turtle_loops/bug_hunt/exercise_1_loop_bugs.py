# =============================================================================
# Bug Hunt: Loop Bugs
# =============================================================================
# Difficulty: 5
# Concepts: loop errors, off-by-one, wrong angles, incorrect range
# =============================================================================

"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}
"""

import turtle


# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Draw a square (4 sides, each 90-degree turn).
# The shape should close completely.
#
# ACTUAL BEHAVIOR:
# The turtle only draws 3 sides and doesn't close the square!
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}


def buggy_a():
    """This code has exactly ONE bug. Find it!"""
    # {{hero}} wanted to draw a square at {{school}}
    t = turtle.Turtle()
    t.speed(0)
    for i in range(3):  # Bug is here!
        t.forward(80)
        t.right(90)


def fix_a():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: How many sides does a square have?
    #
    # The fix:

    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Draw an equilateral triangle (3 equal sides).
# The shape should close completely.
#
# ACTUAL BEHAVIOR:
# The turtle draws a shape but it doesn't close properly!
# It looks more like a bent line than a triangle.
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}


def buggy_b():
    """This code has exactly ONE bug. Find it!"""
    # {{creature}} tried to draw a triangle
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(150, 0)
    t.pendown()
    for i in range(3):
        t.forward(70)
        t.right(60)  # Bug is here!


def fix_b():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: The exterior angle of a triangle is 120 degrees, not 60.
    # Think: 360 / 3 = ?
    #
    # The fix:

    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Print numbers 1, 2, 3, 4, 5 (one per line).
#
# ACTUAL BEHAVIOR:
# Prints 0, 1, 2, 3, 4 instead!
# The starting number is wrong.
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}


def buggy_c():
    """This code has exactly ONE bug. Find it!"""
    # Counting {{item}} items for {{hero}}
    for i in range(5):  # Bug is here!
        print(i)


def fix_c():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: range(5) starts at 0, not 1.
    # To get 1-5, use range(start, stop).
    #
    # The fix:

    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Draw a hexagon (6 sides) at {{location}}.
#
# ACTUAL BEHAVIOR:
# The shape closes too early! It looks like a pentagon!
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}


def buggy_d():
    """This code has exactly ONE bug. Find it!"""
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    for i in range(6):
        t.forward(50)
        t.left(72)  # Bug is here!


def fix_d():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: A hexagon has 6 sides, so the angle should be 360/6 = 60.
    # The code uses 72, which is the angle for a pentagon (360/5).
    #
    # The fix:

    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Buggy version:")
    buggy_a()
    print("\nFixed version:")
    # fix_a()  # Uncomment when fixed

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Buggy version:")
    buggy_b()
    print("\nFixed version:")
    # fix_b()

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Buggy version:")
    buggy_c()
    print("\nFixed version:")
    # fix_c()

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Buggy version:")
    buggy_d()
    print("\nFixed version:")
    # fix_d()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
    turtle.done()


main()
