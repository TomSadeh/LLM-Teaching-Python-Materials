# Exercise 1: Bug Hunt - Game Logic
#
# {{villain}} has sabotaged these game spells!
# Each function has exactly ONE bug in its logic.
# Read the story, find the bug, and fix it.
#
# DO NOT run the code first - use your detective skills!


# ============================================================
# BUG HUNT A: The Impossible Win
# ============================================================
"""
STORY:
{{hero}} wrote a number guessing game, but players can
NEVER win! Even when they guess correctly, it says "Wrong!"

EXPECTED BEHAVIOR:
If guess equals secret_number → "You win!"
Otherwise → "Wrong! Try again."

ACTUAL BEHAVIOR:
Always shows "Wrong!" even for correct guesses.
"""

def buggy_check_guess(guess, secret_number):
    if guess = secret_number:  # BUG IS HERE (= vs ==)
        return "You win!"
    else:
        return "Wrong! Try again."


def fix_check_guess(guess, secret_number):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: = is assignment, == is comparison
    #
    # The fix:
    pass


# ============================================================
# BUG HUNT B: The Infinite Game
# ============================================================
"""
STORY:
{{friend}}'s dice game never ends! The game should stop
when the player says "quit", but it loops forever.

EXPECTED BEHAVIOR:
- Player types "roll" → roll dice
- Player types "quit" → game ends

ACTUAL BEHAVIOR:
Game never ends, even when typing "quit"
"""

def buggy_game_loop():
    import random
    playing = True

    while playing:
        action = input("Type 'roll' or 'quit': ")
        if action == "roll":
            dice = random.randint(1, 6)
            print(f"You rolled a {dice}!")
        elif action == "quit":
            print("Thanks for playing!")
            # BUG: playing is never set to False!


def fix_game_loop():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: What makes the while loop stop?
    #
    # The fix:
    import random
    playing = True

    pass  # Your code here


# ============================================================
# BUG HUNT C: The Unfair Score
# ============================================================
"""
STORY:
In {{mentor}}'s quiz game, correct answers should add 10 points,
but the score stays at 10 no matter how many you get right!

EXPECTED BEHAVIOR:
3 correct answers → score = 30

ACTUAL BEHAVIOR:
Score is always 10, regardless of correct answers.
"""

def buggy_calculate_score(correct_answers):
    score = 0
    for i in range(correct_answers):
        score = 10  # BUG IS HERE
    return score


def fix_calculate_score(correct_answers):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: We want to ADD 10 each time, not SET to 10
    #
    # The fix:
    score = 0

    pass  # Your code here

    return score


# ============================================================
# BUG HUNT D: The Wrong Winner
# ============================================================
"""
STORY:
Rock-Paper-Scissors at {{school}} is broken!
It always says the player wins, even when they should lose!

EXPECTED BEHAVIOR:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

ACTUAL BEHAVIOR:
Player wins every time, regardless of choices.
"""

def buggy_determine_winner(player, computer):
    # Check if player wins
    if player == "rock" and computer == "scissors":
        return "You win!"
    if player == "scissors" and computer == "paper":
        return "You win!"
    if player == "paper" and computer == "rock":
        return "You win!"
    if player == computer:
        return "It's a tie!"
    # BUG: What if computer wins? There's no else!
    return "You win!"


def fix_determine_winner(player, computer):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: What should happen when none of the win
    #       conditions are met and it's not a tie?
    #
    # The fix:
    pass


# ============================================================
# BUG HUNT E: The Stuck Counter
# ============================================================
"""
STORY:
{{hero}}'s attempt counter should track how many guesses
were made, but it always shows 0 at the end!

EXPECTED BEHAVIOR:
After 5 guesses, display "You took 5 attempts"

ACTUAL BEHAVIOR:
Always displays "You took 0 attempts"
"""

def buggy_counting_game():
    import random
    secret = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess (1-10): "))
        attempts = 0  # BUG: Resets counter every time!

        if guess == secret:
            print(f"Correct! You took {attempts} attempts")
            break
        else:
            print("Try again!")


def fix_counting_game():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: Where should attempts = 0 go? Where should
    #       attempts be incremented?
    #
    # The fix:
    import random
    secret = random.randint(1, 10)

    pass  # Your code here


def main():
    print("=== Bug Hunt: Game Logic ===")
    print()
    print("Each game has exactly ONE logic bug.")
    print("Find the bug, then write the fix.")
    print()
    print("="*50)

    # Test what we can without input():
    # print("\nBuggy Check Guess (5, 5):", buggy_check_guess(5, 5))
    # Note: The above would cause SyntaxError due to = vs ==
    print("\nBug A: Uses = instead of == (SyntaxError)")
    print("  Expected for (5, 5): You win!")

    print("\nBuggy Calculate Score (3):", buggy_calculate_score(3))
    print("  Expected: 30")

    print("\nBuggy Determine Winner ('scissors', 'rock'):",
          buggy_determine_winner("scissors", "rock"))
    print("  Expected: Computer wins! (or similar)")

    print("\n" + "="*50)
    print("Now fix each function and test your fixes!")


main()
