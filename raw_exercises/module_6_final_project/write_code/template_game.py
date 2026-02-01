# Final Project Template: Game

import random

# ==================
# YOUR GAME SETTINGS
# ==================
GAME_NAME = "My Awesome Game"


# ==================
# HELPER FUNCTIONS
# ==================

def show_welcome():
    print("🎮 " + GAME_NAME + " 🎮")
    print("=" * (len(GAME_NAME) + 6))
    # Add instructions here


def get_player_choice():
    # Get input from player
    pass


def check_result():
    # Check if player won/lost
    pass


def update_score(score, points):
    # Add points to score
    return score + points


def show_game_over(score):
    print("\n=== GAME OVER ===")
    print("Final score:", score)
    # Add ending message based on score


# ==================
# MAIN GAME
# ==================

def play_round(score):
    # One round of your game
    # Return the new score
    return score


def main():
    show_welcome()

    score = 0
    playing = True

    while playing:
        score = play_round(score)

        play_again = input("\nPlay again? (y/n): ")
        if play_again != "y":
            playing = False

    show_game_over(score)


main()
