# Bonus Example: Rainbow Spiral

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(0)
    turtle.Screen().bgcolor("black")
    return t


def draw_spiral(t):
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(180):
        t.color(colors[i % 6])
        t.forward(i * 2)
        t.right(61)


def main():
    t = setup()
    draw_spiral(t)
    turtle.done()


main()
