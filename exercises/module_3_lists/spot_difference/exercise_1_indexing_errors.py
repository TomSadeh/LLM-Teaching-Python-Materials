# =============================================================================
# Spot the Difference: Indexing Errors
# =============================================================================
# Difficulty: 2-3
# Concepts: Off-by-one errors, common indexing mistakes
# =============================================================================

"""
{{CONTEXT_SPOT_DIFFERENCE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{COMPARISON_1_TITLE}}
# ============================================================
# {{CONTEXT_COMPARISON_1_NARRATIVE}}
# One version gets the last element correctly, one causes an error.


def snippet_a1():
    """Version 1 - Using len()"""
    items = ["{{item}}", "potion", "key"]
    last_index = len(items) - 1
    print(f"Last item: {items[last_index]}")


def snippet_a2():
    """Version 2 - spot the difference!"""
    items = ["{{item}}", "potion", "key"]
    last_index = len(items)
    print(f"Last item: {items[last_index]}")


def explain_difference_a():
    # EXPLAIN THE DIFFERENCE
    #
    # Hint: What does len() return vs what is the last valid index?

    explanation = """
    The difference is:
    -

    Version 1 behavior:
    -

    Version 2 behavior:
    -

    Why this matters:
    -
    """
    return explanation


# ============================================================
# {{COMPARISON_2_TITLE}}
# ============================================================
# {{CONTEXT_COMPARISON_2_NARRATIVE}}
# One version accesses elements safely in a loop, one goes too far.


def snippet_b1():
    """Version 1 - Correct loop range"""
    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    for i in range(len(team)):
        print(f"Member {i}: {team[i]}")


def snippet_b2():
    """Version 2 - spot the difference!"""
    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    for i in range(len(team) + 1):
        print(f"Member {i}: {team[i]}")


def explain_difference_b():
    # EXPLAIN THE DIFFERENCE
    #
    # Hint: What values does each range() produce?

    explanation = """
    The difference is:
    -

    Version 1 behavior:
    -

    Version 2 behavior:
    -

    Why this matters:
    -
    """
    return explanation


# ============================================================
# {{COMPARISON_3_TITLE}}
# ============================================================
# {{CONTEXT_COMPARISON_3_NARRATIVE}}
# Both access an element, but one modifies the list and one doesn't.


def snippet_c1():
    """Version 1 - Accessing an element"""
    scores = [85, 92, 78]
    bonus = scores[0] + 10
    print(f"Bonus: {bonus}")
    print(f"Scores: {scores}")


def snippet_c2():
    """Version 2 - spot the difference!"""
    scores = [85, 92, 78]
    scores[0] = scores[0] + 10
    print(f"Bonus: {scores[0]}")
    print(f"Scores: {scores}")


def explain_difference_c():
    # EXPLAIN THE DIFFERENCE
    #
    # Hint: What happens to the original list in each version?

    explanation = """
    The difference is:
    -

    Version 1 behavior:
    -

    Version 2 behavior:
    -

    Why this matters:
    -
    """
    return explanation


# ============================================================
# {{COMPARISON_4_TITLE}}
# ============================================================
# {{CONTEXT_COMPARISON_4_NARRATIVE}}
# Two ways to get the last element - which is safer?


def snippet_d1():
    """Version 1 - Using -1"""
    inventory = ["{{item}}", "potion"]
    last = inventory[-1]
    print(f"Last: {last}")


def snippet_d2():
    """Version 2 - spot the difference!"""
    inventory = ["{{item}}", "potion"]
    last = inventory[1]
    print(f"Last: {last}")


def explain_difference_d():
    # EXPLAIN THE DIFFERENCE
    #
    # Hint: What if the list length changes?

    explanation = """
    The difference is:
    -

    Version 1 behavior:
    -

    Version 2 behavior:
    -

    Why -1 is often better:
    -
    """
    return explanation


def main():
    print("{{CONTEXT_SPOT_DIFFERENCE_INTRO}}")
    print("=" * 50)

    print("\n=== {{COMPARISON_1_TITLE}} ===")
    print("Version 1:")
    snippet_a1()
    # print("\nVersion 2:")
    # snippet_a2()  # Uncomment to see the error
    print(f"\nExplanation:{explain_difference_a()}")

    print("\n=== {{COMPARISON_2_TITLE}} ===")
    print("Version 1:")
    snippet_b1()
    # print("\nVersion 2:")
    # snippet_b2()  # Uncomment to see the error
    print(f"\nExplanation:{explain_difference_b()}")

    print("\n=== {{COMPARISON_3_TITLE}} ===")
    print("Version 1:")
    snippet_c1()
    print("\nVersion 2:")
    snippet_c2()
    print(f"\nExplanation:{explain_difference_c()}")

    print("\n=== {{COMPARISON_4_TITLE}} ===")
    print("Version 1:")
    snippet_d1()
    print("\nVersion 2:")
    snippet_d2()
    print(f"\nExplanation:{explain_difference_d()}")

    print("=" * 50)
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()
