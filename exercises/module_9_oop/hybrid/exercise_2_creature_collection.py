"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part exercise where you build a {{creature}} management
system using classes. You'll create creatures, display them, manage
collections, and implement interactions.

Programming concepts: classes, __str__, object collections, interactions
"""


# ============================================================
# PART 1: Growth - Create the Base Creature Class
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Start by creating a class to represent a single creature.


def part1_base_creature():
    # ✏️ CREATE THE CREATURE CLASS ✏️
    #
    # Define a class called `Creature` with:
    #
    # __init__(self, name, species, power, health):
    #     Store all as instance attributes
    #     Also set self.is_tamed = False
    #
    # tame(self):
    #     Set self.is_tamed to True
    #     Print: "[name] has been tamed!"
    #
    # Test your class:
    #     creature = Creature("Fang", "{{creature}}", 45, 80)
    #     print(f"Name: {creature.name}")
    #     print(f"Species: {creature.species}")
    #     print(f"Tamed: {creature.is_tamed}")
    #     creature.tame()
    #     print(f"Tamed: {creature.is_tamed}")

    pass


# ============================================================
# PART 2: Growth - Add String Representation
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Add a __str__ method to display creature information nicely.


def part2_str_method():
    # ✏️ ENHANCE THE CREATURE CLASS WITH __str__ ✏️
    #
    # Copy your Creature class from Part 1 and add:
    #
    # __str__(self):
    #     If tamed: "[name] the [species] (Power: [power], HP: [health]) [TAMED]"
    #     If wild: "[name] the [species] (Power: [power], HP: [health]) [WILD]"
    #
    # Test:
    #     creature1 = Creature("Fang", "{{creature}}", 45, 80)
    #     print(creature1)  # Should show [WILD]
    #
    #     creature1.tame()
    #     print(creature1)  # Should show [TAMED]

    pass


# ============================================================
# PART 3: Growth - Create a Collection Class
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Create a class to manage multiple creatures.


def part3_collection():
    # ✏️ CREATE THE COLLECTION CLASS ✏️
    #
    # First, keep your Creature class from Part 2.
    #
    # Then define a class called `CreatureCollection` with:
    #
    # __init__(self, owner_name):
    #     self.owner_name = owner_name
    #     self.creatures = []  # List of Creature objects
    #
    # add_creature(self, creature):
    #     Append the creature to self.creatures
    #     Print: "[owner_name] added [creature.name] to collection!"
    #
    # list_creatures(self):
    #     Print: "[owner_name]'s Creatures:"
    #     For each creature in self.creatures:
    #         Print the creature (uses __str__)
    #     If no creatures: Print "  (empty)"
    #
    # count_tamed(self):
    #     Return the count of creatures where is_tamed is True
    #
    # Test:
    #     collection = CreatureCollection("{{hero}}")
    #     collection.add_creature(Creature("Fang", "{{creature}}", 45, 80))
    #     collection.add_creature(Creature("Spark", "{{creature}}", 30, 60))
    #     collection.list_creatures()
    #     print(f"Tamed: {collection.count_tamed()}")

    pass


# ============================================================
# PART 4: Ownership - Add Creature Interaction
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# Add the ability for creatures to battle each other.


def part4_interaction():
    # ✏️ ADD BATTLE INTERACTION ✏️
    #
    # Enhance your Creature class with:
    #
    # battle(self, other):
    #     - other is another Creature object
    #     - Compare power levels:
    #         If self.power > other.power:
    #             Reduce other.health by (self.power - other.power)
    #             Return self (the winner)
    #         Else if other.power > self.power:
    #             Reduce self.health by (other.power - self.power)
    #             Return other (the winner)
    #         Else:
    #             Return None (tie)
    #     - Print the battle result
    #
    # Add to CreatureCollection:
    #
    # find_strongest(self):
    #     Return the creature with highest power (or None if empty)
    #
    # Test battles:
    #     creature1 = Creature("Fang", "{{creature}}", 45, 80)
    #     creature2 = Creature("Spark", "{{creature}}", 30, 60)
    #
    #     winner = creature1.battle(creature2)
    #     if winner:
    #         print(f"Winner: {winner.name}")
    #
    #     print(f"After battle:")
    #     print(creature1)
    #     print(creature2)
    #
    # Test find_strongest:
    #     collection = CreatureCollection("{{hero}}")
    #     # Add several creatures...
    #     strongest = collection.find_strongest()
    #     print(f"Strongest: {strongest.name if strongest else 'None'}")

    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("Building a {{creature}} Management System")
    print("=" * 60)
    print()

    print(">>> PART 1: Base Creature Class")
    print("(Create the basic Creature class)")
    part1_base_creature()
    print()

    print(">>> PART 2: String Representation")
    print("(Add __str__ for nice display)")
    part2_str_method()
    print()

    print(">>> PART 3: Collection Management")
    print("(Create CreatureCollection class)")
    part3_collection()
    print()

    print(">>> PART 4: Creature Interactions")
    print("(Add battle and find_strongest)")
    part4_interaction()

    print()
    print("=" * 60)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
