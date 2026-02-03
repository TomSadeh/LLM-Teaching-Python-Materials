# =============================================================================
# Hybrid Exercise: The Mystery - The Vanishing Element
# =============================================================================
# Difficulty: 3
# Arc: Mystery (DISCOVERY -> INVESTIGATION -> IMPROVEMENT)
# Concepts: List mutation, unexpected behavior with methods
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: DISCOVERY - Observe Unexpected Behavior
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Something strange is happening with {{hero}}'s inventory.
# Study this code and predict what it will print.


def mysterious_code():
    """Study this code - predict the output BEFORE running!"""
    inventory = ["{{item}}", "potion", "key", "map"]
    print(f"Step 1 - Start: {inventory}")

    # {{hero}} saves the inventory
    saved = inventory

    # {{heroine}} removes an item
    inventory.remove("potion")
    print(f"Step 2 - After remove: {inventory}")

    # {{hero}} checks saved inventory
    print(f"Step 3 - Saved copy: {saved}")


# YOUR PREDICTION:
# Step 1 - Start: _______________
# Step 2 - After remove: _______________
# Step 3 - Saved copy: _______________
#
# SURPRISE: Did the "saved" inventory change too? Why?


def part_1_observations():
    # RECORD YOUR OBSERVATIONS
    #
    # After running the code, answer these questions:

    observations = {
        "did_saved_change": "?",  # "yes" or "no"
        "why_do_you_think": "Because...",
        "is_saved_independent": "?",  # "yes" or "no"
    }

    return observations


# ============================================================
# PART 2: INVESTIGATION - Trace to Find the Cause
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Trace through this code step by step to understand WHY
# both variables point to the same list.


def investigation_code():
    """Trace this code carefully."""
    original = ["A", "B", "C"]
    print(f"Original ID: {id(original)}")

    # Assignment creates an ALIAS, not a copy!
    alias = original
    print(f"Alias ID: {id(alias)}")
    print(f"Same object? {original is alias}")

    # Modifying one affects both
    original.append("D")
    print(f"Original: {original}")
    print(f"Alias: {alias}")


def trace_table_investigation():
    # FILL IN THE TRACING TABLE
    #
    # Track what happens at each step.
    #
    # | Step | original        | alias           | Are they the same object? |
    # |------|-----------------|-----------------|---------------------------|
    # | 1    | ['A','B','C']   | -               | -                         |
    # | 2    | ['A','B','C']   | points to same  | Yes (same id)             |
    # | 3    | ?               | ?               | ?                         |
    #
    # Key insight: "alias = original" does NOT copy the list.
    # Both variables point to the SAME list in memory.

    pass


# ============================================================
# PART 3: IMPROVEMENT - Fix the Bug
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Now fix the original mystery! {{hero}} wants to ACTUALLY
# save a backup of the inventory before {{heroine}} removes items.


def buggy_inventory():
    """The original buggy code"""
    inventory = ["{{item}}", "potion", "key", "map"]
    print(f"Original: {inventory}")

    # BUG: This creates an alias, not a copy!
    backup = inventory

    inventory.remove("potion")
    inventory.remove("key")
    print(f"Modified: {inventory}")
    print(f"Backup: {backup}")  # Oops! Backup changed too!


def fixed_inventory():
    # FIX THE BUG
    #
    # There are multiple ways to create a TRUE copy:
    # 1. backup = inventory[:]      (slice creates a copy)
    # 2. backup = list(inventory)   (list() creates a copy)
    # 3. backup = inventory.copy()  (explicit copy method)
    #
    # Choose one and implement the fix:

    inventory = ["{{item}}", "potion", "key", "map"]
    print(f"Original: {inventory}")

    # YOUR CODE HERE
    # Create a REAL backup (not an alias)
    backup = None  # Fix this line!

    inventory.remove("potion")
    inventory.remove("key")
    print(f"Modified: {inventory}")
    print(f"Backup: {backup}")  # Should still have all 4 items!

    pass


def verify_fix():
    # VERIFICATION
    #
    # After fixing, the output should be:
    # Original: ['{{item}}', 'potion', 'key', 'map']
    # Modified: ['{{item}}', 'map']
    # Backup: ['{{item}}', 'potion', 'key', 'map']
    #
    # The backup should be UNCHANGED!

    pass


def main():
    print("=" * 60)
    print("THE MYSTERY: The Vanishing Element")
    print("=" * 60)

    print("\n--- PART 1: DISCOVERY ---")
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("\nRun this mysterious code:")
    mysterious_code()
    print("\nYour observations:", part_1_observations())

    print("\n--- PART 2: INVESTIGATION ---")
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("\nTracing the cause:")
    investigation_code()

    print("\n--- PART 3: IMPROVEMENT ---")
    print("{{CONTEXT_IMPROVEMENT_INTRO}}")
    print("\nBuggy version:")
    buggy_inventory()
    print("\nFixed version:")
    # fixed_inventory()  # Uncomment after fixing!

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
