"""
TEMPLATE 14: COLLECTION BUILDER
Purpose: Accumulate items into growing collection over time
Complexity: ⭐ Simple
Best for: Building inventory, gathering data, compiling results, list/set/dict building
"""

"""
{{CONTEXT_COLLECTION_INTRO}}

{{CONTEXT_COLLECTION_GOAL}}
"""

# ============================================================
# {{COLLECTION_TYPE_TITLE}}
# ============================================================
# {{CONTEXT_COLLECTION_TYPE_NARRATIVE}}


def initialize_collection():
    """
    {{COLLECTION_INIT_DESCRIPTION}}

    Returns:
        list/set/dict: {{COLLECTION_INIT_RETURN}}

    {{CONTEXT_COLLECTION_STRUCTURE}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Create empty collection of appropriate type
    pass


# ============================================================
# {{ADD_ITEM_TITLE}}
# ============================================================
# {{CONTEXT_ADD_ITEM_NARRATIVE}}


def add_to_collection(collection, item):
    """
    {{ADD_ITEM_DESCRIPTION}}

    Args:
        collection (list/set/dict): {{ADD_ITEM_COLLECTION_PARAM}}
        item (type): {{ADD_ITEM_ITEM_PARAM}}

    Returns:
        None (modifies collection in-place) or new collection

    {{CONTEXT_ADD_ITEM_RULES}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Add item to collection
    # Handle duplicates if applicable
    # Validate item if needed
    pass


# ============================================================
# {{REMOVE_ITEM_TITLE}}
# ============================================================
# {{CONTEXT_REMOVE_ITEM_NARRATIVE}}


def remove_from_collection(collection, item):
    """
    {{REMOVE_ITEM_DESCRIPTION}}

    Args:
        collection (list/set/dict): {{REMOVE_ITEM_COLLECTION_PARAM}}
        item (type): {{REMOVE_ITEM_ITEM_PARAM}}

    Returns:
        bool: {{REMOVE_ITEM_RETURN}}

    {{CONTEXT_REMOVE_ITEM_RULES}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Remove item from collection if present
    # Return True if removed, False if not found
    pass


# ============================================================
# {{CHECK_ITEM_TITLE}}
# ============================================================
# {{CONTEXT_CHECK_ITEM_NARRATIVE}}


def check_collection(collection, item):
    """
    {{CHECK_ITEM_DESCRIPTION}}

    Args:
        collection (list/set/dict): {{CHECK_ITEM_COLLECTION_PARAM}}
        item (type): {{CHECK_ITEM_ITEM_PARAM}}

    Returns:
        bool: {{CHECK_ITEM_RETURN}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Check if item exists in collection
    pass


# ============================================================
# {{DISPLAY_TITLE}}
# ============================================================
# {{CONTEXT_DISPLAY_NARRATIVE}}


def display_collection(collection):
    """
    {{DISPLAY_DESCRIPTION}}

    Args:
        collection (list/set/dict): {{DISPLAY_COLLECTION_PARAM}}

    {{CONTEXT_DISPLAY_FORMAT}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Display collection contents in readable format
    # Include count/size
    # Format nicely
    pass


# ============================================================
# COLLECTION BUILDING SIMULATION
# ============================================================


def build_collection_simulation():
    """
    {{CONTEXT_SIMULATION_DESCRIPTION}}

    Demonstrates the complete lifecycle of collection building.
    """
    print("=" * 60)
    print("{{CONTEXT_SIMULATION_START}}")
    print("=" * 60)
    print()

    # Initialize
    print("{{CONTEXT_INIT_STEP}}")
    print("-" * 60)
    collection = initialize_collection()
    if collection is not None:
        print("{{CONTEXT_INIT_SUCCESS}}")
        display_collection(collection)
    print()

    # Add items
    print("{{CONTEXT_ADD_STEP}}")
    print("-" * 60)
    items_to_add = [
        "{{ADD_ITEM_1}}",
        "{{ADD_ITEM_2}}",
        "{{ADD_ITEM_3}}",
        "{{ADD_ITEM_4}}",
        "{{ADD_ITEM_5}}"
    ]

    for item in items_to_add:
        print(f"{{CONTEXT_ADDING_MESSAGE}}: {item}")
        add_to_collection(collection, item)

    print(f"\n{{CONTEXT_ADD_COMPLETE}}")
    display_collection(collection)
    print()

    # Check for items
    print("{{CONTEXT_CHECK_STEP}}")
    print("-" * 60)
    check_items = ["{{CHECK_ITEM_1}}", "{{CHECK_ITEM_2}}"]

    for item in check_items:
        exists = check_collection(collection, item)
        if exists:
            print(f"✅ {item}: {{CONTEXT_ITEM_FOUND}}")
        else:
            print(f"❌ {item}: {{CONTEXT_ITEM_NOT_FOUND}}")
    print()

    # Remove items
    print("{{CONTEXT_REMOVE_STEP}}")
    print("-" * 60)
    items_to_remove = ["{{REMOVE_ITEM_1}}", "{{REMOVE_ITEM_2}}"]

    for item in items_to_remove:
        success = remove_from_collection(collection, item)
        if success:
            print(f"✅ {{CONTEXT_REMOVED_MESSAGE}}: {item}")
        else:
            print(f"❌ {{CONTEXT_NOT_FOUND_MESSAGE}}: {item}")

    print(f"\n{{CONTEXT_REMOVE_COMPLETE}}")
    display_collection(collection)
    print()

    print("=" * 60)
    print("{{CONTEXT_SIMULATION_COMPLETE}}")
    print("=" * 60)


# ============================================================
# INTERACTIVE MODE
# ============================================================


def interactive_collection_builder():
    """
    {{CONTEXT_INTERACTIVE_DESCRIPTION}}

    Lets user build collection interactively.
    """
    collection = initialize_collection()
    print("{{CONTEXT_INTERACTIVE_WELCOME}}")
    print()

    while True:
        print("\n{{CONTEXT_MENU_TITLE}}")
        print("-" * 60)
        print("1. {{CONTEXT_MENU_ADD}}")
        print("2. {{CONTEXT_MENU_REMOVE}}")
        print("3. {{CONTEXT_MENU_CHECK}}")
        print("4. {{CONTEXT_MENU_DISPLAY}}")
        print("5. {{CONTEXT_MENU_QUIT}}")

        choice = input("\n{{CONTEXT_MENU_PROMPT}} ")

        if choice == "1":
            item = input("{{CONTEXT_INPUT_ADD_PROMPT}} ")
            add_to_collection(collection, item)
            print(f"{{CONTEXT_INPUT_ADD_SUCCESS}}: {item}")

        elif choice == "2":
            item = input("{{CONTEXT_INPUT_REMOVE_PROMPT}} ")
            success = remove_from_collection(collection, item)
            if success:
                print(f"{{CONTEXT_INPUT_REMOVE_SUCCESS}}: {item}")
            else:
                print(f"{{CONTEXT_INPUT_REMOVE_FAILURE}}: {item}")

        elif choice == "3":
            item = input("{{CONTEXT_INPUT_CHECK_PROMPT}} ")
            exists = check_collection(collection, item)
            if exists:
                print(f"✅ {{CONTEXT_INPUT_CHECK_SUCCESS}}")
            else:
                print(f"❌ {{CONTEXT_INPUT_CHECK_FAILURE}}")

        elif choice == "4":
            display_collection(collection)

        elif choice == "5":
            print("{{CONTEXT_INTERACTIVE_GOODBYE}}")
            break

        else:
            print("{{CONTEXT_INVALID_CHOICE}}")


def main():
    """Run collection builder in chosen mode."""
    print("{{CONTEXT_MAIN_WELCOME}}")
    print()
    print("1. {{CONTEXT_MODE_SIMULATION}}")
    print("2. {{CONTEXT_MODE_INTERACTIVE}}")
    print()

    mode = input("{{CONTEXT_MODE_PROMPT}} ")

    if mode == "1":
        build_collection_simulation()
    elif mode == "2":
        interactive_collection_builder()
    else:
        print("{{CONTEXT_INVALID_MODE}}")


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_COLLECTION_INTRO}}         - Why collections matter
# {{CONTEXT_COLLECTION_GOAL}}          - What we're building
# {{COLLECTION_TYPE_TITLE}}            - Type of collection heading
# {{CONTEXT_COLLECTION_TYPE_NARRATIVE}} - Story behind collection
# {{COLLECTION_INIT_DESCRIPTION}}      - Technical: what init does
# {{COLLECTION_INIT_RETURN}}           - What init returns
# {{CONTEXT_COLLECTION_STRUCTURE}}     - Structure details
#
# Add operation:
# {{ADD_ITEM_TITLE}}                   - Add heading
# {{CONTEXT_ADD_ITEM_NARRATIVE}}       - Story behind adding
# {{ADD_ITEM_DESCRIPTION}}             - Technical description
# {{ADD_ITEM_COLLECTION_PARAM}}        - Collection parameter
# {{ADD_ITEM_ITEM_PARAM}}              - Item parameter
# {{CONTEXT_ADD_ITEM_RULES}}           - Rules for adding
#
# Remove operation:
# {{REMOVE_ITEM_TITLE}}                - Remove heading
# {{CONTEXT_REMOVE_ITEM_NARRATIVE}}    - Story behind removing
# {{REMOVE_ITEM_DESCRIPTION}}          - Technical description
# {{REMOVE_ITEM_COLLECTION_PARAM}}     - Collection parameter
# {{REMOVE_ITEM_ITEM_PARAM}}           - Item parameter
# {{REMOVE_ITEM_RETURN}}               - Return value
# {{CONTEXT_REMOVE_ITEM_RULES}}        - Rules for removing
#
# Check operation:
# {{CHECK_ITEM_TITLE}}                 - Check heading
# {{CONTEXT_CHECK_ITEM_NARRATIVE}}     - Story behind checking
# {{CHECK_ITEM_DESCRIPTION}}           - Technical description
# {{CHECK_ITEM_COLLECTION_PARAM}}      - Collection parameter
# {{CHECK_ITEM_ITEM_PARAM}}            - Item parameter
# {{CHECK_ITEM_RETURN}}                - Return value
#
# Display:
# {{DISPLAY_TITLE}}                    - Display heading
# {{CONTEXT_DISPLAY_NARRATIVE}}        - Story behind display
# {{DISPLAY_DESCRIPTION}}              - Technical description
# {{DISPLAY_COLLECTION_PARAM}}         - Collection parameter
# {{CONTEXT_DISPLAY_FORMAT}}           - Format requirements
#
# Simulation items:
# {{ADD_ITEM_N}}                       - Items to add (5 total)
# {{CHECK_ITEM_N}}                     - Items to check (2 total)
# {{REMOVE_ITEM_N}}                    - Items to remove (2 total)
#
# Simulation messages:
# {{CONTEXT_SIMULATION_DESCRIPTION}}   - What simulation does
# {{CONTEXT_SIMULATION_START}}         - Opening message
# {{CONTEXT_INIT_STEP}}                - Init step label
# {{CONTEXT_INIT_SUCCESS}}             - Init success message
# {{CONTEXT_ADD_STEP}}                 - Add step label
# {{CONTEXT_ADDING_MESSAGE}}           - Adding message
# {{CONTEXT_ADD_COMPLETE}}             - Add complete message
# {{CONTEXT_CHECK_STEP}}               - Check step label
# {{CONTEXT_ITEM_FOUND}}               - Item found message
# {{CONTEXT_ITEM_NOT_FOUND}}           - Item not found message
# {{CONTEXT_REMOVE_STEP}}              - Remove step label
# {{CONTEXT_REMOVED_MESSAGE}}          - Removed message
# {{CONTEXT_NOT_FOUND_MESSAGE}}        - Not found message
# {{CONTEXT_REMOVE_COMPLETE}}          - Remove complete message
# {{CONTEXT_SIMULATION_COMPLETE}}      - Closing message
#
# Interactive mode:
# {{CONTEXT_INTERACTIVE_DESCRIPTION}}  - What interactive mode does
# {{CONTEXT_INTERACTIVE_WELCOME}}      - Welcome message
# {{CONTEXT_MENU_TITLE}}               - Menu heading
# {{CONTEXT_MENU_ADD}}                 - Add menu option
# {{CONTEXT_MENU_REMOVE}}              - Remove menu option
# {{CONTEXT_MENU_CHECK}}               - Check menu option
# {{CONTEXT_MENU_DISPLAY}}             - Display menu option
# {{CONTEXT_MENU_QUIT}}                - Quit menu option
# {{CONTEXT_MENU_PROMPT}}              - Menu prompt
# {{CONTEXT_INPUT_ADD_PROMPT}}         - Prompt for add
# {{CONTEXT_INPUT_ADD_SUCCESS}}        - Add success message
# {{CONTEXT_INPUT_REMOVE_PROMPT}}      - Prompt for remove
# {{CONTEXT_INPUT_REMOVE_SUCCESS}}     - Remove success message
# {{CONTEXT_INPUT_REMOVE_FAILURE}}     - Remove failure message
# {{CONTEXT_INPUT_CHECK_PROMPT}}       - Prompt for check
# {{CONTEXT_INPUT_CHECK_SUCCESS}}      - Check success message
# {{CONTEXT_INPUT_CHECK_FAILURE}}      - Check failure message
# {{CONTEXT_INTERACTIVE_GOODBYE}}      - Goodbye message
# {{CONTEXT_INVALID_CHOICE}}           - Invalid choice message
#
# Main:
# {{CONTEXT_MAIN_WELCOME}}             - Main welcome message
# {{CONTEXT_MODE_SIMULATION}}          - Simulation mode description
# {{CONTEXT_MODE_INTERACTIVE}}         - Interactive mode description
# {{CONTEXT_MODE_PROMPT}}              - Mode selection prompt
# {{CONTEXT_INVALID_MODE}}             - Invalid mode message
