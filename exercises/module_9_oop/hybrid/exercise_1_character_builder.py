"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise where you learn to build characters
for {{school}} by studying examples, adding methods, and creating
your own class designs.

Programming concepts: classes, __init__, self, instance methods, attributes
"""


# ============================================================
# PART 1: Guidance - Study and Complete the Class
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} has created a character class for you to study.
# Complete the missing method to understand how the class works.


class BaseCharacter:
    """A basic character class - study this structure!"""

    def __init__(self, name, role, level=1):
        """Initialize a character with name, role, and level."""
        self.name = name
        self.role = role
        self.level = level
        self.experience = 0

    def gain_experience(self, amount):
        """
        Add experience points to the character.

        Args:
            amount: Experience points to add

        The character levels up when experience reaches level * 100.
        When leveling up:
        - Increase level by 1
        - Reset experience to 0
        - Print a level up message
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_1}}
        #
        # Step 1: Add amount to self.experience
        #
        # Step 2: Calculate experience needed: self.level * 100
        #
        # Step 3: If experience >= needed:
        #         - Increase self.level by 1
        #         - Set self.experience to 0
        #         - Print: "[name] leveled up to [level]!"

        pass

    def get_info(self):
        """Return character info as a formatted string."""
        return f"{self.name} ({self.role}) - Level {self.level}, XP: {self.experience}"


def part1_test_base_character():
    """Test the BaseCharacter class with your completed method."""
    print(">>> PART 1: Testing BaseCharacter...")
    print()

    hero = BaseCharacter("{{hero}}", "{{ROLE_TITLE}}")
    print(hero.get_info())

    hero.gain_experience(50)
    print(f"After 50 XP: {hero.get_info()}")

    hero.gain_experience(60)  # Should trigger level up
    print(f"After 60 more XP: {hero.get_info()}")


# ============================================================
# PART 2: Growth - Add New Methods
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Now extend the character with combat abilities.


class CombatCharacter:
    """A character with combat capabilities."""

    def __init__(self, name, role, health=100, strength=10):
        """Initialize a combat character."""
        self.name = name
        self.role = role
        self.health = health
        self.max_health = health
        self.strength = strength
        self.is_defending = False

    # ✏️ ADD THESE METHODS ✏️
    #
    # Method 1: attack(self, target)
    #     Calculate damage: self.strength
    #     If target.is_defending, reduce damage by half (use integer division)
    #     Call target.take_damage(damage)
    #     Return the damage dealt

    # Method 2: take_damage(self, amount)
    #     Subtract amount from self.health
    #     Make sure health doesn't go below 0
    #     Set self.is_defending to False (defending ends after being hit)
    #     If health reaches 0, print: "[name] has been defeated!"

    # Method 3: defend(self)
    #     Set self.is_defending to True
    #     Print: "[name] takes a defensive stance!"

    # Method 4: get_status(self)
    #     Return: "[name]: [health]/[max_health] HP"

    pass  # Remove this line when you add methods


def part2_test_combat():
    """Test combat between characters."""
    print("\n>>> PART 2: Testing CombatCharacter...")
    print()

    hero = CombatCharacter("{{hero}}", "{{ROLE_TITLE}}", health=100, strength=15)
    enemy = CombatCharacter("{{villain}}", "Antagonist", health=80, strength=12)

    print(f"Initial: {hero.get_status()}")
    print(f"Initial: {enemy.get_status()}")

    print()
    damage = hero.attack(enemy)
    print(f"{{{{hero}}}} attacks for {damage} damage!")
    print(f"After attack: {enemy.get_status()}")

    print()
    enemy.defend()
    damage = hero.attack(enemy)
    print(f"{{{{hero}}}} attacks defending enemy for {damage} damage!")
    print(f"After attack: {enemy.get_status()}")


# ============================================================
# PART 3: Ownership - Create Your Own Class
# ============================================================
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# Design your own character class with unique abilities.


def part3_create_your_class():
    # ✏️ CREATE YOUR OWN CHARACTER CLASS ✏️
    #
    # Design a class for a specific type of character (e.g., healer,
    # ranged attacker, support). Include:
    #
    # Required:
    #     __init__ with at least 4 attributes
    #     At least 3 methods that operate on the character's state
    #     One method that interacts with another character object
    #
    # Ideas:
    #     - A healer with heal_ally(target) method
    #     - A character with a resource (mana, energy) that limits abilities
    #     - A character with buff/debuff abilities
    #
    # After defining your class:
    #     1. Create at least 2 instances
    #     2. Test all your methods
    #     3. Demonstrate the interaction method

    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("=" * 60)
    print()

    # Uncomment each part as you complete it:

    # print(">>> PART 1: Guidance - Complete the Method")
    # part1_test_base_character()

    # print()
    # print(">>> PART 2: Growth - Add Combat Methods")
    # part2_test_combat()

    # print()
    # print(">>> PART 3: Ownership - Create Your Own Class")
    # part3_create_your_class()

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
