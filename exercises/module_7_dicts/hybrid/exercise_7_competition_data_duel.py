"""
{{CONTEXT_EVALUATION_INTRO}}

This is a multi-part exercise comparing different data structure approaches
for a character management system. Build, compare, and choose wisely!

Programming concepts: dictionaries, nested data, data design trade-offs
"""


# ============================================================
# PART 1: Evaluation - Compare Data Structures
# ============================================================
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Two approaches exist for storing character data.
# Which is better for different operations?


# --- Approach A: List of Dictionaries ---
characters_list = [
    {"name": "{{hero}}", "level": 5, "health": 100, "class": "warrior"},
    {"name": "{{heroine}}", "level": 7, "health": 120, "class": "mage"},
    {"name": "{{friend}}", "level": 3, "health": 80, "class": "rogue"}
]


def find_in_list(char_list, name):
    """Find a character by name in the list."""
    for char in char_list:
        if char["name"] == name:
            return char
    return None


# --- Approach B: Dictionary of Dictionaries ---
characters_dict = {
    "{{hero}}": {"level": 5, "health": 100, "class": "warrior"},
    "{{heroine}}": {"level": 7, "health": 120, "class": "mage"},
    "{{friend}}": {"level": 3, "health": 80, "class": "rogue"}
}


def find_in_dict(char_dict, name):
    """Find a character by name in the dictionary."""
    return char_dict.get(name)


def analysis_part_1():
    # ✏️ YOUR ANALYSIS ✏️

    analysis = """
    OPERATION: Find character by name

    List approach:
    - How many steps to find "{{friend}}"?
    - What if there are 1000 characters?

    Dict approach:
    - How many steps to find "{{friend}}"?
    - What if there are 1000 characters?

    Better for lookups: ___

    ---

    OPERATION: Get all characters

    List approach:
    - Easy to iterate?
    - Maintains insertion order?

    Dict approach:
    - Easy to iterate?
    - What do you iterate over? (keys, values, items?)

    Better for iteration: ___

    ---

    OPERATION: Add new character

    List approach:
    - How? (char_list.append({...}))
    - Need to check for duplicates manually?

    Dict approach:
    - How? (char_dict["name"] = {...})
    - Automatically prevents duplicates by name?

    Better for adding: ___
    """
    return analysis


# ============================================================
# PART 2: Growth - Build with Dictionary Approach
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Implement a complete character management system using dictionaries.


def create_character_db():
    """
    Create an empty character database.

    Returns:
        dict: Empty dictionary for storing characters
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def add_character(db, name, level, health, char_class):
    """
    Add a new character to the database.

    Args:
        db: The character database
        name: Character name (used as key)
        level: Starting level
        health: Starting health
        char_class: Character class (warrior, mage, etc.)

    Returns:
        bool: True if added, False if name already exists
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Check if name already exists.
    # If new, add with all attributes and return True.

    pass


def get_character(db, name):
    """
    Get a character's data.

    Args:
        db: The character database
        name: Character to look up

    Returns:
        dict or None: Character data, or None if not found
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def level_up(db, name):
    """
    Increase a character's level by 1 and health by 10.

    Args:
        db: The character database
        name: Character to level up

    Returns:
        bool: True if leveled up, False if character not found
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Check if character exists.
    # If found, increase level by 1 and health by 10.

    pass


def get_by_class(db, char_class):
    """
    Get all characters of a specific class.

    Args:
        db: The character database
        char_class: Class to filter by

    Returns:
        list: Names of characters with that class
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Iterate through db.items() and collect matching names.

    pass


# ============================================================
# PART 3: Growth - Add Advanced Operations
# ============================================================
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Implement more complex operations that benefit from the dict structure.


def get_highest_level(db):
    """
    Find the character with the highest level.

    Args:
        db: The character database

    Returns:
        str or None: Name of highest level character, None if empty
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Iterate and track the highest level seen.

    pass


def get_class_stats(db):
    """
    Get statistics for each character class.

    Args:
        db: The character database

    Returns:
        dict: Mapping class name to {"count": N, "avg_level": X}
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Count characters and sum levels by class
    # Step 2: Calculate averages
    #
    # Result format: {"warrior": {"count": 2, "avg_level": 6.0}, ...}

    pass


def transfer_health(db, from_name, to_name, amount):
    """
    Transfer health from one character to another.

    Args:
        db: The character database
        from_name: Character giving health
        to_name: Character receiving health
        amount: Health to transfer

    Returns:
        bool: True if successful, False if either character missing
              or source doesn't have enough health
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Check both characters exist.
    # Check source has enough health.
    # Transfer the health.

    pass


# ============================================================
# PART 4: Evaluation - Final Comparison
# ============================================================
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Reflect on when each approach is best.


def final_evaluation():
    # ✏️ YOUR FINAL EVALUATION ✏️

    evaluation = """
    FINAL VERDICT:

    USE LIST OF DICTS WHEN:
    1.
    2.
    3.

    USE DICT OF DICTS WHEN:
    1.
    2.
    3.

    FOR A CHARACTER DATABASE, I CHOOSE: ___

    BECAUSE:
    -

    ONE DOWNSIDE OF MY CHOICE:
    -

    HOW I WOULD MITIGATE THAT DOWNSIDE:
    -
    """
    return evaluation


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_EVALUATION_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Compare data structures...")
    print()
    print("List approach:")
    print(f"  Find {{{{hero}}}}: {find_in_list(characters_list, '{{hero}}')}")
    print()
    print("Dict approach:")
    print(f"  Find {{{{hero}}}}: {find_in_dict(characters_dict, '{{hero}}')}")
    print()
    print("Your analysis:")
    print(analysis_part_1())

    print()
    print(">>> PART 2: Build the dictionary-based system...")
    print("(Implement create_character_db, add_character, get_character, level_up, get_by_class)")
    print()
    # Uncomment after implementing:
    # db = create_character_db()
    # add_character(db, "{{hero}}", 5, 100, "warrior")
    # add_character(db, "{{heroine}}", 7, 120, "mage")
    # add_character(db, "{{friend}}", 3, 80, "rogue")
    # add_character(db, "{{mentor}}", 15, 200, "mage")
    # print(f"Database: {db}")
    # print(f"Get {{{{hero}}}}: {get_character(db, '{{hero}}')}")
    # level_up(db, "{{hero}}")
    # print(f"After level up: {get_character(db, '{{hero}}')}")
    # print(f"Mages: {get_by_class(db, 'mage')}")

    print()
    print(">>> PART 3: Add advanced operations...")
    print("(Implement get_highest_level, get_class_stats, transfer_health)")
    # Uncomment after implementing:
    # print(f"Highest level: {get_highest_level(db)}")
    # print(f"Class stats: {get_class_stats(db)}")
    # transfer_health(db, "{{mentor}}", "{{friend}}", 50)
    # print(f"After transfer: {{{{friend}}}} health = {db['{{friend}}']['health']}")

    print()
    print(">>> PART 4: Final evaluation...")
    print()
    print(final_evaluation())

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
