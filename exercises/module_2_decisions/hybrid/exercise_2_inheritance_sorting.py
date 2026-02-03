# =============================================================================
# Hybrid Exercise: The Inheritance - The Sorting System
# =============================================================================
# Difficulty: 3-4
# Arc: The Inheritance
# Parts: DISCOVERY -> OWNERSHIP -> INVESTIGATION
# Concepts: if/elif/else, understanding existing code, extending systems
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: DISCOVERY - Understand the Inherited Code
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} has left {{school}} and given {{hero}} their sorting system.
# Study how it works before you can extend it.


def inherited_sorting_system():
    """DO NOT MODIFY - This is the inherited code to study"""
    # The old sorting system for {{school}}
    # It assigns students to houses based on their primary attribute score

    # Example student data
    student = "{{friend}}"
    courage = 70
    wisdom = 85
    kindness = 60

    # Find the highest attribute
    if courage > wisdom and courage > kindness:
        house = "House of Warriors"
        trait = "courage"
    elif wisdom > courage and wisdom > kindness:
        house = "House of Scholars"
        trait = "wisdom"
    else:
        house = "House of Healers"
        trait = "kindness"

    print(f"{student} sorted into {house}")
    print(f"Dominant trait: {trait}")


def your_understanding():
    # ✏️ YOUR ANALYSIS HERE ✏️
    #
    # Study the inherited_sorting_system and answer these questions:
    #
    # 1. How many houses can students be sorted into? ___
    #
    # 2. What happens if courage = 70, wisdom = 85, kindness = 60?
    #    - courage > wisdom? (70 > 85) _____ (True/False)
    #    - wisdom > courage? (85 > 70) _____ (True/False)
    #    - wisdom > kindness? (85 > 60) _____ (True/False)
    #    - Which house? _____________________
    #
    # 3. What happens if two attributes are tied for highest?
    #    Example: courage = 80, wisdom = 80, kindness = 60
    #    - courage > wisdom? (80 > 80) _____ (True/False)
    #    - First condition fails, check elif...
    #    - wisdom > courage? (80 > 80) _____ (True/False)
    #    - elif fails too, so... _____________________
    #
    # 4. Is this fair? What if kindness is actually lowest but gets assigned?
    #    _____________________________________________________
    pass


# ============================================================
# PART 2: OWNERSHIP - Add Your Own Feature
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# {{hero}} wants to add a new house: "House of Adventurers" for students
# whose highest trait is "bravery". Extend the system!


def your_extended_system():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create an improved sorting system with FOUR houses:
    # - House of Warriors (courage is highest)
    # - House of Scholars (wisdom is highest)
    # - House of Healers (kindness is highest)
    # - House of Adventurers (bravery is highest) <-- NEW!
    #
    # Step 1: Create variables for a test student:
    #         student = "{{hero}}"
    #         courage = 60
    #         wisdom = 70
    #         kindness = 55
    #         bravery = 85  <-- new trait
    #
    # Step 2: Write if/elif/elif/elif/else to find the highest:
    #         (You'll need to check 4 conditions)
    #         - if bravery is highest of all 4: "House of Adventurers"
    #         - elif courage is highest: "House of Warriors"
    #         - elif wisdom is highest: "House of Scholars"
    #         - elif kindness is highest: "House of Healers"
    #         - else: "House of Balance" (for ties or edge cases)
    #
    # Step 3: Print the result
    #
    # Hint: To check if bravery is highest of all 4:
    #       if bravery > courage and bravery > wisdom and bravery > kindness:
    #
    # Expected output for the test values:
    #   {{hero}} sorted into House of Adventurers
    pass


# ============================================================
# PART 3: INVESTIGATION - Find the Hidden Bug
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# {{hero}} discovers the original system has a bug that causes
# unfair sorting in some cases. Find and understand it!


def buggy_edge_case():
    """This shows the bug in the original system"""
    # What if ALL traits are equal?
    student = "{{villain}}"
    courage = 75
    wisdom = 75
    kindness = 75

    # Original logic:
    if courage > wisdom and courage > kindness:
        house = "House of Warriors"
    elif wisdom > courage and wisdom > kindness:
        house = "House of Scholars"
    else:
        house = "House of Healers"

    print(f"{student}: courage={courage}, wisdom={wisdom}, kindness={kindness}")
    print(f"Sorted into: {house}")
    print("Is this fair when all traits are equal?")


def trace_the_bug():
    # ✏️ TRACE THE BUG ✏️
    #
    # When courage = 75, wisdom = 75, kindness = 75:
    #
    # Check 1: courage > wisdom AND courage > kindness
    #          75 > 75 = _____ AND 75 > 75 = _____
    #          Combined: _____ AND _____ = _____ (True/False)
    #          First branch executes? _____
    #
    # Check 2: wisdom > courage AND wisdom > kindness
    #          75 > 75 = _____ AND 75 > 75 = _____
    #          Combined: _____ AND _____ = _____
    #          Second branch executes? _____
    #
    # Since both conditions are False, what runs? _____
    #
    # The bug: When all traits are equal, the student is assigned to
    # _____________________ even though kindness might not be their strength!
    #
    # A better approach would be: _____________________________________
    pass


def your_fixed_system():
    # ✏️ FIX THE BUG ✏️
    #
    # Create a fairer system that handles ties explicitly.
    #
    # Step 1: Create equal trait values:
    #         student = "{{friend}}"
    #         courage = 75
    #         wisdom = 75
    #         kindness = 75
    #
    # Step 2: First check for a tie (all equal):
    #         if courage == wisdom and wisdom == kindness:
    #             print f"{student} has balanced traits!"
    #             print "Special placement: House of Balance"
    #
    # Step 3: Otherwise, use the original logic with elif:
    #         elif courage > wisdom and courage > kindness:
    #             ... (Warriors)
    #         elif wisdom > courage and wisdom > kindness:
    #             ... (Scholars)
    #         else:
    #             ... (Healers)
    #
    # Expected output when all traits are 75:
    #   {{friend}} has balanced traits!
    #   Special placement: House of Balance
    pass


def main():
    print("=" * 50)
    print("PART 1: DISCOVERY - Understand the Inherited Code")
    print("=" * 50)

    print("\n--- inherited_sorting_system ---")
    inherited_sorting_system()

    print("\n--- Your Understanding ---")
    your_understanding()

    print("\n" + "=" * 50)
    print("PART 2: OWNERSHIP - Add Your Own Feature")
    print("=" * 50)

    print("\n--- your_extended_system ---")
    your_extended_system()

    print("\n" + "=" * 50)
    print("PART 3: INVESTIGATION - Find the Hidden Bug")
    print("=" * 50)

    print("\n--- buggy_edge_case ---")
    buggy_edge_case()

    print("\n--- trace_the_bug ---")
    trace_the_bug()

    print("\n--- your_fixed_system ---")
    # your_fixed_system()  # Uncomment after fixing

    print("\n" + "=" * 50)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
