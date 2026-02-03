# =============================================================================
# Hybrid Exercise: The Mystery - Strange Shapes
# =============================================================================
# Difficulty: 4-5
# Arc: The Mystery
# Parts: DISCOVERY -> INVESTIGATION -> IMPROVEMENT
# Concepts: debugging loops, tracing, fixing turtle programs
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""

import turtle


# ============================================================
# PART 1: DISCOVERY - Observe the Unexpected
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{hero}} found some drawing code at {{school}}.
# The code is supposed to draw a square, but something is wrong!
# Study the output and notice the problem.


def mystery_code_1():
    """Run this and observe what happens"""
    # This should draw a square... but does it?
    t = turtle.Turtle()
    t.speed(0)
    for i in range(4):
        t.forward(80)
        t.right(80)  # Something's off!


def mystery_code_2():
    """Run this and observe what happens"""
    # This should count 1 to 5, but look at the output!
    for num in range(5):
        print(f"Count: {num}")


def mystery_code_3():
    """Run this and observe what happens"""
    # This should draw a growing spiral...
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(150, 50)
    t.pendown()
    for i in range(1, 6):
        length = 20  # All lines are the same!
        t.forward(length)
        t.right(90)


def your_observations():
    # ✏️ YOUR OBSERVATIONS HERE ✏️
    #
    # mystery_code_1:
    #   Expected: A closed square
    #   Actual: ________________________________
    #   What seems wrong? ________________________________
    #
    # mystery_code_2:
    #   Expected: Prints 1, 2, 3, 4, 5
    #   Actual: ________________________________
    #   What seems wrong? ________________________________
    #
    # mystery_code_3:
    #   Expected: Lines get longer (20, 40, 60, 80, 100)
    #   Actual: ________________________________
    #   What seems wrong? ________________________________
    pass


# ============================================================
# PART 2: INVESTIGATION - Trace the Code
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Now trace through each mystery to understand exactly why
# it behaves unexpectedly.


def trace_mystery_1():
    # ✏️ TRACE THE CODE ✏️
    #
    # mystery_code_1 uses right(80) instead of right(90).
    #
    # | Iteration | Angle turned so far |
    # |-----------|---------------------|
    # | 1         | 80                  |
    # | 2         |                     |
    # | 3         |                     |
    # | 4         |                     |
    #
    # Total angle: ___ degrees
    # For a closed shape: should be ___ degrees
    #
    # The bug: ________________________________
    pass


def trace_mystery_2():
    # ✏️ TRACE THE CODE ✏️
    #
    # range(5) produces: ___, ___, ___, ___, ___
    # But we wanted: 1, 2, 3, 4, 5
    #
    # To get 1-5, we should use: range(___, ___)
    #
    # The bug: ________________________________
    pass


def trace_mystery_3():
    # ✏️ TRACE THE CODE ✏️
    #
    # | Iteration | i | length (should be) | length (actual) |
    # |-----------|---|-------------------|-----------------|
    # | 1         | 1 | 20                | 20              |
    # | 2         | 2 | 40                | 20              |
    # | 3         | 3 | 60                | 20              |
    # | 4         | 4 | 80                | 20              |
    # | 5         | 5 | 100               | 20              |
    #
    # The code sets length = 20 directly, ignoring i.
    # It should be: length = i * ___
    #
    # The bug: ________________________________
    pass


# ============================================================
# PART 3: IMPROVEMENT - Fix the Issues
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Now that you understand the bugs, fix them!


def fixed_code_1():
    # ✏️ FIX THE BUG ✏️
    #
    # Fix the angle so the square closes properly.
    #
    # Your fix:

    pass


def fixed_code_2():
    # ✏️ FIX THE BUG ✏️
    #
    # Fix the range so it counts 1 to 5.
    #
    # Your fix:

    pass


def fixed_code_3():
    # ✏️ FIX THE BUG ✏️
    #
    # Fix the length calculation so lines grow.
    #
    # Your fix:

    pass


def main():
    print("=" * 50)
    print("PART 1: DISCOVERY - Observe the Unexpected")
    print("=" * 50)

    print("\n--- mystery_code_1 ---")
    print("This should draw a square...")
    mystery_code_1()

    print("\n--- mystery_code_2 ---")
    print("This should count 1 to 5...")
    mystery_code_2()

    print("\n--- mystery_code_3 ---")
    print("This should draw a growing spiral...")
    mystery_code_3()

    print("\n--- Your Observations ---")
    your_observations()

    print("\n" + "=" * 50)
    print("PART 2: INVESTIGATION - Trace the Code")
    print("=" * 50)

    print("\n--- trace_mystery_1 ---")
    trace_mystery_1()

    print("\n--- trace_mystery_2 ---")
    trace_mystery_2()

    print("\n--- trace_mystery_3 ---")
    trace_mystery_3()

    print("\n" + "=" * 50)
    print("PART 3: IMPROVEMENT - Fix the Issues")
    print("=" * 50)

    print("\n--- fixed_code_1 ---")
    # fixed_code_1()  # Uncomment when fixed

    print("\n--- fixed_code_2 ---")
    # fixed_code_2()

    print("\n--- fixed_code_3 ---")
    # fixed_code_3()

    print("\n" + "=" * 50)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    turtle.done()


main()
