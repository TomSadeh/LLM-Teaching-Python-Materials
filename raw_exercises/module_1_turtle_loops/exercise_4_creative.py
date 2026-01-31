# Exercise 4: Creative Magic Art!

import turtle


def setup():
    t = turtle.Turtle()
    t.speed(5)
    # Try: turtle.Screen().bgcolor("black") for a night sky effect!
    # Or "navy" for a magical twilight
    return t


def draw_art(t):
    # ✏️ YOUR CODE HERE ✏️
    # Create magical art inspired by your favorite books!
    #
    # Ideas:
    # - Harry Potter: A wand with sparkles, the Golden Snitch, stars
    # - Percy Jackson: Waves (Poseidon), a trident, lightning bolts
    # - Hunger Games: The Mockingjay pin (circle + bird shape), flames
    # - Keeper of the Lost Cities: An alicorn, glowing eyes, light beams
    #
    # Useful commands:
    # - t.circle(50) - draw a circle
    # - t.penup(), t.pendown() - move without drawing
    # - t.begin_fill(), t.end_fill() - fill shapes with color
    # - t.pensize(3) - thicker lines
    pass


def main():
    t = setup()
    draw_art(t)
    turtle.done()


main()
