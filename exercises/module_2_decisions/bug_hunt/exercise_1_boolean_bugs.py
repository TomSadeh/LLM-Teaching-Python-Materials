# =============================================================================
# Bug Hunt: Boolean Expression Bugs
# =============================================================================
# Difficulty: 4
# Concepts: and/or confusion, not placement, operator precedence
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
# {{hero}} wrote code to check if they can buy an item.
# They need at least 100 gold AND at least 50 gems.
#
# EXPECTED BEHAVIOR:
# With gold=150 and gems=30, should print "Cannot afford item"
# (because gems is too low)
#
# ACTUAL BEHAVIOR:
# It prints "Buying item!" even though gems is only 30
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

def buggy_a():
    """This code has exactly ONE bug. Find it!"""
    gold = 150
    gems = 30

    # Need BOTH resources to be sufficient
    if gold >= 100 or gems >= 50:  # BUG: Wrong operator
        print(f"{{hero}} buys the {{item}}!")
    else:
        print("Cannot afford the {{item}}.")


def fix_a():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: Using 'or' when 'and' is needed
    # The bug: 'or' means only ONE condition needs to be True
    #          'and' means BOTH conditions must be True
    #
    # The fix:
    gold = 150
    gems = 30
    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# {{hero}} wants to enter {{danger_location}} if there is NO {{obstacle}}.
#
# EXPECTED BEHAVIOR:
# With danger_detected=True, should print "Too dangerous!"
#
# ACTUAL BEHAVIOR:
# It prints "Entering!" even when danger is detected
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

def buggy_b():
    """This code has exactly ONE bug. Find it!"""
    danger_detected = True

    if danger_detected == False:  # Awkward but works
        print("{{hero}} enters {{danger_location}}!")
    else:
        print("Too dangerous! {{hero}} stays back.")

    # Wait, the bug is actually in this version:
    if not danger_detected == True:  # BUG: Operator precedence!
        print("Entering safely...")


def fix_b():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: 'not danger_detected == True' is confusing
    # The bug: 'not' applies to 'danger_detected' first, then compares to True
    #          'not True' is False, then 'False == True' is False
    #          So the condition is always False!
    #
    # Better ways to write "if danger_detected is False":
    # Option 1: if not danger_detected:
    # Option 2: if danger_detected == False:
    # Option 3: if not (danger_detected == True):  # with parentheses
    #
    # The fix:
    danger_detected = True
    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# {{mentor}} grades students: need score >= 60 OR extra_credit to pass.
#
# EXPECTED BEHAVIOR:
# With score=55 and extra_credit=True, should print "Passed!"
# (because extra_credit is True)
#
# ACTUAL BEHAVIOR:
# It prints "Failed." even with extra credit
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

def buggy_c():
    """This code has exactly ONE bug. Find it!"""
    score = 55
    extra_credit = True

    if score >= 60 and extra_credit:  # BUG: Wrong operator
        print("{{hero}} passed!")
    else:
        print("{{hero}} failed.")


def fix_c():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: Using 'and' when 'or' is needed
    # The bug: 'and' requires BOTH conditions to be True
    #          The requirement says EITHER high score OR extra credit
    #
    # The fix:
    score = 55
    extra_credit = True
    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# {{hero}} can rest if NOT {{busy_activity}} AND NOT {{harmful_status}}.
#
# EXPECTED BEHAVIOR:
# With is_busy=False and is_harmed=True, should print "Cannot rest"
# (because harmed, even though not busy)
#
# ACTUAL BEHAVIOR:
# It prints "Resting..." even when harmed
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

def buggy_d():
    """This code has exactly ONE bug. Find it!"""
    is_busy = False
    is_harmed = True

    if not is_busy or is_harmed:  # BUG: Logic error
        print("{{hero}} rests and recovers.")
    else:
        print("Cannot rest right now!")


def fix_d():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: The condition is backwards
    # The bug: 'not is_busy or is_harmed' means:
    #          "can rest if NOT busy OR if harmed"
    #          But we want: "can rest if NOT busy AND NOT harmed"
    #
    # The fix (need both conditions for resting):
    is_busy = False
    is_harmed = True
    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Expected: 'Cannot afford' (gems too low)")
    print("Buggy version:")
    buggy_a()
    print("\nFixed version:")
    # fix_a()

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Expected: 'Too dangerous' when danger detected")
    print("Buggy version:")
    buggy_b()
    print("\nFixed version:")
    # fix_b()

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Expected: 'Passed' with extra credit")
    print("Buggy version:")
    buggy_c()
    print("\nFixed version:")
    # fix_c()

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Expected: 'Cannot rest' when harmed")
    print("Buggy version:")
    buggy_d()
    print("\nFixed version:")
    # fix_d()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
