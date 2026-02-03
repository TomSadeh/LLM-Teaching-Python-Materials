"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to use .get() for safe dictionary access.
The .get() method returns a default value when a key doesn't exist,
instead of raising a KeyError.
"""


# ============================================================
# {{FUNCTION_1_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}


def get_character_stat(stats, stat_name):
    """
    Safely get a character's stat value.

    Args:
        stats: Dictionary of character stats (e.g., {"health": 100, "strength": 10})
        stat_name: The stat to look up (e.g., "health")

    Returns:
        int: The stat value if found, or 0 if not found.

    Examples:
        >>> get_character_stat({"health": 100}, "health")
        100
        >>> get_character_stat({"health": 100}, "mana")
        0
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # {{CONTEXT_FUNCTION_HINT_1}}
    #
    # Use stats.get(stat_name, default_value)
    # The second argument is returned if the key doesn't exist.

    pass


# ============================================================
# {{FUNCTION_2_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}


def get_inventory_count(inventory, item_name):
    """
    Get how many of an item the player has.

    Args:
        inventory: Dictionary mapping item names to quantities
        item_name: The item to look up

    Returns:
        int: The quantity (0 if item not in inventory)

    Examples:
        >>> get_inventory_count({"{{item}}": 5}, "{{item}}")
        5
        >>> get_inventory_count({"{{item}}": 5}, "{{spell1}}")
        0
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # {{CONTEXT_FUNCTION_HINT_2}}
    #
    # Use .get() to safely access the inventory.

    pass


# ============================================================
# {{FUNCTION_3_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}


def get_ability_description(abilities, ability_name):
    """
    Get the description of an ability.

    Args:
        abilities: Dictionary mapping ability names to descriptions
        ability_name: The ability to look up

    Returns:
        str: The description, or "Unknown ability" if not found.

    Examples:
        >>> get_ability_description({"{{spell1}}": "A basic technique"}, "{{spell1}}")
        'A basic technique'
        >>> get_ability_description({"{{spell1}}": "A basic technique"}, "{{spell3}}")
        'Unknown ability'
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # {{CONTEXT_FUNCTION_HINT_3}}
    #
    # Return the description or "Unknown ability" as default.

    pass


# ============================================================
# {{FUNCTION_4_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_4_NARRATIVE}}


def safe_add_to_inventory(inventory, item_name, quantity):
    """
    Add items to inventory, creating entry if needed.

    Args:
        inventory: Dictionary mapping item names to quantities
        item_name: The item to add
        quantity: How many to add

    Returns:
        int: The new total quantity of that item

    This function modifies the inventory dictionary in place.

    Examples:
        >>> inv = {"{{item}}": 5}
        >>> safe_add_to_inventory(inv, "{{item}}", 3)
        8
        >>> inv
        {'{{item}}': 8}
        >>> safe_add_to_inventory(inv, "{{spell1}}", 2)
        2
        >>> inv
        {'{{item}}': 8, '{{spell1}}': 2}
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # {{CONTEXT_FUNCTION_HINT_4}}
    #
    # Step 1: Get current quantity (default 0 if not in inventory)
    # Step 2: Add the new quantity
    # Step 3: Store back in inventory
    # Step 4: Return the new total
    #
    # Pattern: inventory[item] = inventory.get(item, 0) + quantity

    pass


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
    stats = {"health": 100, "strength": 10}
    print(f"Health: {get_character_stat(stats, 'health')}")
    print(f"Mana (not set): {get_character_stat(stats, 'mana')}")

    print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
    inventory = {"{{item}}": 5, "{{spell1}}": 3}
    print(f"{{{{item}}}}: {get_inventory_count(inventory, '{{item}}')}")
    print(f"{{{{spell2}}}} (not owned): {get_inventory_count(inventory, '{{spell2}}')}")

    print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
    abilities = {
        "{{spell1}}": "A fundamental technique",
        "{{spell2}}": "An intermediate skill"
    }
    print(f"{{{{spell1}}}}: {get_ability_description(abilities, '{{spell1}}')}")
    print(f"{{{{spell3}}}}: {get_ability_description(abilities, '{{spell3}}')}")

    print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
    inv = {}
    safe_add_to_inventory(inv, "{{item}}", 3)
    safe_add_to_inventory(inv, "{{item}}", 2)
    safe_add_to_inventory(inv, "{{spell1}}", 1)
    print(f"Inventory: {inv}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
