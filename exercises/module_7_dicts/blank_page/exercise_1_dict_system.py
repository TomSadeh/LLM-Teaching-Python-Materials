"""
{{CONTEXT_BLANK_PAGE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Implement these functions based only on their docstrings.
This is the ultimate test of your dictionary skills!
"""


# ============================================================
# {{BLANK_1_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_1_NARRATIVE}}


def create_profile(name, level=1):
    """
    Create a new profile dictionary.

    Args:
        name: The profile name (str)
        level: Starting level (int, default 1)

    Returns:
        dict: A profile with keys 'name', 'level', 'experience', 'inventory'
              - 'experience' starts at 0
              - 'inventory' starts as an empty dict

    Examples:
        >>> create_profile("{{hero}}")
        {'name': '{{hero}}', 'level': 1, 'experience': 0, 'inventory': {}}
        >>> create_profile("{{heroine}}", 5)
        {'name': '{{heroine}}', 'level': 5, 'experience': 0, 'inventory': {}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_2_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_2_NARRATIVE}}


def add_experience(profile, amount):
    """
    Add experience to a profile. Level up at 100 experience.

    Args:
        profile: A profile dictionary
        amount: Experience points to add (int)

    Returns:
        bool: True if leveled up, False otherwise

    Modifies the profile in place.
    When experience >= 100: level up, reset experience to 0.

    Examples:
        >>> p = create_profile("{{hero}}")
        >>> add_experience(p, 50)
        False
        >>> p['experience']
        50
        >>> add_experience(p, 60)  # 50 + 60 = 110 >= 100
        True
        >>> p['level']
        2
        >>> p['experience']
        0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_3_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_3_NARRATIVE}}


def add_item(profile, item_name, quantity=1):
    """
    Add items to the profile's inventory.

    Args:
        profile: A profile dictionary
        item_name: Name of the item (str)
        quantity: How many to add (int, default 1)

    Modifies the profile's inventory in place.
    If item already exists, adds to existing quantity.

    Examples:
        >>> p = create_profile("{{hero}}")
        >>> add_item(p, "{{item}}", 3)
        >>> p['inventory']
        {'{{item}}': 3}
        >>> add_item(p, "{{item}}", 2)
        >>> p['inventory']
        {'{{item}}': 5}
        >>> add_item(p, "{{spell1}}")
        >>> p['inventory']
        {'{{item}}': 5, '{{spell1}}': 1}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_4_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_4_NARRATIVE}}


def use_item(profile, item_name):
    """
    Use one of an item from inventory.

    Args:
        profile: A profile dictionary
        item_name: Name of the item to use

    Returns:
        bool: True if used successfully, False if item not available

    Decreases quantity by 1. Removes item if quantity reaches 0.

    Examples:
        >>> p = create_profile("{{hero}}")
        >>> add_item(p, "{{item}}", 2)
        >>> use_item(p, "{{item}}")
        True
        >>> p['inventory']
        {'{{item}}': 1}
        >>> use_item(p, "{{item}}")
        True
        >>> p['inventory']
        {}
        >>> use_item(p, "{{item}}")
        False
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_5_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_5_NARRATIVE}}


def get_inventory_summary(profile):
    """
    Get a summary of the profile's inventory.

    Args:
        profile: A profile dictionary

    Returns:
        dict: Summary with 'total_items' and 'unique_items' keys

    Examples:
        >>> p = create_profile("{{hero}}")
        >>> add_item(p, "{{item}}", 5)
        >>> add_item(p, "{{spell1}}", 3)
        >>> get_inventory_summary(p)
        {'total_items': 8, 'unique_items': 2}
        >>> p2 = create_profile("{{heroine}}")
        >>> get_inventory_summary(p2)
        {'total_items': 0, 'unique_items': 0}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_6_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_6_NARRATIVE}}


def merge_profiles(profile1, profile2):
    """
    Merge two profiles into a new combined profile.

    Args:
        profile1: First profile dictionary
        profile2: Second profile dictionary

    Returns:
        dict: New profile with:
              - name: "profile1_name & profile2_name"
              - level: higher of the two levels
              - experience: sum of both experiences (may cause level up)
              - inventory: combined inventories

    Does NOT modify the original profiles.

    Examples:
        >>> p1 = create_profile("{{hero}}", 5)
        >>> p1['experience'] = 30
        >>> add_item(p1, "{{item}}", 3)
        >>> p2 = create_profile("{{heroine}}", 3)
        >>> p2['experience'] = 50
        >>> add_item(p2, "{{item}}", 2)
        >>> add_item(p2, "{{spell1}}", 1)
        >>> merged = merge_profiles(p1, p2)
        >>> merged['name']
        '{{hero}} & {{heroine}}'
        >>> merged['level']
        5
        >>> merged['experience']
        80
        >>> merged['inventory']
        {'{{item}}': 5, '{{spell1}}': 1}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Run tests for all functions."""
    print("Testing your implementations...\n")

    # Test create_profile
    print("{{BLANK_1_TITLE}}: create_profile")
    p = create_profile("{{hero}}")
    assert p["name"] == "{{hero}}", "Name should be '{{hero}}'"
    assert p["level"] == 1, "Default level should be 1"
    assert p["experience"] == 0, "Experience should start at 0"
    assert p["inventory"] == {}, "Inventory should be empty"
    p2 = create_profile("{{heroine}}", 5)
    assert p2["level"] == 5, "Custom level should be 5"
    print("   Passed!\n")

    # Test add_experience
    print("{{BLANK_2_TITLE}}: add_experience")
    p = create_profile("{{hero}}")
    result = add_experience(p, 50)
    assert result == False, "Should not level up at 50 xp"
    assert p["experience"] == 50, "Experience should be 50"
    result = add_experience(p, 60)
    assert result == True, "Should level up at 110 xp"
    assert p["level"] == 2, "Level should be 2"
    assert p["experience"] == 0, "Experience should reset to 0"
    print("   Passed!\n")

    # Test add_item
    print("{{BLANK_3_TITLE}}: add_item")
    p = create_profile("{{hero}}")
    add_item(p, "{{item}}", 3)
    assert p["inventory"]["{{item}}"] == 3, "Should have 3 {{item}}"
    add_item(p, "{{item}}", 2)
    assert p["inventory"]["{{item}}"] == 5, "Should have 5 {{item}}"
    add_item(p, "{{spell1}}")
    assert p["inventory"]["{{spell1}}"] == 1, "Should have 1 {{spell1}}"
    print("   Passed!\n")

    # Test use_item
    print("{{BLANK_4_TITLE}}: use_item")
    p = create_profile("{{hero}}")
    add_item(p, "{{item}}", 2)
    result = use_item(p, "{{item}}")
    assert result == True, "Should successfully use item"
    assert p["inventory"]["{{item}}"] == 1, "Should have 1 left"
    result = use_item(p, "{{item}}")
    assert "{{item}}" not in p["inventory"], "Item should be removed when 0"
    result = use_item(p, "{{item}}")
    assert result == False, "Should return False when item not available"
    print("   Passed!\n")

    # Test get_inventory_summary
    print("{{BLANK_5_TITLE}}: get_inventory_summary")
    p = create_profile("{{hero}}")
    add_item(p, "{{item}}", 5)
    add_item(p, "{{spell1}}", 3)
    summary = get_inventory_summary(p)
    assert summary["total_items"] == 8, "Total should be 8"
    assert summary["unique_items"] == 2, "Unique should be 2"
    print("   Passed!\n")

    # Test merge_profiles
    print("{{BLANK_6_TITLE}}: merge_profiles")
    p1 = create_profile("{{hero}}", 5)
    p1["experience"] = 30
    add_item(p1, "{{item}}", 3)
    p2 = create_profile("{{heroine}}", 3)
    p2["experience"] = 50
    add_item(p2, "{{item}}", 2)
    merged = merge_profiles(p1, p2)
    assert merged["name"] == "{{hero}} & {{heroine}}", "Name should be combined"
    assert merged["level"] == 5, "Level should be max of both"
    assert merged["experience"] == 80, "Experience should be summed"
    assert merged["inventory"]["{{item}}"] == 5, "Inventory should be merged"
    # Original profiles should be unchanged
    assert p1["inventory"]["{{item}}"] == 3, "Original p1 should not change"
    print("   Passed!\n")

    print("=" * 40)
    print("All tests passed!")


def main():
    print("{{CONTEXT_BLANK_PAGE_INTRO}}")
    print("=" * 50)
    print()
    print("Implement each function based on its docstring.")
    print("When ready, run the tests to check your work.")
    print()

    # Uncomment to run tests after implementing:
    # run_tests()

    print("{{CONTEXT_MASTERY_COMPLETE}}")


main()
