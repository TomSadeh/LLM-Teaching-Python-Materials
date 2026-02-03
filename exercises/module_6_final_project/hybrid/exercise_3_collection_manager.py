"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part project where you'll build a collection manager.
You'll design functions from specifications, implement CRUD operations,
and create a complete menu-driven application.

{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# PART 1: Core Function Design (Blank Page)
# ============================================================
# {{CONTEXT_BLANK_PAGE_INTRO}}
#
# Design and implement these core functions based only on their
# docstrings. This tests your ability to translate requirements into code.
#
# Your collection will store {{item}} objects. Each item is a list:
# [name, category, quantity]


def create_item(name, category, quantity):
    """
    Create a new item for the collection.

    Args:
        name: Item name (string)
        category: Item category like "rare", "common", "legendary" (string)
        quantity: How many of this item (integer)

    Returns:
        A list: [name, category, quantity]

    Examples:
        >>> create_item("{{item}}", "rare", 3)
        ['{{item}}', 'rare', 3]
        >>> create_item("{{item}}", "common", 10)
        ['{{item}}', 'common', 10]
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_item_name(item):
    """
    Get the name from an item.

    Args:
        item: An item list [name, category, quantity]

    Returns:
        The item's name (string)

    Examples:
        >>> item = ["{{item}}", "rare", 3]
        >>> get_item_name(item)
        '{{item}}'
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_item_category(item):
    """
    Get the category from an item.

    Args:
        item: An item list [name, category, quantity]

    Returns:
        The item's category (string)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_item_quantity(item):
    """
    Get the quantity from an item.

    Args:
        item: An item list [name, category, quantity]

    Returns:
        The item's quantity (integer)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def set_item_quantity(item, new_quantity):
    """
    Update the quantity of an item.

    Args:
        item: An item list to modify
        new_quantity: The new quantity (integer)

    Returns:
        None (modifies the item in place)

    Examples:
        >>> item = ["{{item}}", "common", 5]
        >>> set_item_quantity(item, 10)
        >>> item
        ['{{item}}', 'common', 10]
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 2: Collection Operations
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
#
# Now implement the core operations for managing a collection.


def add_item(collection, item):
    """
    Add an item to the collection.

    Args:
        collection: The list of items
        item: An item list to add

    Returns:
        None (modifies collection in place)

    Note:
        If an item with the same name exists, increase its quantity instead.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def remove_item(collection, item_name):
    """
    Remove an item from the collection by name.

    Args:
        collection: The list of items
        item_name: Name of item to remove (string)

    Returns:
        True if item was removed, False if not found.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def find_item(collection, item_name):
    """
    Find an item in the collection by name.

    Args:
        collection: The list of items
        item_name: Name to search for (case-insensitive)

    Returns:
        The item list if found, None otherwise.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_collection(collection):
    """
    Display all items in the collection.

    Args:
        collection: The list of items

    Prints:
        A formatted list of all items:
        === Your Collection ===
        1. [name] (category) x[quantity]
        2. [name] (category) x[quantity]
        ...
        =======================
        Total items: N

        If empty: "Your collection is empty."
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 3: Search and Filter Functions
# ============================================================
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Add powerful search and filter capabilities.


def filter_by_category(collection, category):
    """
    Get all items of a specific category.

    Args:
        collection: The list of items
        category: Category to filter by (string)

    Returns:
        A NEW list containing only items of that category.

    Note:
        Do not modify the original collection.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def search_items(collection, search_term):
    """
    Search for items whose name contains the search term.

    Args:
        collection: The list of items
        search_term: Text to search for (case-insensitive)

    Returns:
        A NEW list of items whose names contain the search term.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_total_quantity(collection):
    """
    Calculate the total quantity of all items.

    Args:
        collection: The list of items

    Returns:
        The sum of all item quantities (integer).
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_categories(collection):
    """
    Get a list of all unique categories in the collection.

    Args:
        collection: The list of items

    Returns:
        A list of unique category names (no duplicates).
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 4: Menu Interface with Validation
# ============================================================
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Build the complete interactive interface.


def print_menu():
    """
    Display the collection manager menu.

    Prints:
        === {{hero}}'s Collection Manager ===
        1. View collection
        2. Add item
        3. Remove item
        4. Search items
        5. Filter by category
        6. Collection stats
        7. Quit
        ====================================
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_menu_choice():
    """
    Get a valid menu choice from the user.

    Returns:
        An integer 1-7.

    Note:
        Keep prompting until valid input is received.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_item_input():
    """
    Get item details from the user.

    Returns:
        A tuple: (name, category, quantity)

    Note:
        - Prompt for name (any non-empty string)
        - Prompt for category (any non-empty string)
        - Prompt for quantity (must be positive integer)
        - Validate each input before accepting
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_stats(collection):
    """
    Display collection statistics.

    Args:
        collection: The list of items

    Prints:
        === Collection Statistics ===
        Total unique items: N
        Total quantity: M
        Categories: [list of categories]
        =============================
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def create_sample_collection():
    """
    Create a sample collection to start with.

    Returns:
        A list containing 3-5 sample items using themed placeholders.
        Include items like {{item}}, potions, keys, etc.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def run_collection_manager():
    """
    Run the main collection manager loop.

    This function:
    1. Creates a sample collection to start
    2. Shows the menu
    3. Gets user choice
    4. Performs the action
    5. Repeats until quit

    Handle each menu option appropriately.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)
    print()
    print("Complete each part to build the collection manager.")
    print()

    # Uncomment to test individual parts:
    # Part 1 test
    # item = create_item("{{item}}", "rare", 5)
    # print(f"Created: {item}")
    # print(f"Name: {get_item_name(item)}")

    # Part 2 test
    # collection = []
    # add_item(collection, create_item("{{item}}", "common", 3))
    # add_item(collection, create_item("{{item}}", "rare", 1))
    # display_collection(collection)

    # Part 3 test
    # collection = create_sample_collection()
    # rare_items = filter_by_category(collection, "rare")
    # print(f"Rare items: {len(rare_items)}")

    # Part 4 - run the full program
    # run_collection_manager()

    print()
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()
