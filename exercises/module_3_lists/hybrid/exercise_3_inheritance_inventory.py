# =============================================================================
# Hybrid Exercise: The Inheritance - The Inventory System
# =============================================================================
# Difficulty: 3-4
# Arc: Inheritance (DISCOVERY -> OWNERSHIP -> INVESTIGATION)
# Concepts: Slicing, list operations, working with existing code
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: DISCOVERY - Understand the Inherited System
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} left behind an inventory management system.
# Study how it works before making any changes.


def legacy_inventory_system():
    """The original inventory system - study how it works!"""
    # The inventory stores items as a list
    inventory = ["{{item}}", "potion", "key", "map", "coin", "gem"]

    # Display functions
    print(f"Full inventory: {inventory}")
    print(f"Total items: {len(inventory)}")

    # The system uses slicing to show categories
    essentials = inventory[:3]  # First 3 items are essentials
    print(f"Essentials: {essentials}")

    valuables = inventory[3:]   # Rest are valuables
    print(f"Valuables: {valuables}")

    # Quick access to first and last
    print(f"Primary item: {inventory[0]}")
    print(f"Latest addition: {inventory[-1]}")


# YOUR TASK: Trace through the code and predict the output
#
# Line 1: Full inventory: _______________
# Line 2: Total items: _______________
# Line 3: Essentials: _______________
# Line 4: Valuables: _______________
# Line 5: Primary item: _______________
# Line 6: Latest addition: _______________


def part_1_understanding():
    # ANSWER THESE QUESTIONS
    #
    # After studying the code:

    answers = {
        "what_does_inventory[:3]_return": "?",
        "what_does_inventory[3:]_return": "?",
        "how_many_essentials": "?",
        "how_many_valuables": "?",
    }

    return answers


# ============================================================
# PART 2: OWNERSHIP - Add Your Own Features
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# The old system is limited. Add new features to make it yours!


def enhanced_inventory_system():
    # YOUR CODE HERE
    #
    # Start with the same inventory
    inventory = ["{{item}}", "potion", "key", "map", "coin", "gem"]

    # FEATURE 1: Show middle items (skip first and last)
    # Step 1: Use slicing to get items from index 1 to -1
    # Step 2: Print f"Middle items: {middle}"
    #
    # Expected: Middle items: ['potion', 'key', 'map', 'coin']

    # FEATURE 2: Show every other item
    # Step 3: Use step slicing to get every other item
    # Step 4: Print f"Every other: {alternating}"
    #
    # Expected: Every other: ['{{item}}', 'key', 'coin']

    # FEATURE 3: Show reversed inventory
    # Step 5: Use [::-1] to reverse the list
    # Step 6: Print f"Reversed: {reversed_inv}"
    #
    # Expected: Reversed: ['gem', 'coin', 'map', 'key', 'potion', '{{item}}']

    # FEATURE 4: Split inventory into two equal parts
    # Step 7: Calculate midpoint: mid = len(inventory) // 2
    # Step 8: Get first_half using [:mid]
    # Step 9: Get second_half using [mid:]
    # Step 10: Print both halves
    #
    # Expected:
    #   First half: ['{{item}}', 'potion', 'key']
    #   Second half: ['map', 'coin', 'gem']

    pass


# ============================================================
# PART 3: INVESTIGATION - Find and Fix Hidden Issues
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Some edge cases weren't handled properly in the old system.
# Find and fix these bugs!


def buggy_feature_1():
    """Bug: Accessing inventory when it might be empty"""
    inventory = []  # Empty inventory!
    print(f"Primary item: {inventory[0]}")  # BUG: IndexError!


def fixed_feature_1():
    # FIX THE BUG
    #
    # Check if inventory has items before accessing index 0.
    # Use: if len(inventory) > 0:
    #
    # If empty, print "Inventory is empty"
    # Otherwise, print the primary item

    inventory = []  # Test with empty inventory

    pass


def buggy_feature_2():
    """Bug: Slicing with wrong assumptions"""
    inventory = ["{{item}}", "potion"]  # Only 2 items
    essentials = inventory[:3]  # Tries to get 3 items
    valuables = inventory[3:]   # Nothing at index 3+

    print(f"Essentials: {essentials}")  # Works, gets what's available
    print(f"Valuables: {valuables}")    # Empty list!
    print(f"Valuable count: {len(valuables)}")


def fixed_feature_2():
    # ANALYZE THE BEHAVIOR
    #
    # This isn't technically a crash, but it may not do what's expected.
    # Slicing beyond list bounds just returns what's available.
    #
    # Run buggy_feature_2() and answer:
    # - What does essentials contain? _______________
    # - What does valuables contain? _______________
    # - Is this a bug or expected behavior? _______________
    #
    # Write improved code that adapts to any inventory size:
    # - If inventory has 5+ items, split at index 3
    # - Otherwise, treat all items as essentials

    inventory = ["{{item}}", "potion"]  # Short inventory

    pass


def buggy_feature_3():
    """Bug: The aliasing problem strikes again!"""
    original = ["{{item}}", "potion", "key"]
    backup = original  # BUG: This is an alias!

    # Remove an item from original
    original.remove("potion")

    print(f"Original: {original}")
    print(f"Backup: {backup}")  # Backup changed too!


def fixed_feature_3():
    # FIX THE BUG
    #
    # Create a true copy of original, not an alias.
    # Use slicing: backup = original[:]
    #
    # After the fix:
    # - Modifying original should NOT affect backup

    original = ["{{item}}", "potion", "key"]

    # YOUR CODE HERE - create a proper backup

    original.remove("potion")

    # These should now be different!
    print(f"Original: {original}")
    print(f"Backup: {backup}")  # Should still have all 3 items

    pass


def main():
    print("=" * 60)
    print("THE INHERITANCE: The Inventory System")
    print("=" * 60)

    print("\n--- PART 1: DISCOVERY ---")
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("\nStudying the legacy system:")
    legacy_inventory_system()
    print("\nYour understanding:", part_1_understanding())

    print("\n--- PART 2: OWNERSHIP ---")
    print("{{CONTEXT_OWNERSHIP_INTRO}}")
    print("\nYour enhanced system:")
    # enhanced_inventory_system()  # Uncomment after implementing

    print("\n--- PART 3: INVESTIGATION ---")
    print("{{CONTEXT_INVESTIGATION_INTRO}}")

    print("\nBuggy Feature 1:")
    # buggy_feature_1()  # Uncomment to see error
    print("Fixed Feature 1:")
    # fixed_feature_1()  # Uncomment after fixing

    print("\nBuggy Feature 2:")
    buggy_feature_2()
    print("Fixed Feature 2:")
    # fixed_feature_2()  # Uncomment after fixing

    print("\nBuggy Feature 3:")
    buggy_feature_3()
    print("Fixed Feature 3:")
    # fixed_feature_3()  # Uncomment after fixing

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
