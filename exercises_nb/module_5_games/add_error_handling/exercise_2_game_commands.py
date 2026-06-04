# %% [markdown]
# {{CONTEXT_ERROR_HANDLING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Handling invalid game commands gracefully
# Difficulty: 3-4
#
# Games need robust command handling - players will type anything!
# Make the game respond helpfully to invalid input.
#
# {{HANDLING_1_TITLE}}
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# This movement system crashes on invalid directions.

# %%
moves = {"north": (0, 1), "south": (0, -1), "east": (1, 0), "west": (-1, 0)}
dx, dy = moves[direction]  # KeyError if direction invalid!
return dx, dy

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_1}}
#
# Step 1: Define moves dictionary
# Step 2: Convert direction to lowercase
# Step 3: If direction in moves, return the delta
# Step 4: Otherwise, print error and return (0, 0)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_2_TITLE}}
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# This attack command crashes if target doesn't exist.

# %%
for i, enemy in enumerate(enemies):
    if enemy["name"] == target_name:
        enemies[i]["hp"] -= 10
        return True
return False

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_2}}
#
# Step 1: Loop through enemies to find target
# Step 2: If not found after loop, return not found message
# Step 3: If found but hp <= 0, return already defeated message
# Step 4: Apply damage
# Step 5: If hp now <= 0, return defeated message
# Step 6: Otherwise return hit message

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_3_TITLE}}
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# This inventory use command has multiple failure modes.

# %%
inventory.remove(item_name)  # ValueError if not present!
return f"Used {item_name}"

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_3}}
#
# Step 1: Check if inventory is empty
# Step 2: Check if item_name is in inventory
# Step 3: If present, remove and return success
# Step 4: Otherwise return appropriate error

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_4_TITLE}}
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# This shop system has multiple ways to fail.

# %%
price = item_prices[item_name]
return gold - price, item_name

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_4}}
#
# Step 1: Check if item_name in item_prices
# Step 2: Get the price
# Step 3: Check if player has enough gold
# Step 4: If all good, return new gold and success message

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_5_TITLE}}
# {{CONTEXT_HANDLING_5_NARRATIVE}}
#
# Build a complete command parser with validation.
#
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_5}}
#
# Step 1: Strip and lowercase the command
# Step 2: If empty, return error
# Step 3: Split into parts
# Step 4: First part is the action
# Step 5: Check if action is valid
# Step 6: For commands needing args (move, attack, use):
#         - Check args provided
#         - For move, validate direction
# Step 7: Return (action, args) or appropriate error

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
print("=" * 50)

print("\n=== {{HANDLING_1_TITLE}} ===")
print("Testing safe movement:")
directions = ["north", "SOUTH", "left", "east"]
for d in directions:
    result = safe_move(d)
    print(f"  {d} -> {result}")

print("\n=== {{HANDLING_2_TITLE}} ===")
print("Testing safe attack:")
enemies = [
    {"name": "{{creature}}", "hp": 20},
    {"name": "{{villain}}", "hp": 0}
]
targets = ["{{creature}}", "{{villain}}", "ghost"]
for t in targets:
    result = safe_attack(enemies, t)
    print(f"  Attack {t}: {result}")

print("\n=== {{HANDLING_3_TITLE}} ===")
print("Testing safe use item:")
inv = ["{{item}}", "{{spell1}}"]
items_to_use = ["{{item}}", "{{spell2}}"]
for item in items_to_use:
    result = safe_use_item(inv, item)
    print(f"  Use {item}: {result}")

print("\n=== {{HANDLING_4_TITLE}} ===")
print("Testing safe shop:")
prices = {"{{item}}": 50, "{{spell1}}": 100}
purchases = [("{{item}}", 60), ("{{spell1}}", 50), ("potion", 100)]
for item, gold in purchases:
    new_gold, msg = safe_buy_item(gold, prices, item)
    print(f"  Buy {item} with {gold}g: {msg}")

print("\n=== {{HANDLING_5_TITLE}} ===")
print("Testing command parser:")
commands = ["move north", "attack goblin", "look", "dance", "", "move"]
for cmd in commands:
    result = parse_game_command(cmd)
    print(f"  '{cmd}' -> {result}")

print("\n" + "=" * 50)
print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")
