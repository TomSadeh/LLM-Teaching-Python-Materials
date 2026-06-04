# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# זוהי תרגילה מרובת-חלקים שבה תבני היררכיית ישויות משחק שלמה
# עבור {{school}}. תיצרי מחלקות בסיס, תת-מחלקות לשחקן ולאויב,
# ותממשי אינטראקציות לחימה.
#
# מושגי תכנות: ירושה, דריסת מתודות, פולימורפיזם, קומפוזיציה
#
# ## חלק 1: צמיחה - יצירת מחלקת הבסיס Entity
# {{CONTEXT_PHASE_1}}
#
# התחילי עם יסוד איתן לכל ישויות המשחק.
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
#         > רמז: ייבאי את `math` והשתמשי ב-`math.sqrt`
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
# בדיקה:
#     entity = Entity("{{hero}}", 100, (5, 5))
#     print(entity)
#     entity.take_damage(30)
#     print(f"After damage: {entity.get_status()}")
#     entity.move_to((10, 10))
#     print(f"Position: {entity.position}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - יצירת תת-מחלקת השחקן
# {{CONTEXT_PHASE_2}}
#
# צרי מחלקת שחקן עם מלאי וניסיון.
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
# בדיקה:
#     player = Player("{{hero}}", 100)
#     player.pick_up_item("{{item}}")
#     player.gain_experience(150)  # Should level up
#     print(player.get_status())
#     print(f"Inventory: {player.inventory}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - יצירת תת-מחלקת האויב
# {{CONTEXT_PHASE_3}}
#
# צרי סוגי אויבים עם התנהגויות שונות.
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
# בדיקה:
#     enemy = Enemy("{{creature}}", 50, (3, 3), 15, 25)
#     player = Player("{{hero}}", 100, (5, 5))
#     print(f"In range: {enemy.is_in_range(player)}")
#     enemy.attack(player)
#     print(player.get_status())

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: צמיחה - מימוש מערכת לחימה
# {{CONTEXT_PHASE_4}}
#
# צרי מערכת לחימה שמטפלת באינטראקציות בין ישויות.
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
# בדיקת לחימה:
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

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 5: בעלות - הוסיפי סוג ישות משלך
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# עצבי סוג ישות ייחודי משלך שמתאים להיררכיה.
#
# רעיונות:
# - Boss(Enemy): כמה שלבים, התקפות מיוחדות
# - Companion(Entity): עוקב אחרי השחקן, נותן חיזוקים
# - NPC(Entity): אפשר לדבר איתו, נותן משימות
# - Trap(Entity): עומד במקום, גורם נזק במגע
# - Healer(Entity): משחזר בריאות לבעלי ברית בסביבה
#
# דרישות:
# - חייבת לרשת מ-`Entity` או מאחת מתת-המחלקות שלה
# - חייבת להוסיף לפחות 2 תכונות חדשות
# - חייבת להוסיף לפחות 2 מתודות חדשות
# - חייבת לדרוס לפחות מתודה אחת מהמחלקה הורה
# - חייבת לקיים אינטראקציה משמעותית עם ישויות אחרות
#
# הדגימי את הישות שלך בפעולה עם ישויות אחרות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
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
