"""
{{CONTEXT_COMPARISON_INTRO}}
{{CONTEXT_COMPARISON_DECISION}}

The great debate: When should you use classes vs dictionaries and functions?
Both approaches can solve the same problems, but each has trade-offs.
"""


# ============================================================
# {{APPROACH_1_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_1_NARRATIVE}}

# Procedural approach using dictionaries and functions


def create_character_proc(name, health, power):
    """Create a character as a dictionary."""
    return {
        "name": name,
        "health": health,
        "max_health": health,
        "power": power
    }


def take_damage_proc(character, amount):
    """Apply damage to a character dictionary."""
    character["health"] = max(0, character["health"] - amount)
    return character["health"]


def heal_proc(character, amount):
    """Heal a character dictionary."""
    max_h = character["max_health"]
    character["health"] = min(max_h, character["health"] + amount)
    return character["health"]


def is_alive_proc(character):
    """Check if character is alive."""
    return character["health"] > 0


def get_status_proc(character):
    """Get character status string."""
    return f"{character['name']}: {character['health']}/{character['max_health']} HP"


# ============================================================
# {{APPROACH_2_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_2_NARRATIVE}}

# Object-Oriented approach using a class


class CharacterOOP:
    """A character represented as an object."""

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.max_health = health
        self.power = power

    def take_damage(self, amount):
        """Apply damage to this character."""
        self.health = max(0, self.health - amount)
        return self.health

    def heal(self, amount):
        """Heal this character."""
        self.health = min(self.max_health, self.health + amount)
        return self.health

    def is_alive(self):
        """Check if this character is alive."""
        return self.health > 0

    def get_status(self):
        """Get status string."""
        return f"{self.name}: {self.health}/{self.max_health} HP"


def comparison_1():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # {{CONTEXT_ANALYSIS_PROMPT}}

    analysis = """
    For a SIMPLE character system (just name, health, basic actions):

    Better approach: ??? (Procedural OR OOP)

    Reasons:
    1.
    2.

    Lines of code comparison:
    - Procedural:
    - OOP:

    Which is easier to read?
    -
    """
    return analysis


# ============================================================
# COMPARISON 2: COMPLEX DATA
# ============================================================

# Procedural approach for inventory


def create_inventory_proc(owner, capacity):
    """Create an inventory as a dictionary."""
    return {
        "owner": owner,
        "capacity": capacity,
        "items": {},
        "gold": 0
    }


def add_item_proc(inventory, item_name, count=1):
    """Add item to inventory."""
    current = inventory["items"].get(item_name, 0)
    total_items = sum(inventory["items"].values())
    if total_items + count <= inventory["capacity"]:
        inventory["items"][item_name] = current + count
        return True
    return False


def remove_item_proc(inventory, item_name, count=1):
    """Remove item from inventory."""
    current = inventory["items"].get(item_name, 0)
    if current >= count:
        inventory["items"][item_name] = current - count
        if inventory["items"][item_name] == 0:
            del inventory["items"][item_name]
        return True
    return False


def add_gold_proc(inventory, amount):
    """Add gold to inventory."""
    inventory["gold"] += amount


def get_inventory_str_proc(inventory):
    """Get inventory as string."""
    items_str = ", ".join(f"{k}: {v}" for k, v in inventory["items"].items())
    return f"{inventory['owner']}'s inventory ({items_str}) - {inventory['gold']} gold"


# OOP approach for inventory


class InventoryOOP:
    """An inventory represented as an object."""

    def __init__(self, owner, capacity):
        self.owner = owner
        self.capacity = capacity
        self.items = {}
        self.gold = 0

    def add_item(self, item_name, count=1):
        """Add item to inventory."""
        current = self.items.get(item_name, 0)
        total_items = sum(self.items.values())
        if total_items + count <= self.capacity:
            self.items[item_name] = current + count
            return True
        return False

    def remove_item(self, item_name, count=1):
        """Remove item from inventory."""
        current = self.items.get(item_name, 0)
        if current >= count:
            self.items[item_name] = current - count
            if self.items[item_name] == 0:
                del self.items[item_name]
            return True
        return False

    def add_gold(self, amount):
        """Add gold to inventory."""
        self.gold += amount

    def __str__(self):
        items_str = ", ".join(f"{k}: {v}" for k, v in self.items.items())
        return f"{self.owner}'s inventory ({items_str}) - {self.gold} gold"


def comparison_2():
    # ✏️ YOUR ANALYSIS ✏️

    analysis = """
    For a MORE COMPLEX system (inventory with multiple operations):

    Better approach: ??? (Procedural OR OOP)

    Key differences:
    1. In procedural, you must pass 'inventory' to every function
    2. In OOP, methods know which inventory they belong to (self)

    Which is easier to extend with new features?
    -

    Which is harder to make mistakes with (e.g., passing wrong data)?
    -

    What if we had 10 different functions/methods? Which scales better?
    -
    """
    return analysis


# ============================================================
# COMPARISON 3: TYPE CHECKING AND SAFETY
# ============================================================


def comparison_3():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Consider this procedural code:
    #     char = create_character_proc("{{hero}}", 100, 20)
    #     inv = create_inventory_proc("{{hero}}", 10)
    #
    #     # Oops! Wrong function for wrong data
    #     take_damage_proc(inv, 50)  # This might crash or corrupt data!
    #
    # Now consider OOP:
    #     char = CharacterOOP("{{hero}}", 100, 20)
    #     inv = InventoryOOP("{{hero}}", 10)
    #
    #     # Can't accidentally call wrong method
    #     # inv.take_damage(50)  # Error: InventoryOOP has no take_damage

    analysis = """
    Type safety comparison:

    In procedural code, what could go wrong?
    1.
    2.

    How does OOP help prevent these errors?
    1.
    2.

    This illustrates the OOP benefit of:
    - (hint: binding data and behavior together)
    """
    return analysis


# ============================================================
# WHEN TO USE EACH
# ============================================================


def final_analysis():
    # ✏️ YOUR FINAL ANALYSIS ✏️

    analysis = """
    Use PROCEDURAL (dictionaries + functions) when:
    1. Data is simple (few fields, few operations)
    2. You need quick prototyping
    3.

    Use OOP (classes) when:
    1. Data and behavior are closely related
    2. You have multiple instances with the same operations
    3.

    General guideline:
    -
    """
    return analysis


def main():
    print("{{CONTEXT_COMPARISON_INTRO}}")
    print("=" * 50)

    print("\n=== Comparison 1: Simple Character ===")
    print()

    # Procedural
    hero_p = create_character_proc("{{hero}}", 100, 20)
    take_damage_proc(hero_p, 30)
    print(f"Procedural: {get_status_proc(hero_p)}")

    # OOP
    hero_o = CharacterOOP("{{hero}}", 100, 20)
    hero_o.take_damage(30)
    print(f"OOP: {hero_o.get_status()}")

    print(f"\nYour analysis:{comparison_1()}")

    print("\n=== Comparison 2: Complex Inventory ===")
    print()

    # Procedural
    inv_p = create_inventory_proc("{{hero}}", 10)
    add_item_proc(inv_p, "{{item}}", 3)
    add_gold_proc(inv_p, 50)
    print(f"Procedural: {get_inventory_str_proc(inv_p)}")

    # OOP
    inv_o = InventoryOOP("{{hero}}", 10)
    inv_o.add_item("{{item}}", 3)
    inv_o.add_gold(50)
    print(f"OOP: {inv_o}")

    print(f"\nYour analysis:{comparison_2()}")

    print("\n=== Comparison 3: Type Safety ===")
    print(f"\nYour analysis:{comparison_3()}")

    print("\n=== When to Use Each ===")
    print(f"\nYour analysis:{final_analysis()}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_EVALUATION_COMPLETE}}")


main()
