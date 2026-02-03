"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part project where you'll build a complete character profile
system. You'll design data structures, create functions, and build an
interactive menu interface.

{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# PART 1: Data Structure Design
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
#
# Every {{PRACTITIONER_SINGULAR}} needs a way to track information about
# characters at {{school}}. You'll start by designing how to store
# character data using lists.
#
# A character profile should track:
# - Name (string)
# - Health points (integer, starts at 100)
# - Special ability (string, like "{{spell1}}")
# - Level (integer, starts at 1)


def create_character(name, ability):
    """
    Create a new character profile as a list.

    Args:
        name: The character's name (string)
        ability: The character's special ability (string)

    Returns:
        A list containing: [name, health, ability, level]
        Health starts at 100, level starts at 1.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def create_sample_characters():
    """
    Create a list of sample characters to test with.

    Returns:
        A list containing 3 character profiles:
        - {{hero}} with ability "{{spell1}}"
        - {{heroine}} with ability "{{spell2}}"
        - {{friend}} with ability "{{spell3}}"
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 2: Display Functions
# ============================================================
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now that you can create characters, you need functions to display
# their information clearly.


def display_character(character):
    """
    Display a single character's profile in a formatted way.

    Args:
        character: A character list [name, health, ability, level]

    Prints:
        A formatted display of the character's stats.
        Example output:
        --- Character Profile ---
        Name: {{hero}}
        Health: 100
        Ability: {{spell1}}
        Level: 1
        ------------------------
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_all_characters(characters):
    """
    Display all characters in the roster.

    Args:
        characters: A list of character profiles

    Prints:
        Each character's profile, numbered.
        If the list is empty, print "No characters in roster."
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 3: Modification Functions
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
#
# Characters need to grow and change! Create functions to modify
# character stats.


def level_up(character):
    """
    Increase a character's level by 1 and add 10 health.

    Args:
        character: A character list to modify

    Returns:
        None (modifies the list in place)

    Prints:
        A message like "{{hero}} leveled up to level 2!"
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def take_damage(character, damage):
    """
    Reduce a character's health by the damage amount.

    Args:
        character: A character list to modify
        damage: Amount of damage (integer)

    Returns:
        None (modifies the list in place)

    Note:
        Health cannot go below 0.
        If health reaches 0, print "{name} has been defeated!"
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def heal_character(character, amount):
    """
    Restore health to a character.

    Args:
        character: A character list to modify
        amount: Amount to heal (integer)

    Returns:
        None (modifies the list in place)

    Note:
        Health cannot exceed 100.
        Print "{name} healed to {health} HP!"
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def find_character(characters, name):
    """
    Find a character by name in the roster.

    Args:
        characters: List of character profiles
        name: Name to search for (case-insensitive)

    Returns:
        The character list if found, None otherwise.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 4: Menu Interface
# ============================================================
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Bring it all together with an interactive menu that lets
# users manage their character roster.


def print_menu():
    """
    Display the main menu options.

    Prints:
        === {{school}} Character Manager ===
        1. View all characters
        2. Add new character
        3. Level up a character
        4. Take damage (simulate challenge)
        5. Heal a character
        6. Quit
        ================================
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_valid_choice(min_choice, max_choice):
    """
    Get a valid menu choice from the user.

    Args:
        min_choice: Minimum valid choice number
        max_choice: Maximum valid choice number

    Returns:
        A valid integer choice within the range.

    Note:
        Keep asking until the user enters a valid number.
        Use .isdigit() to check if input is a number.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def run_character_manager():
    """
    Run the main character manager loop.

    This function:
    1. Creates sample characters to start
    2. Shows the menu
    3. Gets user choice
    4. Performs the selected action
    5. Repeats until user chooses to quit

    Use a while loop and call the functions you created above.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)
    print()
    print("Complete each part to build the character manager.")
    print()

    # Uncomment to test individual parts:
    # Part 1 test
    # char = create_character("{{hero}}", "{{spell1}}")
    # print(f"Created: {char}")

    # Part 2 test
    # chars = create_sample_characters()
    # display_all_characters(chars)

    # Part 3 test
    # char = create_character("{{hero}}", "{{spell1}}")
    # level_up(char)
    # take_damage(char, 30)
    # heal_character(char, 20)

    # Part 4 - run the full program
    # run_character_manager()

    print()
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()
