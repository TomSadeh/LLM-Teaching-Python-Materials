"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise where {{hero}} discovers legacy code from
{{mentor}} and must understand, extend, and improve it through inheritance.

Programming concepts: inheritance, super(), method overriding, polymorphism
"""


# ============================================================
# PART 1: Discovery - Understand the Parent Class
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} left behind this class. Before extending it, you need to
# understand how it works. Study the code and complete the trace.


class BaseEntity:
    """The original entity class from {{mentor}}."""

    def __init__(self, name, health, level=1):
        self.name = name
        self.health = health
        self.max_health = health
        self.level = level

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        return self.health

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        return self.health

    def get_stats(self):
        return f"{self.name} (Lv.{self.level}) - HP: {self.health}/{self.max_health}"


def part1_trace_parent():
    # ✏️ TRACE THE EXECUTION ✏️
    #
    # Given this code:
    #     entity = BaseEntity("{{hero}}", 100, 5)
    #     entity.take_damage(30)
    #     entity.heal(15)
    #     entity.take_damage(100)
    #
    # Fill in the tracing table:
    # | Step | Operation       | self.health | Return Value |
    # |------|-----------------|-------------|--------------|
    # | 0    | __init__        |             |              |
    # | 1    | take_damage(30) |             |              |
    # | 2    | heal(15)        |             |              |
    # | 3    | take_damage(100)|             |              |
    #
    # Questions:
    # 1. Why does heal(15) not restore health to 100?
    # 2. What prevents health from going below 0?
    #
    # Write your completed table and answers as comments below:
    #

    pass


# ============================================================
# PART 2: Growth - Create First Subclass
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Create a specialized character class that inherits from BaseEntity.


def part2_first_subclass():
    # ✏️ CREATE THE WARRIOR SUBCLASS ✏️
    #
    # Define `Warrior` inheriting from BaseEntity with:
    #
    # __init__(self, name, health, level, strength):
    #     Call super().__init__ with name, health, level
    #     Add self.strength
    #
    # attack(self, target):
    #     target is another BaseEntity or subclass
    #     Deal damage equal to self.strength to target
    #     Print: "[name] attacks [target.name] for [strength] damage!"
    #     Return the target's remaining health
    #
    # get_stats(self):
    #     Override to include strength:
    #     Call super().get_stats() and add " | STR: [strength]"
    #
    # Test:
    #     warrior = Warrior("{{hero}}", 100, 5, 25)
    #     print(warrior.get_stats())
    #
    #     target = BaseEntity("Training Dummy", 60, 1)
    #     warrior.attack(target)
    #     print(target.get_stats())

    pass


# ============================================================
# PART 3: Growth - Create Second Subclass
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Create a different specialization with its own unique behavior.


def part3_second_subclass():
    # ✏️ CREATE THE MAGE SUBCLASS ✏️
    #
    # Define `Mage` inheriting from BaseEntity with:
    #
    # __init__(self, name, health, level, mana, spell_power):
    #     Call super().__init__ with name, health, level
    #     Add self.mana and self.spell_power
    #     Set self.max_mana = mana
    #
    # cast_spell(self, target, mana_cost=10):
    #     If self.mana < mana_cost:
    #         Print: "[name] has insufficient mana!"
    #         Return 0
    #     Else:
    #         Reduce self.mana by mana_cost
    #         Deal self.spell_power damage to target
    #         Print: "[name] casts a spell on [target.name] for [spell_power] damage!"
    #         Return the damage dealt
    #
    # rest(self):
    #     Restore 20 mana (not exceeding max_mana)
    #     Print: "[name] rests and recovers mana. Mana: [current]/[max]"
    #
    # get_stats(self):
    #     Override to include mana:
    #     Call super().get_stats() and add " | MP: [mana]/[max_mana]"
    #
    # Test:
    #     mage = Mage("{{heroine}}", 60, 5, 50, 30)
    #     print(mage.get_stats())
    #
    #     target = BaseEntity("Target", 100, 1)
    #     mage.cast_spell(target)
    #     mage.cast_spell(target)
    #     print(mage.get_stats())
    #     mage.rest()

    pass


# ============================================================
# PART 4: Ownership - Add Shared Functionality
# ============================================================
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# Create a party system that can work with any BaseEntity subclass.


def part4_party_system():
    # ✏️ CREATE THE PARTY CLASS ✏️
    #
    # Define `Party` (does NOT inherit from BaseEntity):
    #
    # __init__(self, name):
    #     self.name = name
    #     self.members = []  # List of BaseEntity objects
    #
    # add_member(self, entity):
    #     Append entity to members
    #     Print: "[entity.name] joined [party name]!"
    #
    # list_members(self):
    #     Print party name and all member stats
    #     Use each member's get_stats() method
    #
    # total_health(self):
    #     Return sum of all members' current health
    #
    # heal_all(self, amount):
    #     Call heal(amount) on each member
    #     Print: "Party healed for [amount]!"
    #
    # Test with mixed party:
    #     party = Party("{{group}}")
    #
    #     warrior = Warrior("{{hero}}", 100, 5, 25)
    #     mage = Mage("{{heroine}}", 60, 5, 50, 30)
    #     ally = BaseEntity("{{friend}}", 80, 3)
    #
    #     party.add_member(warrior)
    #     party.add_member(mage)
    #     party.add_member(ally)
    #
    #     party.list_members()  # Each shows their specialized stats!
    #
    #     # Simulate damage
    #     warrior.take_damage(30)
    #     mage.take_damage(20)
    #
    #     print(f"Total health: {party.total_health()}")
    #     party.heal_all(15)
    #     party.list_members()

    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("Inheritance Journey: Extending {{mentor}}'s Legacy")
    print("=" * 60)
    print()

    print(">>> PART 1: Discovery - Understand BaseEntity")
    print("(Study the code and complete the trace)")
    part1_trace_parent()
    print()

    print(">>> PART 2: Growth - Create Warrior Subclass")
    print("(Inherit from BaseEntity, add strength)")
    part2_first_subclass()
    print()

    print(">>> PART 3: Growth - Create Mage Subclass")
    print("(Different specialization with mana)")
    part3_second_subclass()
    print()

    print(">>> PART 4: Ownership - Build Party System")
    print("(Work with any BaseEntity subclass)")
    part4_party_system()

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
