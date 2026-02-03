"""
{{CONTEXT_SETBACK_INTRO}}

This is a multi-part exercise where you rescue a crashed leaderboard system.
The competition is tomorrow and the system must be fixed!

Programming concepts: dictionaries, CRUD operations, sorting, error handling
"""


# ============================================================
# PART 1: The Setback - Diagnose the Crash
# ============================================================
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# The leaderboard crashed during last night's tournament!
# Read the error and understand what went wrong.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "leaderboard.py", line 23, in <module>
    update_score(leaderboard, "NewPlayer", 50)
  File "leaderboard.py", line 15, in update_score
    leaderboard[player_name] += points
KeyError: 'NewPlayer'
"""


def buggy_update_score(leaderboard, player_name, points):
    """BUGGY: Add points to a player's score."""
    leaderboard[player_name] += points


def diagnose_crash():
    # ✏️ DIAGNOSE THE ERROR ✏️
    #
    # Answer these questions:
    #
    # 1. What type of error occurred?
    #    Answer:
    #
    # 2. Why did the error happen?
    #    Answer:
    #
    # 3. What was the code trying to do?
    #    Answer:
    #
    # 4. What's the difference between updating an existing player
    #    and adding a new player?
    #    Answer:

    pass


# ============================================================
# PART 2: Investigation - Trace the Score Logic
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Trace through the intended behavior to understand
# how the leaderboard should work.


def code_to_trace():
    """Trace this correct version."""
    leaderboard = {"{{hero}}": 100, "{{heroine}}": 150}

    # Update existing player
    leaderboard["{{hero}}"] = leaderboard.get("{{hero}}", 0) + 50

    # Add new player
    leaderboard["{{friend}}"] = leaderboard.get("{{friend}}", 0) + 75

    print(leaderboard)


def trace_leaderboard():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | Operation              | .get() returns | leaderboard after           |
    # |------|------------------------|----------------|----------------------------|
    # | 0    | Initial state          | -              | {"{{hero}}": 100, "{{heroine}}": 150} |
    # | 1    | Update {{hero}} +50    | 100            |                            |
    # | 2    | Add {{friend}} +75     |                |                            |
    #
    # What is printed?

    pass


# ============================================================
# PART 3: Improvement - Rebuild the Leaderboard
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Build a robust leaderboard system from scratch.


def create_leaderboard():
    """
    Create a new empty leaderboard.

    Returns:
        dict: Empty dictionary for storing player scores
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def add_player(leaderboard, player_name, initial_score=0):
    """
    Add a new player to the leaderboard.

    Args:
        leaderboard: The leaderboard dict
        player_name: Name of the new player
        initial_score: Starting score (default 0)

    Returns:
        bool: True if added, False if player already exists
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Check if player exists first.
    # If they exist, return False (don't overwrite).
    # If new, add them with initial_score and return True.

    pass


def update_score(leaderboard, player_name, points):
    """
    Update a player's score (add points).

    Args:
        leaderboard: The leaderboard dict
        player_name: Player to update
        points: Points to add (can be negative)

    If player doesn't exist, they are automatically added.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use .get() to safely handle new players.

    pass


def get_score(leaderboard, player_name):
    """
    Get a player's current score.

    Args:
        leaderboard: The leaderboard dict
        player_name: Player to look up

    Returns:
        int: The player's score, or 0 if not on leaderboard
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def get_top_players(leaderboard, n=3):
    """
    Get the top N players by score.

    Args:
        leaderboard: The leaderboard dict
        n: Number of top players to return

    Returns:
        list: List of (name, score) tuples, sorted by score descending
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Convert to list of (name, score) tuples using .items()
    # Step 2: Sort by score (hint: use sorted() with key parameter)
    # Step 3: Return the top n
    #
    # Hint: sorted(items, key=lambda x: x[1], reverse=True)

    pass


def display_leaderboard(leaderboard):
    """
    Display the full leaderboard in a nice format.

    Args:
        leaderboard: The leaderboard dict

    Prints the leaderboard with rankings.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Get all players sorted by score
    # Print with ranking: "1. PlayerName: 150 points"

    pass


# ============================================================
# PART 4: Growth - Add New Features
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Add advanced features to the leaderboard.


def get_rank(leaderboard, player_name):
    """
    Get a player's current rank.

    Args:
        leaderboard: The leaderboard dict
        player_name: Player to find

    Returns:
        int: The player's rank (1 = first place), or -1 if not found
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Sort all players by score, then find the player's position.

    pass


def get_players_above(leaderboard, threshold):
    """
    Get all players with scores above a threshold.

    Args:
        leaderboard: The leaderboard dict
        threshold: Minimum score

    Returns:
        list: Names of players with score > threshold
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def reset_scores(leaderboard):
    """
    Reset all scores to 0 (for a new tournament).

    Args:
        leaderboard: The leaderboard dict (modified in place)
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Keep all players but set scores to 0.

    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_SETBACK_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Diagnose the crash...")
    print("(Complete diagnose_crash())")
    print()

    print(">>> PART 2: Trace the logic...")
    print("(Complete trace_leaderboard())")
    # Uncomment to verify:
    # code_to_trace()
    print()

    print(">>> PART 3: Rebuild the leaderboard...")
    print("(Implement all leaderboard functions)")
    print()
    # Uncomment after implementing Part 3:
    # board = create_leaderboard()
    # add_player(board, "{{hero}}", 100)
    # add_player(board, "{{heroine}}", 150)
    # add_player(board, "{{friend}}", 75)
    # print(f"Leaderboard: {board}")
    #
    # update_score(board, "{{hero}}", 60)
    # update_score(board, "NewPlayer", 200)  # Should not crash!
    # print(f"After updates: {board}")
    #
    # print(f"{{{{hero}}}}'s score: {get_score(board, '{{hero}}')}")
    # print(f"Top 3: {get_top_players(board, 3)}")
    # print()
    # display_leaderboard(board)

    print()
    print(">>> PART 4: Add new features...")
    print("(Implement get_rank, get_players_above, reset_scores)")
    # Uncomment after implementing Part 4:
    # print(f"{{{{hero}}}}'s rank: {get_rank(board, '{{hero}}')}")
    # print(f"Players above 100: {get_players_above(board, 100)}")
    # reset_scores(board)
    # print(f"After reset: {board}")

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
