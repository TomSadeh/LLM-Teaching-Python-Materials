# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Using the random module
# Difficulty: 2-3
#
# The random module lets you generate random numbers and make random choices.
# Essential for games with unpredictable elements!

# %%
import random

# %% [markdown]
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# random.randint(a, b) returns a random integer from a to b INCLUSIVE.
# Unlike range(), both endpoints are included!
#
# ✏️ YOUR CODE HERE ✏️
#
# Use random.randint(1, num_sides) to get a number from 1 to num_sides

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Initialize total = 0
# Step 2: Loop num_dice times
# Step 3: Add a random roll to total
# Step 4: Return total

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# random.choice(sequence) picks a random item from a list or string.
#
# ✏️ YOUR CODE HERE ✏️
#
# Use random.choice(items)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create the adjectives list
# Step 2: Create the nouns list
# Step 3: Pick random adjective with random.choice()
# Step 4: Pick random noun with random.choice()
# Step 5: Return f"{adjective} {noun}"

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# random.random() returns a float from 0.0 to 1.0 (exclusive).
# Useful for percentage-based chances.
#
# ✏️ YOUR CODE HERE ✏️
#
# If random.random() < probability, return True
# Otherwise return False

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Use chance_event() to determine if successful
# Print the appropriate message
# Return "success" or "failure"

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# Combine random functions to create game mechanics.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Get a random float with random.random()
# Step 2: Track cumulative probability
# Step 3: Loop through options and weights together
#         - Add weight to cumulative
#         - If random value < cumulative, return that option
# Step 4: Return last option (safety fallback)
#
# Hint: Use zip(options, weights) to loop through both

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Define rarities and weights
# Step 2: Use weighted_random_choice to pick rarity
# Step 3: Create item name based on rarity
# Step 4: Return (item_name, rarity)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# Generate random numbers within ranges for game scenarios.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Generate each base stat with random.randint()
# Step 2: Calculate derived stats
# Step 3: Return dictionary with all stats

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Calculate attacker's damage
# Calculate defender's damage
# Return both as a tuple

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print(f"Rolling a 6-sided die: {roll_dice(6)}")
print(f"Rolling a 20-sided die: {roll_dice(20)}")
print(f"Rolling 3d6: {roll_multiple_dice(3, 6)}")

print("\n=== {{PHASE_2_TITLE}} ===")
characters = ["{{hero}}", "{{villain}}", "{{friend}}", "{{mentor}}"]
print(f"Random character: {pick_random_item(characters)}")
print(f"Random name: {generate_random_name()}")

print("\n=== {{PHASE_3_TITLE}} ===")
print("Attempting action with 75% success rate:")
attempt_action(0.75)

print("\n=== {{PHASE_4_TITLE}} ===")
print("Generating loot:")
item, rarity = generate_loot()
print(f"Found: {item} ({rarity})")

print("\n=== {{PHASE_5_TITLE}} ===")
print("Generating character stats:")
stats = generate_stats()
print(f"Stats: {stats}")
print("\nSimulating battle round (power 15 vs 12):")
atk_dmg, def_dmg = simulate_battle_round(15, 12)
print(f"Attacker dealt {atk_dmg}, Defender dealt {def_dmg}")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
