"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn how objects can interact with each other.
Methods can take other objects as parameters, allowing objects to
communicate and affect each other's state.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create two classes that interact with each other.
    #
    # Step 1: Define a class called `Character` with __init__ that takes:
    #         - self, name, gold=0
    #         Store as instance attributes.
    #
    # Step 2: Add a method `give_gold(self, other, amount)`:
    #         - other is another Character object
    #         - If self.gold >= amount:
    #             Subtract amount from self.gold
    #             Add amount to other.gold
    #             Return True
    #         - Otherwise return False
    #
    # Step 3: Test the interaction:
    #         hero = Character("{{hero}}", 100)
    #         friend = Character("{{friend}}", 20)
    #
    #         print(f"{hero.name}: {hero.gold} gold")
    #         print(f"{friend.name}: {friend.gold} gold")
    #
    #         hero.give_gold(friend, 30)
    #
    #         print(f"After transfer:")
    #         print(f"{hero.name}: {hero.gold} gold")
    #         print(f"{friend.name}: {friend.gold} gold")
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create objects that affect each other's state.
    #
    # Step 1: Define a class called `Combatant` with __init__:
    #         - self, name, health, attack_power
    #         Store all as instance attributes.
    #         Also add: self.is_alive = True
    #
    # Step 2: Add an `attack(self, target)` method:
    #         - target is another Combatant object
    #         - Reduce target.health by self.attack_power
    #         - If target.health <= 0:
    #             Set target.health = 0
    #             Set target.is_alive = False
    #         - Print: "[self.name] attacks [target.name] for [power] damage!"
    #
    # Step 3: Add a `get_status(self)` method:
    #         - Return: "[name]: [health] HP (Alive)" or "(Defeated)"
    #
    # Step 4: Simulate a battle:
    #         hero = Combatant("{{hero}}", 100, 25)
    #         enemy = Combatant("{{villain}}", 60, 15)
    #
    #         while hero.is_alive and enemy.is_alive:
    #             hero.attack(enemy)
    #             if enemy.is_alive:
    #                 enemy.attack(hero)
    #             print(f"  {hero.get_status()}")
    #             print(f"  {enemy.get_status()}")
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class that manages a collection of other objects.
    #
    # Step 1: Define a class called `Item` with __init__:
    #         - self, name, value
    #         Store as instance attributes.
    #
    # Step 2: Define a class called `Shop` with __init__:
    #         - self, name
    #         Set self.name = name
    #         Set self.inventory = []  (list of Item objects)
    #
    # Step 3: Add `add_item(self, item)` to Shop:
    #         - item is an Item object
    #         - Append it to self.inventory
    #
    # Step 4: Add `sell_to(self, item_name, buyer)` to Shop:
    #         - buyer is a Character object (has .gold attribute)
    #         - Find the item with matching name in self.inventory
    #         - If found and buyer.gold >= item.value:
    #             Remove item from inventory
    #             Subtract value from buyer.gold
    #             Return the item
    #         - Otherwise return None
    #
    # Step 5: Test the shop:
    #         shop = Shop("{{location}}")
    #         shop.add_item(Item("{{item}}", 50))
    #         shop.add_item(Item("{{spell1}}", 30))
    #
    #         buyer = Character("{{hero}}", 100)
    #         purchased = shop.sell_to("{{item}}", buyer)
    #         if purchased:
    #             print(f"Bought {purchased.name}!")
    #             print(f"Gold remaining: {buyer.gold}")
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a more complex interaction between objects.
    #
    # Step 1: Define a class called `Healer` with:
    #         - __init__(self, name, heal_power, energy)
    #         Store all as instance attributes.
    #
    # Step 2: Add `heal(self, target)` method:
    #         - target is any object with a .health and .max_health attribute
    #         - If self.energy >= 10:
    #             Subtract 10 from self.energy
    #             Add self.heal_power to target.health
    #             If target.health > target.max_health:
    #                 Set target.health = target.max_health
    #             Print: "[self.name] heals [target.name] for [amount]!"
    #             Return the amount healed
    #         - Otherwise:
    #             Print: "[self.name] has no energy!"
    #             Return 0
    #
    # Step 3: Define a class called `Warrior` with:
    #         - __init__(self, name, health, max_health)
    #         Store all as instance attributes.
    #
    # Step 4: Test healing interaction:
    #         healer = Healer("{{heroine}}", 30, 50)
    #         warrior = Warrior("{{hero}}", 40, 100)
    #
    #         print(f"{warrior.name}: {warrior.health}/{warrior.max_health}")
    #         healer.heal(warrior)
    #         print(f"{warrior.name}: {warrior.health}/{warrior.max_health}")
    #         healer.heal(warrior)
    #         print(f"{warrior.name}: {warrior.health}/{warrior.max_health}")
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    exercise_c()

    print("\n=== {{PHASE_4_TITLE}} ===")
    exercise_d()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
