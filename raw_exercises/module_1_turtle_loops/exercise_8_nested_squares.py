# Exercise 8: Nested Squares

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(5)
    t.color("blue")
    return t


def draw_square(t, size):
    """Helper function to draw one square of a given size"""
    for i in range(4):
        t.forward(size)
        t.right(90)


def draw_nested_squares(t):
    # ✏️ YOUR CODE HERE ✏️
    # Draw 5 squares, each one bigger than the last
    # Start with size 20, then 40, then 60, then 80, then 100
    #
    # Hint: use a for loop with range()
    # Hint: call the draw_square function above for each square
    #
    # Bonus: Can you use different colors for each square?
    pass


def main():
    t = setup()
    draw_nested_squares(t)
    turtle.done()


main()
