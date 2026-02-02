# Exercise 3: Draw a Star

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(3)
    t.color("gold")
    t.pensize(3)
    return t


def draw_star(t):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a 5-pointed star using a for loop
    # Hint: try angles bigger than 90 - like 100, 120, 144, 150
    pass


def main():
    t = setup()
    draw_star(t)
    turtle.done()


main()
