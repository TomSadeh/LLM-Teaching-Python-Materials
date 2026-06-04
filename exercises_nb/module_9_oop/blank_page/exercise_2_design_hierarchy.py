# %% [markdown]
# {{CONTEXT_BLANK_PAGE_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# עצבי ומימשי היררכיית מחלקות מאפס.
# זה דורש תכנון של קשרי הורה-ילד ושימוש בירושה.
#
# ## {{BLANK_1_TITLE}}
# {{CONTEXT_BLANK_1_NARRATIVE}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{BLANK_2_TITLE}}
# {{CONTEXT_BLANK_2_NARRATIVE}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{BLANK_3_TITLE}}
# {{CONTEXT_BLANK_3_NARRATIVE}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## בדיקות

# %%
print("Testing your implementations...\n")

print("{{BLANK_1_TITLE}} - Ability Hierarchy")
# Uncomment to test:
# fireball = DamageAbility("Fireball", 20, 3, 50)
# assert fireball.can_use() == True
# result = fireball.use()
# assert "50 damage" in result
# assert fireball.can_use() == False
print("   (Uncomment tests after implementing)\n")

print("{{BLANK_2_TITLE}} - Item Hierarchy")
# Uncomment to test:
# sword = Equipment("Sword", 100, "weapon")
# assert sword.get_value() == 100
# sword.use()
# assert sword.durability == 90
# potion = Consumable("Potion", 50, 3, "Heals 50")
# assert potion.consume() == "Heals 50"
# assert potion.quantity == 2
print("   (Uncomment tests after implementing)\n")

print("{{BLANK_3_TITLE}} - Character Hierarchy")
# Uncomment to test:
# player = Player("Hero", 100)
# player.gain_experience(150)
# assert player.level == 2
# enemy = Enemy("Goblin", 50, 15, 20)
# enemy.attack(player)
# assert player.health == 85
# boss = Boss("Dragon", 100, 30, 50, 3)
# boss.take_damage(150)
# assert boss.is_alive() == True
# assert boss.phase == 2
print("   (Uncomment tests after implementing)\n")

print("=" * 40)
print("All tests passed!")

# %%
print("{{CONTEXT_BLANK_PAGE_INTRO}}")
print("=" * 50)
print()
print("Design each class hierarchy based on the specifications.")
print("Think carefully about what goes in the base class vs subclasses.")
print()

# Uncomment the hierarchy you're working on:
# ability_hierarchy()
# item_hierarchy()
# character_hierarchy()

# Uncomment to run tests:
# run_tests()

print("{{CONTEXT_MASTERY_COMPLETE}}")
