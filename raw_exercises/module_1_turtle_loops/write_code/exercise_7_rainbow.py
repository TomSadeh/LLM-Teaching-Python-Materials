# Exercise 7: Rainbow Lines

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(3)
    t.pensize(5)  # thick lines
    return t


def draw_rainbow_lines(t):
    # Here are the rainbow colors for you to use:
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # ✏️ YOUR CODE HERE ✏️
    # Loop through the colors list and draw a line with each color
    # After each line, move to a new position so lines don't overlap
    #
    # Hint: use t.color(color_name) to change colors
    # Hint: use t.penup() and t.pendown() to move without drawing
    pass


def main():
    t = setup()
    draw_rainbow_lines(t)
    turtle.done()


main()
