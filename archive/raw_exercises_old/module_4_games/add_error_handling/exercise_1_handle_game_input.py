# Exercise 1: Add Error Handling - Game Input
#
# Each function works for good input but crashes on bad input.
# Add try/except blocks to handle errors gracefully.
#
# Theme: Making {{hero}}'s games robust against invalid player input


# ============================================================
# ERROR HANDLING A: Number Guessing Input
# ============================================================

def original_get_guess():
    """ORIGINAL: Crashes if player types non-number"""
    user_input = input("Guess a number (1-100): ")
    guess = int(user_input)  # Crashes on "abc" or ""
    return guess


def safe_get_guess():
    """
    Get a number guess from the player.

    Should handle:
    - Non-numeric input → return None and print "Please enter a number!"
    - Empty input → return None and print "Please enter something!"

    Returns:
        int or None: The guess as integer, or None if invalid
    """
    # ✏️ ADD ERROR HANDLING ✏️
    user_input = input("Guess a number (1-100): ")

    # Wrap the conversion in try/except
    # Hint: int("abc") raises ValueError

    pass


# ============================================================
# ERROR HANDLING B: Dice Roll Selection
# ============================================================

def original_select_dice(dice_list, index):
    """ORIGINAL: Crashes if index out of range"""
    return dice_list[index]  # Crashes on bad index


def safe_select_dice(dice_list, index):
    """
    Select a die from the list by index.

    Should handle:
    - Index out of range → return None and print "Invalid dice selection!"
    - Empty list → return None and print "No dice available!"

    Args:
        dice_list: List of dice values
        index: Which die to select (0-based)

    Returns:
        int or None: The selected die value, or None if invalid
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: bad index raises IndexError

    pass


# ============================================================
# ERROR HANDLING C: Score Division
# ============================================================

def original_calculate_average(total_score, num_rounds):
    """ORIGINAL: Crashes if num_rounds is zero"""
    return total_score / num_rounds  # Crashes on division by zero


def safe_calculate_average(total_score, num_rounds):
    """
    Calculate average score per round.

    Should handle:
    - Division by zero → return 0 and print "No rounds played yet!"

    Args:
        total_score: Total points earned
        num_rounds: Number of rounds played

    Returns:
        float: Average score, or 0 if no rounds played
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: 1/0 raises ZeroDivisionError

    pass


# ============================================================
# ERROR HANDLING D: Player Choice Menu
# ============================================================

def original_get_menu_choice(options):
    """ORIGINAL: Crashes on non-numeric or out-of-range input"""
    print("Choose an option:")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    choice = int(input("Enter number: "))
    return options[choice - 1]  # Could crash twice!


def safe_get_menu_choice(options):
    """
    Display menu and get player's choice.

    Should handle:
    - Non-numeric input → print "Please enter a number!" and return None
    - Number out of range → print "Choose 1-{len(options)}!" and return None
    - Empty options list → print "No options available!" and return None

    Args:
        options: List of menu options

    Returns:
        str or None: The selected option, or None if invalid
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Multiple things can go wrong here!

    pass


# ============================================================
# ERROR HANDLING E: Rock Paper Scissors
# ============================================================

VALID_MOVES = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def original_check_winner(player_move, computer_move):
    """ORIGINAL: Crashes if moves not in valid set"""
    if player_move == computer_move:
        return "tie"
    elif VALID_MOVES[player_move] == computer_move:  # Crashes on invalid move
        return "player"
    else:
        return "computer"


def safe_check_winner(player_move, computer_move):
    """
    Determine the winner of rock-paper-scissors.

    Should handle:
    - Invalid player move → return "invalid" and print "Invalid move: {move}"
    - Invalid computer move → return "error" (this shouldn't happen!)

    Args:
        player_move: "rock", "paper", or "scissors"
        computer_move: "rock", "paper", or "scissors"

    Returns:
        str: "player", "computer", "tie", "invalid", or "error"
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: invalid key raises KeyError

    pass


# ============================================================
# ERROR HANDLING F: High Score Update
# ============================================================

def original_update_high_score(scores_dict, player_name, new_score):
    """ORIGINAL: Crashes on None values or missing key check"""
    current_score = scores_dict[player_name]
    if new_score > current_score:
        scores_dict[player_name] = new_score
        return True
    return False


def safe_update_high_score(scores_dict, player_name, new_score):
    """
    Update high score if new score is higher.

    Should handle:
    - Player not in dict → add them with new_score, return True
    - None dict → print "Score system not initialized!" return False
    - None score → print "Invalid score!" return False

    Args:
        scores_dict: Dictionary of player names to scores
        player_name: Name of the player
        new_score: Their latest score

    Returns:
        bool: True if score was updated/added, False otherwise
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Multiple error types possible!

    pass


def main():
    print("=== Test A: Number Guessing Input ===")
    print("Try typing 'abc' or pressing Enter with no input")
    # result = safe_get_guess()
    # print(f"Got: {result}")

    print("\n=== Test B: Dice Selection ===")
    dice = [3, 5, 2, 6]
    print(f"Dice: {dice}")
    print(f"Select index 1: {safe_select_dice(dice, 1)}")
    print(f"Select index 99: {safe_select_dice(dice, 99)}")
    print(f"Select from empty: {safe_select_dice([], 0)}")

    print("\n=== Test C: Score Division ===")
    print(f"100 points / 4 rounds = {safe_calculate_average(100, 4)}")
    print(f"50 points / 0 rounds = {safe_calculate_average(50, 0)}")

    print("\n=== Test D: Menu Choice ===")
    options = ["Start Game", "High Scores", "Quit"]
    # result = safe_get_menu_choice(options)
    # print(f"Selected: {result}")

    print("\n=== Test E: Rock Paper Scissors ===")
    print(f"rock vs scissors: {safe_check_winner('rock', 'scissors')}")
    print(f"paper vs paper: {safe_check_winner('paper', 'paper')}")
    print(f"banana vs rock: {safe_check_winner('banana', 'rock')}")

    print("\n=== Test F: High Score Update ===")
    scores = {"{{hero}}": 100, "{{friend}}": 85}
    print(f"Update {{hero}} with 150: {safe_update_high_score(scores, '{{hero}}', 150)}")
    print(f"Update {{heroine}} with 90: {safe_update_high_score(scores, '{{heroine}}', 90)}")
    print(f"Scores now: {scores}")


main()
