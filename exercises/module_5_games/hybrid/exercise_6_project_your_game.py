"""
{{CONTEXT_OWNERSHIP_INTRO}}

This is your capstone project: Build Your Own Game!
Follow the guided steps to create a complete, polished game.

Programming concepts: Everything from Module 5!
"""

import random


# ============================================================
# PART 1: Design Your Game
# ============================================================
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


"""
MY GAME DESIGN
--------------
Theme: ________________________________
Goal: ________________________________
Win condition: ________________________________
Lose condition: ________________________________
Core mechanic: ________________________________

Player actions:
1. ________________________________
2. ________________________________
3. ________________________________

Game state to track:
- ________________________________
- ________________________________
- ________________________________
"""


# ============================================================
# PART 2: Build the Core
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Implement the basic game mechanics.


def initialize_game():
    """
    Set up the initial game state.

    Returns:
        dict: Initial game state

    Include whatever your game needs:
    - Player stats (hp, score, level, etc.)
    - Game progress (round, turn, etc.)
    - Any other state variables

    Example structure:
        {
            "player_hp": 100,
            "score": 0,
            "round": 1,
            "playing": True
        }
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create and return your initial game state
    pass


def display_status(game_state):
    """
    Show the current game status to the player.

    Args:
        game_state: Your game state dictionary

    Display whatever is relevant:
    - Health/lives
    - Score/progress
    - Current situation
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_player_input(game_state):
    """
    Get the player's next action.

    Args:
        game_state: Current game state (might affect available actions)

    Returns:
        str: The valid action chosen

    Requirements:
    - Show available actions
    - Validate input
    - Return a valid action string
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Define your valid actions
    # Show menu
    # Get and validate input
    # Return the action
    pass


def process_action(game_state, action):
    """
    Process the player's chosen action.

    Args:
        game_state: Current game state (will be modified)
        action: The action string

    Returns:
        str: Message describing what happened

    This is where your game logic lives!
    Update game_state based on the action.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Handle each possible action
    # Update game_state appropriately
    # Return a description of what happened
    pass


# ============================================================
# PART 3: Add Win/Lose Conditions
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Define when the game ends.


def check_win(game_state):
    """
    Check if the player has won.

    Args:
        game_state: Current game state

    Returns:
        bool: True if player has won

    What triggers a win in your game?
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def check_lose(game_state):
    """
    Check if the player has lost.

    Args:
        game_state: Current game state

    Returns:
        bool: True if player has lost

    What triggers a loss in your game?
    (Return False if your game has no lose condition)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_end_message(game_state, won):
    """
    Show the appropriate end-game message.

    Args:
        game_state: Final game state
        won: True if player won, False if lost

    Include:
    - Win/lose message
    - Final stats (score, etc.)
    - Any achievements
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 4: Make It Crash-Proof
# ============================================================
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Add validation and error handling throughout.


def validate_game_state(game_state):
    """
    Ensure game state is valid.

    Args:
        game_state: The state to validate

    Returns:
        bool: True if valid

    Check for:
    - Required keys exist
    - Values are in valid ranges
    - No corruption
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def safe_update_stat(game_state, stat_name, change, min_val=0, max_val=None):
    """
    Safely update a game stat with bounds checking.

    Args:
        game_state: Game state dict
        stat_name: Key to update
        change: Amount to add (can be negative)
        min_val: Minimum allowed value
        max_val: Maximum allowed value (None = no max)

    Ensures stat stays within bounds.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 5: Add Polish
# ============================================================
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Make your game feel complete!


def display_intro():
    """
    Show the game introduction.

    Include:
    - Game title
    - Brief story/context
    - How to play
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create an engaging introduction for your game
    # Use {{placeholders}} for theme-agnostic content!
    pass


def display_help():
    """
    Show help/instructions.

    List:
    - All commands
    - Game rules
    - Tips
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def ask_play_again():
    """
    Ask if the player wants to play again.

    Returns:
        bool: True if yes
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 6: The Complete Game
# ============================================================
# {{CONTEXT_TRIUMPH_COMPLETE}}
#
# Put it all together!


def game_loop(game_state):
    """
    The main game loop.

    Args:
        game_state: Initial game state

    Loop structure:
    1. Display status
    2. Check win/lose conditions
    3. Get player input
    4. Process action
    5. Repeat until game ends
    """
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


def play_game():
    """
    Run the complete game experience.

    Structure:
    1. Display intro
    2. Initialize game
    3. Run game loop
    4. Ask play again
    5. Repeat or exit
    """
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


# ============================================================
# MAIN
# ============================================================

def main():
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


if __name__ == "__main__":
    main()
