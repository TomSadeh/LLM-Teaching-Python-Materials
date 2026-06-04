# =============================================================================
# Bug Hunt: Aliasing Bugs
# =============================================================================
# Difficulty: 4
# Concepts: Aliasing, unexpected mutations, copy vs reference
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Create a backup of inventory, modify original, backup stays unchanged.
# Expected: Backup: ['{{item}}', 'potion', 'key']
#
# ACTUAL BEHAVIOR:
# Backup changes when original changes!
# Actual: Backup: ['{{item}}', 'key', 'map']
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
inventory = ["{{item}}", "potion", "key"]
print(f"Original inventory: {inventory}")

# Save a backup before making changes
backup = inventory  # BUG: This creates an alias, not a copy!

# Make changes to inventory
inventory.remove("potion")
inventory.append("map")

print(f"Modified inventory: {inventory}")
print(f"Backup (should be unchanged): {backup}")

# %%
# FIX THE BUG
#
# What I found: ________________________________
#
# Hint: Use slicing to create a true copy: backup = inventory[:]
# Or use: backup = list(inventory)
# Or use: backup = inventory.copy()
#
# The fix:

pass

# %% [markdown]
# {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Two teams should be independent.
# Team A changes shouldn't affect Team B.
#
# ACTUAL BEHAVIOR:
# Both teams end up with the same members!
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
base_roster = ["{{hero}}", "{{heroine}}"]

team_a = base_roster  # BUG: Alias!
team_b = base_roster  # BUG: Another alias to the same list!

# Add different members to each team
team_a.append("{{friend}}")
team_b.append("{{mentor}}")

print(f"Base roster: {base_roster}")
print(f"Team A: {team_a}")
print(f"Team B: {team_b}")
print(f"All three are the same object: {team_a is team_b is base_roster}")

# %%
# FIX THE BUG
#
# What I found: ________________________________
#
# Hint: Each team needs its own copy of the base roster.
#
# The fix:

pass

# %% [markdown]
# {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Function should return a modified version without changing original.
# Original scores should remain [85, 90, 75, 95]
#
# ACTUAL BEHAVIOR:
# Original scores get modified too!
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
# BUG: Modifying the original list!
for i in range(len(scores)):
    scores[i] = scores[i] + bonus
return scores

# %%
original_scores = [85, 90, 75, 95]
print(f"Original: {original_scores}")

boosted = add_bonus_buggy(original_scores, 10)

print(f"Boosted: {boosted}")
print(f"Original (should be unchanged): {original_scores}")

# %%
# FIX THE BUG
#
# Make a copy of scores before modifying, then return the copy.
#
# Hint: result = scores[:]  # or list(scores)

pass

# %%
original_scores = [85, 90, 75, 95]
print(f"Original: {original_scores}")

boosted = add_bonus_fixed(original_scores, 10)

print(f"Boosted: {boosted}")
print(f"Original (should be unchanged): {original_scores}")

# %% [markdown]
# {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Undo the last action (restore previous state).
#
# ACTUAL BEHAVIOR:
# History is empty after modifications!
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
inventory = ["{{item}}", "potion"]
history = []

print(f"Initial: {inventory}")

# Save state before change
history.append(inventory)  # BUG: Appending the reference, not a copy!

# Make first change
inventory.append("key")
print(f"After adding key: {inventory}")

# Save state before second change
history.append(inventory)  # BUG: Still the same reference!

# Make second change
inventory.remove("potion")
print(f"After removing potion: {inventory}")

# Try to undo to first saved state
print(f"\nHistory entries: {len(history)}")
print(f"History[0] (should be ['{{item}}', 'potion']): {history[0]}")
print(f"History[1] (should be ['{{item}}', 'potion', 'key']): {history[1]}")

# %%
# FIX THE BUG
#
# What I found: ________________________________
#
# Hint: When saving to history, save a COPY of the current state.
# Use: history.append(inventory[:])
#
# The fix:

pass

# %% [markdown]
# {{CASE_5_TITLE}}
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Each player should have their own independent inventory.
#
# ACTUAL BEHAVIOR:
# All players share the same inventory somehow!
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

# %%
return {
    "name": name,
    "inventory": starting_items  # BUG: Using the reference directly!
}

# %%
starter_kit = ["{{item}}", "potion"]

player1 = create_player_buggy("{{hero}}", starter_kit)
player2 = create_player_buggy("{{heroine}}", starter_kit)

# Player 1 finds a key
player1["inventory"].append("key")

# Player 2 finds a map
player2["inventory"].append("map")

print(f"{player1['name']}'s inventory: {player1['inventory']}")
print(f"{player2['name']}'s inventory: {player2['inventory']}")
print(f"Are they the same list? {player1['inventory'] is player2['inventory']}")

# %%
# FIX THE BUG
#
# Each player should get their OWN copy of starting items.
#
# Hint: Copy the starting_items when creating the player.

pass

# %%
starter_kit = ["{{item}}", "potion"]

player1 = create_player_fixed("{{hero}}", starter_kit)
player2 = create_player_fixed("{{heroine}}", starter_kit)

player1["inventory"].append("key")
player2["inventory"].append("map")

print(f"{player1['name']}'s inventory: {player1['inventory']}")
print(f"{player2['name']}'s inventory: {player2['inventory']}")
print(f"Are they the same list? {player1['inventory'] is player2['inventory']}")

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Buggy version:")
buggy_a()
print("\nFixed version:")
# fix_a()

print("\n=== {{CASE_2_TITLE}} ===")
print("Buggy version:")
buggy_b()
print("\nFixed version:")
# fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Buggy version:")
buggy_c()
print("\nFixed version:")
# fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Buggy version:")
buggy_d()
print("\nFixed version:")
# fix_d()

print("\n=== {{CASE_5_TITLE}} ===")
print("Buggy version:")
buggy_e()
print("\nFixed version:")
# fix_e()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
