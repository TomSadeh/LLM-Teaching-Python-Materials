"""
{{CONTEXT_SETBACK_INTRO}}

This is a multi-part exercise rescuing a text adventure game.
Find bugs, debug navigation, add error handling, then extend it!

Programming concepts: while loops, dictionaries (preview), command parsing, game state
"""


# ============================================================
# PART 1: The Broken Adventure
# ============================================================
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{friend}}'s text adventure has critical bugs.
# Players get stuck and the game crashes!
#
# BUGS TO FIND: 3


# Game world (simplified - no dictionaries, use parallel lists)
ROOM_NAMES = ["entrance", "hallway", "treasure_room", "exit"]
ROOM_DESCRIPTIONS = [
    "You are at the entrance of {{location}}.",
    "A long hallway stretches before you.",
    "{{exclamation}} A treasure chest gleams!",
    "The exit! Fresh air awaits."
]
# Connections: index = from room, value = [north, south, east, west] or -1 if blocked
ROOM_CONNECTIONS = [
    [-1, -1, 1, -1],   # entrance: east to hallway
    [2, -1, 3, 0],     # hallway: north to treasure, east to exit, west to entrance
    [-1, 1, -1, -1],   # treasure: south to hallway
    [-1, -1, -1, 1]    # exit: west to hallway
]


def buggy_get_room_description(room_index):
    """Get description for a room. BUG: No bounds checking!"""
    return ROOM_DESCRIPTIONS[room_index]  # BUG 1: Crashes if index out of range


def buggy_move(current_room, direction):
    """
    Move in a direction.

    BUG 2: Direction mapping is wrong
    BUG 3: Returns wrong room on blocked path
    """
    # BUG 2: Direction indices are wrong!
    direction_index = {
        "north": 2,  # Should be 0
        "south": 0,  # Should be 1
        "east": 3,   # Should be 2
        "west": 1    # Should be 3
    }

    if direction not in direction_index:
        return current_room

    idx = direction_index[direction]
    next_room = ROOM_CONNECTIONS[current_room][idx]

    # BUG 3: Returns -1 instead of current_room when blocked!
    return next_room  # Should check if -1 and return current_room


def buggy_adventure():
    """Play the buggy adventure."""
    current_room = 0
    print("=== {{school}} Adventure ===")
    print(buggy_get_room_description(current_room))

    while current_room != 3:  # Exit is room 3
        command = input("\n> ").lower().strip()

        if command in ["north", "south", "east", "west"]:
            new_room = buggy_move(current_room, command)
            if new_room == current_room:
                print("You can't go that way.")
            else:
                current_room = new_room
                print(buggy_get_room_description(current_room))
        elif command == "look":
            print(buggy_get_room_description(current_room))
        elif command == "quit":
            break
        else:
            print("Unknown command.")

    print("\nThanks for playing!")


def fixed_get_room_description(room_index):
    """
    Fix Bug 1: Add bounds checking.

    Return "Invalid room" if index out of range.
    """
    # ✏️ FIX THE BUG ✏️
    pass


def fixed_move(current_room, direction):
    """
    Fix Bugs 2 and 3:
    - Correct direction indices
    - Return current_room when blocked (not -1)
    """
    # ✏️ FIX THE BUGS ✏️
    pass


# ============================================================
# PART 2: Debug the Navigation
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# The movement system has more subtle bugs.
# Find and fix these navigation issues.


def buggy_parse_command(command_string):
    """
    Parse a movement command.

    BUGS:
    1. Doesn't handle extra spaces
    2. Doesn't handle "go north" style commands
    """
    # BUG 1: No stripping of extra spaces
    # BUG 2: Doesn't extract direction from "go north"
    parts = command_string.split()
    if len(parts) == 1:
        return parts[0]
    return None  # Fails on "go north"


def fixed_parse_command(command_string):
    """
    Fix command parsing to handle:
    - Extra spaces
    - "go <direction>" format
    - Just "<direction>" format
    - Return None for invalid commands
    """
    # ✏️ FIX THE BUGS ✏️
    #
    # Step 1: Strip and lowercase
    # Step 2: Split into parts
    # Step 3: If one part and it's a direction, return it
    # Step 4: If two parts and first is "go", return second if valid
    # Step 5: Otherwise return None
    pass


def buggy_check_item(room_index, has_treasure):
    """
    Check for items in the room.

    BUG: Always says no treasure even in treasure room!
    """
    if room_index == 2:  # Treasure room
        if has_treasure:  # BUG: Logic inverted! Should be "not has_treasure"
            return False
        print("You found the treasure!")
        return True
    return has_treasure


def fixed_check_item(room_index, has_treasure):
    """
    Fix the item check logic.

    Should return True if player now has treasure.
    Should only find treasure if in room 2 AND don't already have it.
    """
    # ✏️ FIX THE BUG ✏️
    pass


# ============================================================
# PART 3: Add Error Handling
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Make the adventure crash-proof!


def safe_get_input(prompt, valid_commands):
    """
    Get input with validation.

    Args:
        prompt: What to display
        valid_commands: List of valid command strings

    Returns:
        str: A valid command

    Requirements:
    - Show prompt
    - Validate input is in valid_commands
    - Show helpful error with valid options
    - Keep asking until valid
    """
    # ✏️ ADD ERROR HANDLING ✏️
    pass


def safe_move_with_feedback(current_room, direction):
    """
    Move with clear feedback messages.

    Args:
        current_room: Current room index
        direction: Direction string

    Returns:
        tuple: (new_room, message)

    Messages:
    - Invalid direction: "Unknown direction: {direction}"
    - Blocked: "You can't go {direction} from here."
    - Success: "You move {direction}."
    """
    # ✏️ ADD ERROR HANDLING ✏️
    pass


def robust_adventure_loop(starting_room):
    """
    A robust game loop that handles all errors gracefully.

    Args:
        starting_room: Room index to start in

    Features:
    - Clear command menu
    - Handles unknown commands
    - Tracks items (treasure)
    - Win condition (exit with treasure)
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Variables:
    # - current_room = starting_room
    # - has_treasure = False
    # - playing = True
    #
    # While playing:
    #   1. Show current room description
    #   2. Show commands: north/south/east/west/look/inventory/quit
    #   3. Get input
    #   4. Process command:
    #      - directions: move and show feedback
    #      - look: show description
    #      - inventory: show if has treasure
    #      - quit: set playing = False
    #   5. Check for treasure
    #   6. Check win condition (at exit with treasure)
    pass


# ============================================================
# PART 4: Extend the Adventure
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Add new features to make the adventure better!


def add_enemy_encounter(room_index):
    """
    Check if there's an enemy in this room.

    Args:
        room_index: Current room

    Returns:
        bool: True if enemy encountered

    Enemies appear in hallway (room 1) with 30% chance.
    Print encounter message if enemy appears.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def simple_combat():
    """
    Simple combat encounter.

    Returns:
        bool: True if player survives

    Combat:
    - Player has 10 HP
    - Enemy has 5 HP
    - Each round: player attacks (2-4 damage), enemy attacks (1-3 damage)
    - Continue until someone reaches 0 HP
    - Print combat messages
    """
    import random

    # ✏️ YOUR CODE HERE ✏️
    pass


def enhanced_adventure():
    """
    The complete enhanced adventure!

    New features:
    - Random enemy encounters
    - Simple combat
    - Score tracking
    - Play again option
    """
    import random

    print("=" * 50)
    print(f"   {{{{school}}}} ADVENTURE")
    print("   Enhanced Edition")
    print("=" * 50)
    print()
    print(f"{{{{hero}}}} seeks treasure in {{{{location}}}}!")
    print("Find the treasure and escape!")
    print()

    # ✏️ YOUR CODE HERE ✏️
    #
    # Game loop:
    # 1. Start in entrance (room 0)
    # 2. Track: current_room, has_treasure, score, hp
    # 3. Each room:
    #    - Check for enemy encounter
    #    - If enemy, run combat
    #    - If defeated, game over
    # 4. Movement and treasure collection
    # 5. Win: reach exit with treasure
    # 6. Track high scores
    # 7. Play again option
    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_SETBACK_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Fix the broken adventure...")
    print("(DON'T RUN buggy_adventure - it has issues!)")
    print("(Implement fixed_get_room_description and fixed_move)")
    print()
    # Test fixes:
    # print(fixed_get_room_description(0))  # Should work
    # print(fixed_get_room_description(99))  # Should say "Invalid room"
    # print(fixed_move(0, "east"))  # Should return 1 (hallway)
    # print(fixed_move(0, "north"))  # Should return 0 (blocked)

    print()
    print(">>> PART 2: Debug navigation...")
    print("(Implement fixed_parse_command and fixed_check_item)")
    print()
    # Test:
    # print(fixed_parse_command("  go  north  "))  # Should return "north"
    # print(fixed_parse_command("east"))  # Should return "east"

    print()
    print(">>> PART 3: Add error handling...")
    print("(Implement safe functions and robust_adventure_loop)")
    print()
    # robust_adventure_loop(0)

    print()
    print(">>> PART 4: Build the enhanced adventure...")
    print("(Implement all enhancements)")
    print()
    # enhanced_adventure()

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
