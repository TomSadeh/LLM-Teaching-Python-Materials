"""
{{CONTEXT_BLANK_PAGE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Design and implement classes from scratch based on requirements.
No starter code is provided - you must design the structure yourself.
"""


# ============================================================
# {{BLANK_1_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_1_NARRATIVE}}


def timer_class():
    """
    Design a Timer class for tracking time at {{school}}.

    Requirements:
        - Initialize with a name for the timer
        - Track seconds elapsed (starts at 0)
        - Method to add time (tick)
        - Method to reset to 0
        - Method to get formatted time as "MM:SS"
        - __str__ should return "[name]: MM:SS"

    Examples:
        >>> timer = Timer("Quest Timer")
        >>> timer.get_time()
        '00:00'
        >>> timer.tick(90)  # Add 90 seconds
        >>> timer.get_time()
        '01:30'
        >>> str(timer)
        'Quest Timer: 01:30'
        >>> timer.reset()
        >>> timer.get_time()
        '00:00'

    Hints:
        - minutes = seconds // 60
        - remaining_seconds = seconds % 60
        - Use f"{value:02d}" to zero-pad numbers
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_2_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_2_NARRATIVE}}


def leaderboard_class():
    """
    Design a Leaderboard class for {{school}} competitions.

    Requirements:
        - Initialize with a competition name
        - Store player scores (name -> score mapping)
        - Method to add/update a player's score
        - Method to get a player's score (0 if not found)
        - Method to get the top N players (list of tuples)
        - Method to get total number of players
        - __str__ should show the competition name and top 3

    Examples:
        >>> board = Leaderboard("{{spell1}} Tournament")
        >>> board.add_score("{{hero}}", 100)
        >>> board.add_score("{{heroine}}", 150)
        >>> board.add_score("{{friend}}", 75)
        >>> board.get_score("{{hero}}")
        100
        >>> board.get_score("unknown")
        0
        >>> board.get_top(2)
        [('{{heroine}}', 150), ('{{hero}}', 100)]
        >>> board.player_count()
        3

    Hints:
        - Use a dictionary for scores
        - sorted(dict.items(), key=lambda x: x[1], reverse=True)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_3_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_3_NARRATIVE}}


def stat_tracker_class():
    """
    Design a StatTracker class for tracking character statistics.

    Requirements:
        - Initialize with character name and a dict of base stats
        - Store current stats (which can change) and base stats (reference)
        - Method to modify a stat by an amount (positive or negative)
        - Method to reset all stats to base values
        - Method to get a stat's current value
        - Method to get stat as percentage of base: current/base * 100
        - Method to check if any stat is below 25% of its base (is_critical)
        - __str__ shows all current stats

    Examples:
        >>> stats = StatTracker("{{hero}}", {"health": 100, "mana": 50, "stamina": 75})
        >>> stats.get_stat("health")
        100
        >>> stats.modify_stat("health", -30)
        >>> stats.get_stat("health")
        70
        >>> stats.get_percentage("health")
        70.0
        >>> stats.is_critical()
        False
        >>> stats.modify_stat("mana", -45)
        >>> stats.is_critical()
        True
        >>> stats.reset_all()
        >>> stats.get_stat("health")
        100

    Hints:
        - Make a copy of base_stats for current_stats
        - Use dict.copy() to avoid shared references
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Run tests for all classes."""
    print("Testing your implementations...\n")

    print("{{BLANK_1_TITLE}} - Timer")
    # Uncomment to test:
    # timer = Timer("Quest Timer")
    # assert timer.get_time() == "00:00"
    # timer.tick(90)
    # assert timer.get_time() == "01:30"
    # timer.reset()
    # assert timer.get_time() == "00:00"
    print("   (Uncomment tests after implementing)\n")

    print("{{BLANK_2_TITLE}} - Leaderboard")
    # Uncomment to test:
    # board = Leaderboard("Tournament")
    # board.add_score("{{hero}}", 100)
    # board.add_score("{{heroine}}", 150)
    # assert board.get_score("{{hero}}") == 100
    # assert board.get_score("unknown") == 0
    # top = board.get_top(1)
    # assert top[0][0] == "{{heroine}}"
    print("   (Uncomment tests after implementing)\n")

    print("{{BLANK_3_TITLE}} - StatTracker")
    # Uncomment to test:
    # stats = StatTracker("{{hero}}", {"health": 100, "mana": 50})
    # assert stats.get_stat("health") == 100
    # stats.modify_stat("health", -30)
    # assert stats.get_stat("health") == 70
    # assert stats.get_percentage("health") == 70.0
    # stats.reset_all()
    # assert stats.get_stat("health") == 100
    print("   (Uncomment tests after implementing)\n")

    print("=" * 40)
    print("All tests passed!")


def main():
    print("{{CONTEXT_BLANK_PAGE_INTRO}}")
    print("=" * 50)
    print()
    print("Implement each class based on its docstring specification.")
    print("When ready, run the tests to check your work.")
    print()

    # Uncomment the function for the class you're working on:
    # timer_class()
    # leaderboard_class()
    # stat_tracker_class()

    # Uncomment to run tests:
    # run_tests()

    print("{{CONTEXT_MASTERY_COMPLETE}}")


main()
