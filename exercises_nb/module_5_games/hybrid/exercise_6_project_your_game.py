# %% [markdown]
# {{CONTEXT_OWNERSHIP_INTRO}}
#
# This is your capstone project: Build Your Own Game!
# Follow the guided steps to create a complete, polished game.
#
# Programming concepts: Everything from Module 5!

# %%
import random

# %% [markdown]
# PART 1: Design Your Game
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Before coding, design your game!
#
# Answer these questions (in comments or on paper):
# 1. What is your game about? (theme, story)
# 2. What does the player do? (actions, goals)
# 3. How does the player win? (win condition)
# 4. How does the player lose? (lose condition, or none?)
# 5. What makes it fun? (randomness, choices, challenge)
#
# MY GAME DESIGN
# --------------
# Theme: ________________________________
# Goal: ________________________________
# Win condition: ________________________________
# Lose condition: ________________________________
# Core mechanic: ________________________________
#
# Player actions:
# 1. ________________________________
# 2. ________________________________
# 3. ________________________________
#
# Game state to track:
# - ________________________________
# - ________________________________
# - ________________________________
#
# PART 2: Build the Core
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Implement the basic game mechanics.
#
# ✏️ YOUR CODE HERE ✏️
#
# Create and return your initial game state

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Define your valid actions
# Show menu
# Get and validate input
# Return the action

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Handle each possible action
# Update game_state appropriately
# Return a description of what happened

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Add Win/Lose Conditions
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Define when the game ends.
#
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 4: Make It Crash-Proof
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Add validation and error handling throughout.
#
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 5: Add Polish
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Make your game feel complete!
#
# ✏️ YOUR CODE HERE ✏️
#
# Create an engaging introduction for your game
# Use {{placeholders}} for theme-agnostic content!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 6: The Complete Game
# {{CONTEXT_TRIUMPH_COMPLETE}}
#
# Put it all together!

# %%
while game_state.get("playing", True):
    # ✏️ YOUR CODE HERE ✏️
    #
    # 1. Display current status
    # 2. Check win condition
    #    If won: display_end_message, break
    # 3. Check lose condition
    #    If lost: display_end_message, break
    # 4. Get player action
    # 5. If action is "quit", break
    # 6. Process action
    # 7. Display result message
    pass

# %%
display_intro()

playing = True
while playing:
    game_state = initialize_game()

    if game_state is None:
        print("Failed to initialize game!")
        break

    game_loop(game_state)

    playing = ask_play_again()

print("\nThanks for playing!")
print(f"{{{{exclamation}}}} Until next time!")

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("   BUILD YOUR OWN GAME")
print("   Module 5 Capstone Project")
print("=" * 60)
print()

print(">>> PART 1: Design your game (see comments above)")
print()

print(">>> PART 2: Build the core")
print("(Implement initialize_game, display_status, get_player_input, process_action)")
print()
# Test core:
# state = initialize_game()
# display_status(state)
# action = get_player_input(state)
# result = process_action(state, action)
# print(result)

print(">>> PART 3: Add win/lose conditions")
print("(Implement check_win, check_lose, display_end_message)")
print()

print(">>> PART 4: Make it crash-proof")
print("(Implement validate_game_state, safe_update_stat)")
print()

print(">>> PART 5: Add polish")
print("(Implement display_intro, display_help, ask_play_again)")
print()

print(">>> PART 6: Launch your game!")
print()
# play_game()

print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
