# Exercise 5: Draw a Hexagon

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(3)
    t.color("purple")
    return t


def draw_hexagon(t):
    # ✏️ YOUR CODE HERE ✏️
    # Write a for loop to draw a hexagon (6 sides)
    # Hint: What angle do you need? (360 divided by number of sides)
    pass


def main():
    t = setup()
    draw_hexagon(t)
    turtle.done()


main()
