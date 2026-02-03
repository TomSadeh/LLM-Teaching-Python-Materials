"""
{{CONTEXT_COMPARISON_INTRO}}
{{CONTEXT_COMPARISON_DECISION}}

In this exercise, you'll analyze different class design approaches.
Both versions work correctly, but they have different trade-offs.
Evaluate which is better for different situations.
"""


# ============================================================
# {{APPROACH_1_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_1_NARRATIVE}}

# Design A: One class does everything


class CharacterAllInOneA:
    """Single class with all functionality built in."""

    def __init__(self, name, health, mana, strength, magic):
        self.name = name
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.strength = strength
        self.magic = magic

    def physical_attack(self, target):
        damage = self.strength
        target.health -= damage
        return damage

    def magic_attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            damage = self.magic
            target.health -= damage
            return damage
        return 0

    def heal_self(self):
        if self.mana >= 15:
            self.mana -= 15
            heal = self.magic // 2
            self.health = min(self.max_health, self.health + heal)
            return heal
        return 0


# ============================================================
# {{APPROACH_2_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_2_NARRATIVE}}

# Design B: Specialized classes through inheritance


class CharacterBaseB:
    """Base class with common functionality."""

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health


class WarriorB(CharacterBaseB):
    """Specialized for physical combat."""

    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def physical_attack(self, target):
        damage = self.strength
        target.health -= damage
        return damage


class MageB(CharacterBaseB):
    """Specialized for magic."""

    def __init__(self, name, health, mana, magic):
        super().__init__(name, health)
        self.mana = mana
        self.max_mana = mana
        self.magic = magic

    def magic_attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            damage = self.magic
            target.health -= damage
            return damage
        return 0

    def heal_self(self):
        if self.mana >= 15:
            self.mana -= 15
            heal = self.magic // 2
            self.health = min(self.max_health, self.health + heal)
            return heal
        return 0


def analysis_1():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # {{CONTEXT_ANALYSIS_PROMPT}}
    # Consider: {{CONTEXT_DECISION_GUIDANCE}}

    analysis = """
    Better design: ??? (A: All-in-one OR B: Specialized classes)

    Advantages of Design A (All-in-one):
    1.
    2.

    Advantages of Design B (Specialized):
    1.
    2.

    Design A is better when:
    -

    Design B is better when:
    -

    If I needed to add a new character type (Paladin with both
    strength AND magic), which would be easier to extend?
    -
    """
    return analysis


# ============================================================
# COMPARISON 2: ATTRIBUTE STORAGE
# ============================================================


# Design C: Direct attributes


class InventoryDirectC:
    """Stores items as a simple list."""

    def __init__(self, owner):
        self.owner = owner
        self.item_names = []
        self.item_counts = []

    def add_item(self, name, count=1):
        if name in self.item_names:
            index = self.item_names.index(name)
            self.item_counts[index] += count
        else:
            self.item_names.append(name)
            self.item_counts.append(count)

    def get_count(self, name):
        if name in self.item_names:
            index = self.item_names.index(name)
            return self.item_counts[index]
        return 0


# Design D: Using a dictionary


class InventoryDictD:
    """Stores items in a dictionary."""

    def __init__(self, owner):
        self.owner = owner
        self.items = {}  # name -> count

    def add_item(self, name, count=1):
        self.items[name] = self.items.get(name, 0) + count

    def get_count(self, name):
        return self.items.get(name, 0)


def analysis_2():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Both designs store the same data. Which is better?

    analysis = """
    Better design: ??? (C: Parallel lists OR D: Dictionary)

    Why Design C is problematic:
    1.
    2.

    Why Design D is better:
    1.
    2.

    The main lesson here is:
    -
    """
    return analysis


# ============================================================
# COMPARISON 3: METHOD PLACEMENT
# ============================================================


# Design E: Methods that operate ON the object


class BattleCharacterE:
    """Character with methods that modify self."""

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        """This character attacks the target."""
        target.health -= self.power

    def take_damage(self, amount):
        """This character takes damage."""
        self.health -= amount


# Design F: External functions


class BattleCharacterF:
    """Character as pure data container."""

    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power


def attack_f(attacker, target):
    """External function to handle attack."""
    target.health -= attacker.power


def take_damage_f(character, amount):
    """External function to handle damage."""
    character.health -= amount


def analysis_3():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Same functionality, but methods are inside vs outside the class.

    analysis = """
    Better design: ??? (E: Methods inside OR F: Functions outside)

    Why OOP (Design E) is typically preferred:
    1.
    2.

    When external functions (Design F) might be appropriate:
    1.
    2.

    The principle this illustrates (hint: encapsulation):
    -
    """
    return analysis


def main():
    print("{{CONTEXT_COMPARISON_INTRO}}")
    print("=" * 50)

    print("\n=== Comparison 1: All-in-One vs Specialized ===")
    print()

    # Both designs work
    char_a = CharacterAllInOneA("{{hero}}", 100, 50, 20, 30)
    warrior_b = WarriorB("{{hero}}", 100, 20)

    dummy = CharacterAllInOneA("Dummy", 100, 0, 0, 0)
    print(f"Design A - Physical attack: {char_a.physical_attack(dummy)}")

    dummy2 = CharacterBaseB("Dummy", 100)
    print(f"Design B - Physical attack: {warrior_b.physical_attack(dummy2)}")

    print(f"\nYour analysis:{analysis_1()}")

    print("\n=== Comparison 2: Parallel Lists vs Dictionary ===")
    print()

    inv_c = InventoryDirectC("{{hero}}")
    inv_c.add_item("{{item}}", 3)
    inv_c.add_item("{{spell1}}", 1)
    print(f"Design C - {{{{item}}}} count: {inv_c.get_count('{{item}}')}")

    inv_d = InventoryDictD("{{hero}}")
    inv_d.add_item("{{item}}", 3)
    inv_d.add_item("{{spell1}}", 1)
    print(f"Design D - {{{{item}}}} count: {inv_d.get_count('{{item}}')}")

    print(f"\nYour analysis:{analysis_2()}")

    print("\n=== Comparison 3: Methods Inside vs Outside ===")
    print()
    print(f"Your analysis:{analysis_3()}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_EVALUATION_COMPLETE}}")


main()
