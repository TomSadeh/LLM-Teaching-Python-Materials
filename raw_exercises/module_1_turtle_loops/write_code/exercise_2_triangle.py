# Exercise 2: Draw a Triangle

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(3)
    t.color("green")
    return t


def draw_triangle(t):
    # ✏️ YOUR CODE HERE ✏️
    # Write a for loop to draw a triangle
    # Hint: what angle makes 3 turns add up to 360?
    pass


def main():
    t = setup()
    draw_triangle(t)
    turtle.done()


main()
