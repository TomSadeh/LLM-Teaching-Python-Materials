# Exercise 4: Turtle Art with Custom Functions

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(0)
    return t


def draw_square(t, size, color="black"):
    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Draw a filled square with the given color
    # Use: t.fillcolor(color), t.begin_fill(), t.end_fill()
    pass


def draw_flower(t, petal_size, num_petals):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a flower by drawing circles in a pattern
    # Hint: for each petal, draw a circle and turn (360 / num_petals)
    # t.circle(size) draws a circle
    pass


def draw_row_of_shapes(t, shape_func, count, spacing):
    # ✏️ YOUR CODE HERE ✏️
    # Draw 'count' shapes in a row with 'spacing' between them
    # shape_func is a function that draws a shape
    # After each shape, move right by 'spacing'
    pass


def create_art(t):
    # ✏️ CREATE YOUR ART! ✏️
    # Use your functions to create something cool!
    #
    # Ideas:
    # - A garden of flowers
    # - A pattern of squares in different colors
    # - A row of shapes that get bigger
    # - Combine everything into a scene!
    pass


def main():
    t = setup()
    turtle.Screen().bgcolor("lightblue")

    create_art(t)

    turtle.done()


main()
