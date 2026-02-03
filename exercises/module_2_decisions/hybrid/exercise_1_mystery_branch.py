# =============================================================================
# Hybrid Exercise: The Mystery - Unexpected Branch
# =============================================================================
# Difficulty: 2-3
# Arc: The Mystery
# Parts: DISCOVERY -> INVESTIGATION -> IMPROVEMENT
# Concepts: if/else debugging, tracing, conditional logic
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: DISCOVERY - Observe the Unexpected
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{hero}} wrote some code at {{school}}, but it's behaving strangely!
# Run each piece of code and notice what's wrong.


def mystery_code_1():
    """Run this and observe what happens"""
    # {{hero}} wants to check if they have enough energy to train.
    # Expected: Should say "Ready to train!" when energy is 75
    # But something is wrong...
    energy = 75
    if energy > 75:
        print("{{hero}} is ready to train!")
    else:
        print("{{hero}} needs to rest.")


def mystery_code_2():
    """Run this and observe what happens"""
    # {{mentor}} is checking if {{hero}} passed the exam.
    # Expected: Score of 60 should say "Passed!"
    # But something is wrong...
    score = 60
    required = 60
    if score > required:
        print("{{hero}} passed!")
    else:
        print("{{hero}} failed.")


def mystery_code_3():
    """Run this and observe what happens"""
    # {{hero}} is trying to enter {{location}} with a password.
    # Expected: Correct password should grant access.
    # But something is wrong...
    secret = "{{password}}"
    entered = "{{password}} "  # Notice the extra space!
    if secret == entered:
        print("Access granted to {{location}}!")
    else:
        print("Access denied!")


def your_observations():
    # ✏️ YOUR OBSERVATIONS HERE ✏️
    #
    # mystery_code_1:
    #   Expected output: "{{hero}} is ready to train!"
    #   Actual output: ________________________________
    #   What's suspicious? ________________________________
    #
    # mystery_code_2:
    #   Expected output: "{{hero}} passed!"
    #   Actual output: ________________________________
    #   What's suspicious? ________________________________
    #
    # mystery_code_3:
    #   Expected output: "Access granted to {{location}}!"
    #   Actual output: ________________________________
    #   What's suspicious? ________________________________
    pass


# ============================================================
# PART 2: INVESTIGATION - Trace the Code
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Now trace through each mystery to find the exact cause.


def trace_mystery_1():
    # ✏️ TRACE THE CODE ✏️
    #
    # mystery_code_1 uses: if energy > 75
    #
    # energy = 75
    # Condition: 75 > 75 = _______ (True/False?)
    #
    # The problem: > means "greater than" but 75 is NOT greater than 75.
    #
    # What operator should be used instead? _______ (hint: >=)
    #
    # The bug: Using > when we need ___
    pass


def trace_mystery_2():
    # ✏️ TRACE THE CODE ✏️
    #
    # mystery_code_2 uses: if score > required
    #
    # score = 60
    # required = 60
    # Condition: 60 > 60 = _______ (True/False?)
    #
    # The problem: A score equal to required should count as passing.
    #
    # What operator should be used instead? _______ (hint: >=)
    #
    # The bug: Using > when we need ___
    pass


def trace_mystery_3():
    # ✏️ TRACE THE CODE ✏️
    #
    # mystery_code_3 compares these strings:
    # secret = "{{password}}"
    # entered = "{{password}} "
    #
    # Are they equal? _______ (True/False?)
    #
    # Count the characters in each:
    # secret has ___ characters
    # entered has ___ characters (count carefully!)
    #
    # The bug: ________________________________
    #
    # Lesson: Strings must match EXACTLY, including spaces!
    pass


# ============================================================
# PART 3: IMPROVEMENT - Fix the Issues
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Now fix each bug you found!


def fixed_code_1():
    # ✏️ FIX THE BUG ✏️
    #
    # Fix the energy check so 75 energy is considered "ready to train".
    #
    # What I found: Using > instead of >= makes 75 not pass the check
    #
    # Your fix:
    energy = 75
    pass


def fixed_code_2():
    # ✏️ FIX THE BUG ✏️
    #
    # Fix the exam check so a score equal to required counts as passing.
    #
    # What I found: Using > instead of >= means equal scores fail
    #
    # Your fix:
    score = 60
    required = 60
    pass


def fixed_code_3():
    # ✏️ FIX THE BUG ✏️
    #
    # Fix the password so it matches exactly (remove the extra space).
    #
    # What I found: The entered password had an extra space at the end
    #
    # Your fix:
    secret = "{{password}}"
    pass


def main():
    print("=" * 50)
    print("PART 1: DISCOVERY - Observe the Unexpected")
    print("=" * 50)

    print("\n--- mystery_code_1 ---")
    print("Expected: '{{hero}} is ready to train!'")
    print("Actual:")
    mystery_code_1()

    print("\n--- mystery_code_2 ---")
    print("Expected: '{{hero}} passed!'")
    print("Actual:")
    mystery_code_2()

    print("\n--- mystery_code_3 ---")
    print("Expected: 'Access granted to {{location}}!'")
    print("Actual:")
    mystery_code_3()

    print("\n--- Your Observations ---")
    your_observations()

    print("\n" + "=" * 50)
    print("PART 2: INVESTIGATION - Trace the Code")
    print("=" * 50)

    print("\n--- trace_mystery_1 ---")
    trace_mystery_1()

    print("\n--- trace_mystery_2 ---")
    trace_mystery_2()

    print("\n--- trace_mystery_3 ---")
    trace_mystery_3()

    print("\n" + "=" * 50)
    print("PART 3: IMPROVEMENT - Fix the Issues")
    print("=" * 50)

    print("\n--- fixed_code_1 ---")
    # fixed_code_1()  # Uncomment after fixing

    print("\n--- fixed_code_2 ---")
    # fixed_code_2()

    print("\n--- fixed_code_3 ---")
    # fixed_code_3()

    print("\n" + "=" * 50)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
