# %% [markdown]
# {{CONTEXT_COMPLETE_FUNCTION_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# In this exercise, you'll learn to use .get() for safe dictionary access.
# The .get() method returns a default value when a key doesn't exist,
# instead of raising a KeyError.
#
# {{FUNCTION_1_TITLE}}
# {{CONTEXT_FUNCTION_1_NARRATIVE}}
#
# ✏️ COMPLETE THIS FUNCTION ✏️
#
# {{CONTEXT_FUNCTION_HINT_1}}
#
# Use stats.get(stat_name, default_value)
# The second argument is returned if the key doesn't exist.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{FUNCTION_2_TITLE}}
# {{CONTEXT_FUNCTION_2_NARRATIVE}}
#
# ✏️ COMPLETE THIS FUNCTION ✏️
#
# {{CONTEXT_FUNCTION_HINT_2}}
#
# Use .get() to safely access the inventory.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{FUNCTION_3_TITLE}}
# {{CONTEXT_FUNCTION_3_NARRATIVE}}
#
# ✏️ COMPLETE THIS FUNCTION ✏️
#
# {{CONTEXT_FUNCTION_HINT_3}}
#
# Return the description or "Unknown ability" as default.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{FUNCTION_4_TITLE}}
# {{CONTEXT_FUNCTION_4_NARRATIVE}}
#
# ✏️ COMPLETE THIS FUNCTION ✏️
#
# {{CONTEXT_FUNCTION_HINT_4}}
#
# Step 1: Get current quantity (default 0 if not in inventory)
# Step 2: Add the new quantity
# Step 3: Store back in inventory
# Step 4: Return the new total
#
# Pattern: inventory[item] = inventory.get(item, 0) + quantity

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
print("=" * 50)

print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
stats = {"health": 100, "strength": 10}
print(f"Health: {get_character_stat(stats, 'health')}")
print(f"Mana (not set): {get_character_stat(stats, 'mana')}")

print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
inventory = {"{{item}}": 5, "{{spell1}}": 3}
print(f"{{{{item}}}}: {get_inventory_count(inventory, '{{item}}')}")
print(f"{{{{spell2}}}} (not owned): {get_inventory_count(inventory, '{{spell2}}')}")

print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
abilities = {
    "{{spell1}}": "A fundamental technique",
    "{{spell2}}": "An intermediate skill"
}
print(f"{{{{spell1}}}}: {get_ability_description(abilities, '{{spell1}}')}")
print(f"{{{{spell3}}}}: {get_ability_description(abilities, '{{spell3}}')}")

print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
inv = {}
safe_add_to_inventory(inv, "{{item}}", 3)
safe_add_to_inventory(inv, "{{item}}", 2)
safe_add_to_inventory(inv, "{{spell1}}", 1)
print(f"Inventory: {inv}")

print("\n" + "=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
