# Exercise 18: Turtle Colors and Pen Control

import turtle


def exercise_a():
    """Draw a red line, then a blue line"""
    t = turtle.Turtle()

    # ✏️ YOUR CODE HERE ✏️
    # 1. Set color to red: t.color("red")
    # 2. Move forward 100
    # 3. Turn right 90
    # 4. Set color to blue: t.color("blue")
    # 5. Move forward 100
    pass

    turtle.done()


def exercise_b():
    """Draw two separate lines using pen up/down"""
    t = turtle.Turtle()

    # ✏️ YOUR CODE HERE ✏️
    # 1. Draw a line forward 50
    # 2. Lift the pen: t.penup()
    # 3. Move forward 30 (this won't draw!)
    # 4. Put pen down: t.pendown()
    # 5. Draw another line forward 50
    pass

    turtle.done()


def exercise_c():
    """Draw a colorful pattern - 4 lines in different colors"""
    t = turtle.Turtle()
    t.speed(3)  # Slow down to see the colors

    # ✏️ YOUR CODE HERE ✏️
    # Draw 4 lines in a fan pattern:
    # 1. Red line forward 100, turn right 90
    # 2. Blue line forward 100, turn right 90
    # 3. Green line forward 100, turn right 90
    # 4. Purple line forward 100, turn right 90
    #
    # Colors you can use: "red", "blue", "green", "purple",
    #                     "orange", "pink", "yellow", "brown"
    pass

    turtle.done()


# Choose which exercise to run:
# exercise_a()
# exercise_b()
exercise_c()
