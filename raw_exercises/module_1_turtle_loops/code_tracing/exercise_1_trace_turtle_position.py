# Exercise 1: Code Tracing - Turtle Position
#
# Trace through the code step by step, tracking the turtle's position.
# Fill in the tracing table to show how x, y coordinates change.
#
# Theme: Tracking magical creature movements


# --- TRACING CHALLENGE A: Simple Movement ---
# Track the turtle's position as it moves forward and turns.

def code_to_trace_a():
    """Study this code - don't run it yet!"""
    import turtle
    t = turtle.Turtle()

    # Starting position is (0, 0), facing East (0 degrees)
    t.forward(100)  # Move east
    t.left(90)      # Turn to face north
    t.forward(50)   # Move north

    print(f"Final position: ({t.xcor()}, {t.ycor()})")


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # The turtle starts at (0, 0) facing East (right).
    # forward() moves in the direction it's facing.
    # left(90) turns 90 degrees counterclockwise.
    #
    # | Step | Command      | x    | y    | Heading |
    # |------|--------------|------|------|---------|
    # | 0    | (start)      | 0    | 0    | East    |
    # | 1    | forward(100) | ?    | ?    | ?       |
    # | 2    | left(90)     | ?    | ?    | ?       |
    # | 3    | forward(50)  | ?    | ?    | ?       |
    #
    # Write your completed table as comments below:
    #
    # Final position: (?, ?)

    pass


# --- TRACING CHALLENGE B: Square Movement ---
# Track position through a loop that draws a square.

def code_to_trace_b():
    """Study this code - don't run it yet!"""
    import turtle
    t = turtle.Turtle()

    for i in range(4):
        t.forward(50)
        t.right(90)

    print(f"Final position: ({t.xcor()}, {t.ycor()})")


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track position after each forward() command.
    # right(90) turns 90 degrees clockwise.
    # Heading changes: East -> South -> West -> North -> East
    #
    # | i | After forward(50)          | Heading after right(90) |
    # |---|----------------------------|-------------------------|
    # | 0 | x=?, y=?                   | ?                       |
    # | 1 | x=?, y=?                   | ?                       |
    # | 2 | x=?, y=?                   | ?                       |
    # | 3 | x=?, y=?                   | ?                       |
    #
    # Write your completed table below:
    #
    # Final position: (?, ?)  (Hint: Where did we start?)

    pass


# --- TRACING CHALLENGE C: Triangle with goto ---
# Track position using goto() commands.

def code_to_trace_c():
    """Study this code - don't run it yet!"""
    import turtle
    t = turtle.Turtle()

    # Draw triangle using goto
    t.goto(100, 0)    # Bottom right
    t.goto(50, 86)    # Top (approximately equilateral)
    t.goto(0, 0)      # Back to start

    print(f"Final position: ({t.xcor()}, {t.ycor()})")


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # goto(x, y) moves the turtle directly to that position.
    # The path drawn depends on where it was and where it goes.
    #
    # | Step | Command       | x    | y    |
    # |------|---------------|------|------|
    # | 0    | (start)       | 0    | 0    |
    # | 1    | goto(100, 0)  | ?    | ?    |
    # | 2    | goto(50, 86)  | ?    | ?    |
    # | 3    | goto(0, 0)    | ?    | ?    |
    #
    # Write your completed table below:

    pass


# --- TRACING CHALLENGE D: Spiral Pattern ---
# Track position with increasing distances.

def code_to_trace_d():
    """Study this code - don't run it yet!"""
    import turtle
    t = turtle.Turtle()

    distance = 20
    for i in range(4):
        t.forward(distance)
        t.right(90)
        distance = distance + 20

    print(f"Final position: ({t.xcor()}, {t.ycor()})")


def trace_table_d():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # distance increases by 20 each iteration.
    # Track both the distance used AND the position.
    #
    # | i | distance | After forward | After right(90) |
    # |---|----------|---------------|-----------------|
    # | 0 | 20       | x=?, y=?      | Heading: ?      |
    # | 1 | ?        | x=?, y=?      | Heading: ?      |
    # | 2 | ?        | x=?, y=?      | Heading: ?      |
    # | 3 | ?        | x=?, y=?      | Heading: ?      |
    #
    # Write your completed table below:
    #
    # Final position: (?, ?)

    pass


# --- TRACING CHALLENGE E: Pen Up/Down ---
# Track when drawing happens vs just moving.

def code_to_trace_e():
    """Study this code - don't run it yet!"""
    import turtle
    t = turtle.Turtle()

    # Draw, move without drawing, draw again
    t.forward(50)      # Draws a line
    t.penup()
    t.forward(30)      # Moves but doesn't draw
    t.pendown()
    t.forward(50)      # Draws a line

    print(f"Final position: ({t.xcor()}, {t.ycor()})")


def trace_table_e():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track position AND whether the pen is down (drawing).
    #
    # | Step | Command     | x    | y    | Pen Down? | Line Drawn? |
    # |------|-------------|------|------|-----------|-------------|
    # | 0    | (start)     | 0    | 0    | Yes       | -           |
    # | 1    | forward(50) | ?    | ?    | ?         | ?           |
    # | 2    | penup()     | ?    | ?    | ?         | -           |
    # | 3    | forward(30) | ?    | ?    | ?         | ?           |
    # | 4    | pendown()   | ?    | ?    | ?         | -           |
    # | 5    | forward(50) | ?    | ?    | ?         | ?           |
    #
    # Write your completed table below:
    #
    # Total line length drawn: ?

    pass


def verify_traces():
    """Run this after completing your traces to check your work"""
    import turtle

    print("=== Trace A - Simple Movement ===")
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.forward(100)
    t.left(90)
    t.forward(50)
    print(f"Actual final position: ({t.xcor()}, {t.ycor()})")
    screen.clear()

    print("\n=== Trace B - Square ===")
    t = turtle.Turtle()
    for i in range(4):
        t.forward(50)
        t.right(90)
    print(f"Actual final position: ({t.xcor()}, {t.ycor()})")
    screen.clear()

    print("\n=== Trace D - Spiral ===")
    t = turtle.Turtle()
    distance = 20
    for i in range(4):
        t.forward(distance)
        t.right(90)
        distance = distance + 20
    print(f"Actual final position: ({round(t.xcor())}, {round(t.ycor())})")
    screen.clear()

    print("\n=== Trace E - Pen Up/Down ===")
    t = turtle.Turtle()
    t.forward(50)
    t.penup()
    t.forward(30)
    t.pendown()
    t.forward(50)
    print(f"Actual final position: ({t.xcor()}, {t.ycor()})")

    turtle.done()


def main():
    print("Complete the tracing tables in trace_table_X functions first!")
    print("Then uncomment the line below to verify your answers.")
    print()
    print("Remember:")
    print("- Turtle starts at (0, 0) facing East (right)")
    print("- forward() moves in the direction it's facing")
    print("- left/right turns change heading, not position")
    print("- goto(x, y) moves directly to coordinates")
    print()

    # Uncomment this line AFTER completing your traces:
    # verify_traces()


main()
