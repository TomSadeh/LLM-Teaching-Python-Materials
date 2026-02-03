"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}

Topic: Finding bugs in random module usage
Difficulty: 2-3

The random module has some common pitfalls:
- randint is INCLUSIVE on both ends (unlike range)
- Forgetting to import random
- Using wrong function for the task
"""

import random


# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# This die roller should roll from 1 to 6, but something's off.
#
# EXPECTED BEHAVIOR:
# Return values from 1 to 6 (inclusive)
#
# ACTUAL BEHAVIOR:
# Returns values from 0 to 5 (never returns 6!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}


def buggy_roll_die():
    """This code has exactly ONE bug. Find it!"""
    return random.randint(0, 5)  # BUG: Range should be 1 to 6


def fix_roll_die():
    """
    Fix the die roller to return 1-6.

    Returns:
        int: A random number from 1 to 6 (inclusive)
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# This picker should select from a list, but picks indices instead.
#
# EXPECTED BEHAVIOR:
# Return one of: "{{hero}}", "{{villain}}", "{{friend}}"
#
# ACTUAL BEHAVIOR:
# Returns 0, 1, or 2 (the indices, not the names!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}


def buggy_pick_character():
    """This code has exactly ONE bug. Find it!"""
    characters = ["{{hero}}", "{{villain}}", "{{friend}}"]
    return random.randint(0, len(characters) - 1)  # BUG: Returns index, not item


def fix_pick_character():
    """
    Fix the picker to return an actual character name.

    Returns:
        str: A randomly chosen character name
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # Hint: Use random.choice() instead of randint for picking from lists
    #
    # The fix:
    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# This chance function should return True about 70% of the time.
#
# EXPECTED BEHAVIOR:
# Returns True approximately 70% of the time
#
# ACTUAL BEHAVIOR:
# Returns True approximately 30% of the time (inverted!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}


def buggy_seventy_percent_chance():
    """This code has exactly ONE bug. Find it!"""
    roll = random.random()
    return roll > 0.7  # BUG: Condition is inverted! Should be < 0.7


def fix_seventy_percent_chance():
    """
    Fix the function to return True about 70% of the time.

    Returns:
        bool: True approximately 70% of the time
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# This damage calculator has an off-by-one error in its range.
#
# EXPECTED BEHAVIOR:
# Deal base damage plus 1-5 bonus (so 11-15 if base is 10)
#
# ACTUAL BEHAVIOR:
# Deals base damage plus 1-6 bonus (includes 6, which is too high)
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}


def buggy_calculate_damage(base_damage):
    """This code has exactly ONE bug. Find it!"""
    bonus = random.randint(1, 6)  # BUG: Should be 1-5, not 1-6
    return base_damage + bonus


def fix_calculate_damage(base_damage):
    """
    Fix the damage calculator.

    Args:
        base_damage: The base damage amount

    Returns:
        int: base_damage plus a random bonus from 1 to 5
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_5_TITLE}}
# ============================================================
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# This coin flipper should return "heads" or "tails" randomly.
#
# EXPECTED BEHAVIOR:
# Return "heads" or "tails" with equal probability
#
# ACTUAL BEHAVIOR:
# Always returns "heads" (the variable is assigned but never used)
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}


def buggy_flip_coin():
    """This code has exactly ONE bug. Find it!"""
    result = random.choice(["heads", "tails"])
    return "heads"  # BUG: Ignores the random result, always returns "heads"


def fix_flip_coin():
    """
    Fix the coin flipper.

    Returns:
        str: Either "heads" or "tails" randomly
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_6_TITLE}}
# ============================================================
# {{CONTEXT_CASE_6_NARRATIVE}}
#
# This stat generator should create balanced stats (total around 30).
#
# EXPECTED BEHAVIOR:
# Generate three stats of 8-12 each, total 24-36
#
# ACTUAL BEHAVIOR:
# All three stats are the SAME value (rolled once, used three times)
#
# {{CONTEXT_INVESTIGATION_PROMPT_6}}


def buggy_generate_balanced_stats():
    """This code has exactly ONE bug. Find it!"""
    roll = random.randint(8, 12)
    return {
        "strength": roll,  # BUG: Same roll used for all three!
        "agility": roll,
        "wisdom": roll
    }


def fix_generate_balanced_stats():
    """
    Fix the stat generator to give different values.

    Returns:
        dict: Three stats, each independently rolled 8-12
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Testing die roller (should be 1-6):")
    results = [buggy_roll_die() for _ in range(10)]
    print(f"Buggy rolls: {results}")
    print("Notice: never gets 6, sometimes gets 0!")

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Testing character picker:")
    print(f"Buggy result: {buggy_pick_character()} (should be a name, not number)")

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Testing 70% chance (100 trials):")
    successes = sum(1 for _ in range(100) if buggy_seventy_percent_chance())
    print(f"Buggy successes: {successes}/100 (should be ~70)")

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Testing damage calculator (base 10):")
    damages = [buggy_calculate_damage(10) for _ in range(10)]
    print(f"Buggy damages: {damages}")
    print("Notice: might include 16 (10+6), which shouldn't be possible!")

    print("\n=== {{CASE_5_TITLE}} ===")
    print("Testing coin flipper (10 flips):")
    flips = [buggy_flip_coin() for _ in range(10)]
    print(f"Buggy flips: {flips}")
    print("Notice: always heads!")

    print("\n=== {{CASE_6_TITLE}} ===")
    print("Testing stat generator:")
    stats = buggy_generate_balanced_stats()
    print(f"Buggy stats: {stats}")
    print("Notice: all stats are identical!")

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
