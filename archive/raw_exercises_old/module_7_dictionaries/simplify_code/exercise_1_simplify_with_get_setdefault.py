# Exercise 1: Simplify This - Dictionary Methods
#
# Each piece of code works but doesn't use Python's dictionary methods.
# Rewrite using .get(), .setdefault(), and dict comprehensions.
#
# Theme: Managing {{school}}'s student records


# ============================================================
# SIMPLIFY A: Checking Before Accessing
# ============================================================

def original_a(student, field):
    """ORIGINAL: Manual key checking"""
    if field in student:
        return student[field]
    else:
        return "Unknown"


def simplified_a(student, field):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: dict.get(key, default) returns default if key doesn't exist

    pass


# ============================================================
# SIMPLIFY B: Safe Nested Access
# ============================================================

def original_b(data, category, item):
    """ORIGINAL: Verbose nested access"""
    if category in data:
        if item in data[category]:
            return data[category][item]
        else:
            return 0
    else:
        return 0


def simplified_b(data, category, item):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Chain .get() calls, with {} as default for the first

    pass


# ============================================================
# SIMPLIFY C: Initialize if Missing
# ============================================================

def original_c(grades, student, subject, score):
    """ORIGINAL: Manual initialization pattern"""
    if student not in grades:
        grades[student] = {}
    if subject not in grades[student]:
        grades[student][subject] = []
    grades[student][subject].append(score)
    return grades


def simplified_c(grades, student, subject, score):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: dict.setdefault(key, default) returns existing value or sets default

    pass


# ============================================================
# SIMPLIFY D: Counting Items
# ============================================================

def original_d(items):
    """ORIGINAL: Manual counting"""
    counts = {}
    for item in items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts


def simplified_d(items):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Use .get() with default 0
    # Or even better: collections.Counter!

    pass


# ============================================================
# SIMPLIFY E: Grouping Items
# ============================================================

def original_e(students):
    """ORIGINAL: Manual grouping by house"""
    # students is a list of {"name": "...", "house": "..."}
    by_house = {}
    for student in students:
        house = student["house"]
        if house not in by_house:
            by_house[house] = []
        by_house[house].append(student["name"])
    return by_house


def simplified_e(students):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: setdefault is perfect for the "create list if missing" pattern

    pass


# ============================================================
# SIMPLIFY F: Merging Dictionaries
# ============================================================

def original_f(defaults, overrides):
    """ORIGINAL: Manual dictionary merging"""
    result = {}
    for key in defaults:
        result[key] = defaults[key]
    for key in overrides:
        result[key] = overrides[key]
    return result


def simplified_f(defaults, overrides):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Use the | operator (Python 3.9+) or {**dict1, **dict2}

    pass


# ============================================================
# SIMPLIFY G: Transforming Values
# ============================================================

def original_g(scores):
    """ORIGINAL: Loop to transform values"""
    # Double all scores
    result = {}
    for name, score in scores.items():
        result[name] = score * 2
    return result


def simplified_g(scores):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Dictionary comprehension {key: value for key, value in dict.items()}

    pass


# ============================================================
# SIMPLIFY H: Filtering Dictionary
# ============================================================

def original_h(students, min_score):
    """ORIGINAL: Loop to filter dictionary"""
    passing = {}
    for name, score in students.items():
        if score >= min_score:
            passing[name] = score
    return passing


def simplified_h(students, min_score):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Dictionary comprehension with condition

    pass


# ============================================================
# SIMPLIFY I: Inverting Dictionary
# ============================================================

def original_i(spell_to_type):
    """ORIGINAL: Swap keys and values"""
    type_to_spell = {}
    for spell, spell_type in spell_to_type.items():
        type_to_spell[spell_type] = spell
    return type_to_spell


def simplified_i(spell_to_type):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Dictionary comprehension with swapped key/value

    pass


# ============================================================
# SIMPLIFY J: Default Factory Pattern
# ============================================================

def original_j():
    """ORIGINAL: Creating dict with default values"""
    houses = ["{{house}}", "Slytherin", "Ravenclaw", "Hufflepuff"]
    house_points = {}
    for house in houses:
        house_points[house] = 0
    return house_points


def simplified_j():
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: dict.fromkeys(keys, default_value)

    pass


def main():
    # Test data
    student = {"name": "{{hero}}", "house": "{{house}}", "year": 3}
    nested_data = {
        "{{house}}": {"points": 500, "wins": 3},
        "Slytherin": {"points": 450, "wins": 2}
    }
    students_list = [
        {"name": "{{hero}}", "house": "{{house}}"},
        {"name": "{{heroine}}", "house": "{{house}}"},
        {"name": "{{friend}}", "house": "Ravenclaw"},
    ]
    defaults = {"theme": "light", "sound": True, "difficulty": "normal"}
    overrides = {"theme": "dark", "difficulty": "hard"}
    scores = {"{{hero}}": 85, "{{heroine}}": 92, "{{friend}}": 78}
    spell_types = {"{{spell1}}": "defense", "{{spell2}}": "charm", "{{spell3}}": "hex"}

    print("=== Test A: Safe Access ===")
    print(f"Original (name): {original_a(student, 'name')}")
    print(f"Original (pet): {original_a(student, 'pet')}")
    print(f"Simplified (name): {simplified_a(student, 'name')}")
    print(f"Simplified (pet): {simplified_a(student, 'pet')}")

    print("\n=== Test B: Nested Access ===")
    print(f"Original: {original_b(nested_data, '{{house}}', 'points')}")
    print(f"Simplified: {simplified_b(nested_data, '{{house}}', 'points')}")

    print("\n=== Test D: Counting ===")
    items = ["{{spell1}}", "{{spell2}}", "{{spell1}}", "{{spell3}}", "{{spell1}}"]
    print(f"Original: {original_d(items)}")
    print(f"Simplified: {simplified_d(items)}")

    print("\n=== Test E: Grouping ===")
    print(f"Original: {original_e(students_list)}")
    print(f"Simplified: {simplified_e(students_list)}")

    print("\n=== Test F: Merging ===")
    print(f"Original: {original_f(defaults, overrides)}")
    print(f"Simplified: {simplified_f(defaults, overrides)}")

    print("\n=== Test G: Transforming ===")
    print(f"Original: {original_g(scores)}")
    print(f"Simplified: {simplified_g(scores)}")

    print("\n=== Test H: Filtering ===")
    print(f"Original (>=80): {original_h(scores, 80)}")
    print(f"Simplified (>=80): {simplified_h(scores, 80)}")

    print("\n=== Test I: Inverting ===")
    print(f"Original: {original_i(spell_types)}")
    print(f"Simplified: {simplified_i(spell_types)}")

    print("\n=== Test J: Default Factory ===")
    print(f"Original: {original_j()}")
    print(f"Simplified: {simplified_j()}")


main()
