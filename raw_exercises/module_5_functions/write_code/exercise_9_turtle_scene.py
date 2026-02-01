# Exercise 9: Magical Scene with Functions!

import turtle


def setup():
    """Set up the screen and turtle"""
    screen = turtle.Screen()
    screen.bgcolor("navy")  # Night sky for magic!
    t = turtle.Turtle()
    t.speed(0)
    return t


def draw_square(t, x, y, size, color):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a filled square at position (x, y)
    #
    # Steps:
    # 1. Pick up pen, go to (x, y), put pen down
    # 2. Set the fill color
    # 3. Begin fill
    # 4. Draw 4 sides of the square
    # 5. End fill
    #
    # Hint: t.penup(), t.goto(x, y), t.pendown()
    # Hint: t.fillcolor(color), t.begin_fill(), t.end_fill()
    pass


def draw_triangle(t, x, y, size, color):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a filled triangle at position (x, y)
    # Similar to square but with 3 sides and 120 degree turns
    pass


def draw_circle_shape(t, x, y, radius, color):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a filled circle at position (x, y)
    #
    # Hint: t.circle(radius) draws a circle
    # The turtle draws from the bottom of the circle
    pass


def draw_star(t, x, y, size, color):
    # ✏️ BONUS FUNCTION ✏️
    # Draw a star at position (x, y)
    # Use a 5-pointed star (like in the {{location}}!)
    # Hint: for a 5-pointed star, turn 144 degrees
    pass


def draw_castle(t, x, y):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a magical castle using the shape functions!
    # Think of {{place}}! It could have:
    # - A main square building
    # - Tall triangle towers
    # - Small windows (yellow for lit-up!)
    # - Multiple towers at different heights
    #
    # Colors: "gray", "darkgray", "yellow" (for windows)
    pass


def draw_moon(t):
    # ✏️ YOUR CODE HERE ✏️
    # Draw a glowing moon in the night sky
    # Use draw_circle_shape with a light color
    pass


def draw_wand(t, x, y):
    # ✏️ BONUS ✏️
    # Draw a magic wand!
    # Could be a thin rectangle with sparkles (small stars)
    pass


def main():
    t = setup()

    # ✏️ DRAW YOUR MAGICAL SCENE HERE ✏️
    # Create a scene from your favorite book!
    #
    # Ideas:
    # - {{place}} at night with a moon and stars
    # - {{school}} with towers and torches
    # - {{location}} glowing in the distance
    # - A forest scene with trees and a campfire
    #
    # Use the functions above to create your scene!

    # Example calls (uncomment and modify):
    # draw_castle(t, -100, -100)
    # draw_moon(t)
    # draw_star(t, 50, 150, 20, "white")
    # draw_star(t, -80, 180, 15, "yellow")

    t.hideturtle()
    turtle.done()


main()
