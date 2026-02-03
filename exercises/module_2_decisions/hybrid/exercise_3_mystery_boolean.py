# =============================================================================
# Hybrid Exercise: The Mystery - Boolean Confusion
# =============================================================================
# Difficulty: 4
# Arc: The Mystery
# Parts: DISCOVERY -> INVESTIGATION -> IMPROVEMENT
# Concepts: and/or/not debugging, tracing boolean expressions
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: DISCOVERY - Observe Confusing Behavior
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{hero}} found some access control code at {{school}}.
# The code seems to allow the wrong people in!


def mystery_code_1():
    """Run this and observe what happens"""
    # Only VIP members with valid tickets should enter
    # Expected: Non-VIP with ticket should NOT enter
    is_vip = False
    has_ticket = True

    if is_vip or has_ticket:
        print("Welcome to the {{location}}!")
    else:
        print("Access denied.")


def mystery_code_2():
    """Run this and observe what happens"""
    # {{hero}} should NOT go outside if it's raining AND cold
    # Expected: Raining alone should be fine
    is_raining = True
    is_cold = False

    if not is_raining and is_cold:  # Something's wrong here
        print("{{hero}} goes outside.")
    else:
        print("{{hero}} stays inside.")


def mystery_code_3():
    """Run this and observe what happens"""
    # {{hero}} needs EITHER a primary {{item}} OR (a backup {{item}} AND supplies) to fight
    # Expected: Having only backup only (no supplies) should NOT work
    has_primary = False
    has_backup = True
    has_supplies = False

    if has_primary or has_backup or has_supplies:  # Logic is wrong
        print("{{hero}} is ready to fight!")
    else:
        print("{{hero}} cannot fight without weapons.")


def your_observations():
    # ✏️ YOUR OBSERVATIONS HERE ✏️
    #
    # mystery_code_1:
    #   Expected: Non-VIP shouldn't enter even with ticket
    #   Actual: ________________________________
    #   Is the 'or' correct for "VIP members with valid tickets"? _____
    #
    # mystery_code_2:
    #   Expected: Only raining (not cold) should allow going outside
    #   Actual: ________________________________
    #   What does "not is_raining and is_cold" actually check? ____________
    #
    # mystery_code_3:
    #   Expected: Backup without supplies shouldn't work
    #   Actual: ________________________________
    #   Does "has_primary or has_backup or has_supplies" match the requirement? _____
    pass


# ============================================================
# PART 2: INVESTIGATION - Trace the Boolean Logic
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Trace through each mystery to understand the boolean expressions.


def trace_mystery_1():
    # ✏️ TRACE THE CODE ✏️
    #
    # Condition: is_vip or has_ticket
    # Values: False or True
    #
    # False or True = _____ (True/False)
    #
    # The issue: "VIP members with valid tickets" means BOTH are needed.
    # 'or' means EITHER one works.
    #
    # The correct operator should be: _____
    pass


def trace_mystery_2():
    # ✏️ TRACE THE CODE ✏️
    #
    # Condition: not is_raining and is_cold
    # Values: not True and False
    #
    # Step 1: not True = _____
    # Step 2: _____ and False = _____
    #
    # This checks: "NOT raining AND cold"
    # But we wanted: "NOT (raining AND cold)"
    #
    # The difference:
    # - "not is_raining and is_cold" = outside if not raining BUT it's cold
    # - "not (is_raining and is_cold)" = outside unless BOTH raining AND cold
    #
    # Current logic goes outside when: _______________________
    # Correct logic should go outside when: _______________________
    pass


def trace_mystery_3():
    # ✏️ TRACE THE CODE ✏️
    #
    # Condition: has_primary or has_backup or has_supplies
    # Values: False or True or False
    #
    # False or True = _____
    # _____ or False = _____
    #
    # This checks: "has ANY of these three items"
    # But we wanted: "has sword OR (has bow AND has arrows)"
    #
    # Correct expression with parentheses:
    # has_primary or (has_backup and has_supplies)
    #
    # Let's verify: False or (True and False)
    # Step 1: True and False = _____
    # Step 2: False or _____ = _____
    #
    # Now it correctly denies entry!
    pass


# ============================================================
# PART 3: IMPROVEMENT - Fix the Boolean Expressions
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Fix each buggy boolean expression!


def fixed_code_1():
    # ✏️ FIX THE BUG ✏️
    #
    # Requirement: VIP members with valid tickets (need BOTH)
    # Original (wrong): is_vip or has_ticket
    #
    # Your fix:
    is_vip = False
    has_ticket = True

    # Fix: Change 'or' to 'and'
    pass


def fixed_code_2():
    # ✏️ FIX THE BUG ✏️
    #
    # Requirement: Don't go outside if it's raining AND cold
    #              (either alone is fine)
    # Original (wrong): not is_raining and is_cold
    #
    # Your fix:
    is_raining = True
    is_cold = False

    # Fix: Add parentheses: not (is_raining and is_cold)
    pass


def fixed_code_3():
    # ✏️ FIX THE BUG ✏️
    #
    # Requirement: Need primary OR (backup AND supplies)
    # Original (wrong): has_primary or has_backup or has_supplies
    #
    # Your fix:
    has_primary = False
    has_backup = True
    has_supplies = False

    # Fix: Use parentheses to group: has_primary or (has_backup and has_supplies)
    pass


def test_fixed_code():
    """Test your fixed code with different values"""
    print("\n--- Testing Fixed Code 1 ---")
    # Test: VIP without ticket
    is_vip = True
    has_ticket = False
    # Should deny entry (missing ticket)

    # Test: Non-VIP with ticket
    is_vip = False
    has_ticket = True
    # Should deny entry (not VIP)

    # Test: VIP with ticket
    is_vip = True
    has_ticket = True
    # Should allow entry

    print("\n--- Testing Fixed Code 2 ---")
    # Test: Raining only
    is_raining = True
    is_cold = False
    # Should allow outside (only one condition, not both)

    # Test: Raining AND cold
    is_raining = True
    is_cold = True
    # Should stay inside (both conditions)

    print("\n--- Testing Fixed Code 3 ---")
    # Test: Only bow
    has_primary = False
    has_backup = True
    has_supplies = False
    # Should deny (bow needs arrows)

    # Test: Bow with arrows
    has_primary = False
    has_backup = True
    has_supplies = True
    # Should allow

    print("If all tests pass, your fixes are correct!")


def main():
    print("=" * 50)
    print("PART 1: DISCOVERY - Observe Confusing Behavior")
    print("=" * 50)

    print("\n--- mystery_code_1 ---")
    print("Expected: 'Access denied' for non-VIP")
    print("Actual:")
    mystery_code_1()

    print("\n--- mystery_code_2 ---")
    print("Expected: 'goes outside' when only raining")
    print("Actual:")
    mystery_code_2()

    print("\n--- mystery_code_3 ---")
    print("Expected: 'cannot fight' with only bow (no arrows)")
    print("Actual:")
    mystery_code_3()

    print("\n--- Your Observations ---")
    your_observations()

    print("\n" + "=" * 50)
    print("PART 2: INVESTIGATION - Trace the Boolean Logic")
    print("=" * 50)

    print("\n--- trace_mystery_1 ---")
    trace_mystery_1()

    print("\n--- trace_mystery_2 ---")
    trace_mystery_2()

    print("\n--- trace_mystery_3 ---")
    trace_mystery_3()

    print("\n" + "=" * 50)
    print("PART 3: IMPROVEMENT - Fix the Boolean Expressions")
    print("=" * 50)

    print("\n--- fixed_code_1 ---")
    # fixed_code_1()  # Uncomment after fixing

    print("\n--- fixed_code_2 ---")
    # fixed_code_2()

    print("\n--- fixed_code_3 ---")
    # fixed_code_3()

    # test_fixed_code()  # Uncomment to test your fixes

    print("\n" + "=" * 50)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
