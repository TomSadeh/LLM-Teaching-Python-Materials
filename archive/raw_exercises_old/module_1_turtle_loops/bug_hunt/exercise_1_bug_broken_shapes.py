# Exercise 1: Bug Hunt - Broken Shapes
#
# {{villain}} has cursed these drawing spells with bugs!
# Each function has exactly ONE bug hiding in it.
# Read the story, find the bug, and fix it.
#
# DO NOT run the code first - use your detective skills!


# ============================================================
# BUG HUNT A: The Incomplete Square
# ============================================================
"""
STORY:
{{hero}} tried to draw a protective square around {{school}},
but the spell leaves a gap! The square should be completely closed.

EXPECTED BEHAVIOR:
A perfect square with 4 equal sides, all connected.

ACTUAL BEHAVIOR:
The turtle draws only 3 sides, leaving one side open.
"""

def buggy_square():
    import turtle
    t = turtle.Turtle()

    for i in range(3):  # BUG IS HERE
        t.forward(100)
        t.right(90)


def fix_square():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    import turtle
    t = turtle.Turtle()

    pass  # Write the corrected code here


# ============================================================
# BUG HUNT B: The Wrong-Way Triangle
# ============================================================
"""
STORY:
{{friend}} is learning to draw triangles, but the triangle
spirals outward instead of closing!

EXPECTED BEHAVIOR:
A closed equilateral triangle (3 equal sides).

ACTUAL BEHAVIOR:
The turtle draws lines that don't connect back to the start.
"""

def buggy_triangle():
    import turtle
    t = turtle.Turtle()

    for i in range(3):
        t.forward(100)
        t.right(60)  # BUG IS HERE - wrong angle!


def fix_triangle():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: For a closed shape, total turn = 360°
    #       Each turn = 360° ÷ number_of_sides
    #
    # The fix:
    import turtle
    t = turtle.Turtle()

    pass  # Write the corrected code here


# ============================================================
# BUG HUNT C: The Stuck Turtle
# ============================================================
"""
STORY:
{{mentor}} wrote a spell to draw a hexagon, but the turtle
doesn't move at all! It just spins in place.

EXPECTED BEHAVIOR:
A hexagon (6-sided shape) drawn on the screen.

ACTUAL BEHAVIOR:
The turtle turns but never moves forward.
"""

def buggy_hexagon():
    import turtle
    t = turtle.Turtle()

    for i in range(6):
        t.right(60)
        # BUG: Something is missing here!


def fix_hexagon():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    import turtle
    t = turtle.Turtle()

    pass  # Write the corrected code here


# ============================================================
# BUG HUNT D: The Never-Ending Star
# ============================================================
"""
STORY:
{{hero}} tried to draw a 5-pointed star, but it never stops!
The turtle keeps drawing forever.

EXPECTED BEHAVIOR:
A 5-pointed star that stops after completing.

ACTUAL BEHAVIOR:
The turtle draws forever in an infinite loop.
"""

def buggy_star():
    import turtle
    t = turtle.Turtle()

    i = 0
    while i < 5:
        t.forward(100)
        t.right(144)
        # BUG: i is never updated!


def fix_star():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: What makes a while loop stop?
    #
    # The fix:
    import turtle
    t = turtle.Turtle()

    pass  # Write the corrected code here


def main():
    print("=== Bug Hunt: Broken Shapes ===")
    print()
    print("Each shape-drawing spell has exactly ONE bug.")
    print("Find the bug, then write the fix in the fix_X function.")
    print()
    print("Bugs to find:")
    print("  A: The Incomplete Square - draws only 3 sides")
    print("  B: The Wrong-Way Triangle - doesn't close properly")
    print("  C: The Stuck Turtle - spins but doesn't move")
    print("  D: The Never-Ending Star - loops forever")
    print()
    print("="*50)

    # Uncomment to test your fixes (requires turtle graphics):
    # print("\nTesting fix_square...")
    # fix_square()

    # print("\nTesting fix_triangle...")
    # fix_triangle()

    # print("\nTesting fix_hexagon...")
    # fix_hexagon()

    # print("\nTesting fix_star...")
    # fix_star()


main()
