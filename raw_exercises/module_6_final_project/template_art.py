# Final Project Template: Art Generator

import turtle
import random


# ==================
# SETUP
# ==================

def setup():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    return t, screen


# ==================
# SHAPE FUNCTIONS
# ==================

def draw_shape_1(t, size, color):
    # Your first shape
    pass


def draw_shape_2(t, size, color):
    # Your second shape
    pass


def draw_pattern(t, shape_func, count):
    # Draw a pattern using a shape function
    pass


# ==================
# COLOR FUNCTIONS
# ==================

def get_random_color():
    colors = ["red", "blue", "green", "purple", "orange", "pink", "yellow"]
    return random.choice(colors)


def get_color_palette(theme):
    # Return colors based on theme
    if theme == "sunset":
        return ["red", "orange", "yellow", "pink"]
    elif theme == "ocean":
        return ["blue", "cyan", "teal", "navy"]
    elif theme == "forest":
        return ["green", "brown", "olive", "lime"]
    else:
        return ["red", "blue", "green", "purple"]


# ==================
# MAIN ART CREATOR
# ==================

def get_user_choices():
    print("🎨 Art Generator 🎨")
    print("==================")

    # Ask user for choices
    # theme = input("Choose theme (sunset/ocean/forest): ")
    # size = input("Size (small/medium/large): ")
    # Return the choices
    pass


def create_art(t, screen, choices):
    # Use choices to create art
    # screen.bgcolor(...)
    # Use your shape functions
    # Add randomness!
    pass


def main():
    t, screen = setup()

    choices = get_user_choices()
    create_art(t, screen, choices)

    turtle.done()


main()
