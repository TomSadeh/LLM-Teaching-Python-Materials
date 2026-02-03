# =============================================================================
# Fill in the Blanks: Loop Syntax
# =============================================================================
# Difficulty: 2
# Concepts: for loop keyword, range() function, in keyword, loop variable
# =============================================================================

"""
{{CONTEXT_FILL_BLANKS_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

import turtle


# --- {{EXERCISE_1_TITLE}} ---
# {{CONTEXT_EXERCISE_1_NARRATIVE}}


def exercise_a():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Complete the for loop to repeat 4 times for {{hero}}.
    #
    # Hint: A for loop starts with the keyword "for".
    #
    # ___ i in range(4):              # Fill in the loop keyword
    #     print("Step", i)
    pass


# --- {{EXERCISE_2_TITLE}} ---
# {{CONTEXT_EXERCISE_2_NARRATIVE}}


def exercise_b():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Complete the loop to iterate over a range for {{creature}}.
    #
    # Hint: The keyword "in" connects the variable to what we loop over.
    #
    # for step ___ range(3):          # Fill in the connecting keyword
    #     print("{{creature}} takes step", step)
    pass


# --- {{EXERCISE_3_TITLE}} ---
# {{CONTEXT_EXERCISE_3_NARRATIVE}}


def exercise_c():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Complete the range to repeat 5 times at {{school}}.
    #
    # Hint: range(n) creates numbers from 0 to n-1.
    #       To repeat 5 times, what should n be?
    #
    # for i in ___(5):                # Fill in the function name
    #     print("Repeat number", i)
    pass


# --- {{EXERCISE_4_TITLE}} ---
# {{CONTEXT_EXERCISE_4_NARRATIVE}}


def exercise_d():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Complete this loop that draws a square at {{location}}.
    #
    # Hint: A square has 4 sides, so we repeat 4 times.
    #
    # t = turtle.Turtle()
    # ___ side ___ range(___):        # Fill in: keyword, keyword, number
    #     t.forward(50)
    #     t.right(90)
    pass


# --- {{EXERCISE_5_TITLE}} ---
# {{CONTEXT_EXERCISE_5_NARRATIVE}}


def exercise_e():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Complete the loop body indentation for {{hero}}'s journey.
    #
    # Hint: Code inside a loop must be indented (4 spaces or 1 tab).
    #
    # t = turtle.Turtle()
    # for i in range(3):
    # ___t.forward(30)                # Add proper indentation
    # ___t.right(120)                 # Add proper indentation
    pass


def main():
    print("{{CONTEXT_FILL_BLANKS_INTRO}}")
    print("=" * 50)

    print("\n=== {{EXERCISE_1_TITLE}} ===")
    # exercise_a()  # Uncomment when you've filled the blanks

    print("\n=== {{EXERCISE_2_TITLE}} ===")
    # exercise_b()

    print("\n=== {{EXERCISE_3_TITLE}} ===")
    # exercise_c()

    print("\n=== {{EXERCISE_4_TITLE}} ===")
    # exercise_d()

    print("\n=== {{EXERCISE_5_TITLE}} ===")
    # exercise_e()

    print("\nFill in all the blanks, then uncomment to test!")
    print("{{CONTEXT_ROLE_COMPLETE}}")
    turtle.done()


main()
