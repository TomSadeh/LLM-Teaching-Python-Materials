"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Topic: Using break to exit loops early
Difficulty: 2-3

The 'break' statement immediately exits the current loop.
Use it when you've found what you're looking for or need to stop early.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Use break to exit a loop when a condition is met.


def find_first_negative(numbers):
    """
    Find the first negative number in a list.

    Args:
        numbers: A list of integers

    Returns:
        The first negative number, or None if all are non-negative

    Example:
        find_first_negative([3, 7, -2, 5, -8]) returns -2
        find_first_negative([1, 2, 3]) returns None
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Set result = None
    # Step 2: Loop through each number in numbers
    # Step 3: If the number is negative:
    #         - Set result to that number
    #         - Break out of the loop
    # Step 4: Return result
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Use break with user input to create exit conditions.


def collect_names_until_done():
    """
    Collect names from the user until they type 'done'.

    Returns:
        list: All the names collected (not including 'done')

    The function should:
    - Ask "Enter a name (or 'done' to finish): "
    - Keep asking until user types 'done'
    - Return the list of names collected
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create an empty list for names
    # Step 2: Start an infinite loop (while True)
    # Step 3: Ask for input
    # Step 4: If input is 'done', break
    # Step 5: Otherwise, add the name to the list
    # Step 6: After the loop, return the list
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Use break in a search to stop once you find the target.


def search_inventory(inventory, target):
    """
    Search for a target item in an inventory.
    Print each item checked, and stop when found.

    Args:
        inventory: List of items
        target: Item to find

    Returns:
        int: Index where found, or -1 if not found

    Example:
        search_inventory(["{{item}}", "{{pet}}", "{{creature}}"], "{{pet}}")
        Prints:
            Checking: {{item}}
            Checking: {{pet}}
            Found {{pet}}!
        Returns: 1
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Loop through inventory with index (use range(len(...)))
    # Step 2: Print f"Checking: {item}"
    # Step 3: If item equals target:
    #         - Print f"Found {target}!"
    #         - Return the index (using break or direct return)
    # Step 4: After the loop, print f"{target} not found."
    # Step 5: Return -1
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# Use break with a counter limit to prevent infinite loops.


def safe_guess_loop():
    """
    Let the user guess a secret word with a maximum of 5 attempts.

    The secret word is "{{password}}".

    Returns:
        bool: True if guessed correctly, False if ran out of attempts

    The function should:
    - Give the user up to 5 attempts
    - If they guess correctly, print a success message and return True
    - If they run out of attempts, print failure message and return False
    """
    secret = "{{password}}"
    max_attempts = 5

    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Set attempts = 0
    # Step 2: While attempts < max_attempts:
    #         - Increase attempts
    #         - Ask for a guess
    #         - If guess equals secret, print success and return True
    # Step 3: After the loop, print failure message
    # Step 4: Return False
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}
#
# Combine break with complex conditions.


def process_until_error(data):
    """
    Process data items until you encounter an error value.
    Error values are: "ERROR", "", or None.

    Args:
        data: List of values to process

    Returns:
        list: Successfully processed values (before the error)

    Example:
        process_until_error(["a", "b", "ERROR", "c"]) returns ["A", "B"]
        (Values are uppercased during processing, stops at ERROR)
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create an empty list for results
    # Step 2: Loop through each item in data
    # Step 3: If item is "ERROR", "", or None:
    #         - Print f"Error encountered! Stopping."
    #         - Break
    # Step 4: Process the item (convert to uppercase) and add to results
    #         - Print f"Processed: {processed_item}"
    # Step 5: Return results
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    numbers = [5, 12, 8, -3, 7, -1]
    result = find_first_negative(numbers)
    print(f"First negative in {numbers}: {result}")

    print("\n=== {{PHASE_2_TITLE}} ===")
    print("Collecting names (type 'done' to finish):")
    # Uncomment to test:
    # names = collect_names_until_done()
    # print(f"Collected: {names}")

    print("\n=== {{PHASE_3_TITLE}} ===")
    inventory = ["{{item}}", "{{pet}}", "{{creature}}", "{{transport}}"]
    index = search_inventory(inventory, "{{creature}}")
    print(f"Found at index: {index}")

    print("\n=== {{PHASE_4_TITLE}} ===")
    print("Guess the secret word:")
    # Uncomment to test:
    # success = safe_guess_loop()
    # print(f"Result: {'Success!' if success else 'Failed'}")

    print("\n=== {{PHASE_5_TITLE}} ===")
    test_data = ["{{hero}}", "{{heroine}}", "ERROR", "{{friend}}"]
    processed = process_until_error(test_data)
    print(f"Processed items: {processed}")

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
