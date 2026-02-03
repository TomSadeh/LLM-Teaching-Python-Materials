"""
{{CONTEXT_SETBACK_INTRO}}

This is a multi-part exercise where you rescue a broken inventory system.
Diagnose the errors, trace the problem, and fix it properly.

Programming concepts: dictionaries, KeyError, .get(), safe access patterns
"""


# ============================================================
# PART 1: The Setback - Diagnose the Crash
# ============================================================
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# The inventory system is crashing! Read the error message
# and understand what went wrong.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "inventory.py", line 15, in <module>
    use_item(inventory, "{{spell3}}")
  File "inventory.py", line 8, in use_item
    inventory[item_name] -= 1
KeyError: '{{spell3}}'
"""


def buggy_use_item(inventory, item_name):
    """BUGGY: Try to use an item from inventory."""
    # This crashes when item_name doesn't exist!
    inventory[item_name] -= 1
    print(f"Used one {{{{item_name}}}}. Remaining: {inventory[item_name]}")


def diagnose_error():
    # ✏️ DIAGNOSE THE ERROR ✏️
    #
    # Answer these questions in comments:
    #
    # 1. What type of error occurred?
    #    Answer:
    #
    # 2. On which line did the error occur?
    #    Answer:
    #
    # 3. Why did this error happen?
    #    Answer:
    #
    # 4. What item was the code trying to access?
    #    Answer:
    #

    pass


# ============================================================
# PART 2: Investigation - Trace the Problem
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Trace through a sequence of operations to see
# where the inventory state goes wrong.


def code_to_trace():
    """Trace this code to understand the problem."""
    inventory = {"{{item}}": 3, "{{spell1}}": 1}

    # These work fine
    inventory["{{item}}"] -= 1
    inventory["{{spell1}}"] -= 1

    # This would crash! (commented out)
    # inventory["{{spell2}}"] -= 1

    print(inventory)


def trace_the_problem():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | inventory contents                 | Notes                |
    # |------|------------------------------------|----------------------|
    # | 0    | {"{{item}}": 3, "{{spell1}}": 1}   | Initial state        |
    # | 1    |                                    | After using {{item}} |
    # | 2    |                                    | After using {{spell1}}|
    # | 3    | ???                                | What if we tried {{spell2}}? |
    #
    # Explain: Why would step 3 crash if uncommented?
    #

    pass


# ============================================================
# PART 3: Improvement - Fix with .get()
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Rewrite the inventory system using .get() to make it robust.


def safe_use_item(inventory, item_name):
    """
    Safely use an item from inventory.

    Args:
        inventory: Dict mapping item names to quantities
        item_name: The item to use

    Returns:
        bool: True if item was used, False if not available

    If the item exists and quantity > 0, decrement and return True.
    Otherwise, return False without crashing.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Get current quantity using .get(item_name, 0)
    #
    # Step 2: If quantity > 0:
    #         - Decrement the inventory
    #         - Print: "Used one [item]. Remaining: [count]"
    #         - Return True
    #
    # Step 3: Otherwise:
    #         - Print: "[item] not available!"
    #         - Return False

    pass


def safe_add_item(inventory, item_name, quantity):
    """
    Safely add items to inventory.

    Args:
        inventory: Dict mapping item names to quantities
        item_name: The item to add
        quantity: How many to add

    Works whether the item already exists or not.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use the pattern: inventory[item] = inventory.get(item, 0) + quantity
    # Print: "Added [quantity] [item]. Total: [new_total]"

    pass


def check_inventory(inventory, item_name):
    """
    Check how many of an item you have.

    Args:
        inventory: Dict mapping item names to quantities
        item_name: The item to check

    Returns:
        int: Quantity owned (0 if not in inventory)
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use .get() to safely return the quantity

    pass


# ============================================================
# PART 4: Testing the Fixed System
# ============================================================


def test_fixed_inventory():
    """Test all the fixed functions."""
    print("=== Testing Fixed Inventory System ===")
    print()

    inventory = {}

    # Add some items
    print("--- Adding items ---")
    safe_add_item(inventory, "{{item}}", 3)
    safe_add_item(inventory, "{{spell1}}", 2)
    safe_add_item(inventory, "{{item}}", 1)  # Add more of same item

    print()
    print(f"Current inventory: {inventory}")
    print()

    # Use items
    print("--- Using items ---")
    safe_use_item(inventory, "{{item}}")
    safe_use_item(inventory, "{{spell2}}")  # Doesn't exist - should NOT crash!
    safe_use_item(inventory, "{{spell1}}")
    safe_use_item(inventory, "{{spell1}}")
    safe_use_item(inventory, "{{spell1}}")  # Out of stock - should handle gracefully

    print()
    print(f"Final inventory: {inventory}")

    # Check quantities
    print()
    print("--- Checking inventory ---")
    print(f"{{{{item}}}}: {check_inventory(inventory, '{{item}}')}")
    print(f"{{{{spell2}}}}: {check_inventory(inventory, '{{spell2}}')}")


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_SETBACK_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Diagnose the crash...")
    print("(Read the error message and complete diagnose_error())")
    print()

    print(">>> PART 2: Trace the problem...")
    print("(Complete trace_the_problem())")
    # Uncomment to see actual execution:
    # code_to_trace()
    print()

    print(">>> PART 3: Fix the system...")
    print("(Implement safe_use_item, safe_add_item, check_inventory)")
    print()

    print(">>> PART 4: Test your fixes...")
    # Uncomment after implementing Part 3:
    # test_fixed_inventory()

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
