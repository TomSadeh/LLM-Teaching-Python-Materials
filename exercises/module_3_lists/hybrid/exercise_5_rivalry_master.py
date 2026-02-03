# =============================================================================
# Hybrid Exercise: The Rivalry - List Master Challenge
# =============================================================================
# Difficulty: 5
# Arc: Rivalry (SETBACK -> GROWTH -> CONFRONTATION -> TRIUMPH)
# Concepts: Integration of all list concepts - capstone exercise
# =============================================================================

"""
{{CONTEXT_SETBACK_INTRO}}

This is the final challenge for Module 3. Complete each part in order.
"""


# ============================================================
# PART 1: SETBACK - Analyze Failed Code
# ============================================================
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# {{villain}} has sabotaged {{hero}}'s list management system.
# Multiple bugs are causing the system to fail. Find and understand them.


def broken_inventory_manager():
    """This code has 3 bugs. Study it carefully!"""
    print("=== Broken Inventory Manager ===")

    # Bug 1: Aliasing issue
    master_inventory = ["{{item}}", "potion", "key"]
    player_inventory = master_inventory  # Should be a copy!

    player_inventory.append("map")
    print(f"Master (should be unchanged): {master_inventory}")
    print(f"Player: {player_inventory}")

    # Bug 2: Off-by-one indexing
    items = ["A", "B", "C", "D"]
    last_item = items[len(items)]  # IndexError! Should be len(items) - 1

    # Bug 3: Wrong method (remove takes value, not index)
    scores = [100, 85, 90, 75]
    scores.remove(1)  # Wants to remove at index 1, but this looks for value 1


def analyze_bugs():
    # YOUR ANALYSIS
    #
    # For each bug, explain:
    # 1. What the bug is
    # 2. What behavior it causes
    # 3. How to fix it

    bug_analysis = {
        "bug_1": {
            "description": "...",
            "symptom": "...",
            "fix": "...",
        },
        "bug_2": {
            "description": "...",
            "symptom": "...",
            "fix": "...",
        },
        "bug_3": {
            "description": "...",
            "symptom": "...",
            "fix": "...",
        },
    }

    return bug_analysis


# ============================================================
# PART 2: GROWTH - Build Core Skills
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Practice the fundamental operations before the final challenge.


def growth_exercise_1():
    # YOUR CODE HERE
    #
    # Create a proper inventory system:
    # 1. Create master_items = ["{{item}}", "potion", "key"]
    # 2. Create player_items as a COPY of master_items (use [:])
    # 3. Add "map" to player_items
    # 4. Remove "potion" from player_items
    # 5. Print both lists to verify they're independent
    #
    # Expected:
    #   Master: ['{{item}}', 'potion', 'key']
    #   Player: ['{{item}}', 'key', 'map']

    pass


def growth_exercise_2():
    # YOUR CODE HERE
    #
    # Process a list with iteration:
    # 1. Create scores = [85, 42, 91, 67, 38, 95, 73]
    # 2. Create passing = [] (empty list)
    # 3. Loop through scores:
    #    - If score >= 60, append to passing
    # 4. Print f"All scores: {scores}"
    # 5. Print f"Passing: {passing}"
    # 6. Print f"Pass rate: {len(passing)}/{len(scores)}"
    #
    # Expected:
    #   All scores: [85, 42, 91, 67, 38, 95, 73]
    #   Passing: [85, 91, 67, 95, 73]
    #   Pass rate: 5/7

    pass


def growth_exercise_3():
    # YOUR CODE HERE
    #
    # Use slicing for data extraction:
    # 1. Create data = [10, 20, 30, 40, 50, 60, 70, 80]
    # 2. Extract first_half using [:4]
    # 3. Extract second_half using [4:]
    # 4. Extract every_other using [::2]
    # 5. Extract reversed using [::-1]
    # 6. Print all results
    #
    # Expected:
    #   First half: [10, 20, 30, 40]
    #   Second half: [50, 60, 70, 80]
    #   Every other: [10, 30, 50, 70]
    #   Reversed: [80, 70, 60, 50, 40, 30, 20, 10]

    pass


# ============================================================
# PART 3: CONFRONTATION - The Ultimate List Challenge
# ============================================================
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# Build a complete party management system using all list skills.


def party_management_system():
    # YOUR CODE HERE
    #
    # Build a complete party management system for {{hero}}'s adventure.
    #
    # SETUP:
    # 1. Create party = ["{{hero}}"] (starting with hero)
    # 2. Create inventory = [] (empty starting inventory)
    # 3. Print "=== Party Management System ==="
    #
    # RECRUITMENT (use append):
    # 4. Add "{{heroine}}" to party
    # 5. Add "{{friend}}" to party
    # 6. Print f"Party formed: {party}"
    # 7. Print f"Party size: {len(party)}"
    #
    # INVENTORY MANAGEMENT (use append, remove):
    # 8. Add items: "{{item}}", "potion", "potion", "key", "map"
    # 9. Print f"Inventory: {inventory}"
    # 10. Count potions: potion_count = 0, loop and count
    # 11. Print f"Potions available: {potion_count}"
    # 12. Use one potion (remove "potion")
    # 13. Print f"After using potion: {inventory}"
    #
    # PARTY OPERATIONS (use indexing, slicing):
    # 14. Print f"Leader: {party[0]}"
    # 15. Print f"Last joined: {party[-1]}"
    # 16. Create scout_team as first 2 members: party[:2]
    # 17. Print f"Scout team: {scout_team}"
    #
    # BACKUP SYSTEM (proper copying):
    # 18. Create backup_party as a COPY of party
    # 19. Create backup_inventory as a COPY of inventory
    # 20. Add "{{mentor}}" to party (original only)
    # 21. Print f"Current party: {party}"
    # 22. Print f"Backup (unchanged): {backup_party}"
    #
    # FINAL STATUS:
    # 23. Print "=== Final Status ==="
    # 24. Print f"Party: {party} ({len(party)} members)"
    # 25. Print f"Inventory: {inventory} ({len(inventory)} items)"
    #
    # This exercise combines: creation, append, remove, indexing,
    # negative indexing, slicing, copying, and iteration!

    pass


# ============================================================
# VERIFICATION - Test Your System
# ============================================================


def verify_all():
    """Run all parts and check results"""
    print("=" * 60)
    print("THE RIVALRY: List Master Challenge")
    print("=" * 60)

    print("\n--- PART 1: SETBACK ---")
    print("Bug analysis:", analyze_bugs())
    # broken_inventory_manager()  # Uncomment to see bugs (will error)

    print("\n--- PART 2: GROWTH ---")
    print("\nGrowth Exercise 1 (Copying):")
    growth_exercise_1()
    print("\nGrowth Exercise 2 (Filtering):")
    growth_exercise_2()
    print("\nGrowth Exercise 3 (Slicing):")
    growth_exercise_3()

    print("\n--- PART 3: CONFRONTATION ---")
    party_management_system()


def main():
    print("=" * 60)
    print("THE RIVALRY: List Master Challenge")
    print("=" * 60)
    print()
    print("{{CONTEXT_SETBACK_INTRO}}")
    print()
    print("This capstone exercise tests ALL your list skills:")
    print("- List creation and modification")
    print("- Indexing (positive and negative)")
    print("- Slicing (basic and step)")
    print("- List methods (append, remove, pop, insert)")
    print("- Iteration and filtering")
    print("- Copying vs aliasing")
    print()
    print("Complete each part in order.")
    print("=" * 60)

    # Uncomment each section as you complete it:

    # print("\n--- PART 1: SETBACK ---")
    # print("{{CONTEXT_SETBACK_NARRATIVE}}")
    # print("\nBroken code analysis:")
    # print(analyze_bugs())

    # print("\n--- PART 2: GROWTH ---")
    # print("{{CONTEXT_GROWTH_INTRO}}")
    # print("\nExercise 1 (Copying):")
    # growth_exercise_1()
    # print("\nExercise 2 (Filtering):")
    # growth_exercise_2()
    # print("\nExercise 3 (Slicing):")
    # growth_exercise_3()

    # print("\n--- PART 3: CONFRONTATION ---")
    # print("{{CONTEXT_CONFRONTATION_INTRO}}")
    # party_management_system()

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


main()
