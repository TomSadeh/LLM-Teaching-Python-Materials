# Exercise 6: Draw a Circle (from straight lines!)

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(0)  # fastest speed
    t.color("red")
    return t


def draw_circle(t):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a circle using a for loop!
    # The trick: move forward a tiny bit, turn a tiny bit, repeat many times
    # Try: 36 steps, moving 10 pixels, turning 10 degrees each time
    # Or: 360 steps, moving 1 pixel, turning 1 degree each time
    pass


def main():
    t = setup()
    draw_circle(t)
    turtle.done()


main()
