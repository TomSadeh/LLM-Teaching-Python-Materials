"""
{{CONTEXT_EVALUATION_INTRO}}

This is a multi-part exercise comparing list-based and dictionary-based
approaches to data lookup. Evaluate, implement, and reflect.

Programming concepts: dictionaries vs lists, lookup performance, data design
"""


# ============================================================
# PART 1: Evaluation - Compare Existing Approaches
# ============================================================
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Two approaches exist for looking up character data.
# Study them and decide which is better.


# --- Approach A: List Search ---

def lookup_list(roster_list, target_name):
    """
    Search through a list of character tuples.
    roster_list = [("name", level, status), ...]
    """
    for name, level, status in roster_list:
        if name == target_name:
            return {"name": name, "level": level, "status": status}
    return None


# --- Approach B: Dictionary Lookup ---

def lookup_dict(roster_dict, target_name):
    """
    Direct dictionary access.
    roster_dict = {"name": {"level": N, "status": "..."}, ...}
    """
    if target_name in roster_dict:
        data = roster_dict[target_name]
        return {"name": target_name, "level": data["level"], "status": data["status"]}
    return None


def analysis_part_1():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Compare the two approaches:

    analysis = """
    LIST APPROACH:
    - How does it find the target? (describe the process)
    - What if the list has 1000 entries?
    - What if the target is at the end?

    DICTIONARY APPROACH:
    - How does it find the target?
    - What if the dict has 1000 entries?
    - Is position in dict relevant?

    BETTER FOR LOOKUPS: ??? (explain)

    WHEN MIGHT LISTS BE PREFERRED?
    -
    """
    return analysis


# ============================================================
# PART 2: Growth - Implement the Dictionary Approach
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Build a complete character lookup system using dictionaries.


def create_roster():
    """
    Create a roster dictionary with character data.

    Returns:
        dict: Mapping character names to their data dictionaries.
              Each character should have 'level' and 'status' keys.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a roster with at least 4 characters.
    # Structure:
    # {
    #     "{{hero}}": {"level": 5, "status": "active"},
    #     "{{heroine}}": {"level": 7, "status": "active"},
    #     ...
    # }

    pass


def find_character(roster, name):
    """
    Look up a character by name.

    Args:
        roster: The roster dictionary
        name: Character name to find

    Returns:
        dict or None: Character data if found, None otherwise
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use .get() for safe access.
    # Return the character's data dict, or None if not found.

    pass


def find_by_status(roster, target_status):
    """
    Find all characters with a specific status.

    Args:
        roster: The roster dictionary
        target_status: Status to search for

    Returns:
        list: Names of characters with that status
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Iterate through roster.items()
    # Collect names where status matches.

    pass


def find_highest_level(roster):
    """
    Find the character with the highest level.

    Args:
        roster: The roster dictionary

    Returns:
        str: Name of the highest level character
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Iterate through roster.items()
    # Track the highest level seen and who has it.

    pass


# ============================================================
# PART 3: Evaluation - Reflect on Trade-offs
# ============================================================
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Now that you've implemented it, reflect on the design choices.


def analysis_part_3():
    # ✏️ YOUR REFLECTION ✏️

    reflection = """
    AFTER IMPLEMENTING:

    1. Was the dictionary approach easy to code?
       -

    2. How would you add a new character to each approach?
       List:
       Dict:

    3. How would you remove a character?
       List:
       Dict:

    4. What if you need to iterate in a specific ORDER?
       List:
       Dict:

    5. What if you need to allow DUPLICATE names?
       List:
       Dict:

    FINAL VERDICT:
    For a character roster, I would choose ___ because:
    -
    """
    return reflection


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_EVALUATION_INTRO}}")
    print("=" * 60)
    print()

    # Sample data for testing
    roster_list = [
        ("{{hero}}", 5, "active"),
        ("{{heroine}}", 7, "active"),
        ("{{friend}}", 3, "training"),
        ("{{mentor}}", 10, "retired")
    ]

    roster_dict = {
        "{{hero}}": {"level": 5, "status": "active"},
        "{{heroine}}": {"level": 7, "status": "active"},
        "{{friend}}": {"level": 3, "status": "training"},
        "{{mentor}}": {"level": 10, "status": "retired"}
    }

    print(">>> PART 1: Compare approaches...")
    print()
    print("List approach result:", lookup_list(roster_list, "{{hero}}"))
    print("Dict approach result:", lookup_dict(roster_dict, "{{hero}}"))
    print()
    print("Your analysis:")
    print(analysis_part_1())

    print()
    print(">>> PART 2: Implement dictionary system...")
    print("(Implement create_roster, find_character, find_by_status, find_highest_level)")
    print()
    # Uncomment after implementing:
    # roster = create_roster()
    # print(f"Roster: {roster}")
    # print(f"Find {{{{hero}}}}: {find_character(roster, '{{hero}}')}")
    # print(f"Active characters: {find_by_status(roster, 'active')}")
    # print(f"Highest level: {find_highest_level(roster)}")

    print()
    print(">>> PART 3: Reflect on trade-offs...")
    print()
    print("Your reflection:")
    print(analysis_part_3())

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
