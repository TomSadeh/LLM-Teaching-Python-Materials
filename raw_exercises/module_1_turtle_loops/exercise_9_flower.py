# Exercise 9: Draw a Flower

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    return t


def draw_petal(t):
    """Draw one petal - this is done for you!"""
    for i in range(2):
        t.forward(50)
        t.right(60)
        t.forward(50)
        t.right(120)


def draw_flower(t):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a flower by repeating petals in a circle
    #
    # Hint: Draw a petal, then turn a little, then draw another petal
    # Hint: If you want 6 petals, turn 60 degrees between each (360/6 = 60)
    # Hint: Use the draw_petal function above!
    #
    # Bonus: Can you make petals different colors?
    pass


def main():
    t = setup()
    draw_flower(t)
    turtle.done()


main()
