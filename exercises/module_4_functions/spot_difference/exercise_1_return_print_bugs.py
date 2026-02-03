# =============================================================================
# Spot the Difference: Return vs Print Bugs
# =============================================================================
# Difficulty: 3
# Concepts: return vs print, understanding function output, None type
# =============================================================================

"""
{{CONTEXT_SPOT_DIFFERENCE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# Comparison 1: Basic Return vs Print
# ============================================================
# {{CONTEXT_COMPARISON_1_NARRATIVE}}
#
# These two functions look similar. Find the critical difference.

def version_a1():
    """Version 1"""
    def get_hero():
        return "{{hero}}"

    name = get_hero()
    print(f"Our hero is: {name}")


def version_a2():
    """Version 2 - spot the difference!"""
    def get_hero():
        print("{{hero}}")

    name = get_hero()
    print(f"Our hero is: {name}")


def explain_difference_a():
    # EXPLAIN THE DIFFERENCE
    #
    # Hint: What value does each function give back?

    explanation = """
    The difference is:
    - Version 1 uses 'return' to give back the value
    - Version 2 uses 'print' which only displays but returns None

    Version 1 behavior:
    - get_hero() returns "{{hero}}"
    - name stores "{{hero}}"
    - Correctly prints: "Our hero is: {{hero}}"

    Version 2 behavior:
    - get_hero() prints "{{hero}}" but returns None
    - name stores None
    - Incorrectly prints: "Our hero is: None"

    Why this matters:
    - print() is for displaying to users
    - return is for giving values back to your code
    """
    return explanation


# ============================================================
# Comparison 2: Using Result in Calculation
# ============================================================
# {{CONTEXT_COMPARISON_2_NARRATIVE}}

def version_b1():
    """Version 1"""
    def calculate_score(base):
        return base * 2

    score = calculate_score(50)
    final = score + 10
    print(f"Final score: {final}")


def version_b2():
    """Version 2 - spot the difference!"""
    def calculate_score(base):
        print(base * 2)

    score = calculate_score(50)
    final = score + 10  # This will crash!
    print(f"Final score: {final}")


def explain_difference_b():
    # EXPLAIN THE DIFFERENCE

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
# Comparison 3: String Building
# ============================================================
# {{CONTEXT_COMPARISON_3_NARRATIVE}}

def version_c1():
    """Version 1"""
    def format_name(first, last):
        return f"{first} {last}"

    full_name = format_name("{{hero}}", "Champion")
    greeting = f"Welcome, {full_name}!"
    print(greeting)


def version_c2():
    """Version 2 - spot the difference!"""
    def format_name(first, last):
        print(f"{first} {last}")

    full_name = format_name("{{hero}}", "Champion")
    greeting = f"Welcome, {full_name}!"  # full_name is None!
    print(greeting)


def explain_difference_c():
    # EXPLAIN THE DIFFERENCE

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
# Comparison 4: Conditional Return
# ============================================================
# {{CONTEXT_COMPARISON_4_NARRATIVE}}

def version_d1():
    """Version 1"""
    def get_status(level):
        if level >= 10:
            return "Expert"
        return "Novice"

    status = get_status(15)
    print(f"Status: {status}")


def version_d2():
    """Version 2 - spot the difference!"""
    def get_status(level):
        if level >= 10:
            print("Expert")
        print("Novice")

    status = get_status(15)
    print(f"Status: {status}")


def explain_difference_d():
    # EXPLAIN THE DIFFERENCE

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
# Comparison 5: Function Chaining
# ============================================================
# {{CONTEXT_COMPARISON_5_NARRATIVE}}

def version_e1():
    """Version 1"""
    def double(n):
        return n * 2

    def add_five(n):
        return n + 5

    result = add_five(double(10))
    print(f"Result: {result}")


def version_e2():
    """Version 2 - spot the difference!"""
    def double(n):
        print(n * 2)

    def add_five(n):
        return n + 5

    result = add_five(double(10))  # double returns None!
    print(f"Result: {result}")


def explain_difference_e():
    # EXPLAIN THE DIFFERENCE

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
    print("{{CONTEXT_SPOT_DIFFERENCE_INTRO}}")
    print("=" * 50)
    print("\nThis is the #1 beginner mistake in Python!")
    print("Compare each pair carefully.\n")

    print("=== Comparison 1: Basic Return vs Print ===")
    print("\nVersion 1:")
    version_a1()
    print("\nVersion 2:")
    version_a2()
    print(f"\nExplanation:{explain_difference_a()}")

    print("\n=== Comparison 2: Using Result ===")
    print("\nVersion 1:")
    version_b1()
    print("\nVersion 2:")
    print("(Would crash if run)")
    # version_b2()  # Don't run - will crash
    print(f"\nExplanation:{explain_difference_b()}")

    print("\n=== Comparison 3: String Building ===")
    print("\nVersion 1:")
    version_c1()
    print("\nVersion 2:")
    version_c2()
    print(f"\nExplanation:{explain_difference_c()}")

    print("\n=== Comparison 4: Conditional ===")
    print("\nVersion 1:")
    version_d1()
    print("\nVersion 2:")
    version_d2()
    print(f"\nExplanation:{explain_difference_d()}")

    print("\n=== Comparison 5: Chaining ===")
    print("\nVersion 1:")
    version_e1()
    print("\nVersion 2:")
    print("(Would crash if run)")
    # version_e2()  # Don't run - will crash
    print(f"\nExplanation:{explain_difference_e()}")

    print("=" * 50)
    print("\nREMEMBER:")
    print("- print() shows output to humans")
    print("- return gives data back to your code")
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()
