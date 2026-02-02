# Exercise 1: Which is Better? - Nested vs Flat Dictionaries
#
# For each pair of solutions, both work correctly.
# Your job: Analyze and explain which is better AND WHY.
# Sometimes the answer is "it depends"!
#
# Theme: Organizing data for {{school}}'s records system


# ============================================================
# COMPARISON A: Character Data
# ============================================================

# Version 1: Flat dictionary with prefixes
character_flat = {
    "name": "{{hero}}",
    "house": "{{house}}",
    "year": 3,
    "wand_wood": "Holly",
    "wand_core": "Phoenix",
    "wand_length": 11,
    "pet_name": "{{pet}}",
    "pet_type": "Owl"
}

# Version 2: Nested dictionary
character_nested = {
    "name": "{{hero}}",
    "house": "{{house}}",
    "year": 3,
    "wand": {
        "wood": "Holly",
        "core": "Phoenix",
        "length": 11
    },
    "pet": {
        "name": "{{pet}}",
        "type": "Owl"
    }
}


def version_a1_get_wand(char):
    """Get wand info from flat structure"""
    return f"{char['wand_wood']} with {char['wand_core']} core"


def version_a2_get_wand(char):
    """Get wand info from nested structure"""
    wand = char["wand"]
    return f"{wand['wood']} with {wand['core']} core"


def analysis_a():
    # ✏️ YOUR ANALYSIS ✏️
    # Which structure is better: flat or nested?
    # Consider: grouping related data, accessing fields, updating

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use flat structure:
    -

    When to use nested structure:
    -
    """
    return analysis


# ============================================================
# COMPARISON B: Accessing Deeply Nested Data
# ============================================================

# Version 1: Deeply nested
school_nested = {
    "school": {
        "name": "{{school}}",
        "houses": {
            "{{house}}": {
                "students": {
                    "{{hero}}": {
                        "year": 3,
                        "grades": {"potions": 85, "charms": 92}
                    }
                }
            }
        }
    }
}

# Version 2: Flatter with composite keys
school_flat = {
    "school_name": "{{school}}",
    "house_{{house}}_student_{{hero}}_year": 3,
    "house_{{house}}_student_{{hero}}_grade_potions": 85,
    "house_{{house}}_student_{{hero}}_grade_charms": 92
}


def version_b1_get_grade(data, house, student, subject):
    """Get grade from nested structure"""
    return data["school"]["houses"][house]["students"][student]["grades"][subject]


def version_b2_get_grade(data, house, student, subject):
    """Get grade from flat structure"""
    key = f"house_{house}_student_{student}_grade_{subject}"
    return data[key]


def analysis_b():
    # ✏️ YOUR ANALYSIS ✏️
    # Which approach handles deep data better?
    # Consider: readability, error handling, iteration

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use deep nesting:
    -

    When to use flat with composite keys:
    -
    """
    return analysis


# ============================================================
# COMPARISON C: Updating Data
# ============================================================

def version_c1_update_flat(char, field, value):
    """Update a field in flat structure"""
    char[field] = value
    return char


def version_c2_update_nested(char, category, field, value):
    """Update a field in nested structure"""
    if category:
        char[category][field] = value
    else:
        char[field] = value
    return char


def analysis_c():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is easier to update: flat or nested?
    # Consider: knowing the full path, error handling

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use flat updates:
    -

    When to use nested updates:
    -
    """
    return analysis


# ============================================================
# COMPARISON D: Iterating Over Related Data
# ============================================================

# Version 1: Flat with numbered keys
inventory_flat = {
    "item_1_name": "{{spell1}}",
    "item_1_quantity": 5,
    "item_2_name": "{{spell2}}",
    "item_2_quantity": 3,
    "item_3_name": "{{spell3}}",
    "item_3_quantity": 7
}

# Version 2: Nested list of dictionaries
inventory_nested = {
    "items": [
        {"name": "{{spell1}}", "quantity": 5},
        {"name": "{{spell2}}", "quantity": 3},
        {"name": "{{spell3}}", "quantity": 7}
    ]
}


def version_d1_list_items(inv):
    """List all items from flat structure"""
    items = []
    i = 1
    while f"item_{i}_name" in inv:
        items.append(f"{inv[f'item_{i}_name']}: {inv[f'item_{i}_quantity']}")
        i += 1
    return items


def version_d2_list_items(inv):
    """List all items from nested structure"""
    return [f"{item['name']}: {item['quantity']}" for item in inv["items"]]


def analysis_d():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is easier to iterate over?
    # Consider: adding items, removing items, looping

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use flat numbered keys:
    -

    When to use nested list:
    -
    """
    return analysis


# ============================================================
# COMPARISON E: JSON Compatibility
# ============================================================

import json


def version_e1_to_json(data):
    """Flat structure to JSON"""
    return json.dumps(data, indent=2)


def version_e2_to_json(data):
    """Nested structure to JSON"""
    return json.dumps(data, indent=2)


def analysis_e():
    # ✏️ YOUR ANALYSIS ✏️
    # Which works better with JSON APIs?
    # Consider: API design, parsing, human readability

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When flat works better with JSON:
    -

    When nested works better with JSON:
    -
    """
    return analysis


def main():
    print("=== Comparison A: Character Data ===")
    print(f"Flat: {version_a1_get_wand(character_flat)}")
    print(f"Nested: {version_a2_get_wand(character_nested)}")
    print(f"\nAnalysis:{analysis_a()}")

    print("\n=== Comparison B: Accessing Deeply Nested Data ===")
    print(f"Nested: {version_b1_get_grade(school_nested, '{{house}}', '{{hero}}', 'potions')}")
    print(f"Flat: {version_b2_get_grade(school_flat, '{{house}}', '{{hero}}', 'potions')}")
    print(f"\nAnalysis:{analysis_b()}")

    print("\n=== Comparison C: Updating Data ===")
    flat_copy = character_flat.copy()
    nested_copy = {k: v.copy() if isinstance(v, dict) else v for k, v in character_nested.items()}
    version_c1_update_flat(flat_copy, "wand_length", 12)
    version_c2_update_nested(nested_copy, "wand", "length", 12)
    print(f"Updated flat: wand_length = {flat_copy['wand_length']}")
    print(f"Updated nested: wand.length = {nested_copy['wand']['length']}")
    print(f"\nAnalysis:{analysis_c()}")

    print("\n=== Comparison D: Iterating Over Related Data ===")
    print(f"Flat iteration: {version_d1_list_items(inventory_flat)}")
    print(f"Nested iteration: {version_d2_list_items(inventory_nested)}")
    print(f"\nAnalysis:{analysis_d()}")

    print("\n=== Comparison E: JSON Compatibility ===")
    print("Flat JSON:")
    print(version_e1_to_json(inventory_flat)[:100] + "...")
    print("\nNested JSON:")
    print(version_e2_to_json(inventory_nested)[:100] + "...")
    print(f"\nAnalysis:{analysis_e()}")


main()
