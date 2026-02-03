# =============================================================================
# Code Ordering: Shape Sequence
# =============================================================================
# Difficulty: 2
# Concepts: turtle setup, for loop structure, loop body order
# =============================================================================

"""
{{CONTEXT_CODE_ORDERING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

import turtle


# ============================================================
# {{ORDERING_1_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_1_NARRATIVE}}
#
# Help {{hero}} draw a triangle. Put these lines in order:
#
# SCRAMBLED LINES:
#   for i in range(3):
#       t.forward(100)
#       t.left(120)
#   t = turtle.Turtle()


def challenge_a():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order.
    #
    # Hint: You must create the turtle before using it.
    # The loop header comes before the loop body.
    # Loop body lines must be indented!

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# {{ORDERING_2_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_2_NARRATIVE}}
#
# Create a square for {{school}}. Put these lines in order:
#
# SCRAMBLED LINES:
#       t.right(90)
#   t = turtle.Turtle()
#       t.forward(80)
#   for side in range(4):


def challenge_b():
    # ✏️ REORDER THE LINES ✏️
    #
    # Hint: What comes first: drawing or turning?
    # After you draw forward, then you turn.

    pass


# ============================================================
# {{ORDERING_3_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_3_NARRATIVE}}
#
# Draw a path with a message for {{creature}}. Put these lines in order:
#
# SCRAMBLED LINES:
#   print("Path complete!")
#   for step in range(5):
#   t = turtle.Turtle()
#       t.forward(20)


def challenge_c():
    # ✏️ REORDER THE LINES ✏️
    #
    # Hint: The print statement should come AFTER all drawing is done.
    # The message announces completion.

    pass


# ============================================================
# {{ORDERING_4_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_4_NARRATIVE}}
#
# Draw a colored square at {{location}}. Put these lines in order:
#
# SCRAMBLED LINES:
#   for i in range(4):
#       t.forward(60)
#   t.color("blue")
#       t.left(90)
#   t = turtle.Turtle()


def challenge_d():
    # ✏️ REORDER THE LINES ✏️
    #
    # Hint: Set the color BEFORE you start drawing.
    # The turtle must exist before you can set its color!

    pass


def main():
    print("{{CONTEXT_CODE_ORDERING_INTRO}}")
    print("=" * 50)

    print("\n=== {{ORDERING_1_TITLE}} ===")
    # challenge_a()  # Uncomment when ordered correctly

    print("\n=== {{ORDERING_2_TITLE}} ===")
    # challenge_b()

    print("\n=== {{ORDERING_3_TITLE}} ===")
    # challenge_c()

    print("\n=== {{ORDERING_4_TITLE}} ===")
    # challenge_d()

    print("\nReorder each challenge, then uncomment to test!")
    print("{{CONTEXT_ROLE_COMPLETE}}")
    turtle.done()


main()
