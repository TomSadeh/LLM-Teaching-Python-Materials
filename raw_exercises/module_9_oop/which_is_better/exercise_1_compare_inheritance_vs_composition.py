# Exercise 1: Which is Better? - Inheritance vs Composition
#
# For each pair of solutions, both work correctly.
# Your job: Analyze and explain which is better AND WHY.
# Sometimes the answer is "it depends"!
#
# Theme: Designing magical beings for {{school}}


# ============================================================
# COMPARISON A: Character with Abilities
# ============================================================

# Version 1: Inheritance
class Character_A1:
    def __init__(self, name):
        self.name = name


class SpellCaster_A1(Character_A1):
    def cast_spell(self, spell):
        return f"{self.name} casts {spell}!"


# Version 2: Composition
class SpellAbility:
    def cast_spell(self, caster_name, spell):
        return f"{caster_name} casts {spell}!"


class Character_A2:
    def __init__(self, name, can_cast_spells=False):
        self.name = name
        self.spell_ability = SpellAbility() if can_cast_spells else None

    def cast_spell(self, spell):
        if self.spell_ability:
            return self.spell_ability.cast_spell(self.name, spell)
        return f"{self.name} cannot cast spells!"


def analysis_a():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: A1 (inheritance) or A2 (composition)?
    # Consider: flexibility, simplicity, adding new abilities

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use inheritance (A1):
    -

    When to use composition (A2):
    -
    """
    return analysis


# ============================================================
# COMPARISON B: Multiple Abilities
# ============================================================

# Version 1: Multiple Inheritance
class Flyer_B1:
    def fly(self):
        return f"{self.name} flies through the air!"


class Swimmer_B1:
    def swim(self):
        return f"{self.name} swims gracefully!"


class Dragon_B1(Character_A1, Flyer_B1):
    pass


class Mermaid_B1(Character_A1, Swimmer_B1):
    pass


# What if we want a creature that can both fly AND swim?
# class FlyingFish_B1(Character_A1, Flyer_B1, Swimmer_B1):
#     pass  # This works but gets complicated...


# Version 2: Composition with multiple abilities
class FlyAbility:
    def fly(self, creature_name):
        return f"{creature_name} flies through the air!"


class SwimAbility:
    def swim(self, creature_name):
        return f"{creature_name} swims gracefully!"


class Creature_B2:
    def __init__(self, name, abilities=None):
        self.name = name
        self.abilities = abilities or {}

    def fly(self):
        if "fly" in self.abilities:
            return self.abilities["fly"].fly(self.name)
        return f"{self.name} cannot fly!"

    def swim(self):
        if "swim" in self.abilities:
            return self.abilities["swim"].swim(self.name)
        return f"{self.name} cannot swim!"


def analysis_b():
    # ✏️ YOUR ANALYSIS ✏️
    # Which handles multiple abilities better?
    # Consider: diamond problem, flexibility, code reuse

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use multiple inheritance (B1):
    -

    When to use composition (B2):
    -
    """
    return analysis


# ============================================================
# COMPARISON C: Is-A vs Has-A Relationship
# ============================================================

# Version 1: Inheritance (Wizard IS-A Person)
class Person_C1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}!"


class Wizard_C1(Person_C1):
    def __init__(self, name, age, wand):
        super().__init__(name, age)
        self.wand = wand

    def cast(self):
        return f"{self.name} waves their {self.wand}!"


# Version 2: Composition (Wizard HAS-A Wand)
class Wand:
    def __init__(self, wood, core):
        self.wood = wood
        self.core = core

    def wave(self):
        return f"The {self.wood} wand with {self.core} core glows!"


class Wizard_C2:
    def __init__(self, name, age, wand):
        self.name = name
        self.age = age
        self.wand = wand  # Has-a relationship

    def greet(self):
        return f"Hello, I'm {self.name}!"

    def cast(self):
        return f"{self.name}: {self.wand.wave()}"


def analysis_c():
    # ✏️ YOUR ANALYSIS ✏️
    # Is a Wizard more of a "type of Person" or "has equipment"?
    # Consider: what changes, what stays the same

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When inheritance makes sense:
    -

    When composition makes sense:
    -
    """
    return analysis


# ============================================================
# COMPARISON D: Extending Behavior
# ============================================================

# Version 1: Override via inheritance
class Animal_D1:
    def speak(self):
        return "..."


class Dog_D1(Animal_D1):
    def speak(self):
        return "Woof!"


class Cat_D1(Animal_D1):
    def speak(self):
        return "Meow!"


# Version 2: Strategy pattern (composition)
class SpeakBehavior:
    def speak(self):
        return "..."


class WoofBehavior(SpeakBehavior):
    def speak(self):
        return "Woof!"


class MeowBehavior(SpeakBehavior):
    def speak(self):
        return "Meow!"


class Animal_D2:
    def __init__(self, name, speak_behavior):
        self.name = name
        self.speak_behavior = speak_behavior

    def speak(self):
        return self.speak_behavior.speak()

    def set_speak_behavior(self, new_behavior):
        """Can change behavior at runtime!"""
        self.speak_behavior = new_behavior


def analysis_d():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better for changing behavior?
    # Consider: runtime changes, testing, simplicity

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use method override (D1):
    -

    When to use strategy pattern (D2):
    -
    """
    return analysis


# ============================================================
# COMPARISON E: Real-World Scenario
# ============================================================

# Scenario: A game with characters, items, and abilities
# Version 1 would use deep inheritance hierarchies
# Version 2 uses composition for flexibility

# Version 2 example (preferred for games):
class GameEntity:
    def __init__(self, name):
        self.name = name
        self.components = {}

    def add_component(self, name, component):
        self.components[name] = component

    def get_component(self, name):
        return self.components.get(name)


class HealthComponent:
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = max_hp

    def take_damage(self, amount):
        self.current_hp = max(0, self.current_hp - amount)
        return self.current_hp

    def heal(self, amount):
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        return self.current_hp


class MagicComponent:
    def __init__(self, spells):
        self.spells = spells

    def cast(self, spell_name):
        if spell_name in self.spells:
            return f"Casting {spell_name}!"
        return f"Unknown spell: {spell_name}"


def analysis_e():
    # ✏️ YOUR ANALYSIS ✏️
    # For a game with many entity types, which approach scales better?
    # Consider: adding new features, combining behaviors, maintainability

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When deep inheritance works:
    -

    When component composition works:
    -
    """
    return analysis


def main():
    print("=== Comparison A: Character with Abilities ===")
    wizard1 = SpellCaster_A1("{{hero}}")
    print(f"Inheritance: {wizard1.cast_spell('{{spell1}}')}")

    wizard2 = Character_A2("{{hero}}", can_cast_spells=True)
    muggle = Character_A2("{{friend}}", can_cast_spells=False)
    print(f"Composition (wizard): {wizard2.cast_spell('{{spell1}}')}")
    print(f"Composition (non-wizard): {muggle.cast_spell('{{spell1}}')}")
    print(f"\nAnalysis:{analysis_a()}")

    print("\n=== Comparison B: Multiple Abilities ===")
    dragon = Dragon_B1("{{creature}}")
    print(f"Inheritance: {dragon.fly()}")

    flying_fish = Creature_B2("Flying Fish", {
        "fly": FlyAbility(),
        "swim": SwimAbility()
    })
    print(f"Composition (fly): {flying_fish.fly()}")
    print(f"Composition (swim): {flying_fish.swim()}")
    print(f"\nAnalysis:{analysis_b()}")

    print("\n=== Comparison C: Is-A vs Has-A ===")
    wizard3 = Wizard_C1("{{hero}}", 11, "Holly wand")
    print(f"Inheritance: {wizard3.cast()}")

    wand = Wand("Holly", "Phoenix feather")
    wizard4 = Wizard_C2("{{hero}}", 11, wand)
    print(f"Composition: {wizard4.cast()}")
    print(f"\nAnalysis:{analysis_c()}")

    print("\n=== Comparison D: Extending Behavior ===")
    dog1 = Dog_D1()
    print(f"Inheritance: {dog1.speak()}")

    dog2 = Animal_D2("Fido", WoofBehavior())
    print(f"Composition: {dog2.speak()}")
    dog2.set_speak_behavior(MeowBehavior())  # Change at runtime!
    print(f"After change: {dog2.speak()}")
    print(f"\nAnalysis:{analysis_d()}")

    print("\n=== Comparison E: Game Entity System ===")
    hero = GameEntity("{{hero}}")
    hero.add_component("health", HealthComponent(100))
    hero.add_component("magic", MagicComponent(["{{spell1}}", "{{spell2}}"]))

    health = hero.get_component("health")
    magic = hero.get_component("magic")
    print(f"Hero HP: {health.current_hp}")
    print(f"Take damage: {health.take_damage(30)} HP remaining")
    print(f"Cast spell: {magic.cast('{{spell1}}')}")
    print(f"\nAnalysis:{analysis_e()}")


main()
