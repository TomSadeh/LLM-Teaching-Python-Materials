# Exercise 1: Fill in the Blanks - Loop Syntax
#
# Complete the code by filling in the blanks (marked with ___).
# Each blank needs a specific piece of code to make the program work.
#
# Theme: {{hero}} practices magical shapes


# --- FILL THE BLANKS A: Basic For Loop ---
#
# Complete the for loop structure

def exercise_a():
    # ✏️ FILL IN THE BLANKS ✏️

    # Print numbers 0 to 4
    # for <variable> in <range>:
    ___ i ___ range(5):  # Hint: keyword "for" and keyword "in"
        print(i)


# --- FILL THE BLANKS B: Range with Start and End ---
#
# Use range() with start and end values

def exercise_b():
    # ✏️ FILL IN THE BLANKS ✏️

    # Print numbers 1 to 5
    # range(start, end) - end is NOT included
    for i in ___(1, ___):  # Hint: range(start, end) where end is one more than last
        print(i)


# --- FILL THE BLANKS C: Drawing a Square ---
#
# Complete the turtle code to draw a square

def exercise_c():
    # ✏️ FILL IN THE BLANKS ✏️

    import turtle
    t = turtle.Turtle()

    # A square has 4 sides
    for i in range(___):  # Hint: How many sides does a square have?
        t.forward(100)
        t.___(90)  # Hint: Which direction? left or right?


# --- FILL THE BLANKS D: Drawing a Triangle ---
#
# Complete the code to draw an equilateral triangle

def exercise_d():
    # ✏️ FILL IN THE BLANKS ✏️

    import turtle
    t = turtle.Turtle()

    # A triangle has 3 sides
    # For a closed shape: total turn = 360°
    # Each turn = 360° ÷ number of sides
    for i in ___(___)  # Hint: range(how many sides?)
        t.___(100)  # Hint: move forward
        t.right(___)  # Hint: 360 ÷ 3 = ?


# --- FILL THE BLANKS E: Loop with Accumulator ---
#
# Use a loop to add up numbers

def exercise_e():
    # ✏️ FILL IN THE BLANKS ✏️

    # Add up numbers 1 through 5
    total = 0

    for number in range(1, 6):
        total = total ___ number  # Hint: We're adding to the total
        print(f"Adding {number}, total is now {total}")

    print(f"Final total: {total}")


# --- FILL THE BLANKS F: Nested Loops ---
#
# Use two loops together

def exercise_f():
    # ✏️ FILL IN THE BLANKS ✏️

    # Print a 3x3 grid of stars
    # Output should be:
    # * * *
    # * * *
    # * * *

    for row in range(___):  # Hint: How many rows?
        ___ col in range(3):  # Hint: keyword for a loop
            print("*", end=" ")
        print()  # New line after each row


def main():
    print("=== Fill in the Blanks: Loop Syntax ===")
    print()
    print("Fill in the blanks in each exercise, then uncomment to test!")
    print()
    print("="*50)

    # Uncomment each exercise after filling in the blanks:

    # print("\n--- Exercise A: Basic For Loop ---")
    # exercise_a()

    # print("\n--- Exercise B: Range with Start and End ---")
    # exercise_b()

    # print("\n--- Exercise C: Drawing a Square ---")
    # exercise_c()

    # print("\n--- Exercise D: Drawing a Triangle ---")
    # exercise_d()

    # print("\n--- Exercise E: Loop with Accumulator ---")
    # exercise_e()

    # print("\n--- Exercise F: Nested Loops ---")
    # exercise_f()

    print("\nFill in all the blanks, then uncomment to test!")


main()


# =============================================================================
# ANSWER KEY (for reference):
# =============================================================================
#
# Exercise A: for, in
# Exercise B: range, 6
# Exercise C: 4, right
# Exercise D: range, 3 (and add colon), forward, 120
# Exercise E: +
# Exercise F: 3, for
#
# =============================================================================
