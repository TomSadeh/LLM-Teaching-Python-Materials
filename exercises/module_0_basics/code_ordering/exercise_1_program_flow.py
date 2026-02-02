# =============================================================================
# Code Ordering: Program Flow
# =============================================================================
# Difficulty: 2-3
# Concepts: variable creation before use, order of operations, program sequence
# =============================================================================

"""
{{CONTEXT_CODE_ORDERING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{ORDERING_1_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_1_NARRATIVE}}
#
# SCRAMBLED LINES:
#   print("Final score:", score)
#   score = base + bonus
#   bonus = 50
#   base = 100


def challenge_a():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order.
    #
    # Hint: You must create a variable before you can use it.
    # What values do you need before you can calculate score?

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# {{ORDERING_2_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_2_NARRATIVE}}
#
# SCRAMBLED LINES:
#   total = price * quantity
#   print("{{hero}} pays:", total)
#   quantity = 4
#   price = 25


def challenge_b():
    # ✏️ REORDER THE LINES ✏️
    #
    # Hint: Think about what values the total calculation needs.
    # price and quantity must exist before you multiply them.

    pass


# ============================================================
# {{ORDERING_3_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_3_NARRATIVE}}
#
# SCRAMBLED LINES:
#   print("{{hero}} has", leftover, "remaining")
#   leftover = total - spent
#   spent = 30
#   print("{{hero}} starts with", total)
#   total = 100


def challenge_c():
    # ✏️ REORDER THE LINES ✏️
    #
    # Hint: There are TWO print statements. Consider when each should appear
    # to tell the story in order: first the starting amount, then the result.

    pass


# ============================================================
# {{ORDERING_4_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_4_NARRATIVE}}
#
# SCRAMBLED LINES:
#   final = doubled ** 2
#   print("Result:", final)
#   start = 3
#   doubled = start * 2


def challenge_d():
    # ✏️ REORDER THE LINES ✏️
    #
    # Hint: Each calculation depends on the previous one.
    # start -> doubled -> final -> print

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


main()
