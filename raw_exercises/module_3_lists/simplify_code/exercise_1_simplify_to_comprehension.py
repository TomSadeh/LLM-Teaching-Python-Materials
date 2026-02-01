# Exercise 1: Simplify This - List Comprehensions
#
# Each piece of code works but is more complex than needed.
# Rewrite each one using list comprehensions.
#
# Theme: Processing magical data for {{school}}


# ============================================================
# SIMPLIFY A: Basic Transformation
# ============================================================

def original_a(names):
    """ORIGINAL: Manually building a list with a loop"""
    result = []
    for name in names:
        result.append(name.upper())
    return result


def simplified_a(names):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Use a list comprehension [expression for item in list]

    pass


# ============================================================
# SIMPLIFY B: With Filtering
# ============================================================

def original_b(spells, min_power):
    """ORIGINAL: Loop with condition"""
    powerful_spells = []
    for spell in spells:
        if spell["power"] >= min_power:
            powerful_spells.append(spell["name"])
    return powerful_spells


def simplified_b(spells, min_power):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: [expression for item in list if condition]

    pass


# ============================================================
# SIMPLIFY C: String to List
# ============================================================

def original_c(text):
    """ORIGINAL: Extract characters that are letters"""
    letters = []
    for char in text:
        if char.isalpha():
            letters.append(char)
    return letters


def simplified_c(text):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: You can iterate over a string just like a list

    pass


# ============================================================
# SIMPLIFY D: Numbers in Range
# ============================================================

def original_d(n):
    """ORIGINAL: Generate squares of numbers 1 to n"""
    squares = []
    for i in range(1, n + 1):
        squares.append(i * i)
    return squares


def simplified_d(n):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: range() works inside comprehensions too

    pass


# ============================================================
# SIMPLIFY E: Multiple Transformations
# ============================================================

def original_e(items):
    """ORIGINAL: Strip whitespace AND convert to title case"""
    cleaned = []
    for item in items:
        stripped = item.strip()
        titled = stripped.title()
        cleaned.append(titled)
    return cleaned


def simplified_e(items):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: You can chain method calls: item.strip().title()

    pass


# ============================================================
# SIMPLIFY F: Filter Empty and Transform
# ============================================================

def original_f(words):
    """ORIGINAL: Skip empty strings, uppercase the rest"""
    result = []
    for word in words:
        if word:  # Skip empty strings
            result.append(word.upper())
    return result


def simplified_f(words):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Combine transformation and filtering

    pass


# ============================================================
# SIMPLIFY G: Nested Data Access
# ============================================================

def original_g(characters):
    """ORIGINAL: Extract names from list of dictionaries"""
    names = []
    for character in characters:
        names.append(character["name"])
    return names


def simplified_g(characters):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Access dictionary keys in the comprehension

    pass


# ============================================================
# SIMPLIFY H: Conditional Value
# ============================================================

def original_h(numbers):
    """ORIGINAL: Replace negatives with zero"""
    result = []
    for num in numbers:
        if num < 0:
            result.append(0)
        else:
            result.append(num)
    return result


def simplified_h(numbers):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Use conditional expression: (value_if_true if condition else value_if_false)
    # This is different from filtering!

    pass


def main():
    # Test data
    names = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    spells = [
        {"name": "{{spell1}}", "power": 10},
        {"name": "{{spell2}}", "power": 50},
        {"name": "{{spell3}}", "power": 30},
    ]
    text = "{{hero}} casts {{spell1}}!"
    items = ["  {{hero}}  ", "  {{friend}}  ", "  {{pet}}  "]
    words = ["{{spell1}}", "", "{{spell2}}", "", "{{spell3}}"]
    characters = [
        {"name": "{{hero}}", "house": "{{house}}"},
        {"name": "{{heroine}}", "house": "{{house}}"},
    ]
    numbers = [5, -3, 10, -8, 2]

    print("=== Test A: Basic Transformation ===")
    print(f"Original: {original_a(names)}")
    print(f"Simplified: {simplified_a(names)}")

    print("\n=== Test B: With Filtering ===")
    print(f"Original: {original_b(spells, 25)}")
    print(f"Simplified: {simplified_b(spells, 25)}")

    print("\n=== Test C: String to List ===")
    print(f"Original: {original_c(text)}")
    print(f"Simplified: {simplified_c(text)}")

    print("\n=== Test D: Numbers in Range ===")
    print(f"Original: {original_d(5)}")
    print(f"Simplified: {simplified_d(5)}")

    print("\n=== Test E: Multiple Transformations ===")
    print(f"Original: {original_e(items)}")
    print(f"Simplified: {simplified_e(items)}")

    print("\n=== Test F: Filter Empty and Transform ===")
    print(f"Original: {original_f(words)}")
    print(f"Simplified: {simplified_f(words)}")

    print("\n=== Test G: Nested Data Access ===")
    print(f"Original: {original_g(characters)}")
    print(f"Simplified: {simplified_g(characters)}")

    print("\n=== Test H: Conditional Value ===")
    print(f"Original: {original_h(numbers)}")
    print(f"Simplified: {simplified_h(numbers)}")


main()
