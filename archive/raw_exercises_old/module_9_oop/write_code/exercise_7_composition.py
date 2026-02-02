# Exercise 7: Composition - Objects Containing Objects!
#
# Composition is when objects CONTAIN other objects.
# A Character HAS an Inventory, HAS a list of Spells, HAS Equipment...


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create separate classes and combine them:
    #
    # class Spell:
    #     def __init__(self, name, power):
    #         self.name = name
    #         self.power = power
    #
    # class Wizard:
    #     def __init__(self, name):
    #         self.name = name
    #         self.spells = []  # Will hold Spell objects!
    #
    #     def learn_spell(self, spell):
    #         self.spells.append(spell)
    #
    # lumos = Spell("{{spell1}}", 10)
    # wizard = Wizard("{{hero}}")
    # wizard.learn_spell(lumos)
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create an Equipment class and a Character that HAS equipment:
    # - Equipment has: name, defense_bonus, attack_bonus
    # - Character has: weapon (Equipment), armor (Equipment)
    # Character's total attack = base_attack + weapon.attack_bonus
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Party class that contains multiple Characters:
    # - party.add_member(character)
    # - party.remove_member(name)
    # - party.show_members()
    # - party.total_health() - sum of all member health
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a School with Houses with Students!
    # School has: name, list of House objects
    # House has: name, list of Student objects
    # Student has: name, year
    #
    # school.add_house(house)
    # house.add_student(student)
    # school.count_students() - total across all houses
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Quest system:
    # - Objective class: description, is_complete
    # - Quest class: name, list of Objectives, reward
    # - quest.complete_objective(index)
    # - quest.is_finished() - True when all objectives complete
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Create a complete RPG Character:
    # - Stats class: strength, intelligence, agility
    # - Inventory class: list of items, gold
    # - Character class: name, Stats, Inventory, health
    # The Character uses its Stats to calculate damage!
    pass


class ExampleGameSystem:
    """A complete game system using composition"""

    class Item:
        def __init__(self, name, item_type, value):
            self.name = name
            self.item_type = item_type
            self.value = value

        def __str__(self):
            return f"{self.name} ({self.item_type})"

    class Inventory:
        def __init__(self):
            self.items = []
            self.gold = 0

        def add_item(self, item):
            self.items.append(item)
            print(f"Added {item.name} to inventory!")

        def show(self):
            print("=== Inventory ===")
            for item in self.items:
                print(f"  - {item}")
            print(f"  Gold: {self.gold}")

    class Character:
        def __init__(self, name):
            self.name = name
            self.health = 100
            self.inventory = ExampleGameSystem.Inventory()  # HAS an inventory

        def pick_up(self, item):
            self.inventory.add_item(item)

        def show_status(self):
            print(f"\n=== {self.name} ===")
            print(f"Health: {self.health}")
            self.inventory.show()


def show_example():
    Item = ExampleGameSystem.Item
    Character = ExampleGameSystem.Character

    # Create a character with their own inventory
    hero = Character("{{hero}}")

    # Create items
    wand = Item("{{item}}", "weapon", 100)
    potion = Item("{{item}}", "consumable", 25)

    # Character picks up items (adds to their inventory)
    hero.pick_up(wand)
    hero.pick_up(potion)
    hero.inventory.gold = 50

    hero.show_status()


def main():
    print("=== Exercise A: Spell Collection ===")
    exercise_a()

    print("\n=== Exercise B: Equipment System ===")
    exercise_b()

    print("\n=== Exercise C: Adventure Party ===")
    exercise_c()

    print("\n=== Exercise D: Nested Organization ===")
    exercise_d()

    print("\n=== Exercise E: Quest System ===")
    exercise_e()

    print("\n=== Exercise F: Complete Character ===")
    exercise_f()

    print("\n=== Example Game System ===")
    show_example()


main()
