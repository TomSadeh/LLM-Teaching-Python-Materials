"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part project where you'll build a complete text adventure game.
You'll design game functions, implement mechanics, add inventory tracking,
and create an adventure with multiple paths.

{{CONTEXT_LEARNING_OBJECTIVE}}
"""

import random


# ============================================================
# PART 1: Game Function Design (Blank Page)
# ============================================================
# {{CONTEXT_BLANK_PAGE_INTRO}}
#
# Design and implement these core game functions from their specifications.
# The adventure takes place at {{school}} where {{hero}} must face {{villain}}.


def create_player(name):
    """
    Create a new player for the adventure.

    Args:
        name: Player's name (string)

    Returns:
        A list representing the player state:
        [name, health, inventory, current_location]
        - health starts at 100
        - inventory is an empty list
        - current_location is "entrance"

    Examples:
        >>> player = create_player("{{hero}}")
        >>> player[0]
        '{{hero}}'
        >>> player[1]
        100
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_player_name(player):
    """
    Get the player's name.

    Args:
        player: Player state list

    Returns:
        The player's name (string)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_player_health(player):
    """
    Get the player's current health.

    Args:
        player: Player state list

    Returns:
        Health points (integer)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_player_inventory(player):
    """
    Get the player's inventory list.

    Args:
        player: Player state list

    Returns:
        The inventory list (may be empty)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_player_location(player):
    """
    Get the player's current location.

    Args:
        player: Player state list

    Returns:
        Location name (string)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def set_player_health(player, health):
    """
    Set the player's health (0-100).

    Args:
        player: Player state list
        health: New health value

    Note:
        Clamp health between 0 and 100.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def set_player_location(player, location):
    """
    Move the player to a new location.

    Args:
        player: Player state list
        location: New location name (string)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 2: Core Game Mechanics
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
#
# Implement the core mechanics that make the adventure work.


def add_to_inventory(player, item):
    """
    Add an item to the player's inventory.

    Args:
        player: Player state list
        item: Item name to add (string)

    Prints:
        "You picked up [item]!"
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def remove_from_inventory(player, item):
    """
    Remove an item from the player's inventory.

    Args:
        player: Player state list
        item: Item name to remove (string)

    Returns:
        True if item was removed, False if not in inventory.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def has_item(player, item):
    """
    Check if player has an item.

    Args:
        player: Player state list
        item: Item name to check (string)

    Returns:
        True if item is in inventory, False otherwise.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_status(player):
    """
    Display the player's current status.

    Args:
        player: Player state list

    Prints:
        === Status ===
        Name: [name]
        Health: [health]/100
        Location: [location]
        Inventory: [item1, item2, ...] or "empty"
        ==============
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def take_damage(player, damage):
    """
    Apply damage to the player.

    Args:
        player: Player state list
        damage: Damage amount (integer)

    Prints:
        "You took [damage] damage!"

    Returns:
        True if player is still alive (health > 0), False otherwise.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def heal_player(player, amount):
    """
    Heal the player.

    Args:
        player: Player state list
        amount: Healing amount (integer)

    Prints:
        "You healed [amount] HP! Health: [new_health]/100"
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 3: Locations and Events
# ============================================================
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Create the world with locations and events.


def get_location_description(location):
    """
    Get the description for a location.

    Args:
        location: Location name (string)

    Returns:
        A description string for the location.

    Locations to include:
        - "entrance": The entrance to {{school}}
        - "hallway": A long corridor with doors
        - "library": A room full of ancient books
        - "chamber": The final chamber where {{villain}} waits
        - "garden": A peaceful garden with healing herbs

    If unknown location, return "You are somewhere unknown..."
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_location_options(location):
    """
    Get the available actions for a location.

    Args:
        location: Current location name (string)

    Returns:
        A list of available action strings.

    Example for "entrance":
        ["go hallway", "look around", "check inventory"]

    Include at least 3 options per location.
    Different locations should have different options.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def process_look_around(player, location):
    """
    Process the "look around" action.

    Args:
        player: Player state list
        location: Current location

    Prints:
        A description of what the player sees.
        Sometimes finds items (add to inventory).
        Use random chance for finding items.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def process_random_event(player):
    """
    Possibly trigger a random event.

    Args:
        player: Player state list

    This function has a chance to trigger events like:
        - Finding a {{item}} (heal player)
        - Encountering a {{creature}} (take damage)
        - Finding coins (add to inventory)
        - Nothing happens

    Use random.randint() to decide.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 4: Complete Adventure
# ============================================================
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Bring it all together into a complete playable adventure.


def display_intro():
    """
    Display the game introduction.

    Prints:
        A themed welcome message about the adventure at {{school}}.
        Explain that {{villain}} is threatening the school.
        The player must find key items and reach the chamber.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_location(player):
    """
    Display the current location and options.

    Args:
        player: Player state list

    Prints:
        The location description and available actions.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_player_action(options):
    """
    Get a valid action from the player.

    Args:
        options: List of valid action strings

    Returns:
        The chosen action (string).

    Note:
        Show numbered options.
        Keep asking until valid choice.
        Also accept "quit" to exit.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def process_action(player, action):
    """
    Process a player action.

    Args:
        player: Player state list
        action: The action string

    Returns:
        True to continue game, False to end.

    Handle actions like:
        - "go [location]" - move to new location
        - "look around" - search the area
        - "check inventory" - show inventory
        - "use [item]" - use an item
        - "status" - show full status
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def check_win_condition(player):
    """
    Check if the player has won.

    Args:
        player: Player state list

    Returns:
        True if player has won, False otherwise.

    Win condition:
        Player is in "chamber" and has "{{item}}" in inventory.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def check_lose_condition(player):
    """
    Check if the player has lost.

    Args:
        player: Player state list

    Returns:
        True if player has lost (health <= 0), False otherwise.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_ending(player, won):
    """
    Display the game ending.

    Args:
        player: Player state list
        won: True if player won, False if lost

    Prints:
        Victory message if won ({{villain}} defeated!)
        Defeat message if lost (try again!)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def run_adventure():
    """
    Run the complete text adventure.

    This function:
    1. Shows the intro
    2. Gets player name
    3. Creates the player
    4. Main game loop:
        - Display location
        - Get action
        - Process action
        - Check for random events
        - Check win/lose conditions
    5. Display ending
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)
    print()
    print("Complete each part to build the text adventure.")
    print()

    # Uncomment to test individual parts:
    # Part 1 test
    # player = create_player("{{hero}}")
    # print(f"Player: {get_player_name(player)}")
    # print(f"Health: {get_player_health(player)}")

    # Part 2 test
    # player = create_player("{{hero}}")
    # add_to_inventory(player, "potion")
    # add_to_inventory(player, "{{item}}")
    # display_status(player)

    # Part 3 test
    # print(get_location_description("entrance"))
    # print(get_location_options("entrance"))

    # Part 4 - run the full adventure
    # run_adventure()

    print()
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()
