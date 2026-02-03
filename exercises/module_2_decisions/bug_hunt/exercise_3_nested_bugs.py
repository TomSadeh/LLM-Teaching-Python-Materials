# =============================================================================
# Bug Hunt: Nested Conditional Bugs
# =============================================================================
# Difficulty: 5
# Concepts: Nested if statements, complex conditional logic
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
# {{hero}} needs to check multiple conditions to enter a restricted area.
# Must be level 10+ AND have a pass OR be a VIP.
#
# EXPECTED BEHAVIOR:
# VIP should enter regardless of level
#
# ACTUAL BEHAVIOR:
# VIP at level 5 is denied entry
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

def buggy_a():
    """This code has exactly ONE bug. Find it!"""
    level = 5
    has_pass = False
    is_vip = True

    # BUG: VIP check is nested inside level check
    if level >= 10:
        if has_pass:
            print("{{hero}} enters with pass!")
        elif is_vip:
            print("{{hero}} enters as VIP!")
        else:
            print("Access denied - no pass.")
    else:
        print("Access denied - level too low.")


def fix_a():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: VIP check should be independent of level
    # The bug: The is_vip check is inside the level >= 10 block
    #          So VIPs with low level never get checked
    #
    # The fix: Check VIP first, OR restructure the logic
    level = 5
    has_pass = False
    is_vip = True

    # Better structure:
    # if is_vip:
    #     enter as VIP
    # elif level >= 10 and has_pass:
    #     enter with pass
    # else:
    #     denied
    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# {{mentor}}'s grade calculator has nested conditions.
# But something's wrong with the indentation logic!
#
# EXPECTED BEHAVIOR:
# Score of 75 should print "C" and "Needs improvement"
#
# ACTUAL BEHAVIOR:
# Score of 75 prints "C" but also "Excellent work!" (wrong!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

def buggy_b():
    """This code has exactly ONE bug. Find it!"""
    score = 75

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"

    print(f"Grade: {grade}")

    # BUG: Wrong indentation - this should be inside an if
    if grade == "A":
        print("{{exclamation}} Excellent work!")
    print("Needs improvement.")  # This always runs!


def fix_b():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: "Needs improvement" runs for everyone
    # The bug: The second message isn't in an else block
    #          It should only print if grade is NOT "A"
    #
    # The fix:
    score = 75
    # ... grade assignment ...
    # if grade == "A":
    #     print("Excellent!")
    # else:
    #     print("Needs improvement.")
    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# {{hero}} checks if they can complete a challenge.
# Multiple requirements must be checked in the right order.
#
# EXPECTED BEHAVIOR:
# Should check level first, then gold, then item
# Missing gold (level ok, no item) should say "Need more gold"
#
# ACTUAL BEHAVIOR:
# Says "Need the {{item}}" even when gold is the problem
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

def buggy_c():
    """This code has exactly ONE bug. Find it!"""
    level = 10
    gold = 30  # Not enough gold!
    has_challenge_item = True

    if level >= 5:
        # BUG: Wrong nesting - checking item before gold
        if has_challenge_item:
            if gold >= 50:
                print("{{hero}} completes the challenge!")
            else:
                print("Need more gold!")
        else:
            print("Need the {{item}}!")
    else:
        print("Level too low for this challenge.")


def fix_c():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: The nesting order gives wrong error messages
    # The bug: With gold=30 and has_challenge_item=True:
    #          - Enters level check (ok)
    #          - Enters has_challenge_item check (True)
    #          - Fails gold check -> "Need more gold!" (correct in this case!)
    #
    # Wait, let me re-read... actually the code works for this input.
    # Let me try: level=10, gold=100, has_challenge_item=False
    #          - Enters level check (ok)
    #          - Fails has_challenge_item check (False)
    #          - Prints "Need the item!" before checking gold
    #
    # The logic issue: We should check what's actually missing
    # A better approach: check each requirement and report what's missing
    level = 10
    gold = 30
    has_challenge_item = True
    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# {{hero}}'s action system chooses what to do based on {{primary_stat}} and {{secondary_stat}}.
# But the nested conditions have a logical flaw!
#
# EXPECTED BEHAVIOR:
# Low {{primary_stat}} AND low {{secondary_stat}} should "{{retreat_action}}"
# Low {{primary_stat}} OR low {{secondary_stat}} (but not both) should "{{basic_action}}"
#
# ACTUAL BEHAVIOR:
# Low {{primary_stat}} always leads to "{{retreat_action}}" regardless of {{secondary_stat}}
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

def buggy_d():
    """This code has exactly ONE bug. Find it!"""
    primary = 20
    secondary = 80  # Plenty of {{secondary_stat}}!

    if primary < 30:
        # BUG: Always retreats when {{primary_stat}} is low, ignoring {{secondary_stat}}
        print("{{hero}} must {{retreat_action}}!")
    elif secondary < 20:
        print("{{hero}} must {{basic_action}}!")
    else:
        print("{{hero}} uses {{spell2}}!")


def fix_d():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: {{retreat_action}} should require BOTH low {{primary_stat}} AND low {{secondary_stat}}
    # The bug: Current code retreats on low {{primary_stat}} alone
    #          Should only {{retreat_action}} if primary < 30 AND secondary < 20
    #
    # The fix:
    primary = 20
    secondary = 80

    # Better logic:
    # if primary < 30 and secondary < 20:
    #     {{retreat_action}}
    # elif primary < 30:
    #     recover {{primary_stat}}
    # elif secondary < 20:
    #     {{basic_action}}
    # else:
    #     use special ability
    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Expected: VIP enters regardless of level")
    print("Buggy version:")
    buggy_a()
    print("\nFixed version:")
    # fix_a()

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Expected: C grade says 'Needs improvement' only")
    print("Buggy version:")
    buggy_b()
    print("\nFixed version:")
    # fix_b()

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Expected: Correct error message for missing requirement")
    print("Buggy version:")
    buggy_c()
    print("\nFixed version:")
    # fix_c()

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Expected: Only {{retreat_action}} if BOTH stats are low")
    print("Buggy version:")
    buggy_d()
    print("\nFixed version:")
    # fix_d()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
