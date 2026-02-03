"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll practice completing __init__ methods
to properly initialize object state. Understanding __init__ is
essential for creating well-structured classes.
"""


# ============================================================
# {{FUNCTION_1_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}


class Creature:
    """A creature that can be encountered at {{school}}."""

    def __init__(self, name, health, strength):
        """
        Initialize a new creature.

        Args:
            name: The creature's name (string)
            health: Starting health points (integer)
            strength: Attack power (integer)

        After initialization, the creature should have:
            - self.name set to the name parameter
            - self.health set to the health parameter
            - self.strength set to the strength parameter
            - self.is_alive set to True

        Examples:
            >>> creature = Creature("{{creature}}", 100, 25)
            >>> creature.name
            '{{creature}}'
            >>> creature.health
            100
            >>> creature.is_alive
            True
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_1}}
        #
        # Store each parameter as an instance attribute using self.
        # Also set self.is_alive to True (not passed as parameter).

        pass


# ============================================================
# {{FUNCTION_2_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}


class Inventory:
    """An inventory system for holding items."""

    def __init__(self, owner, capacity=10):
        """
        Initialize an empty inventory for a character.

        Args:
            owner: Name of the inventory owner (string)
            capacity: Maximum items the inventory can hold (default 10)

        After initialization, the inventory should have:
            - self.owner set to the owner parameter
            - self.capacity set to the capacity parameter
            - self.items set to an empty list []
            - self.gold set to 0

        Examples:
            >>> inv = Inventory("{{hero}}")
            >>> inv.owner
            '{{hero}}'
            >>> inv.items
            []
            >>> inv.capacity
            10
            >>> inv = Inventory("{{heroine}}", capacity=20)
            >>> inv.capacity
            20
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_2}}
        #
        # Set up the owner, capacity (from parameters), and
        # initialize items as empty list and gold as 0.

        pass


# ============================================================
# {{FUNCTION_3_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}


class QuestLog:
    """Tracks active and completed quests."""

    def __init__(self, character_name, max_active=5):
        """
        Initialize a new quest log.

        Args:
            character_name: Name of the character (string)
            max_active: Maximum concurrent active quests (default 5)

        After initialization, the quest log should have:
            - self.character_name set to character_name
            - self.max_active set to max_active
            - self.active_quests set to an empty list []
            - self.completed_quests set to an empty list []
            - self.total_quests_completed set to 0

        Examples:
            >>> log = QuestLog("{{hero}}")
            >>> log.character_name
            '{{hero}}'
            >>> log.active_quests
            []
            >>> log.completed_quests
            []
            >>> log.total_quests_completed
            0
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_3}}
        #
        # Initialize all five attributes as described above.
        # Some come from parameters, others start at fixed values.

        pass


# ============================================================
# {{FUNCTION_4_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_4_NARRATIVE}}


class SkillTree:
    """A skill tree for character progression."""

    def __init__(self, class_name, starting_points=0):
        """
        Initialize a skill tree for a character class.

        Args:
            class_name: The character's class (e.g., "{{ROLE_TITLE}}")
            starting_points: Skill points available to spend (default 0)

        After initialization:
            - self.class_name set to class_name
            - self.available_points set to starting_points
            - self.spent_points set to 0
            - self.unlocked_skills set to an empty dictionary {}
            - self.skill_levels set to an empty dictionary {}

        Examples:
            >>> tree = SkillTree("{{ROLE_TITLE}}", 5)
            >>> tree.class_name
            '{{ROLE_TITLE}}'
            >>> tree.available_points
            5
            >>> tree.unlocked_skills
            {}
        """
        # ✏️ COMPLETE THIS METHOD ✏️
        #
        # {{CONTEXT_FUNCTION_HINT_4}}
        #
        # Initialize all attributes. Note that some should be
        # empty dictionaries {} rather than empty lists [].

        pass


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
    creature = Creature("{{creature}}", 100, 25)
    if creature.name:
        print(f"Created: {creature.name}")
        print(f"  Health: {creature.health}")
        print(f"  Strength: {creature.strength}")
        print(f"  Alive: {creature.is_alive}")
    else:
        print("  (Complete the __init__ method)")

    print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
    inventory = Inventory("{{hero}}")
    if inventory.owner:
        print(f"Owner: {inventory.owner}")
        print(f"  Capacity: {inventory.capacity}")
        print(f"  Items: {inventory.items}")
        print(f"  Gold: {inventory.gold}")
    else:
        print("  (Complete the __init__ method)")

    print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
    quest_log = QuestLog("{{heroine}}", max_active=3)
    if quest_log.character_name:
        print(f"Quest log for: {quest_log.character_name}")
        print(f"  Max active: {quest_log.max_active}")
        print(f"  Active quests: {quest_log.active_quests}")
        print(f"  Completed: {quest_log.total_quests_completed}")
    else:
        print("  (Complete the __init__ method)")

    print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
    skill_tree = SkillTree("{{ROLE_TITLE}}", 10)
    if skill_tree.class_name:
        print(f"Skill tree for: {skill_tree.class_name}")
        print(f"  Available points: {skill_tree.available_points}")
        print(f"  Spent points: {skill_tree.spent_points}")
        print(f"  Unlocked skills: {skill_tree.unlocked_skills}")
    else:
        print("  (Complete the __init__ method)")

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
