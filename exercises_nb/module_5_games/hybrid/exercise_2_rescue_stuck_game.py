"""
{{CONTEXT_SETBACK_INTRO}}

This is a multi-part exercise where you rescue a stuck game.
The game freezes and crashes - find out why and fix it!

Programming concepts: while loops, infinite loops, input validation
"""


# ============================================================
# PART 1: The Freeze
# ============================================================
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{friend}}'s game freezes every time! The loop never ends.
# Examine the code and find where it gets stuck.
#
# BUGS TO FIND: 2 infinite loop bugs


def buggy_game_loop():
    """
    This game loop freezes. Find the 2 bugs!

    BUG 1: The main game loop counter never updates
    BUG 2: The score display loop has wrong condition
    """
    print("=== {{school}} Adventure ===")
    print()

    score = 0
    round_num = 1
    max_rounds = 3

    # Game loop
    while round_num <= max_rounds:
        print(f"Round {round_num}")

        # Player gains some points
        score += 10
        print(f"Score: {score}")

        # BUG 1: round_num never increments! Loop runs forever!

    print()
    print("=== Final Scores ===")

    # Display score with stars
    stars_shown = 0
    while stars_shown < score:  # BUG 2: If score > 0, shows infinite stars!
        print("*", end="")
        # stars_shown never increases!

    print()
    print(f"Final score: {score}")


def fixed_game_loop():
    """
    Fix both infinite loop bugs.

    Bug 1: Add round_num += 1 inside the game loop
    Bug 2: Add stars_shown += 1 inside the stars loop
    """
    # ✏️ FIX THE BUGS ✏️
    #
    # What I found:
    # Bug 1: ________________________________
    # Bug 2: ________________________________
    pass


# ============================================================
# PART 2: More Problems
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# After fixing the freezes, {{friend}} found more issues.
# Find and fix these additional loop bugs.
#
# BUGS TO FIND: 2 more bugs


def buggy_inventory_system():
    """
    This inventory system has issues. Find the 2 bugs!

    BUG 1: The exit condition is wrong (= instead of ==)
    BUG 2: Items are added but loop condition never changes
    """
    inventory = []
    max_items = 5

    print("=== {{hero}}'s Inventory ===")
    print("Commands: 'add <item>' or 'done'")
    print()

    while len(inventory) < max_items:
        command = input("> ")

        # BUG 1: Assignment instead of comparison!
        if command = "done":  # Should be ==
            break

        if command.startswith("add "):
            item = command[4:]  # Get text after "add "
            # Items get added correctly
            print(f"Added: {item}")
            # BUG 2: Forgot to actually add to inventory!
            # inventory.append(item) is missing!
        else:
            print("Unknown command")

    print(f"Inventory: {inventory}")


def fixed_inventory_system():
    """
    Fix both bugs in the inventory system.

    Bug 1: Change = to == in the condition
    Bug 2: Add inventory.append(item) when adding
    """
    # ✏️ FIX THE BUGS ✏️
    #
    # What I found:
    # Bug 1: ________________________________
    # Bug 2: ________________________________
    pass


# ============================================================
# PART 3: Make It Robust
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Now that the bugs are fixed, add input validation
# to prevent future crashes!


def robust_number_input():
    """
    Add validation to this number input function.
    Currently crashes if user enters non-numeric input.

    Requirements:
    - Ask for a number between 1 and 10
    - If input is not a number, show error and ask again
    - If number is out of range, show error and ask again
    - Return the valid number

    Returns:
        int: A valid number from 1 to 10
    """
    # ✏️ ADD INPUT VALIDATION ✏️
    #
    # Step 1: Start while True loop
    # Step 2: Get input
    # Step 3: Check if input.isdigit()
    #         If not, print "Please enter a number." and continue
    # Step 4: Convert to int
    # Step 5: Check if 1 <= number <= 10
    #         If not, print "Number must be 1-10." and continue
    # Step 6: Return the valid number
    pass


def robust_command_parser():
    """
    Add validation to this command parser.
    Currently accepts any input, even garbage.

    Valid commands:
    - "attack" - Attack the {{villain}}
    - "defend" - Defend against attacks
    - "heal" - Restore {{primary_stat}}
    - "quit" - Exit the game

    Requirements:
    - Show menu of valid commands
    - If invalid command, show error and valid options
    - Case insensitive
    - Return the valid command (lowercase)

    Returns:
        str: A valid command
    """
    # ✏️ ADD INPUT VALIDATION ✏️
    #
    # Step 1: Define valid_commands list
    # Step 2: Print the menu
    # Step 3: Start while True loop
    # Step 4: Get input and convert to lowercase
    # Step 5: If in valid_commands, return it
    # Step 6: Otherwise print "Invalid. Commands: attack, defend, heal, quit"
    pass


def robust_game_menu():
    """
    Create a complete game menu with full validation.

    Menu options:
    1. Start new game
    2. Load game
    3. Settings
    4. Quit

    Requirements:
    - Display numbered menu
    - Accept number (1-4) or text (e.g., "start", "quit")
    - Case insensitive for text
    - Return the choice as a lowercase string

    Returns:
        str: "start", "load", "settings", or "quit"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Define menu options mapping
    #         options = {"1": "start", "start": "start", "new": "start",
    #                    "2": "load", "load": "load", ...}
    # Step 2: Print menu
    # Step 3: Start while True loop
    # Step 4: Get input lowercase
    # Step 5: If input in options, return options[input]
    # Step 6: Print "Invalid choice. Enter 1-4 or command name."
    pass


# ============================================================
# PART 4: The Better Game
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now build a complete, crash-proof mini-game using
# everything you've learned!


def battle_game():
    """
    A simple turn-based battle game with full input validation.

    Game loop:
    1. Show player and enemy {{primary_stat}}
    2. Get valid command (attack, defend, heal, quit)
    3. Process command
    4. Enemy attacks (if not quit)
    5. Check for win/lose
    6. Repeat until someone wins or player quits

    Stats:
    - Player starts with 30 {{primary_stat}}
    - {{villain}} starts with 25 {{primary_stat}}
    - Attack deals 5-8 damage
    - Defend reduces incoming damage by half
    - Heal restores 5-10 {{primary_stat}}
    - {{villain}} always attacks for 3-6 damage
    """
    import random

    print("=" * 40)
    print(f"   {{{{hero}}}} vs {{{{villain}}}}")
    print("=" * 40)
    print()

    player_hp = 30
    enemy_hp = 25
    defending = False

    # ✏️ YOUR CODE HERE ✏️
    #
    # While both player and enemy have {{primary_stat}} > 0:
    #   1. Display current {{primary_stat}}
    #   2. Get command with robust_command_parser()
    #   3. If "quit", print farewell and return
    #   4. Process player action:
    #      - "attack": enemy loses 5-8 {{primary_stat}}
    #      - "defend": set defending = True
    #      - "heal": player gains 5-10 {{primary_stat}}
    #   5. If enemy still alive, enemy attacks:
    #      - Base damage = random 3-6
    #      - If defending, damage = damage // 2
    #      - Player loses that much {{primary_stat}}
    #   6. Reset defending to False
    #   7. Check win/lose conditions
    #
    # After loop: Announce winner
    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_SETBACK_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Find the infinite loops...")
    print("(DON'T RUN buggy_game_loop - it freezes!)")
    print("(Implement fixed_game_loop)")
    print()
    # Uncomment to test:
    # fixed_game_loop()

    print()
    print(">>> PART 2: Find more bugs...")
    print("(Note: buggy_inventory_system has a syntax error)")
    print("(Implement fixed_inventory_system)")
    print()
    # Uncomment to test:
    # fixed_inventory_system()

    print()
    print(">>> PART 3: Add validation...")
    print("(Implement the robust input functions)")
    print()
    # Uncomment to test:
    # num = robust_number_input()
    # print(f"You entered: {num}")
    # cmd = robust_command_parser()
    # print(f"Command: {cmd}")
    # choice = robust_game_menu()
    # print(f"Menu choice: {choice}")

    print()
    print(">>> PART 4: Build the better game...")
    print("(Implement battle_game)")
    print()
    # Uncomment to test:
    # battle_game()

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
