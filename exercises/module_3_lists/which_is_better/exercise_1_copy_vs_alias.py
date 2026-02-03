# =============================================================================
# Which is Better: Copy vs Alias
# =============================================================================
# Difficulty: 4
# Concepts: List aliasing, copying, mutability implications
# =============================================================================

"""
{{CONTEXT_COMPARISON_INTRO}}
{{CONTEXT_COMPARISON_DECISION}}
"""


# ============================================================
# {{APPROACH_1_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_1_NARRATIVE}}
#
# Version A: Direct Assignment (Creates an Alias)


def backup_inventory_alias(inventory):
    """Version A: Direct assignment"""
    backup = inventory  # This creates an ALIAS
    return backup


def demo_alias():
    """Demonstrate what happens with an alias"""
    inventory = ["{{item}}", "potion", "key"]
    print(f"Original: {inventory}")

    backup = inventory  # Alias!

    # Modify original
    inventory.append("map")
    inventory.remove("potion")

    print(f"After modifications:")
    print(f"  Inventory: {inventory}")
    print(f"  Backup: {backup}")
    print(f"  Same object? {inventory is backup}")


# ============================================================
# {{APPROACH_2_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_2_NARRATIVE}}
#
# Version B: Slice Copy (Creates Independent Copy)


def backup_inventory_copy(inventory):
    """Version B: Slice creates a copy"""
    backup = inventory[:]  # This creates a COPY
    return backup


def demo_copy():
    """Demonstrate what happens with a copy"""
    inventory = ["{{item}}", "potion", "key"]
    print(f"Original: {inventory}")

    backup = inventory[:]  # Copy!

    # Modify original
    inventory.append("map")
    inventory.remove("potion")

    print(f"After modifications:")
    print(f"  Inventory: {inventory}")
    print(f"  Backup: {backup}")
    print(f"  Same object? {inventory is backup}")


# ============================================================
# {{APPROACH_3_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_3_NARRATIVE}}
#
# Version C: list() Constructor (Also Creates Copy)


def backup_inventory_list(inventory):
    """Version C: list() also creates a copy"""
    backup = list(inventory)  # This creates a COPY
    return backup


# ============================================================
# YOUR ANALYSIS
# ============================================================


def analysis_backup():
    # YOUR ANALYSIS
    #
    # Consider these questions:
    # 1. When would you WANT changes to affect both variables?
    # 2. When would you NEED an independent copy?
    # 3. Is there a performance difference?

    analysis = """
    When to use ALIAS (direct assignment):
    -

    When to use COPY (slice or list()):
    -

    Performance consideration:
    -

    Most common mistake beginners make:
    -
    """
    return analysis


# ============================================================
# COMPARISON 2: Passing Lists to Functions
# ============================================================
#
# What happens when you pass a list to a function?


def modify_in_function_v1(items):
    """Version 1: Modifies the original list"""
    items.append("new item")
    items[0] = "changed"
    # No return needed - original is modified


def modify_in_function_v2(items):
    """Version 2: Works on a copy, returns new list"""
    result = items[:]  # Work on a copy
    result.append("new item")
    result[0] = "changed"
    return result


def demo_function_modifications():
    """Show the difference between modifying vs copying in functions"""
    print("=== Version 1: Direct Modification ===")
    inventory1 = ["{{item}}", "potion"]
    print(f"Before: {inventory1}")
    modify_in_function_v1(inventory1)
    print(f"After: {inventory1}")

    print("\n=== Version 2: Copy and Return ===")
    inventory2 = ["{{item}}", "potion"]
    print(f"Before: {inventory2}")
    new_inventory = modify_in_function_v2(inventory2)
    print(f"Original after: {inventory2}")
    print(f"Returned: {new_inventory}")


def analysis_function():
    # YOUR ANALYSIS
    #
    # Which approach is better for functions?

    analysis = """
    Version 1 (modify in place) is better when:
    -

    Version 2 (copy and return) is better when:
    -

    Which is safer for beginners?
    -

    Which is more "functional" style?
    -
    """
    return analysis


# ============================================================
# COMPARISON 3: Building Up vs Replacing
# ============================================================


def collect_items_v1():
    """Version 1: Build up with append"""
    items = []
    items.append("{{item}}")
    items.append("potion")
    items.append("key")
    return items


def collect_items_v2():
    """Version 2: Create and extend"""
    items = []
    new_items = ["{{item}}", "potion", "key"]
    items = items + new_items  # Creates a new list
    return items


def collect_items_v3():
    """Version 3: Just create directly"""
    items = ["{{item}}", "potion", "key"]
    return items


def analysis_building():
    # YOUR ANALYSIS
    #
    # All three create the same result. Which is best?

    analysis = """
    Version 1 (append one by one):
    - Good when:
    - Less ideal when:

    Version 2 (concatenation):
    - Good when:
    - Less ideal when:

    Version 3 (direct creation):
    - Good when:
    - Less ideal when:

    General recommendation:
    -
    """
    return analysis


def main():
    print("{{CONTEXT_COMPARISON_INTRO}}")
    print("=" * 50)

    print("\n=== COMPARISON 1: Alias vs Copy ===")
    print("\nVersion A (Alias):")
    demo_alias()
    print("\nVersion B (Copy):")
    demo_copy()
    print(f"\nYour analysis:{analysis_backup()}")

    print("\n=== COMPARISON 2: Functions ===")
    demo_function_modifications()
    print(f"\nYour analysis:{analysis_function()}")

    print("\n=== COMPARISON 3: Building Lists ===")
    print(f"V1 result: {collect_items_v1()}")
    print(f"V2 result: {collect_items_v2()}")
    print(f"V3 result: {collect_items_v3()}")
    print(f"\nYour analysis:{analysis_building()}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_EVALUATION_COMPLETE}}")


main()
