# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# This is a multi-part exercise where you expand {{school}}'s game
# system with advanced random features. You'll use choice(), shuffle(),
# and sample() to create engaging game mechanics.
#
# Programming concepts: random module, game mechanics, list manipulation
# Difficulty: 2-3

# %%
import random

# %% [markdown]
# PART 1: Growth - Random Selection with choice()
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Use random.choice() to select random items from collections.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create lists of options:
#         creatures = ["{{creature}}", "guardian", "wanderer", "spirit"]
#         actions = ["approaches", "appears", "emerges", "awaits"]
#         locations = ["{{location}}", "the path", "the shadows", "ahead"]
#
# Step 2: Use random.choice() to pick from each list
#
# Step 3: Build and return a sentence:
#         f"A {creature} {action} from {location}!"

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create a weighted list:
#         outcomes = ["success"] * 3 + ["partial"] * 2 + ["failure"] * 1
#         This gives: 50% success, 33% partial, 17% failure
#
# Step 2: Use random.choice(outcomes)
#
# Step 3: Return the result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create reward pools for each tier:
#         common = ["gold coins", "health potion", "basic scroll"]
#         rare = ["{{item}}", "enchanted gem", "silver key"]
#         legendary = ["ancient artifact", "{{spell3}}", "master key"]
#
# Step 2: Select the right pool based on tier
#
# Step 3: Use random.choice() on that pool
#
# Step 4: Return the reward

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 2: Growth - Shuffling with shuffle()
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Use random.shuffle() to randomize order for fair gameplay.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Make a copy: deck = items.copy() or list(items)
#         (shuffle modifies in place, we don't want to change original)
#
# Step 2: Shuffle the copy: random.shuffle(deck)
#
# Step 3: Return the shuffled deck

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Use create_shuffled_deck to get random order

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Return a shuffled copy of challenges

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Growth - Sampling with sample()
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Use random.sample() for lottery-style selections.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Make sure count isn't larger than pool
#         if count > len(pool):
#             count = len(pool)
#
# Step 2: Use random.sample(pool, count)
#
# Step 3: Return the result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Use draw_items to select team members

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create participant numbers: range(1, participant_count + 1)
#
# Step 2: Use random.sample() to pick winners
#
# Step 3: Sort the winners: sorted(winners)
#
# Step 4: Return the sorted list

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Random Adventures in {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Random Selection")
print("-" * 40)
print("Generating random encounters...")
# Uncomment to test:
# for i in range(3):
#     print(f"  {get_random_encounter()}")
# print()
# print("Testing outcomes:")
# for i in range(5):
#     print(f"  Attempt {i+1}: {random_event_outcome()}")
# print()
# print("Reward tiers:")
# print(f"  Common: {select_reward('common')}")
# print(f"  Rare: {select_reward('rare')}")
# print(f"  Legendary: {select_reward('legendary')}")
print()

print(">>> PART 2: Shuffling")
print("-" * 40)
# Uncomment to test:
# players = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
# print(f"Original order: {players}")
# turn_order = determine_turn_order(players)
# print(f"Turn order: {turn_order}")
# print(f"Original unchanged: {players}")
print()

print(">>> PART 3: Sampling")
print("-" * 40)
# Uncomment to test:
# rewards = ["gold", "gem", "key", "scroll", "potion", "armor", "weapon"]
# drawn = draw_items(rewards, 3)
# print(f"Drew 3 items: {drawn}")
# print()
# all_chars = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}", "ally1", "ally2"]
# team = generate_quest_team(all_chars, 3)
# print(f"Quest team: {team}")
# print()
# winners = lucky_draw(100, 5)
# print(f"Lucky draw winners (from 100): {winners}")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
