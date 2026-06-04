# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# This is a multi-part exercise following {{hero}}'s journey from defeat to victory.
# Complete each part in order.
#
# Programming concepts: while loops, random, game state, conditionals

# %%
import random

# %% [markdown]
# PART 1: The Defeat
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{hero}}'s code from the last match had bugs. That's why {{villain}} won.
# Find and fix the 3 bugs so this never happens again.
#
# BUGS TO FIND: 3

# %%
player_a_score = 0
player_b_score = 0
rounds_played = 0
max_rounds = 5

print(f"=== {{{{hero}}}} vs {{{{villain}}}} ===")
print()

while rounds_played < max_rounds:  # BUG 1: Should be <=, misses round 5
    rounds_played += 1
    print(f"--- Round {rounds_played} ---")

    # {{hero}}'s turn
    player_a_result = random.choice(["success", "success", "fail"])
    if player_a_result == "success":
        player_a_score + 1  # BUG 2: Should be player_a_score += 1
        print(f"{{{{hero}}}} scores! Total: {player_a_score}")
    else:
        print(f"{{{{hero}}}} misses...")

    # {{villain}}'s turn
    player_b_result = random.choice(["success", "success", "fail"])
    if player_b_result == "success":
        player_b_score += 1
        print(f"{{{{villain}}}} scores. Total: {player_b_score}")
    else:
        print(f"{{{{villain}}}} misses!")

    print()

print("=== FINAL RESULT ===")
print(f"{{{{hero}}}}: {player_a_score}")
print(f"{{{{villain}}}}: {player_b_score}")

if player_a_score >= player_b_score:  # BUG 3: Should be > for hero win, = is tie
    print(f"{{{{villain}}}} wins!")
else:
    print(f"{{{{hero}}}} wins!")

# %% [markdown]
# ## ✏️ FIX THE CODE BELOW ✏️
#
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 2: Training
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# {{hero}} needs a new ability: the POWER MOVE.
#
# A power move is high risk, high reward:
# - 40% chance: CRITICAL SUCCESS (2 points!)
# - 30% chance: Normal success (1 point)
# - 30% chance: Fail (0 points)
#
# Implement the power move and a training loop to practice it.
#
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
result = random.choice(["success", "success", "fail"])
if result == "success":
    return 1
return 0

# %%
total_points = 0
attempts = 0

print("=== TRAINING SESSION ===")
print(f"{{{{hero}}}} practices for the rematch against {{{{villain}}}}.")
print()
print("Commands: 'r' = regular move, 'p' = power move, 'q' = quit")
print()

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
# Implement the training loop:
# 1. Ask for input (r/p/q)
# 2. Execute the chosen move
# 3. Display result and running totals
# 4. Continue until 'q'

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass

print()
print("=== TRAINING COMPLETE ===")
print(f"Total points: {total_points}")
print(f"Attempts: {attempts}")
if attempts > 0:
    print(f"Average: {total_points / attempts:.2f} points per attempt")

# %% [markdown]
# PART 3: The Showdown
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# The rematch! Build the complete showdown:
# - 5 rounds of competition
# - {{hero}} can choose regular or power move each round
# - {{villain}} always uses regular moves
# - If tied after 5 rounds: sudden death until someone leads
#
# Use everything you've learned. This is the final test.
#
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print(f"--- Round {round_num} ---")
print(f"Score: {{{{hero}}}} {player_a_score} - {player_b_score} {{{{villain}}}}")

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("   THE FINAL SHOWDOWN")
print(f"   {{{{hero}}}} vs {{{{villain}}}}")
print("=" * 50)
print()

player_a_score = 0
player_b_score = 0

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
# 1. Main match: 5 rounds
# 2. Check for winner
# 3. If tied: sudden death
# 4. Announce winner

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_SETBACK_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Analyzing the defeat...")
print("(Review buggy_match() and implement fixed_match())")
print()
# Uncomment to test:
# fixed_match()

print()
print(">>> PART 2: Training begins...")
print("(Implement attempt_power_move() and training_session())")
print()
# Uncomment to test:
# training_session()

print()
print(">>> PART 3: The showdown awaits...")
print("(Implement all showdown functions)")
print()
# Uncomment to test:
# the_showdown()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
