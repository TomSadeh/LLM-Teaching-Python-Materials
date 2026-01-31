# Exercise 1: Draw a Square

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(3)
    t.color("blue")
    return t


def draw_square(t):
    # ✏️ YOUR CODE HERE ✏️
    # Write a for loop to draw a square
    # Hint: a square has 4 sides and 90 degree turns
    pass


def main():
    t = setup()
    draw_square(t)
    turtle.done()


main()
