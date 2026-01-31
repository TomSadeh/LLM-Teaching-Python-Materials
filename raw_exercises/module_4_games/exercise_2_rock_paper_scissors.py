# Exercise 2: Rock, Paper, Scissors

import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def get_winner(player, computer):
    # ✏️ YOUR CODE HERE ✏️
    # Return who wins:
    # - "tie" if player and computer are the same
    # - "player" if player wins
    # - "computer" if computer wins
    #
    # Remember:
    # - rock beats scissors
    # - scissors beats paper
    # - paper beats rock
    #
    # Hint: check for tie first, then check player wins
    pass


def play_round():
    player = input("Choose rock, paper, or scissors: ")
    computer = get_computer_choice()

    print("You chose:", player)
    print("Computer chose:", computer)

    winner = get_winner(player, computer)

    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win!")
    else:
        print("Computer wins!")


def main():
    print("✊ Rock, Paper, Scissors ✋")
    print("==========================")
    play_round()

    # BONUS: Add a loop to play multiple rounds and keep score!


main()
