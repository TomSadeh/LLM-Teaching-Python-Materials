# =============================================================================
# Bug Hunt: Drawing Bugs
# =============================================================================
# Difficulty: 5
# Concepts: multi-step drawing errors, accumulator bugs, pen state errors
# =============================================================================

"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}
"""

import turtle


# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Draw two separate squares with a gap between them.
#
# ACTUAL BEHAVIOR:
# The squares are connected by a line! There should be no line
# between them.
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}


def buggy_a():
    """This code has exactly ONE bug. Find it!"""
    # {{hero}} wants two separate squares at {{school}}
    t = turtle.Turtle()
    t.speed(0)

    # Draw first square
    for i in range(4):
        t.forward(50)
        t.right(90)

    # Move to next position (BUG: forgot something!)
    t.forward(70)

    # Draw second square
    for i in range(4):
        t.forward(50)
        t.right(90)


def fix_a():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: To move without drawing, you need to lift the pen first!
    # Use t.penup() before moving and t.pendown() after.
    #
    # The fix:

    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Calculate total = 10 + 20 + 30 + 40 = 100 and print it.
#
# ACTUAL BEHAVIOR:
# The program prints 0 at the end! The sum is wrong.
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}


def buggy_b():
    """This code has exactly ONE bug. Find it!"""
    # Calculate total distance for {{creature}}
    total = 0
    for i in range(1, 5):
        distance = i * 10
        total = 0 + distance  # Bug is here!
    print("Total distance:", total)


def fix_b():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: The accumulator pattern should be: total = total + distance
    # Not: total = 0 + distance (which resets to the last value)
    #
    # The fix:

    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Draw a star shape using 5 iterations with 144-degree turns.
#
# ACTUAL BEHAVIOR:
# The program crashes with a NameError!
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}


def buggy_c():
    """This code has exactly ONE bug. Find it!"""
    # Drawing a star at {{location}}
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(100, 100)
    t.pendown()
    for i in range(5):
        t.forward(80)
        turtle.right(144)  # Bug is here!


def fix_c():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: We created a turtle named 't', but one line uses 'turtle'
    # instead of 't'. Variable names must be consistent!
    #
    # The fix:

    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Draw a spiral with lines getting longer: 10, 20, 30, 40, 50.
#
# ACTUAL BEHAVIOR:
# All lines are the same length! The spiral doesn't grow.
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}


def buggy_d():
    """This code has exactly ONE bug. Find it!"""
    # Creating a spiral for {{hero}} at {{place}}
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    for i in range(1, 6):
        length = 10  # Bug is here!
        t.forward(length)
        t.right(90)


def fix_d():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: The length should change based on i.
    # For a growing spiral: length = i * 10
    #
    # The fix:

    pass


# ============================================================
# {{CASE_5_TITLE}}
# ============================================================
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Draw 5 dashes separated by gaps.
#
# ACTUAL BEHAVIOR:
# After the first dash, nothing else is drawn!
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}


def buggy_e():
    """This code has exactly ONE bug. Find it!"""
    # Creating a dashed line at {{school}}
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, -50)
    t.pendown()
    for i in range(5):
        t.forward(30)   # Draw dash
        t.penup()       # Lift pen
        t.forward(15)   # Move gap
        # Bug: forgot to put pen back down!


def fix_e():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: After moving the gap, you need t.pendown() to draw again!
    #
    # The fix:

    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Buggy version:")
    buggy_a()
    print("\nFixed version:")
    # fix_a()

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Buggy version:")
    buggy_b()
    print("\nFixed version:")
    # fix_b()

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Buggy version:")
    # buggy_c()  # This one crashes!
    print("(Skipped - would crash)")
    print("\nFixed version:")
    # fix_c()

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Buggy version:")
    buggy_d()
    print("\nFixed version:")
    # fix_d()

    print("\n=== {{CASE_5_TITLE}} ===")
    print("Buggy version:")
    buggy_e()
    print("\nFixed version:")
    # fix_e()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
    turtle.done()


main()
