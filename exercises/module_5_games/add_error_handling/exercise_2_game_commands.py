"""
{{CONTEXT_ERROR_HANDLING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Topic: Handling invalid game commands gracefully
Difficulty: 3-4

Games need robust command handling - players will type anything!
Make the game respond helpfully to invalid input.
"""


# ============================================================
# {{HANDLING_1_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# This movement system crashes on invalid directions.


def original_move(direction):
    """ORIGINAL: Crashes on invalid direction"""
    moves = {"north": (0, 1), "south": (0, -1), "east": (1, 0), "west": (-1, 0)}
    dx, dy = moves[direction]  # KeyError if direction invalid!
    return dx, dy


def safe_move(direction):
    """
    Get movement delta for a direction, handling invalid input.

    Args:
        direction: A string like "north", "south", "east", "west"

    Returns:
        tuple: (dx, dy) movement delta, or (0, 0) for invalid

    Should:
    - Accept any case (North, NORTH, north all work)
    - Return (0, 0) and print error for invalid direction
    - Print "Invalid direction. Use north/south/east/west."
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_1}}
    #
    # Step 1: Define moves dictionary
    # Step 2: Convert direction to lowercase
    # Step 3: If direction in moves, return the delta
    # Step 4: Otherwise, print error and return (0, 0)
    pass


# ============================================================
# {{HANDLING_2_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# This attack command crashes if target doesn't exist.


def original_attack(enemies, target_name):
    """ORIGINAL: Crashes if target not in list"""
    for i, enemy in enumerate(enemies):
        if enemy["name"] == target_name:
            enemies[i]["hp"] -= 10
            return True
    return False


def safe_attack(enemies, target_name):
    """
    Attack a target by name, handling invalid targets.

    Args:
        enemies: List of enemy dicts with "name" and "hp" keys
        target_name: Name of enemy to attack

    Returns:
        str: Result message

    Should handle:
    - Target not found: "No enemy named {target_name}"
    - Target already defeated (hp <= 0): "{target_name} is already defeated"
    - Successful attack: "Hit {target_name} for 10 damage!"
    - Enemy defeated by this attack: "{target_name} defeated!"
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_2}}
    #
    # Step 1: Loop through enemies to find target
    # Step 2: If not found after loop, return not found message
    # Step 3: If found but hp <= 0, return already defeated message
    # Step 4: Apply damage
    # Step 5: If hp now <= 0, return defeated message
    # Step 6: Otherwise return hit message
    pass


# ============================================================
# {{HANDLING_3_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# This inventory use command has multiple failure modes.


def original_use_item(inventory, item_name):
    """ORIGINAL: Crashes if item not in inventory"""
    inventory.remove(item_name)  # ValueError if not present!
    return f"Used {item_name}"


def safe_use_item(inventory, item_name):
    """
    Use an item from inventory, handling errors.

    Args:
        inventory: List of item names
        item_name: Item to use

    Returns:
        tuple: (success, message)

    Should handle:
    - Empty inventory: "Inventory is empty!"
    - Item not found: "{item_name} not in inventory"
    - Success: "Used {item_name}!" and remove from inventory
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_3}}
    #
    # Step 1: Check if inventory is empty
    # Step 2: Check if item_name is in inventory
    # Step 3: If present, remove and return success
    # Step 4: Otherwise return appropriate error
    pass


# ============================================================
# {{HANDLING_4_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# This shop system has multiple ways to fail.


def original_buy_item(gold, item_prices, item_name):
    """ORIGINAL: Crashes if item doesn't exist"""
    price = item_prices[item_name]
    return gold - price, item_name


def safe_buy_item(gold, item_prices, item_name):
    """
    Buy an item from the shop, handling all error cases.

    Args:
        gold: Player's current gold
        item_prices: Dict of {item_name: price}
        item_name: Item to purchase

    Returns:
        tuple: (new_gold, message)

    Should handle:
    - Item not in shop: "Shop doesn't sell {item_name}"
    - Not enough gold: "Need {price} gold, you have {gold}"
    - Success: Return (gold - price, "Bought {item_name}!")
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_4}}
    #
    # Step 1: Check if item_name in item_prices
    # Step 2: Get the price
    # Step 3: Check if player has enough gold
    # Step 4: If all good, return new gold and success message
    pass


# ============================================================
# {{HANDLING_5_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_5_NARRATIVE}}
#
# Build a complete command parser with validation.


def parse_game_command(command_string):
    """
    Parse a game command string into action and arguments.

    Valid commands:
    - "move <direction>" (north/south/east/west)
    - "attack <target>"
    - "use <item>"
    - "look"
    - "help"
    - "quit"

    Args:
        command_string: Raw input from player

    Returns:
        tuple: (action, args) or (None, error_message)

    Examples:
        parse_game_command("move north") returns ("move", "north")
        parse_game_command("attack goblin") returns ("attack", "goblin")
        parse_game_command("look") returns ("look", None)
        parse_game_command("dance") returns (None, "Unknown command: dance")
        parse_game_command("") returns (None, "Please enter a command")
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_5}}
    #
    # Step 1: Strip and lowercase the command
    # Step 2: If empty, return error
    # Step 3: Split into parts
    # Step 4: First part is the action
    # Step 5: Check if action is valid
    # Step 6: For commands needing args (move, attack, use):
    #         - Check args provided
    #         - For move, validate direction
    # Step 7: Return (action, args) or appropriate error
    pass


def main():
    print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
    print("=" * 50)

    print("\n=== {{HANDLING_1_TITLE}} ===")
    print("Testing safe movement:")
    directions = ["north", "SOUTH", "left", "east"]
    for d in directions:
        result = safe_move(d)
        print(f"  {d} -> {result}")

    print("\n=== {{HANDLING_2_TITLE}} ===")
    print("Testing safe attack:")
    enemies = [
        {"name": "{{creature}}", "hp": 20},
        {"name": "{{villain}}", "hp": 0}
    ]
    targets = ["{{creature}}", "{{villain}}", "ghost"]
    for t in targets:
        result = safe_attack(enemies, t)
        print(f"  Attack {t}: {result}")

    print("\n=== {{HANDLING_3_TITLE}} ===")
    print("Testing safe use item:")
    inv = ["{{item}}", "{{spell1}}"]
    items_to_use = ["{{item}}", "{{spell2}}"]
    for item in items_to_use:
        result = safe_use_item(inv, item)
        print(f"  Use {item}: {result}")

    print("\n=== {{HANDLING_4_TITLE}} ===")
    print("Testing safe shop:")
    prices = {"{{item}}": 50, "{{spell1}}": 100}
    purchases = [("{{item}}", 60), ("{{spell1}}", 50), ("potion", 100)]
    for item, gold in purchases:
        new_gold, msg = safe_buy_item(gold, prices, item)
        print(f"  Buy {item} with {gold}g: {msg}")

    print("\n=== {{HANDLING_5_TITLE}} ===")
    print("Testing command parser:")
    commands = ["move north", "attack goblin", "look", "dance", "", "move"]
    for cmd in commands:
        result = parse_game_command(cmd)
        print(f"  '{cmd}' -> {result}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")


main()
