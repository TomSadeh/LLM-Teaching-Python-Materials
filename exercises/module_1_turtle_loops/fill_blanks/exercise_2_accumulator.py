# =============================================================================
# Fill in the Blanks: Accumulator Pattern
# =============================================================================
# Difficulty: 4
# Concepts: accumulator variables, running totals, loop-based calculations
# =============================================================================

"""
{{CONTEXT_FILL_BLANKS_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# --- {{EXERCISE_1_TITLE}} ---
# {{CONTEXT_EXERCISE_1_NARRATIVE}}


def exercise_a():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Calculate the sum of numbers 1 through 5 for {{hero}}.
    #
    # Hint: Initialize the accumulator to 0 before the loop.
    #
    # total = ___                         # Start with zero
    # for num in range(1, 6):
    #     total = total ___ num           # Add each number
    # print("Sum:", total)                # Should print 15
    pass


# --- {{EXERCISE_2_TITLE}} ---
# {{CONTEXT_EXERCISE_2_NARRATIVE}}


def exercise_b():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Count down and track total distance at {{school}}.
    #
    # Hint: Each step adds to total_distance.
    #
    # total_distance = 0
    # for step in range(1, 5):
    #     distance = step * 10
    #     total_distance = ___ + distance  # Add to accumulator
    # print("Total distance:", ___)        # Print the result
    pass


# --- {{EXERCISE_3_TITLE}} ---
# {{CONTEXT_EXERCISE_3_NARRATIVE}}


def exercise_c():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Build a message by adding words for {{creature}}.
    #
    # Hint: Strings can be accumulated too! Start with empty string "".
    #
    # message = ___                        # Start with empty string
    # for i in range(3):
    #     message = message ___ "Go! "     # Add "Go! " each time
    # print(message)                       # Should print "Go! Go! Go! "
    pass


# --- {{EXERCISE_4_TITLE}} ---
# {{CONTEXT_EXERCISE_4_NARRATIVE}}


def exercise_d():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Calculate total turning for drawing at {{location}}.
    # When drawing a shape, track total degrees turned.
    #
    # total_turns = ___                    # Initialize accumulator
    # for side in range(4):
    #     turn_amount = 90
    #     total_turns = total_turns + ___  # Add turn amount
    # print("Total turned:", total_turns, "degrees")  # Should be 360
    pass


# --- {{EXERCISE_5_TITLE}} ---
# {{CONTEXT_EXERCISE_5_NARRATIVE}}


def exercise_e():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Calculate total line length for {{hero}}'s path.
    # Lines increase: 10, 20, 30, 40, 50 units.
    #
    # total_length = 0
    # ___ i in range(1, 6):               # Fill in loop keyword
    #     line_length = i ___ 10          # Calculate: i times 10
    #     total_length = total_length + line_length
    # print("Total length:", ___)         # Print the accumulator
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


main()
