# Exercise 1: Which is Better? - Loop vs Comprehension
#
# For each pair of solutions, both work correctly.
# Your job: Analyze and explain which is better AND WHY.
# Sometimes the answer is "it depends"!
#
# Theme: Processing magical data for {{school}}


# ============================================================
# COMPARISON A: Simple Transformation
# ============================================================

def version_a1(names):
    """Version 1: For loop with append"""
    uppercase_names = []
    for name in names:
        uppercase_names.append(name.upper())
    return uppercase_names


def version_a2(names):
    """Version 2: List comprehension"""
    return [name.upper() for name in names]


def analysis_a():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: A1 or A2?
    # Consider: readability, length, performance, beginner-friendliness

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version A1 (for loop):
    -

    When to use version A2 (comprehension):
    -
    """
    return analysis


# ============================================================
# COMPARISON B: Filtering
# ============================================================

def version_b1(spells, min_power):
    """Version 1: For loop with condition"""
    powerful_spells = []
    for spell in spells:
        if spell["power"] >= min_power:
            powerful_spells.append(spell["name"])
    return powerful_spells


def version_b2(spells, min_power):
    """Version 2: List comprehension with condition"""
    return [spell["name"] for spell in spells if spell["power"] >= min_power]


def analysis_b():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: B1 or B2?
    # Consider: complex conditions, debugging, readability

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version B1 (for loop):
    -

    When to use version B2 (comprehension):
    -
    """
    return analysis


# ============================================================
# COMPARISON C: With Side Effects
# ============================================================

def version_c1(items):
    """Version 1: For loop with multiple operations"""
    processed = []
    for item in items:
        cleaned = item.strip()
        if cleaned:  # Skip empty strings
            print(f"Processing: {cleaned}")  # Side effect: logging
            processed.append(cleaned.title())
    return processed


def version_c2(items):
    """Version 2: Comprehension attempt"""
    # Note: This doesn't include the print statement!
    return [item.strip().title() for item in items if item.strip()]


def analysis_c():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: C1 or C2?
    # Consider: side effects, maintainability, equivalence

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version C1 (for loop):
    -

    When to use version C2 (comprehension):
    -
    """
    return analysis


# ============================================================
# COMPARISON D: Building a Dictionary
# ============================================================

def version_d1(heroes):
    """Version 1: For loop"""
    hero_lengths = {}
    for hero in heroes:
        hero_lengths[hero] = len(hero)
    return hero_lengths


def version_d2(heroes):
    """Version 2: Dictionary comprehension"""
    return {hero: len(hero) for hero in heroes}


def analysis_d():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: D1 or D2?
    # Consider: when to learn dict comprehensions

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version D1 (for loop):
    -

    When to use version D2 (dict comprehension):
    -
    """
    return analysis


# ============================================================
# COMPARISON E: Nested Loops
# ============================================================

def version_e1(matrix):
    """Version 1: Nested for loops"""
    flattened = []
    for row in matrix:
        for item in row:
            flattened.append(item)
    return flattened


def version_e2(matrix):
    """Version 2: Nested comprehension"""
    return [item for row in matrix for item in row]


def analysis_e():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: E1 or E2?
    # Consider: readability of nested comprehensions

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version E1 (nested loops):
    -

    When to use version E2 (nested comprehension):
    -
    """
    return analysis


def main():
    # Test data
    names = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    spells = [
        {"name": "{{spell1}}", "power": 10},
        {"name": "{{spell2}}", "power": 50},
        {"name": "{{spell3}}", "power": 30},
    ]
    items = ["  {{item}}  ", "", "  {{pet}}  ", "  "]
    matrix = [["A", "B"], ["C", "D"], ["E", "F"]]

    print("=== Comparison A: Simple Transformation ===")
    print(f"Version 1: {version_a1(names)}")
    print(f"Version 2: {version_a2(names)}")
    print(f"\nAnalysis:{analysis_a()}")

    print("\n=== Comparison B: Filtering ===")
    print(f"Version 1: {version_b1(spells, 25)}")
    print(f"Version 2: {version_b2(spells, 25)}")
    print(f"\nAnalysis:{analysis_b()}")

    print("\n=== Comparison C: With Side Effects ===")
    print("Version 1:")
    result1 = version_c1(items)
    print(f"Result: {result1}")
    print("\nVersion 2:")
    result2 = version_c2(items)
    print(f"Result: {result2}")
    print(f"\nAnalysis:{analysis_c()}")

    print("\n=== Comparison D: Building a Dictionary ===")
    print(f"Version 1: {version_d1(names)}")
    print(f"Version 2: {version_d2(names)}")
    print(f"\nAnalysis:{analysis_d()}")

    print("\n=== Comparison E: Nested Loops ===")
    print(f"Version 1: {version_e1(matrix)}")
    print(f"Version 2: {version_e2(matrix)}")
    print(f"\nAnalysis:{analysis_e()}")


main()
