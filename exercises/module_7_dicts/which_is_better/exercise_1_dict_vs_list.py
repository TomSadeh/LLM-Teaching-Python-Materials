"""
{{CONTEXT_COMPARISON_INTRO}}
{{CONTEXT_COMPARISON_DECISION}}

Compare dictionary-based and list-based approaches to solve
the same problem. When should you use each data structure?
"""


# ============================================================
# Comparison 1: Looking Up Data
# ============================================================
# {{CONTEXT_APPROACH_1_NARRATIVE}}
#
# We need to look up a character's score by their name.


# --- {{APPROACH_1_NAME}}: List of Tuples ---

def lookup_with_list(data, target_name):
    """
    Version 1: Store data as a list of (name, score) tuples.
    Search through the list to find the target.
    """
    # Data stored as list of tuples
    # data = [("{{hero}}", 100), ("{{heroine}}", 150), ("{{friend}}", 75)]

    for name, score in data:
        if name == target_name:
            return score
    return None  # Not found


# --- {{APPROACH_2_NAME}}: Dictionary ---

def lookup_with_dict(data, target_name):
    """
    Version 2: Store data as a dictionary.
    Direct access by key.
    """
    # Data stored as dictionary
    # data = {"{{hero}}": 100, "{{heroine}}": 150, "{{friend}}": 75}

    return data.get(target_name, None)


def analysis_1():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # {{CONTEXT_ANALYSIS_PROMPT}}
    # Consider: {{CONTEXT_DECISION_GUIDANCE}}

    analysis = """
    Which is better for lookups?

    List approach:
    - Pros:
    - Cons:

    Dictionary approach:
    - Pros:
    - Cons:

    Better choice: ??? (explain why)
    """
    return analysis


# ============================================================
# Comparison 2: Counting Occurrences
# ============================================================
# {{CONTEXT_APPROACH_2_NARRATIVE}}
#
# Count how many times each item appears in a collection.

items_found = ["{{item}}", "{{spell1}}", "{{item}}", "{{spell1}}", "{{item}}"]


# --- Approach A: Using a List ---

def count_with_list(items):
    """
    Version 1: Use a list of [item, count] pairs.
    Must search list each time to update count.
    """
    counts = []  # Will be like [["{{item}}", 3], ["{{spell1}}", 2]]

    for item in items:
        found = False
        for pair in counts:
            if pair[0] == item:
                pair[1] = pair[1] + 1
                found = True
                break
        if not found:
            counts.append([item, 1])

    return counts


# --- Approach B: Using a Dictionary ---

def count_with_dict(items):
    """
    Version 2: Use a dictionary mapping item to count.
    Direct access and update.
    """
    counts = {}

    for item in items:
        counts[item] = counts.get(item, 0) + 1

    return counts


def analysis_2():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Compare the two counting approaches.

    analysis = """
    Which is better for counting?

    List approach:
    - Lines of code:
    - Easy to understand?
    - Efficient?

    Dictionary approach:
    - Lines of code:
    - Easy to understand?
    - Efficient?

    Better choice: ??? (explain why)
    """
    return analysis


# ============================================================
# Comparison 3: Storing Character Data
# ============================================================
# {{CONTEXT_APPROACH_3_NARRATIVE}}
#
# Store multiple attributes for each character.


# --- Approach A: Parallel Lists ---

def parallel_lists_approach():
    """
    Version 1: Use separate lists for each attribute.
    Index i in all lists refers to the same character.
    """
    names = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    levels = [5, 7, 3]
    health = [100, 120, 80]

    # To get {{hero}}'s data:
    hero_index = names.index("{{hero}}")
    hero_level = levels[hero_index]
    hero_health = health[hero_index]

    return f"{{{{hero}}}}: level {hero_level}, health {hero_health}"


# --- Approach B: Dictionary of Dictionaries ---

def dict_of_dicts_approach():
    """
    Version 2: Use nested dictionaries.
    Each character name maps to their attributes.
    """
    characters = {
        "{{hero}}": {"level": 5, "health": 100},
        "{{heroine}}": {"level": 7, "health": 120},
        "{{friend}}": {"level": 3, "health": 80}
    }

    # To get {{hero}}'s data:
    hero_data = characters["{{hero}}"]
    hero_level = hero_data["level"]
    hero_health = hero_data["health"]

    return f"{{{{hero}}}}: level {hero_level}, health {hero_health}"


def analysis_3():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Compare the two data organization approaches.

    analysis = """
    Which is better for storing character data?

    Parallel lists:
    - Easy to add a new character?
    - Easy to add a new attribute?
    - Can the lists get out of sync?

    Dictionary of dictionaries:
    - Easy to add a new character?
    - Easy to add a new attribute?
    - Data stays together?

    Better choice: ??? (explain why)

    When might parallel lists actually be better?
    -
    """
    return analysis


# ============================================================
# Summary: When to Use Each
# ============================================================

def final_summary():
    # ✏️ WRITE YOUR SUMMARY ✏️

    summary = """
    USE A LIST WHEN:
    -
    -
    -

    USE A DICTIONARY WHEN:
    -
    -
    -
    """
    return summary


def main():
    print("{{CONTEXT_COMPARISON_INTRO}}")
    print("=" * 50)

    print("\n=== Comparison 1: Lookups ===")
    list_data = [("{{hero}}", 100), ("{{heroine}}", 150)]
    dict_data = {"{{hero}}": 100, "{{heroine}}": 150}
    print(f"List lookup: {lookup_with_list(list_data, '{{hero}}')}")
    print(f"Dict lookup: {lookup_with_dict(dict_data, '{{hero}}')}")
    print(f"\nYour analysis:{analysis_1()}")

    print("\n=== Comparison 2: Counting ===")
    print(f"List count: {count_with_list(items_found)}")
    print(f"Dict count: {count_with_dict(items_found)}")
    print(f"\nYour analysis:{analysis_2()}")

    print("\n=== Comparison 3: Character Data ===")
    print(f"Parallel lists: {parallel_lists_approach()}")
    print(f"Dict of dicts: {dict_of_dicts_approach()}")
    print(f"\nYour analysis:{analysis_3()}")

    print("\n=== Your Summary ===")
    print(final_summary())

    print("\n" + "=" * 50)
    print("{{CONTEXT_EVALUATION_COMPLETE}}")


main()
