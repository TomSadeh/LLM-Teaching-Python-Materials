# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# This is a multi-part exercise building Rock Paper Scissors.
# Complete each part to go from buggy code to a full game!
#
# Programming concepts: while loops, random, conditionals, game state

# %%
import random

# %% [markdown]
# PART 1: The Buggy RPS
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{hero}}'s first RPS game had bugs. {{villain}} exploited them!
# Find and fix the 3 bugs.
#
# BUGS TO FIND: 3

# %%
# BUG 1: Wrong comparison - paper vs rock
if player == "rock" and computer == "scissors":
    return "player"
elif player == "paper" and computer == "scissors":  # BUG: should be rock!
    return "player"
elif player == "scissors" and computer == "paper":
    return "player"
# BUG 2: These conditions are duplicates of player wins!
elif player == "rock" and computer == "paper":
    return "player"  # BUG: Should return "computer"!
elif player == "paper" and computer == "scissors":
    return "computer"
elif player == "scissors" and computer == "rock":
    return "computer"
# BUG 3: Missing the equals case properly
else:
    return None  # BUG: Should explicitly check for tie

# %%
choices = ["rock", "paper", "scissors"]

player = input("Choose (rock/paper/scissors): ").lower()
computer = random.choice(choices)

print(f"You chose: {player}")
print(f"{{{{villain}}}} chose: {computer}")

result = buggy_determine_winner(player, computer)
if result == "player":
    print("You win!")
elif result == "computer":
    print("{{{{villain}}}} wins!")
else:
    print("It's a tie!")

# %% [markdown]
# ✏️ FIX THE BUGS ✏️
#
# Hint: Check ties first with player == computer
# Then check all three player win conditions
# Then the remaining cases are computer wins

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 2: Build the Core
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Build proper RPS functions from scratch.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Define valid_choices and shortcuts
#         shortcuts = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
# Step 2: While True loop
# Step 3: Get input, lowercase
# Step 4: Check if in shortcuts, convert
# Step 5: Check if in valid_choices
# Step 6: If valid, return. Otherwise print error.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Get player choice
# Step 2: Get computer choice
# Step 3: Print choices (use {{villain}} for computer)
# Step 4: Determine winner using fixed_determine_winner
# Step 5: Announce result
# Step 6: Return result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: The Championship
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# Build the complete best-of game with:
# - Score tracking
# - Play-again loop
# - Match statistics
#
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print(f"\n=== First to {rounds_to_win} wins! ===\n")

player_wins = 0
computer_wins = 0
ties = 0

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# While neither player has enough wins:
#   1. Play a round
#   2. Update appropriate counter
#   3. Display current score
#   4. Check for winner
#
# After loop: Announce match winner

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("   ROCK PAPER SCISSORS CHAMPIONSHIP")
print(f"   {{{{hero}}}} vs {{{{villain}}}}")
print("=" * 50)

total_games = 0
player_championships = 0
villain_championships = 0

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Play again loop:
#   1. Ask for match length (1, 2, or 3 for best of 3/5/7)
#   2. Convert to rounds_to_win (2, 3, or 4)
#   3. Play match
#   4. Update championship stats
#   5. Show overall record
#   6. Ask to play again
#
# Final: Show farewell and final record

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_SETBACK_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Fix the buggy RPS...")
print("(Review buggy_determine_winner and implement fixed version)")
print()
# Test the fix:
# print("Testing fixed winner logic:")
# test_cases = [
#     ("rock", "scissors", "player"),
#     ("paper", "rock", "player"),
#     ("scissors", "paper", "player"),
#     ("rock", "paper", "computer"),
#     ("paper", "scissors", "computer"),
#     ("scissors", "rock", "computer"),
#     ("rock", "rock", "tie"),
# ]
# for p, c, expected in test_cases:
#     result = fixed_determine_winner(p, c)
#     status = "OK" if result == expected else "FAIL"
#     print(f"  {p} vs {c}: {result} ({status})")

print()
print(">>> PART 2: Build the core game...")
print("(Implement get_player_choice, get_computer_choice, play_round)")
print()
# Uncomment to test:
# result = play_round()
# print(f"Result: {result}")

print()
print(">>> PART 3: The Championship awaits...")
print("(Implement display_score, play_match, championship)")
print()
# Uncomment to play:
# championship()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
