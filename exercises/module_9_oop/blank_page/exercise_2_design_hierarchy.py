"""
{{CONTEXT_BLANK_PAGE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Design and implement a class hierarchy from scratch.
This requires planning parent-child relationships and using inheritance.
"""


# ============================================================
# {{BLANK_1_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_1_NARRATIVE}}


def ability_hierarchy():
    """
    Design an Ability class hierarchy for {{school}}.

    Base class: Ability
        - name (string)
        - cost (integer, resource cost to use)
        - cooldown (integer, turns until can be used again)
        - current_cooldown (starts at 0)
        - can_use() -> True if current_cooldown == 0
        - use() -> sets current_cooldown to cooldown, returns description
        - tick() -> reduces current_cooldown by 1 (minimum 0)
        - __str__ -> "[name] (cost: [cost], CD: [current]/[cooldown])"

    Subclass: DamageAbility(Ability)
        - Additional: damage (integer)
        - Override use() to return "[name] deals [damage] damage!"
        - Inherits everything else

    Subclass: HealAbility(Ability)
        - Additional: heal_amount (integer)
        - Override use() to return "[name] heals for [heal_amount]!"
        - Inherits everything else

    Subclass: BuffAbility(Ability)
        - Additional: buff_name (string), duration (integer)
        - Override use() to return "[name] applies [buff] for [duration] turns!"
        - Inherits everything else

    Examples:
        >>> fireball = DamageAbility("{{spell2}}", 20, 3, 50)
        >>> fireball.can_use()
        True
        >>> fireball.use()
        '{{spell2}} deals 50 damage!'
        >>> fireball.can_use()
        False
        >>> fireball.tick()
        >>> fireball.tick()
        >>> fireball.tick()
        >>> fireball.can_use()
        True

        >>> heal = HealAbility("{{spell1}}", 15, 2, 30)
        >>> heal.use()
        '{{spell1}} heals for 30!'

        >>> buff = BuffAbility("{{spell3}}", 10, 5, "Shield", 3)
        >>> buff.use()
        '{{spell3}} applies Shield for 3 turns!'
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_2_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_2_NARRATIVE}}


def item_hierarchy():
    """
    Design an Item class hierarchy for {{school}}'s shop.

    Base class: Item
        - name (string)
        - base_value (integer, gold value)
        - get_value() -> returns base_value
        - get_description() -> "[name] worth [value] gold"
        - __str__ -> calls get_description()

    Subclass: Equipment(Item)
        - Additional: slot (string like "weapon", "armor", "accessory")
        - Additional: durability (integer, starts at 100)
        - use() -> reduces durability by 10, returns True if durability > 0
        - Override get_description() to include slot and durability
        - get_value() -> base_value * (durability / 100)

    Subclass: Consumable(Item)
        - Additional: quantity (integer, starts at given amount)
        - Additional: effect (string describing what it does)
        - consume() -> reduces quantity by 1, returns effect if quantity > 0
        - Override get_description() to include quantity and effect
        - is_empty() -> True if quantity == 0

    Subclass: QuestItem(Item)
        - Additional: quest_name (string, the quest it belongs to)
        - Override get_value() to return 0 (can't sell quest items)
        - Override get_description() to note it's a quest item

    Examples:
        >>> sword = Equipment("{{item}}", 100, "weapon")
        >>> sword.get_value()
        100
        >>> sword.use()
        True
        >>> sword.durability
        90
        >>> sword.get_value()
        90

        >>> potion = Consumable("Healing Potion", 50, 3, "Restores 50 HP")
        >>> potion.consume()
        'Restores 50 HP'
        >>> potion.quantity
        2

        >>> key = QuestItem("Ancient Key", 500, "Find the Lost Vault")
        >>> key.get_value()
        0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_3_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_3_NARRATIVE}}


def character_hierarchy():
    """
    Design a Character class hierarchy for a {{school}} game.

    Base class: Character
        - name (string)
        - health, max_health (integers)
        - is_alive() -> health > 0
        - take_damage(amount) -> reduces health, min 0
        - heal(amount) -> increases health, max max_health
        - get_status() -> "[name]: [health]/[max_health] HP"

    Subclass: Player(Character)
        - Additional: experience (starts at 0), level (starts at 1)
        - gain_experience(amount) -> adds XP, levels up at 100 XP per level
        - Override get_status() to include level and XP

    Subclass: Enemy(Character)
        - Additional: damage (attack power), loot_value (gold dropped)
        - attack(target) -> deals damage to target
        - Override get_status() to include damage

    Subclass: Boss(Enemy)
        - Additional: phase (starts at 1), max_phases (integer)
        - Override take_damage: at 0 HP, if phase < max_phases,
          restore to full health and increment phase
        - Override get_status() to include phase

    Examples:
        >>> player = Player("{{hero}}", 100)
        >>> player.gain_experience(150)
        >>> player.level
        2
        >>> player.experience
        50

        >>> enemy = Enemy("{{creature}}", 50, 15, 20)
        >>> enemy.attack(player)
        >>> player.health
        85

        >>> boss = Boss("{{villain}}", 100, 30, 50, 3)
        >>> boss.take_damage(150)
        >>> boss.is_alive()
        True
        >>> boss.phase
        2
        >>> boss.health
        100
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Run tests for all hierarchies."""
    print("Testing your implementations...\n")

    print("{{BLANK_1_TITLE}} - Ability Hierarchy")
    # Uncomment to test:
    # fireball = DamageAbility("Fireball", 20, 3, 50)
    # assert fireball.can_use() == True
    # result = fireball.use()
    # assert "50 damage" in result
    # assert fireball.can_use() == False
    print("   (Uncomment tests after implementing)\n")

    print("{{BLANK_2_TITLE}} - Item Hierarchy")
    # Uncomment to test:
    # sword = Equipment("Sword", 100, "weapon")
    # assert sword.get_value() == 100
    # sword.use()
    # assert sword.durability == 90
    # potion = Consumable("Potion", 50, 3, "Heals 50")
    # assert potion.consume() == "Heals 50"
    # assert potion.quantity == 2
    print("   (Uncomment tests after implementing)\n")

    print("{{BLANK_3_TITLE}} - Character Hierarchy")
    # Uncomment to test:
    # player = Player("Hero", 100)
    # player.gain_experience(150)
    # assert player.level == 2
    # enemy = Enemy("Goblin", 50, 15, 20)
    # enemy.attack(player)
    # assert player.health == 85
    # boss = Boss("Dragon", 100, 30, 50, 3)
    # boss.take_damage(150)
    # assert boss.is_alive() == True
    # assert boss.phase == 2
    print("   (Uncomment tests after implementing)\n")

    print("=" * 40)
    print("All tests passed!")


def main():
    print("{{CONTEXT_BLANK_PAGE_INTRO}}")
    print("=" * 50)
    print()
    print("Design each class hierarchy based on the specifications.")
    print("Think carefully about what goes in the base class vs subclasses.")
    print()

    # Uncomment the hierarchy you're working on:
    # ability_hierarchy()
    # item_hierarchy()
    # character_hierarchy()

    # Uncomment to run tests:
    # run_tests()

    print("{{CONTEXT_MASTERY_COMPLETE}}")


main()
