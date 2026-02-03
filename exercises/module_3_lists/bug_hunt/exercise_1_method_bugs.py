# =============================================================================
# Bug Hunt: List Method Bugs
# =============================================================================
# Difficulty: 3
# Concepts: Common mistakes with append, pop, insert, remove
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
# EXPECTED BEHAVIOR:
# Build a team roster and print it.
# Expected output: ['{{hero}}', '{{heroine}}', '{{friend}}']
#
# ACTUAL BEHAVIOR:
# Prints: None
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}


def buggy_a():
    """This code has exactly ONE bug. Find it!"""
    team = []
    team = team.append("{{hero}}")
    team = team.append("{{heroine}}")
    team = team.append("{{friend}}")
    print(team)


def fix_a():
    # FIX THE BUG
    #
    # What I found: ________________________________
    #
    # Hint: append() modifies the list IN PLACE and returns None.
    # You don't need to reassign the result.
    #
    # The fix:

    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Remove the item "potion" from the inventory.
# Expected output: After: ['{{item}}', 'key']
#
# ACTUAL BEHAVIOR:
# ValueError: list.remove(x): x not in list
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}


def buggy_b():
    """This code has exactly ONE bug. Find it!"""
    inventory = ["{{item}}", "potion", "key"]
    print(f"Before: {inventory}")
    inventory.remove(1)  # BUG: remove() takes a VALUE, not an index!
    print(f"After: {inventory}")


def fix_b():
    # FIX THE BUG
    #
    # What I found: ________________________________
    #
    # Hint: remove() takes a VALUE to find and remove.
    # To remove by index, use pop(index) instead.
    #
    # The fix:

    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Pop the last item and print what was removed.
# Expected output:
#   Removed: {{spell3}}
#   Remaining: ['{{spell1}}', '{{spell2}}']
#
# ACTUAL BEHAVIOR:
#   Removed: ['{{spell1}}', '{{spell2}}']
#   Remaining: {{spell3}}
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}


def buggy_c():
    """This code has exactly ONE bug. Find it!"""
    abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    removed = abilities
    abilities = abilities.pop()
    print(f"Removed: {removed}")
    print(f"Remaining: {abilities}")


def fix_c():
    # FIX THE BUG
    #
    # What I found: ________________________________
    #
    # Hint: The variables got swapped! pop() returns the removed item.
    # The list is modified in place - it doesn't need reassignment.
    #
    # The fix:

    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Insert "{{mentor}}" at position 1 (second position).
# Expected output: ['{{hero}}', '{{mentor}}', '{{heroine}}', '{{friend}}']
#
# ACTUAL BEHAVIOR:
# Prints: None
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}


def buggy_d():
    """This code has exactly ONE bug. Find it!"""
    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    team = team.insert(1, "{{mentor}}")
    print(team)


def fix_d():
    # FIX THE BUG
    #
    # What I found: ________________________________
    #
    # Hint: Just like append(), insert() modifies the list in place
    # and returns None.
    #
    # The fix:

    pass


# ============================================================
# {{CASE_5_TITLE}}
# ============================================================
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Remove all occurrences of "coin" from the items.
# Expected output: ['{{item}}', 'key']
#
# ACTUAL BEHAVIOR:
# Output: ['{{item}}', 'coin', 'key']  (one coin remains!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}


def buggy_e():
    """This code has exactly ONE bug. Find it!"""
    items = ["{{item}}", "coin", "coin", "key"]
    print(f"Before: {items}")
    items.remove("coin")
    print(f"After: {items}")


def fix_e():
    # FIX THE BUG
    #
    # What I found: ________________________________
    #
    # Hint: remove() only removes the FIRST occurrence.
    # To remove all, you'd need to call it multiple times.
    # (A loop with "in" check, or use a different approach)
    #
    # The fix (remove both coins):

    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Buggy version:")
    buggy_a()
    print("\nFixed version:")
    # fix_a()

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Buggy version:")
    # buggy_b()  # Uncomment to see the error
    print("\nFixed version:")
    # fix_b()

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Buggy version:")
    buggy_c()
    print("\nFixed version:")
    # fix_c()

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Buggy version:")
    buggy_d()
    print("\nFixed version:")
    # fix_d()

    print("\n=== {{CASE_5_TITLE}} ===")
    print("Buggy version:")
    buggy_e()
    print("\nFixed version:")
    # fix_e()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
