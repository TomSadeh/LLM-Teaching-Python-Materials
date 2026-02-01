# Exercise 1: Write From Scratch - Class Design
#
# Design and implement classes from scratch based on specifications.
# This is how real object-oriented programming works!
#
# Theme: Creating game entities for {{school}} adventure


# ============================================================
# CHALLENGE A: EASY - Simple Item Class
# ============================================================

class Item:
    """
    A simple item that can be picked up.

    Attributes:
        name (str): The item's name
        value (int): The item's worth in gold

    Methods:
        __init__(name, value=0): Create an item
        __str__(): Return "Item: {name} (worth {value} gold)"

    Examples:
        >>> wand = Item("Elder Wand", 1000)
        >>> wand.name
        'Elder Wand'
        >>> wand.value
        1000
        >>> str(wand)
        'Item: Elder Wand (worth 1000 gold)'
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE B: EASY - Counter Class
# ============================================================

class Counter:
    """
    A simple counter that can be incremented and reset.

    Attributes:
        count (int): Current count, starts at 0

    Methods:
        __init__(): Create counter at 0
        increment(): Add 1 to count
        reset(): Set count back to 0
        __str__(): Return "Count: {count}"

    Examples:
        >>> c = Counter()
        >>> c.count
        0
        >>> c.increment()
        >>> c.increment()
        >>> c.count
        2
        >>> c.reset()
        >>> c.count
        0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE C: MEDIUM - Character Class
# ============================================================

class Character:
    """
    A game character with health and basic combat.

    Attributes:
        name (str): Character's name
        max_health (int): Maximum health points
        health (int): Current health points

    Methods:
        __init__(name, max_health=100): Create character
        take_damage(amount): Reduce health (minimum 0)
        heal(amount): Restore health (maximum max_health)
        is_alive(): Return True if health > 0
        __str__(): Return "{name}: {health}/{max_health} HP"

    Examples:
        >>> hero = Character("{{hero}}", 100)
        >>> hero.take_damage(30)
        >>> hero.health
        70
        >>> hero.heal(50)
        >>> hero.health
        100  # Can't exceed max
        >>> hero.is_alive()
        True
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE D: MEDIUM - Inventory Class
# ============================================================

class Inventory:
    """
    A container for items with add/remove functionality.

    Attributes:
        items (list): List of Item objects
        capacity (int): Maximum number of items

    Methods:
        __init__(capacity=10): Create empty inventory
        add(item): Add item if space available, return True/False
        remove(item_name): Remove item by name, return the item or None
        find(item_name): Find item by name without removing
        is_full(): Return True if at capacity
        __len__(): Return number of items
        __str__(): Return inventory contents

    Examples:
        >>> inv = Inventory(3)
        >>> inv.add(Item("Wand", 100))
        True
        >>> inv.add(Item("Potion", 50))
        True
        >>> len(inv)
        2
        >>> inv.find("Wand").value
        100
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE E: HARD - Spell Class with Cooldown
# ============================================================

class Spell:
    """
    A spell with power, cost, and cooldown mechanics.

    Attributes:
        name (str): Spell name
        power (int): Damage/effect strength
        mana_cost (int): Mana required to cast
        cooldown (int): Turns before can cast again
        current_cooldown (int): Turns remaining until available

    Methods:
        __init__(name, power, mana_cost, cooldown=0): Create spell
        can_cast(available_mana): True if enough mana and not on cooldown
        cast(): Use the spell, set cooldown, return power
        tick(): Reduce cooldown by 1 (minimum 0)
        __str__(): Return spell info string

    Examples:
        >>> fireball = Spell("{{spell1}}", 50, 30, cooldown=2)
        >>> fireball.can_cast(30)
        True
        >>> damage = fireball.cast()
        >>> damage
        50
        >>> fireball.can_cast(30)  # Now on cooldown
        False
        >>> fireball.tick()
        >>> fireball.tick()
        >>> fireball.can_cast(30)  # Cooldown finished
        True
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE F: HARD - Player Class (Uses Other Classes)
# ============================================================

class Player(Character):
    """
    A player character that extends Character with inventory and spells.

    Additional Attributes:
        mana (int): Current mana
        max_mana (int): Maximum mana
        inventory (Inventory): Player's inventory
        spells (list): List of known Spell objects

    Additional Methods:
        __init__(name, max_health=100, max_mana=50): Create player
        learn_spell(spell): Add spell to known spells
        cast_spell(spell_name, target): Cast spell on target if possible
        rest(): Restore 25% health and mana
        __str__(): Extended status string

    Examples:
        >>> player = Player("{{hero}}")
        >>> player.learn_spell(Spell("{{spell1}}", 30, 20))
        >>> enemy = Character("Troll", 100)
        >>> player.cast_spell("{{spell1}}", enemy)
        True
        >>> enemy.health
        70
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Test all classes."""
    print("Testing Class Implementations...\n")

    # Test Item
    print("A: Item")
    wand = Item("Elder Wand", 1000)
    assert wand.name == "Elder Wand"
    assert wand.value == 1000
    assert "Elder Wand" in str(wand)
    print("   ✓ Passed!\n")

    # Test Counter
    print("B: Counter")
    c = Counter()
    assert c.count == 0
    c.increment()
    c.increment()
    assert c.count == 2
    c.reset()
    assert c.count == 0
    print("   ✓ Passed!\n")

    # Test Character
    print("C: Character")
    hero = Character("{{hero}}", 100)
    assert hero.health == 100
    hero.take_damage(30)
    assert hero.health == 70
    hero.heal(50)
    assert hero.health == 100  # Capped at max
    hero.take_damage(200)
    assert hero.health == 0  # Minimum 0
    assert hero.is_alive() == False
    print("   ✓ Passed!\n")

    # Test Inventory
    print("D: Inventory")
    inv = Inventory(2)
    assert inv.add(Item("Wand", 100)) == True
    assert inv.add(Item("Potion", 50)) == True
    assert inv.add(Item("Book", 30)) == False  # Full
    assert len(inv) == 2
    assert inv.find("Wand").value == 100
    removed = inv.remove("Potion")
    assert removed.name == "Potion"
    assert len(inv) == 1
    print("   ✓ Passed!\n")

    # Test Spell
    print("E: Spell")
    fireball = Spell("{{spell1}}", 50, 30, cooldown=2)
    assert fireball.can_cast(30) == True
    assert fireball.can_cast(10) == False  # Not enough mana
    damage = fireball.cast()
    assert damage == 50
    assert fireball.can_cast(30) == False  # On cooldown
    fireball.tick()
    fireball.tick()
    assert fireball.can_cast(30) == True
    print("   ✓ Passed!\n")

    # Test Player
    print("F: Player")
    player = Player("{{hero}}", max_health=100, max_mana=50)
    player.learn_spell(Spell("{{spell1}}", 30, 20))
    enemy = Character("Troll", 100)
    result = player.cast_spell("{{spell1}}", enemy)
    assert result == True
    assert enemy.health == 70
    assert player.mana == 30  # 50 - 20
    print("   ✓ Passed!\n")

    print("=" * 40)
    print("All tests passed! 🎉")


def main():
    print("=== Class Design Challenges ===")
    print()
    print("Implement each class based on its docstring.")
    print("When ready, uncomment run_tests() to check your work.")
    print()

    # Uncomment to run tests:
    # run_tests()


main()
