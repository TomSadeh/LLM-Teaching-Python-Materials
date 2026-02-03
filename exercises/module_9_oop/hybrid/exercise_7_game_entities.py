"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part exercise where you build a complete game entity
hierarchy for {{school}}. You'll create base classes, player and enemy
subclasses, and implement combat interactions.

Programming concepts: inheritance, method overriding, polymorphism, composition
"""


# ============================================================
# PART 1: Growth - Create the Base Entity Class
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Start with a solid foundation for all game entities.


def part1_base_entity():
    # ✏️ CREATE THE BASE ENTITY CLASS ✏️
    #
    # class Entity:
    #     """Base class for all game entities."""
    #
    #     def __init__(self, name, health, position=(0, 0)):
    #         """
    #         Initialize an entity.
    #
    #         Args:
    #             name: Entity name
    #             health: Starting health (also sets max_health)
    #             position: (x, y) tuple for location
    #         """
    #         # Set name, health, max_health, position
    #         # Set is_alive = True
    #         pass
    #
    #     def take_damage(self, amount):
    #         """Reduce health by amount, minimum 0. Update is_alive."""
    #         pass
    #
    #     def heal(self, amount):
    #         """Restore health by amount, maximum max_health."""
    #         pass
    #
    #     def move_to(self, new_position):
    #         """Update position to new (x, y) tuple."""
    #         pass
    #
    #     def distance_to(self, other):
    #         """Calculate distance to another entity.
    #         Use: sqrt((x2-x1)^2 + (y2-y1)^2)
    #         Hint: import math, use math.sqrt
    #         """
    #         pass
    #
    #     def get_status(self):
    #         """Return status string."""
    #         pass
    #
    #     def __str__(self):
    #         """Return string representation."""
    #         pass
    #
    # Test:
    #     entity = Entity("{{hero}}", 100, (5, 5))
    #     print(entity)
    #     entity.take_damage(30)
    #     print(f"After damage: {entity.get_status()}")
    #     entity.move_to((10, 10))
    #     print(f"Position: {entity.position}")

    pass


# ============================================================
# PART 2: Growth - Create the Player Subclass
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Create a player class with inventory and experience.


def part2_player_class():
    # ✏️ CREATE THE PLAYER CLASS ✏️
    #
    # class Player(Entity):
    #     """A player-controlled entity."""
    #
    #     def __init__(self, name, health, position=(0, 0)):
    #         """Initialize player with experience system and inventory."""
    #         # Call super().__init__
    #         # Add: level = 1, experience = 0, inventory = []
    #         pass
    #
    #     def gain_experience(self, amount):
    #         """Add XP. Level up at 100 XP per level."""
    #         # Add amount to experience
    #         # While experience >= level * 100:
    #         #     Subtract level * 100 from experience
    #         #     Increment level
    #         #     Increase max_health by 10
    #         #     Restore health to full
    #         #     Print level up message
    #         pass
    #
    #     def pick_up_item(self, item_name):
    #         """Add item to inventory."""
    #         pass
    #
    #     def use_item(self, item_name):
    #         """Remove and return item from inventory, or None."""
    #         pass
    #
    #     def get_status(self):
    #         """Override to include level and XP."""
    #         pass
    #
    # Test:
    #     player = Player("{{hero}}", 100)
    #     player.pick_up_item("{{item}}")
    #     player.gain_experience(150)  # Should level up
    #     print(player.get_status())
    #     print(f"Inventory: {player.inventory}")

    pass


# ============================================================
# PART 3: Growth - Create the Enemy Subclass
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Create enemy types with different behaviors.


def part3_enemy_class():
    # ✏️ CREATE THE ENEMY CLASS ✏️
    #
    # class Enemy(Entity):
    #     """An AI-controlled hostile entity."""
    #
    #     def __init__(self, name, health, position, damage, xp_reward):
    #         """Initialize enemy with combat stats."""
    #         # Call super().__init__
    #         # Add: damage, xp_reward, aggro_range = 5.0
    #         pass
    #
    #     def attack(self, target):
    #         """Attack a target entity."""
    #         # Deal self.damage to target
    #         # Print attack message
    #         # Return damage dealt
    #         pass
    #
    #     def is_in_range(self, target):
    #         """Check if target is within aggro_range."""
    #         pass
    #
    #     def on_death(self, killer):
    #         """Called when enemy dies. Give XP to killer if Player."""
    #         # If killer has gain_experience method, call it with xp_reward
    #         # Print death message
    #         pass
    #
    # Test:
    #     enemy = Enemy("{{creature}}", 50, (3, 3), 15, 25)
    #     player = Player("{{hero}}", 100, (5, 5))
    #     print(f"In range: {enemy.is_in_range(player)}")
    #     enemy.attack(player)
    #     print(player.get_status())

    pass


# ============================================================
# PART 4: Growth - Implement Combat Interaction
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# Create a combat system that handles entity interactions.


def part4_combat_system():
    # ✏️ CREATE THE COMBAT SYSTEM ✏️
    #
    # class CombatSystem:
    #     """Manages combat between entities."""
    #
    #     def __init__(self):
    #         """Initialize with empty entity lists."""
    #         self.players = []
    #         self.enemies = []
    #         self.combat_log = []
    #
    #     def add_player(self, player):
    #         """Add a player to the system."""
    #         pass
    #
    #     def add_enemy(self, enemy):
    #         """Add an enemy to the system."""
    #         pass
    #
    #     def log_event(self, message):
    #         """Add message to combat log and print it."""
    #         pass
    #
    #     def player_attack(self, player, target):
    #         """Handle player attacking an enemy."""
    #         # Calculate damage (could add player weapon damage later)
    #         # Deal damage to target
    #         # Log the attack
    #         # If target dies, call on_death and remove from enemies
    #         pass
    #
    #     def enemy_turn(self):
    #         """Process all enemy actions."""
    #         # For each alive enemy:
    #         #     Find nearest player
    #         #     If in range, attack
    #         #     Log actions
    #         pass
    #
    #     def get_battle_status(self):
    #         """Return summary of all combatants."""
    #         pass
    #
    # Test combat:
    #     combat = CombatSystem()
    #     player = Player("{{hero}}", 100, (0, 0))
    #     enemy1 = Enemy("{{creature}}", 30, (2, 2), 10, 20)
    #     enemy2 = Enemy("{{creature}}", 40, (3, 1), 12, 25)
    #
    #     combat.add_player(player)
    #     combat.add_enemy(enemy1)
    #     combat.add_enemy(enemy2)
    #
    #     print(combat.get_battle_status())
    #     combat.player_attack(player, enemy1)
    #     combat.enemy_turn()
    #     print(combat.get_battle_status())

    pass


# ============================================================
# PART 5: Ownership - Add Your Own Entity Type
# ============================================================
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# Design your own unique entity type that fits the hierarchy.


def part5_custom_entity():
    # ✏️ CREATE YOUR OWN ENTITY TYPE ✏️
    #
    # Ideas:
    # - Boss(Enemy): Multiple phases, special attacks
    # - Companion(Entity): Follows player, provides buffs
    # - NPC(Entity): Can be talked to, gives quests
    # - Trap(Entity): Stationary, damages on contact
    # - Healer(Entity): Restores health to nearby allies
    #
    # Requirements:
    # - Must inherit from Entity or one of its subclasses
    # - Must add at least 2 new attributes
    # - Must add at least 2 new methods
    # - Must override at least 1 parent method
    # - Must interact meaningfully with other entities
    #
    # Demonstrate your entity in action with other entities.

    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("Building a Game Entity System")
    print("=" * 60)
    print()

    print(">>> PART 1: Base Entity Class")
    print("(Create the foundation for all entities)")
    part1_base_entity()
    print()

    print(">>> PART 2: Player Subclass")
    print("(Add inventory and experience system)")
    part2_player_class()
    print()

    print(">>> PART 3: Enemy Subclass")
    print("(Create hostile entities with combat)")
    part3_enemy_class()
    print()

    print(">>> PART 4: Combat System")
    print("(Manage entity interactions)")
    part4_combat_system()
    print()

    print(">>> PART 5: Your Custom Entity")
    print("(Design your own unique entity type)")
    part5_custom_entity()

    print()
    print("=" * 60)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
