# Exercise 1: Code Ordering - Drawing Steps
#
# The lines of code are scrambled! Put them in the correct order
# to make the turtle draw correctly.
#
# Theme: Drawing magical symbols and shapes


# ============================================================
# ORDERING CHALLENGE A: Draw a Line
# ============================================================
#
# Draw a simple line from the starting position.
# The turtle needs to be set up before it can draw!
#
# SCRAMBLED LINES:
#   t.forward(100)
#   t = turtle.Turtle()
#   import turtle

def challenge_a():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: import → create turtle → use turtle

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE B: Colored Square
# ============================================================
#
# Draw a filled square. The fill must start before drawing
# and end after the shape is complete.
#
# SCRAMBLED LINES:
#   t.end_fill()
#   for i in range(4):
#       t.forward(50)
#       t.right(90)
#   t.begin_fill()
#   t.fillcolor("blue")

def challenge_b():
    import turtle
    t = turtle.Turtle()

    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: set color → begin fill → draw shape → end fill

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE C: Position Then Draw
# ============================================================
#
# Move to a position, then draw a triangle.
# We want to move WITHOUT drawing, then draw the shape.
#
# SCRAMBLED LINES:
#   t.pendown()
#   for i in range(3):
#       t.forward(60)
#       t.left(120)
#   t.goto(50, 50)
#   t.penup()

def challenge_c():
    import turtle
    t = turtle.Turtle()

    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: penup → move → pendown → draw

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE D: Complete Drawing Sequence
# ============================================================
#
# A complete turtle program that draws a star and displays it.
#
# SCRAMBLED LINES:
#   turtle.done()
#   for i in range(5):
#       t.forward(100)
#       t.right(144)
#   import turtle
#   t.speed(3)
#   t = turtle.Turtle()
#   t.color("gold")

def challenge_d():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Pattern: import → create → setup (speed, color) → draw → done

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE E: Loop Preparation
# ============================================================
#
# Draw 3 squares in a row. The loop counter and movement
# must be in the right order.
#
# SCRAMBLED LINES:
#   for count in range(3):
#       for side in range(4):
#           t.forward(30)
#           t.right(90)
#       t.penup()
#       t.forward(50)
#       t.pendown()

def challenge_e():
    import turtle
    t = turtle.Turtle()

    # ✏️ REORDER THE LINES ✏️
    # The lines are already in the correct order!
    # But you need to understand WHY this order works.
    #
    # Copy and study: What happens if pendown came before forward(50)?

    pass  # Delete this and add the correctly ordered lines


def main():
    print("=== Challenge A: Draw a Line ===")
    # challenge_a()  # Uncomment when ready

    print("\n=== Challenge B: Colored Square ===")
    # challenge_b()

    print("\n=== Challenge C: Position Then Draw ===")
    # challenge_c()

    print("\n=== Challenge D: Complete Drawing Sequence ===")
    # challenge_d()

    print("\n=== Challenge E: Loop Preparation ===")
    # challenge_e()

    print("\nReorder each challenge, then uncomment to test!")


main()
