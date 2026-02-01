# Exercise 1: Spot the Difference - Return vs Print
#
# Each pair of code snippets looks almost identical but behaves differently.
# Your task: Identify the difference and explain how it changes the behavior.
#
# Theme: Magical function spells for {{hero}}


# ============================================================
# SPOT DIFFERENCE A: Return vs Print
# ============================================================

def snippet_a1():
    """Version 1"""
    def create_spell(name):
        return f"*{name}*"

    spell = create_spell("{{spell1}}")
    print(f"Casting: {spell}")


def snippet_a2():
    """Version 2 - spot the difference!"""
    def create_spell(name):
        print(f"*{name}*")

    spell = create_spell("{{spell1}}")
    print(f"Casting: {spell}")


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
# SPOT DIFFERENCE B: Missing Return (Implicit None)
# ============================================================

def snippet_b1():
    """Version 1"""
    def calculate_power(level):
        result = level * 10
        return result

    power = calculate_power(5)
    total = power + 100
    print(f"Total power: {total}")


def snippet_b2():
    """Version 2 - spot the difference!"""
    def calculate_power(level):
        result = level * 10

    power = calculate_power(5)
    total = power + 100
    print(f"Total power: {total}")


def explain_difference_b():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    # Hint: What does a function return if there's no return statement?

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
# SPOT DIFFERENCE C: Return in Loop
# ============================================================

def snippet_c1():
    """Version 1"""
    def find_hero(team, target):
        for member in team:
            if member == target:
                return True
        return False

    team = ["{{hero}}", "{{friend}}", "{{heroine}}"]
    print(find_hero(team, "{{hero}}"))
    print(find_hero(team, "{{villain}}"))


def snippet_c2():
    """Version 2 - spot the difference!"""
    def find_hero(team, target):
        for member in team:
            if member == target:
                return True
            return False

    team = ["{{hero}}", "{{friend}}", "{{heroine}}"]
    print(find_hero(team, "{{hero}}"))
    print(find_hero(team, "{{villain}}"))


def explain_difference_c():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    # Hint: Look carefully at the indentation of return False

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
# SPOT DIFFERENCE D: Return Stops Execution
# ============================================================

def snippet_d1():
    """Version 1"""
    def greet_hero(name):
        greeting = f"Hello, {name}!"
        print("Creating greeting...")
        return greeting
        print("Greeting created!")

    result = greet_hero("{{hero}}")
    print(result)


def snippet_d2():
    """Version 2 - spot the difference!"""
    def greet_hero(name):
        greeting = f"Hello, {name}!"
        print("Creating greeting...")
        print("Greeting created!")
        return greeting

    result = greet_hero("{{hero}}")
    print(result)


def explain_difference_d():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    # Hint: Code after return never runs!

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
# SPOT DIFFERENCE E: Modifying vs Returning
# ============================================================

def snippet_e1():
    """Version 1"""
    def add_spell(spellbook, spell):
        spellbook.append(spell)
        return spellbook

    my_spells = ["{{spell1}}"]
    result = add_spell(my_spells, "{{spell2}}")
    print(f"Result: {result}")
    print(f"Original: {my_spells}")


def snippet_e2():
    """Version 2 - spot the difference!"""
    def add_spell(spellbook, spell):
        new_book = spellbook + [spell]
        return new_book

    my_spells = ["{{spell1}}"]
    result = add_spell(my_spells, "{{spell2}}")
    print(f"Result: {result}")
    print(f"Original: {my_spells}")


def explain_difference_e():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    # Hint: One modifies the original list, one creates a new list

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
# SPOT DIFFERENCE F: Default Parameter Trap
# ============================================================

def snippet_f1():
    """Version 1"""
    def add_to_team(member, team=None):
        if team is None:
            team = []
        team.append(member)
        return team

    print(add_to_team("{{hero}}"))
    print(add_to_team("{{friend}}"))


def snippet_f2():
    """Version 2 - spot the difference!"""
    def add_to_team(member, team=[]):
        team.append(member)
        return team

    print(add_to_team("{{hero}}"))
    print(add_to_team("{{friend}}"))


def explain_difference_f():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    # This is a famous Python gotcha!

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
    print("=== Difference A: Return vs Print ===")
    print("Version 1:")
    snippet_a1()
    print("\nVersion 2:")
    snippet_a2()
    print(f"\nExplanation:{explain_difference_a()}")

    print("\n=== Difference B: Missing Return ===")
    print("Version 1:")
    snippet_b1()
    print("\nVersion 2:")
    # snippet_b2()  # This crashes - uncomment to see!
    print("(Uncomment to see the TypeError)")
    print(f"\nExplanation:{explain_difference_b()}")

    print("\n=== Difference C: Return in Loop ===")
    print("Version 1:")
    snippet_c1()
    print("\nVersion 2:")
    snippet_c2()
    print(f"\nExplanation:{explain_difference_c()}")

    print("\n=== Difference D: Return Stops Execution ===")
    print("Version 1:")
    snippet_d1()
    print("\nVersion 2:")
    snippet_d2()
    print(f"\nExplanation:{explain_difference_d()}")

    print("\n=== Difference E: Modifying vs Returning ===")
    print("Version 1:")
    snippet_e1()
    print("\nVersion 2:")
    snippet_e2()
    print(f"\nExplanation:{explain_difference_e()}")

    print("\n=== Difference F: Default Parameter Trap ===")
    print("Version 1:")
    snippet_f1()
    print("\nVersion 2:")
    snippet_f2()
    print(f"\nExplanation:{explain_difference_f()}")


main()
