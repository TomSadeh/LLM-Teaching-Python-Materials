# Exercise 17: Turtle Shapes - Drawing Without Loops

import turtle


def exercise_a():
    """Draw a square by writing each step manually (no loops yet!)"""
    t = turtle.Turtle()

    # ✏️ YOUR CODE HERE ✏️
    # Draw a square step by step:
    # Side 1: forward 100, right 90
    # Side 2: forward 100, right 90
    # Side 3: forward 100, right 90
    # Side 4: forward 100, right 90
    pass

    turtle.done()


def exercise_b():
    """Draw a triangle step by step"""
    t = turtle.Turtle()

    # ✏️ YOUR CODE HERE ✏️
    # Draw a triangle:
    # Each turn needs to be 120 degrees (not 90!)
    # Hint: 360 / 3 = 120
    pass

    turtle.done()


def exercise_c():
    """Draw a simple house (square + triangle roof)"""
    t = turtle.Turtle()

    # ✏️ YOUR CODE HERE ✏️
    # 1. Draw a square for the house
    # 2. Move to the top-left corner
    # 3. Draw a triangle for the roof
    #
    # Hint: After the square, the turtle is back at start.
    # You need to move it up to draw the roof!
    pass

    turtle.done()


# Choose which exercise to run:
# exercise_a()
# exercise_b()
exercise_c()
