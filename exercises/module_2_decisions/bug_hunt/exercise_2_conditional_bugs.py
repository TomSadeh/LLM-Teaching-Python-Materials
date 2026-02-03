# =============================================================================
# Bug Hunt: General Conditional Bugs
# =============================================================================
# Difficulty: 5
# Concepts: Common conditional mistakes across all types
# =============================================================================

"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}
"""


# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# {{hero}} checks if their score qualifies for a bonus.
# Score of exactly 100 should get the bonus too!
#
# EXPECTED BEHAVIOR:
# With score=100, should print "Bonus earned!"
#
# ACTUAL BEHAVIOR:
# With score=100, prints "No bonus."
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

def buggy_a():
    """This code has exactly ONE bug. Find it!"""
    score = 100
    if score > 100:  # BUG: Wrong operator
        print("{{hero}} earned a bonus!")
    else:
        print("No bonus this time.")


def fix_a():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: Using > instead of >=
    # The bug: > means "greater than" but doesn't include equal
    #          score=100 is NOT > 100, so it fails
    #
    # The fix:
    score = 100
    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# {{mentor}} wants to give different messages based on grade.
# But the conditions are in the wrong order!
#
# EXPECTED BEHAVIOR:
# With score=95, should print "Excellent!" (highest tier)
#
# ACTUAL BEHAVIOR:
# With score=95, prints "Good job!" (wrong tier)
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

def buggy_b():
    """This code has exactly ONE bug. Find it!"""
    score = 95
    # BUG: Conditions in wrong order - first match wins!
    if score >= 60:
        print("Good job!")
    elif score >= 80:
        print("Great work!")
    elif score >= 90:
        print("Excellent!")
    else:
        print("Keep practicing.")


def fix_b():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: Conditions should check highest first
    # The bug: score=95 matches "score >= 60" first, so it stops there
    #          The elif conditions are never checked
    #
    # The fix (check highest thresholds first):
    score = 95
    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# {{hero}} tries to update their gold after a purchase.
# But the gold doesn't actually change!
#
# EXPECTED BEHAVIOR:
# After buying, gold should be 70 (100 - 30)
#
# ACTUAL BEHAVIOR:
# After buying, gold is still 100
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

def buggy_c():
    """This code has exactly ONE bug. Find it!"""
    gold = 100
    item_price = 30

    if gold >= item_price:
        print("{{hero}} buys the {{item}}!")
        # BUG: Forgot to actually subtract!
        # gold - item_price  # This calculates but doesn't save!

    print(f"Gold remaining: {gold}")


def fix_c():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: The calculation doesn't save the result
    # The bug: "gold - item_price" calculates but doesn't assign
    #          Need: "gold = gold - item_price" to save the result
    #
    # The fix:
    gold = 100
    item_price = 30
    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# {{hero}} has code to check if two passwords match.
# But the code has a syntax issue with comparison!
#
# EXPECTED BEHAVIOR:
# Correct password should print "Access granted!"
#
# ACTUAL BEHAVIOR:
# This code won't even run - syntax error!
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

def buggy_d():
    """This code has exactly ONE bug. Find it!"""
    # NOTE: This code is commented because it would cause a syntax error
    #
    # password = "{{password}}"
    # attempt = "{{password}}"
    #
    # if attempt = password:  # BUG: = instead of ==
    #     print("Access granted to {{location}}!")
    # else:
    #     print("Access denied!")

    # The bug is using = (assignment) instead of == (comparison)
    print("(This function shows a common bug - see comments)")


def fix_d():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: Using = instead of ==
    # The bug: = is assignment (set value), == is comparison (check equality)
    #          In a condition, we need to COMPARE, not assign
    #
    # The fix:
    password = "{{password}}"
    attempt = "{{password}}"
    pass


# ============================================================
# {{CASE_5_TITLE}}
# ============================================================
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# {{hero}}'s level-up code should trigger at level 10.
# But it never prints the level-up message!
#
# EXPECTED BEHAVIOR:
# When level reaches 10, should print "Level up!"
#
# ACTUAL BEHAVIOR:
# The message never appears
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

def buggy_e():
    """This code has exactly ONE bug. Find it!"""
    level = 9

    # {{hero}} gains experience...
    level = level + 1  # Now level is 10

    # BUG: Checking wrong variable/value
    if level == 9:
        print("{{hero}} leveled up! Now level 10!")

    print(f"Current level: {level}")


def fix_e():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: Checking if level == 9 after adding 1
    # The bug: After level + 1, level is 10, not 9
    #          The condition should check == 10
    #
    # The fix:
    level = 9
    level = level + 1
    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Expected: 'Bonus earned' when score is 100")
    print("Buggy version:")
    buggy_a()
    print("\nFixed version:")
    # fix_a()

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Expected: 'Excellent' for score of 95")
    print("Buggy version:")
    buggy_b()
    print("\nFixed version:")
    # fix_b()

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Expected: Gold should be 70 after purchase")
    print("Buggy version:")
    buggy_c()
    print("\nFixed version:")
    # fix_c()

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Expected: Working password comparison")
    print("Buggy version:")
    buggy_d()
    print("\nFixed version:")
    # fix_d()

    print("\n=== {{CASE_5_TITLE}} ===")
    print("Expected: 'Level up' message when reaching level 10")
    print("Buggy version:")
    buggy_e()
    print("\nFixed version:")
    # fix_e()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
