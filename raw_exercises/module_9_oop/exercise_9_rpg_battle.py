# Exercise 9: Build a Complete RPG Battle System!
#
# Create a turn-based battle game using everything you've learned!

import random


# =====================
# BASE CHARACTER CLASS
# =====================

class Character:
    """Base class for all characters"""

    def __init__(self, name, health=100, attack_power=10):
        # ✏️ YOUR CODE HERE ✏️
        # Set up: name, health, max_health, attack_power, is_defending
        pass

    def attack(self, target):
        # ✏️ YOUR CODE HERE ✏️
        # Calculate damage (reduced if target is defending)
        # Apply damage to target
        # Reset target's defending status
        # Return the damage dealt
        pass

    def defend(self):
        # ✏️ YOUR CODE HERE ✏️
        # Set is_defending to True
        pass

    def is_alive(self):
        # ✏️ YOUR CODE HERE ✏️
        pass

    def __str__(self):
        # ✏️ YOUR CODE HERE ✏️
        # Return a health bar like: "{{hero}} [████████░░] 80/100 HP"
        pass


# =====================
# SPECIALIZED CLASSES
# =====================

class Wizard(Character):
    """A wizard who can cast spells"""

    def __init__(self, name, health=80, attack_power=8):
        # ✏️ YOUR CODE HERE ✏️
        # Call super().__init__
        # Add mana = 100
        pass

    def cast_spell(self, spell_name, target):
        # ✏️ YOUR CODE HERE ✏️
        # Different spells with different effects and mana costs:
        # - "{{spell2}}" (15 mana): 25 damage
        # - "{{spell3}}" (30 mana): 40 damage
        # - "{{spell1}}" (5 mana): just for show, no damage
        # Return True if spell was cast, False if not enough mana
        pass


class Warrior(Character):
    """A warrior who builds rage for powerful attacks"""

    def __init__(self, name, health=120, attack_power=12):
        # ✏️ YOUR CODE HERE ✏️
        # Call super().__init__
        # Add rage = 0
        pass

    def attack(self, target):
        # ✏️ YOUR CODE HERE ✏️
        # Normal attack + gain 20 rage
        pass

    def power_attack(self, target):
        # ✏️ YOUR CODE HERE ✏️
        # Requires 50 rage
        # Deals 2.5x damage!
        # Uses all rage
        pass


class Healer(Character):
    """A healer who can restore health"""

    def __init__(self, name, health=90, attack_power=6):
        # ✏️ YOUR CODE HERE ✏️
        # Add faith = 100
        pass

    def heal(self, target):
        # ✏️ YOUR CODE HERE ✏️
        # Costs 20 faith
        # Heals 30 health (not above max_health!)
        pass


# =====================
# BATTLE SYSTEM
# =====================

class Battle:
    """Manages a battle between two characters"""

    def __init__(self, player, enemy):
        # ✏️ YOUR CODE HERE ✏️
        pass

    def show_status(self):
        # ✏️ YOUR CODE HERE ✏️
        # Print both characters' status
        pass

    def player_turn(self):
        # ✏️ YOUR CODE HERE ✏️
        # Show options based on player class:
        # All: Attack, Defend
        # Wizard: Cast Spell
        # Warrior: Power Attack (if rage >= 50)
        # Healer: Heal
        # Get player choice and execute
        pass

    def enemy_turn(self):
        # ✏️ YOUR CODE HERE ✏️
        # Simple AI: random choice between attack and defend
        # Or smarter: defend when low health, attack otherwise
        pass

    def run(self):
        # ✏️ YOUR CODE HERE ✏️
        # Main battle loop:
        # While both alive:
        #   - Show status
        #   - Player turn
        #   - Check if enemy defeated
        #   - Enemy turn
        #   - Check if player defeated
        # Announce winner!
        pass


# =====================
# MAIN GAME
# =====================

def choose_character():
    """Let player choose their character class"""
    print("\nChoose your class:")
    print("1. Wizard (Low health, powerful spells)")
    print("2. Warrior (High health, builds rage)")
    print("3. Healer (Can heal, balanced stats)")

    choice = input("\nEnter 1, 2, or 3: ")
    name = input("Enter your name: ")

    if choice == "1":
        return Wizard(name)
    elif choice == "2":
        return Warrior(name)
    else:
        return Healer(name)


def main():
    print("=" * 50)
    print("   ⚔️  RPG BATTLE ARENA  ⚔️")
    print("=" * 50)

    # For testing - uncomment when classes are complete:
    # player = choose_character()
    # enemy = Warrior("{{villain}}", health=100, attack_power=15)
    # battle = Battle(player, enemy)
    # battle.run()

    print("\nComplete the classes above to play!")
    print("\nHere's a mini working example:\n")

    # Simple working demo
    class SimpleFighter:
        def __init__(self, name, hp):
            self.name = name
            self.hp = hp

        def hit(self, target, damage):
            target.hp -= damage
            print(f"{self.name} hits {target.name} for {damage}!")
            print(f"{target.name} has {target.hp} HP left")

    hero = SimpleFighter("{{hero}}", 100)
    villain = SimpleFighter("{{villain}}", 80)

    print("=== Quick Battle Demo ===")
    while hero.hp > 0 and villain.hp > 0:
        # Hero attacks
        hero.hit(villain, random.randint(10, 20))
        if villain.hp <= 0:
            break
        # Villain attacks
        villain.hit(hero, random.randint(8, 15))

    winner = hero if hero.hp > 0 else villain
    print(f"\n🏆 {winner.name} wins!")


main()
