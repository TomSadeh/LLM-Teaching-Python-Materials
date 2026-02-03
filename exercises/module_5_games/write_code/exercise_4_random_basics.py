"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Topic: Using the random module
Difficulty: 2-3

The random module lets you generate random numbers and make random choices.
Essential for games with unpredictable elements!
"""

import random


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# random.randint(a, b) returns a random integer from a to b INCLUSIVE.
# Unlike range(), both endpoints are included!


def roll_dice(num_sides):
    """
    Roll a single die with the given number of sides.

    Args:
        num_sides: Number of sides on the die (e.g., 6 for standard die)

    Returns:
        int: A random number from 1 to num_sides

    Example:
        roll_dice(6) might return 1, 2, 3, 4, 5, or 6
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use random.randint(1, num_sides) to get a number from 1 to num_sides
    pass


def roll_multiple_dice(num_dice, num_sides):
    """
    Roll multiple dice and return the total.

    Args:
        num_dice: How many dice to roll
        num_sides: Number of sides per die

    Returns:
        int: Sum of all dice rolls

    Example:
        roll_multiple_dice(2, 6) might return any value from 2 to 12
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Initialize total = 0
    # Step 2: Loop num_dice times
    # Step 3: Add a random roll to total
    # Step 4: Return total
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# random.choice(sequence) picks a random item from a list or string.


def pick_random_item(items):
    """
    Pick a random item from a list.

    Args:
        items: A non-empty list

    Returns:
        A randomly selected item from the list

    Example:
        pick_random_item(["{{hero}}", "{{villain}}", "{{friend}}"])
        might return any of those three names
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use random.choice(items)
    pass


def generate_random_name():
    """
    Generate a random name by combining a random adjective and noun.

    Returns:
        str: A randomly generated name like "Swift {{creature}}"

    Use these lists:
        adjectives = ["Swift", "Brave", "Clever", "Mighty", "Silent"]
        nouns = ["{{creature}}", "{{hero}}", "{{villain}}"]
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create the adjectives list
    # Step 2: Create the nouns list
    # Step 3: Pick random adjective with random.choice()
    # Step 4: Pick random noun with random.choice()
    # Step 5: Return f"{adjective} {noun}"
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# random.random() returns a float from 0.0 to 1.0 (exclusive).
# Useful for percentage-based chances.


def chance_event(probability):
    """
    Return True with the given probability, False otherwise.

    Args:
        probability: Float from 0.0 to 1.0 (e.g., 0.7 for 70% chance)

    Returns:
        bool: True if the event happens, False otherwise

    Example:
        chance_event(0.5) returns True about 50% of the time
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # If random.random() < probability, return True
    # Otherwise return False
    pass


def attempt_action(success_rate):
    """
    Attempt an action that might succeed or fail.

    Args:
        success_rate: Float from 0.0 to 1.0 (chance of success)

    Returns:
        str: "success" or "failure"

    Also prints the result:
        "{{exclamation}} Success!" or "Failed..."
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use chance_event() to determine if successful
    # Print the appropriate message
    # Return "success" or "failure"
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# Combine random functions to create game mechanics.


def weighted_random_choice(options, weights):
    """
    Choose from options with weighted probabilities.

    Args:
        options: List of choices
        weights: List of weights (must sum to 1.0)

    Returns:
        A randomly chosen option based on weights

    Example:
        weighted_random_choice(["common", "rare", "legendary"], [0.7, 0.25, 0.05])
        Returns "common" 70%, "rare" 25%, "legendary" 5%
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Get a random float with random.random()
    # Step 2: Track cumulative probability
    # Step 3: Loop through options and weights together
    #         - Add weight to cumulative
    #         - If random value < cumulative, return that option
    # Step 4: Return last option (safety fallback)
    #
    # Hint: Use zip(options, weights) to loop through both
    pass


def generate_loot():
    """
    Generate random loot with rarities.

    Returns:
        tuple: (item_name, rarity)

    Rarities:
        - "common" (60% chance)
        - "uncommon" (25% chance)
        - "rare" (12% chance)
        - "legendary" (3% chance)

    Use placeholder items based on rarity:
        - common: "{{item}}"
        - uncommon: "Enhanced {{item}}"
        - rare: "{{creature}}'s {{item}}"
        - legendary: "{{hero}}'s Legendary {{item}}"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Define rarities and weights
    # Step 2: Use weighted_random_choice to pick rarity
    # Step 3: Create item name based on rarity
    # Step 4: Return (item_name, rarity)
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}
#
# Generate random numbers within ranges for game scenarios.


def generate_stats():
    """
    Generate random stats for a character.

    Returns:
        dict: Character stats

    Stats to generate:
        - "strength": random 5-15
        - "agility": random 5-15
        - "wisdom": random 5-15
        - "luck": random 1-10

    Also calculate:
        - "power": strength + agility
        - "total": sum of all four base stats
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Generate each base stat with random.randint()
    # Step 2: Calculate derived stats
    # Step 3: Return dictionary with all stats
    pass


def simulate_battle_round(attacker_power, defender_power):
    """
    Simulate one round of battle between attacker and defender.

    Args:
        attacker_power: Attacker's power stat
        defender_power: Defender's power stat

    Returns:
        tuple: (attacker_damage_dealt, defender_damage_dealt)

    Damage formula:
        base_damage = power // 3
        actual_damage = base_damage + random.randint(0, 5)

    Example:
        simulate_battle_round(15, 12) might return (7, 6)
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Calculate attacker's damage
    # Calculate defender's damage
    # Return both as a tuple
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    print(f"Rolling a 6-sided die: {roll_dice(6)}")
    print(f"Rolling a 20-sided die: {roll_dice(20)}")
    print(f"Rolling 3d6: {roll_multiple_dice(3, 6)}")

    print("\n=== {{PHASE_2_TITLE}} ===")
    characters = ["{{hero}}", "{{villain}}", "{{friend}}", "{{mentor}}"]
    print(f"Random character: {pick_random_item(characters)}")
    print(f"Random name: {generate_random_name()}")

    print("\n=== {{PHASE_3_TITLE}} ===")
    print("Attempting action with 75% success rate:")
    attempt_action(0.75)

    print("\n=== {{PHASE_4_TITLE}} ===")
    print("Generating loot:")
    item, rarity = generate_loot()
    print(f"Found: {item} ({rarity})")

    print("\n=== {{PHASE_5_TITLE}} ===")
    print("Generating character stats:")
    stats = generate_stats()
    print(f"Stats: {stats}")
    print("\nSimulating battle round (power 15 vs 12):")
    atk_dmg, def_dmg = simulate_battle_round(15, 12)
    print(f"Attacker dealt {atk_dmg}, Defender dealt {def_dmg}")

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
