"""
{{CONTEXT_SETBACK_INTRO}}

This is a multi-part exercise following the journey to build a number guessing game.
Complete each part in order.

Programming concepts: while loops, random, comparisons, input validation
"""

import random


# ============================================================
# PART 1: The Broken Game
# ============================================================
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{hero}}'s first attempt at a guessing game had bugs.
# {{villain}} found all the flaws and exploited them!
#
# Find and fix the 3 bugs in the code below.
#
# BUGS TO FIND: 3


def buggy_guessing_game():
    """
    A buggy guessing game. Find the 3 bugs!

    BUG 1: The secret number range is wrong
    BUG 2: The comparison logic is inverted
    BUG 3: The guess counter never increases
    """
    secret = random.randint(0, 9)  # BUG 1: Should be 1-10, not 0-9
    guesses = 0
    max_guesses = 5

    print("Guess my number (1-10)!")

    while guesses < max_guesses:
        guess_str = input("Your guess: ")

        if not guess_str.isdigit():
            print("Please enter a number!")
            continue

        guess = int(guess_str)

        if guess < secret:  # BUG 2: Logic inverted! < should give "higher" hint
            print("Go lower!")
        elif guess > secret:
            print("Go higher!")
        else:
            print(f"Correct! You got it in {guesses} guesses!")
            return True
        # BUG 3: guesses is never incremented!

    print(f"Out of guesses! The number was {secret}")
    return False


def fixed_guessing_game():
    """
    Fix all 3 bugs from the buggy version.

    Bug fixes needed:
    1. Secret number should be 1-10 (inclusive)
    2. Hints should be correct (guess < secret means "go higher")
    3. Increment guesses after each guess
    """
    # ✏️ FIX THE BUGS ✏️
    #
    # What I found:
    # Bug 1: ________________________________
    # Bug 2: ________________________________
    # Bug 3: ________________________________
    pass


# ============================================================
# PART 2: Building Better
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now build a proper guessing game with these features:
# - Configurable range (min to max)
# - Unlimited guesses
# - Track guess count
# - Validate input is within range


def validate_guess(guess_str, min_val, max_val):
    """
    Validate that a guess string is a valid number within range.

    Args:
        guess_str: The string input from user
        min_val: Minimum valid value
        max_val: Maximum valid value

    Returns:
        tuple: (is_valid, value_or_error_message)
            - If valid: (True, integer_value)
            - If invalid: (False, error_message)

    Examples:
        validate_guess("5", 1, 10) returns (True, 5)
        validate_guess("abc", 1, 10) returns (False, "Not a number")
        validate_guess("15", 1, 10) returns (False, "Out of range (1-10)")
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Check if guess_str is a digit (use .lstrip('-').isdigit() for negatives)
    #         If not, return (False, "Not a number")
    # Step 2: Convert to integer
    # Step 3: Check if in range
    #         If not, return (False, f"Out of range ({min_val}-{max_val})")
    # Step 4: Return (True, integer_value)
    pass


def give_hint(guess, secret):
    """
    Give a hint based on the guess.

    Args:
        guess: The player's guess
        secret: The secret number

    Returns:
        str: "higher", "lower", or "correct"

    Also prints an appropriate message:
        "Too low! Guess higher."
        "Too high! Guess lower."
        "{{exclamation}} Correct!"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Compare guess to secret and return/print appropriate response
    pass


def play_guessing_round(min_val, max_val):
    """
    Play one round of the guessing game.

    Args:
        min_val: Minimum value for secret number
        max_val: Maximum value for secret number

    Returns:
        int: Number of guesses it took to win

    Game flow:
    1. Generate secret number
    2. Loop: get guess, validate, give hint
    3. Continue until correct
    4. Return guess count
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Generate secret with random.randint(min_val, max_val)
    # Step 2: Initialize guess_count = 0
    # Step 3: Loop until guessed correctly:
    #         - Get input
    #         - Validate with validate_guess()
    #         - If invalid, print error and continue
    #         - Increment guess_count
    #         - Get hint with give_hint()
    #         - If correct, break
    # Step 4: Return guess_count
    pass


# ============================================================
# PART 3: The Championship
# ============================================================
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# Build the complete championship guessing game:
# - Best of 3 rounds
# - Track wins for {{hero}} and {{villain}}
# - {{villain}} guesses using a simple strategy
# - Whoever guesses in fewer tries wins the round


def computer_guess(min_val, max_val, secret):
    """
    Simulate {{villain}}'s guessing strategy (binary search).

    Args:
        min_val: Current minimum possibility
        max_val: Current maximum possibility
        secret: The secret number (to determine result)

    Returns:
        tuple: (guess, new_min, new_max)

    Strategy: Always guess the middle value
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Calculate middle = (min_val + max_val) // 2
    # Step 2: If middle < secret, new range is (middle + 1, max_val)
    # Step 3: If middle > secret, new range is (min_val, middle - 1)
    # Step 4: Return (middle, new_min, new_max)
    pass


def computer_play_round(min_val, max_val):
    """
    {{villain}} plays a guessing round using binary search.

    Args:
        min_val: Minimum value
        max_val: Maximum value

    Returns:
        int: Number of guesses to find the secret
    """
    secret = random.randint(min_val, max_val)
    guesses = 0
    current_min = min_val
    current_max = max_val

    print(f"\n{{{{villain}}}}'s turn! (Secret: {secret})")

    while True:
        guess, current_min, current_max = computer_guess(
            current_min, current_max, secret
        )
        guesses += 1
        print(f"{{{{villain}}}} guesses: {guess}")

        if guess == secret:
            print(f"{{{{villain}}}} got it in {guesses} guesses!")
            return guesses
        elif guess < secret:
            print("Too low...")
        else:
            print("Too high...")


def championship_match():
    """
    The championship: {{hero}} vs {{villain}} in best of 3!

    Game structure:
    - 3 rounds, each with range 1-100
    - Each round: both players guess a NEW secret number
    - Fewer guesses wins the round
    - First to 2 round wins takes the championship

    Display:
    - Current score before each round
    - Winner of each round
    - Final champion announcement
    """
    print("=" * 50)
    print("   GUESSING CHAMPIONSHIP")
    print(f"   {{{{hero}}}} vs {{{{villain}}}}")
    print("=" * 50)
    print()

    hero_wins = 0
    villain_wins = 0
    round_num = 0

    # ✏️ YOUR CODE HERE ✏️
    #
    # While neither player has 2 wins:
    #   1. Increment round number
    #   2. Print round header and current score
    #   3. {{hero}} guesses (use play_guessing_round)
    #   4. {{villain}} guesses (use computer_play_round)
    #   5. Compare guess counts, award point to winner
    #   6. Announce round winner
    #
    # After loop: Announce championship winner
    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_SETBACK_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Fix the broken game...")
    print("(Review buggy_guessing_game() and implement fixed_guessing_game())")
    print()
    # Uncomment to test:
    # fixed_guessing_game()

    print()
    print(">>> PART 2: Build better validation and hints...")
    print("(Implement validate_guess, give_hint, play_guessing_round)")
    print()
    # Uncomment to test:
    # guesses = play_guessing_round(1, 20)
    # print(f"You won in {guesses} guesses!")

    print()
    print(">>> PART 3: The Championship awaits...")
    print("(Implement computer_guess and championship_match)")
    print()
    # Uncomment to test:
    # championship_match()

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
