# Exercise 1: Spot the Difference - Index Errors
#
# Each pair of code snippets looks almost identical but behaves differently.
# Your task: Identify the difference and explain how it changes the behavior.
#
# Theme: Managing {{hero}}'s team of magical creatures


# ============================================================
# SPOT DIFFERENCE A: len vs len-1
# ============================================================

def snippet_a1():
    """Version 1"""
    creatures = ["{{creature}}", "Phoenix", "Hippogriff"]
    last_creature = creatures[len(creatures) - 1]
    print(f"Last creature: {last_creature}")


def snippet_a2():
    """Version 2 - spot the difference!"""
    creatures = ["{{creature}}", "Phoenix", "Hippogriff"]
    last_creature = creatures[len(creatures)]
    print(f"Last creature: {last_creature}")


def explain_difference_a():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️

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
# SPOT DIFFERENCE B: range(len) vs range(len+1)
# ============================================================

def snippet_b1():
    """Version 1"""
    spells = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    for i in range(len(spells)):
        print(f"{i}: {spells[i]}")


def snippet_b2():
    """Version 2 - spot the difference!"""
    spells = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    for i in range(len(spells) + 1):
        print(f"{i}: {spells[i]}")


def explain_difference_b():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️

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
# SPOT DIFFERENCE C: append vs extend
# ============================================================

def snippet_c1():
    """Version 1"""
    team = ["{{hero}}"]
    new_members = ["{{friend}}", "{{heroine}}"]
    team.append(new_members)
    print(f"Team: {team}")
    print(f"Team size: {len(team)}")


def snippet_c2():
    """Version 2 - spot the difference!"""
    team = ["{{hero}}"]
    new_members = ["{{friend}}", "{{heroine}}"]
    team.extend(new_members)
    print(f"Team: {team}")
    print(f"Team size: {len(team)}")


def explain_difference_c():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️

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
# SPOT DIFFERENCE D: Copy vs Reference
# ============================================================

def snippet_d1():
    """Version 1"""
    original = ["{{spell1}}", "{{spell2}}"]
    copy = original
    copy.append("{{spell3}}")
    print(f"Original: {original}")


def snippet_d2():
    """Version 2 - spot the difference!"""
    original = ["{{spell1}}", "{{spell2}}"]
    copy = original[:]
    copy.append("{{spell3}}")
    print(f"Original: {original}")


def explain_difference_d():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️

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
# SPOT DIFFERENCE E: Element vs Sublist
# ============================================================

def snippet_e1():
    """Version 1"""
    heroes = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    first = heroes[0]
    print(f"First: {first}")
    print(f"Type: {type(first)}")


def snippet_e2():
    """Version 2 - spot the difference!"""
    heroes = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    first = heroes[0:1]
    print(f"First: {first}")
    print(f"Type: {type(first)}")


def explain_difference_e():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️

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
# SPOT DIFFERENCE F: sort vs sorted
# ============================================================

def snippet_f1():
    """Version 1"""
    numbers = [3, 1, 4, 1, 5]
    result = numbers.sort()
    print(f"Result: {result}")
    print(f"Numbers: {numbers}")


def snippet_f2():
    """Version 2 - spot the difference!"""
    numbers = [3, 1, 4, 1, 5]
    result = sorted(numbers)
    print(f"Result: {result}")
    print(f"Numbers: {numbers}")


def explain_difference_f():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️

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


def main():
    print("=== Difference A: len vs len-1 ===")
    print("Version 1:")
    snippet_a1()
    print("\nVersion 2:")
    # snippet_a2()  # This crashes - uncomment to see!
    print("(Uncomment to see the IndexError)")
    print(f"\nExplanation:{explain_difference_a()}")

    print("\n=== Difference B: range(len) vs range(len+1) ===")
    print("Version 1:")
    snippet_b1()
    print("\nVersion 2:")
    # snippet_b2()  # This crashes on the last iteration
    print("(Uncomment to see the IndexError)")
    print(f"\nExplanation:{explain_difference_b()}")

    print("\n=== Difference C: append vs extend ===")
    print("Version 1:")
    snippet_c1()
    print("\nVersion 2:")
    snippet_c2()
    print(f"\nExplanation:{explain_difference_c()}")

    print("\n=== Difference D: Copy vs Reference ===")
    print("Version 1:")
    snippet_d1()
    print("\nVersion 2:")
    snippet_d2()
    print(f"\nExplanation:{explain_difference_d()}")

    print("\n=== Difference E: Element vs Sublist ===")
    print("Version 1:")
    snippet_e1()
    print("\nVersion 2:")
    snippet_e2()
    print(f"\nExplanation:{explain_difference_e()}")

    print("\n=== Difference F: sort vs sorted ===")
    print("Version 1:")
    snippet_f1()
    print("\nVersion 2:")
    snippet_f2()
    print(f"\nExplanation:{explain_difference_f()}")


main()
