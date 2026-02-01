# Exercise 1: Shape Drawing Functions

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(5)
    return t


def draw_square(t, size):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a square with the given size
    pass


def draw_triangle(t, size):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a triangle with the given size
    pass


def draw_polygon(t, sides, size):
    # ✏️ YOUR CODE HERE ✏️
    # Draw any polygon!
    # Hint: the angle to turn is 360 / sides
    pass


def main():
    t = setup()

    # Test your functions!
    draw_square(t, 50)

    t.penup()
    t.forward(100)
    t.pendown()

    draw_triangle(t, 50)

    t.penup()
    t.forward(100)
    t.pendown()

    # Draw a hexagon (6 sides)
    draw_polygon(t, 6, 50)

    turtle.done()


main()
