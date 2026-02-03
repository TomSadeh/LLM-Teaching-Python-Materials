"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll practice using super() to call parent class
methods. Understanding super() is essential for properly initializing
subclasses and extending parent behavior.
"""


# ============================================================
# {{FUNCTION_1_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}


class BaseUnit:
    """Base class for all units at {{school}}."""

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health


class AdvancedUnit(BaseUnit):
    """
    A unit with additional capabilities.

    This class extends BaseUnit by adding a power attribute.

    Examples:
        >>> unit = AdvancedUnit("{{hero}}", 100, 50)
        >>> unit.name
        '{{hero}}'
        >>> unit.health
        100
        >>> unit.power
        50
    """

    def __init__(self, name, health, power):
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_1}}
        #
        # Step 1: Call the parent class __init__ using super()
        #         super().__init__(name, health)
        #
        # Step 2: Add the new attribute for this class
        #         self.power = power

        pass


# ============================================================
# {{FUNCTION_2_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}


class BaseCharacter:
    """Base class for characters."""

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.experience = 0


class PlayerCharacter(BaseCharacter):
    """
    A player-controlled character with a class role.

    Extends BaseCharacter with role and skills.

    Examples:
        >>> player = PlayerCharacter("{{hero}}", "{{ROLE_TITLE}}", 5)
        >>> player.name
        '{{hero}}'
        >>> player.level
        5
        >>> player.role
        '{{ROLE_TITLE}}'
        >>> player.skills
        []
    """

    def __init__(self, name, role, level=1):
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_2}}
        #
        # Step 1: Call parent __init__ with name and level
        #         Note: The parent doesn't know about 'role'
        #
        # Step 2: Add role as a new attribute
        #
        # Step 3: Initialize skills as an empty list

        pass


# ============================================================
# {{FUNCTION_3_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}


class BaseCreature:
    """Base class for creatures."""

    def __init__(self, species, health, power):
        self.species = species
        self.health = health
        self.power = power
        self.is_wild = True


class TamedCreature(BaseCreature):
    """
    A creature that has been tamed by a character.

    Extends BaseCreature with owner and loyalty.

    Examples:
        >>> creature = TamedCreature("{{creature}}", 80, 40, "{{hero}}")
        >>> creature.species
        '{{creature}}'
        >>> creature.is_wild
        False
        >>> creature.owner
        '{{hero}}'
        >>> creature.loyalty
        50
    """

    def __init__(self, species, health, power, owner):
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_3}}
        #
        # Step 1: Call parent __init__ with species, health, power
        #
        # Step 2: Override is_wild to be False (tamed creatures aren't wild)
        #
        # Step 3: Add owner attribute
        #
        # Step 4: Add loyalty attribute, initialized to 50

        pass


# ============================================================
# {{FUNCTION_4_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_4_NARRATIVE}}


class BaseItem:
    """Base class for items."""

    def __init__(self, name, base_value):
        self.name = name
        self.base_value = base_value

    def get_value(self):
        """Return the item's value."""
        return self.base_value


class EnchantedItem(BaseItem):
    """
    An item with magical enhancements.

    Extends BaseItem with enchantment level and multiplied value.

    The actual value is base_value * (1 + enchantment_level * 0.5)

    Examples:
        >>> item = EnchantedItem("{{item}}", 100, 2)
        >>> item.name
        '{{item}}'
        >>> item.enchantment_level
        2
        >>> item.get_value()
        200.0
    """

    def __init__(self, name, base_value, enchantment_level):
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_4}}
        #
        # Step 1: Call parent __init__ with name and base_value
        #
        # Step 2: Add enchantment_level attribute

        pass

    def get_value(self):
        """
        Return the enchanted item's value.

        Value = base_value * (1 + enchantment_level * 0.5)

        Examples:
            >>> item = EnchantedItem("{{item}}", 100, 2)
            >>> item.get_value()
            200.0
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # Calculate: self.base_value * (1 + self.enchantment_level * 0.5)

        pass


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
    unit = AdvancedUnit("{{hero}}", 100, 50)
    if unit.name:
        print(f"Name: {unit.name}")
        print(f"Health: {unit.health}/{unit.max_health}")
        print(f"Power: {unit.power}")
    else:
        print("  (Complete the __init__ method)")

    print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
    player = PlayerCharacter("{{heroine}}", "{{ROLE_TITLE}}", 5)
    if player.name:
        print(f"Name: {player.name}")
        print(f"Level: {player.level}")
        print(f"Role: {player.role}")
        print(f"Skills: {player.skills}")
    else:
        print("  (Complete the __init__ method)")

    print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
    creature = TamedCreature("{{creature}}", 80, 40, "{{hero}}")
    if creature.species:
        print(f"Species: {creature.species}")
        print(f"Owner: {creature.owner}")
        print(f"Is wild: {creature.is_wild}")
        print(f"Loyalty: {creature.loyalty}")
    else:
        print("  (Complete the __init__ method)")

    print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
    item = EnchantedItem("{{item}}", 100, 2)
    if item.name:
        print(f"Name: {item.name}")
        print(f"Base value: {item.base_value}")
        print(f"Enchantment: +{item.enchantment_level}")
        print(f"Actual value: {item.get_value()}")
    else:
        print("  (Complete the __init__ and get_value methods)")

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
