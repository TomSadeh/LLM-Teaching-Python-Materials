# Exercise 1: Spot the Difference - Variable Typos
#
# Each pair of code snippets looks almost identical but behaves differently.
# Your task: Identify the difference and explain how it changes the behavior.
#
# Theme: Magical mix-ups with {{hero}} and {{heroine}}


# ============================================================
# SPOT DIFFERENCE A: Case Sensitivity
# ============================================================

def snippet_a1():
    """Version 1"""
    hero = "{{hero}}"
    print(f"Welcome, {hero}!")


def snippet_a2():
    """Version 2 - spot the difference!"""
    Hero = "{{hero}}"
    print(f"Welcome, {hero}!")


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
# SPOT DIFFERENCE B: Assignment vs Comparison
# ============================================================

def snippet_b1():
    """Version 1"""
    spell_count = 5
    spell_count = spell_count + 1
    print(f"Spells learned: {spell_count}")


def snippet_b2():
    """Version 2 - spot the difference!"""
    spell_count = 5
    spell_count == spell_count + 1
    print(f"Spells learned: {spell_count}")


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
# SPOT DIFFERENCE C: String Quote Types
# ============================================================

def snippet_c1():
    """Version 1"""
    message = "{{hero}} said: 'Hello!'"
    print(message)


def snippet_c2():
    """Version 2 - spot the difference!"""
    message = '{{hero}} said: 'Hello!''
    print(message)


def explain_difference_c():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    # Hint: This one causes a syntax error in Version 2!

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
# SPOT DIFFERENCE D: Plus vs Comma in Print
# ============================================================

def snippet_d1():
    """Version 1"""
    name = "{{hero}}"
    age = 11
    print("Name: " + name + ", Age: " + str(age))


def snippet_d2():
    """Version 2 - spot the difference!"""
    name = "{{hero}}"
    age = 11
    print("Name:", name, ", Age:", age)


def explain_difference_d():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    # Both work, but the output looks different!

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
# SPOT DIFFERENCE E: Integer vs String
# ============================================================

def snippet_e1():
    """Version 1"""
    year = 2023
    next_year = year + 1
    print(f"Next year: {next_year}")


def snippet_e2():
    """Version 2 - spot the difference!"""
    year = "2023"
    next_year = year + 1
    print(f"Next year: {next_year}")


def explain_difference_e():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    # Hint: One of these will crash!

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
    print("=== Difference A: Case Sensitivity ===")
    print("Version 1:")
    snippet_a1()
    print("\nVersion 2:")
    # snippet_a2()  # This will cause an error - that's the point!
    print("(Uncomment to see the error)")
    print(f"\nExplanation:{explain_difference_a()}")

    print("\n=== Difference B: Assignment vs Comparison ===")
    print("Version 1:")
    snippet_b1()
    print("\nVersion 2:")
    snippet_b2()
    print(f"\nExplanation:{explain_difference_b()}")

    print("\n=== Difference D: Plus vs Comma in Print ===")
    print("Version 1:")
    snippet_d1()
    print("\nVersion 2:")
    snippet_d2()
    print(f"\nExplanation:{explain_difference_d()}")

    print("\n=== Difference E: Integer vs String ===")
    print("Version 1:")
    snippet_e1()
    print("\nVersion 2:")
    # snippet_e2()  # This will cause an error!
    print("(Uncomment to see the error)")
    print(f"\nExplanation:{explain_difference_e()}")


main()
