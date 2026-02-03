# =============================================================================
# Complete the Function: Return Statements
# =============================================================================
# Difficulty: 2-3
# Concepts: return statement, returning values, using return values
# =============================================================================

"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# Function 1: Return a Simple Value
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}

def get_greeting():
    """
    Return a greeting message.

    Returns:
        A greeting string.

    Examples:
        >>> get_greeting()
        'Welcome to {{school}}!'
    """
    # COMPLETE THIS FUNCTION
    #
    # Return the string "Welcome to {{school}}!"
    #
    # Hint: Use the return keyword to send a value back.

    pass  # Replace with implementation


# ============================================================
# Function 2: Return with Parameter
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}

def format_name(name):
    """
    Return a formatted name with a title.

    Args:
        name: A person's name.

    Returns:
        The name with a title prefix.

    Examples:
        >>> format_name("{{hero}}")
        'Champion {{hero}}'
        >>> format_name("{{heroine}}")
        'Champion {{heroine}}'
    """
    # Started for you:
    title = "Champion"

    # COMPLETE THIS FUNCTION
    #
    # Return the title combined with the name using an f-string.
    #
    # Hint: return f"{title} {name}"

    pass


# ============================================================
# Function 3: Return a Calculation
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}

def calculate_total_points(base, bonus):
    """
    Calculate the total points from base and bonus.

    Args:
        base: The base point value (integer).
        bonus: The bonus points to add (integer).

    Returns:
        The sum of base and bonus.

    Examples:
        >>> calculate_total_points(100, 25)
        125
        >>> calculate_total_points(50, 10)
        60
    """
    # COMPLETE THIS FUNCTION
    #
    # Calculate the sum of base and bonus, then return it.
    #
    # Hint: You can calculate and return in one line:
    #       return base + bonus

    pass


# ============================================================
# Function 4: Return with Conditional
# ============================================================
# {{CONTEXT_FUNCTION_4_NARRATIVE}}

def get_status_message(level):
    """
    Return a status message based on level.

    Args:
        level: The current level (integer).

    Returns:
        "Beginner" if level < 10
        "Intermediate" if level < 20
        "Expert" otherwise

    Examples:
        >>> get_status_message(5)
        'Beginner'
        >>> get_status_message(15)
        'Intermediate'
        >>> get_status_message(25)
        'Expert'
    """
    # COMPLETE THIS FUNCTION
    #
    # Use if/elif/else to check the level and return the appropriate string.
    #
    # Hint: Each branch should have a return statement.

    pass


# ============================================================
# Function 5: Using Returned Values
# ============================================================
# {{CONTEXT_FUNCTION_5_NARRATIVE}}

def double_value(number):
    """
    Return double the input value.

    Args:
        number: A number to double.

    Returns:
        The number multiplied by 2.

    Examples:
        >>> double_value(5)
        10
        >>> double_value(7)
        14
    """
    # COMPLETE THIS FUNCTION
    #
    # Return the number multiplied by 2.

    pass


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing get_greeting ===")
    result = get_greeting()
    print(f"Result: {result}")
    print(f"Expected: Welcome to {{school}}!")

    print("\n=== Testing format_name ===")
    result1 = format_name("{{hero}}")
    result2 = format_name("{{heroine}}")
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
    print("Expected: Champion {{hero}}, Champion {{heroine}}")

    print("\n=== Testing calculate_total_points ===")
    total1 = calculate_total_points(100, 25)
    total2 = calculate_total_points(50, 10)
    print(f"100 + 25 = {total1}")
    print(f"50 + 10 = {total2}")
    print("Expected: 125, 60")

    print("\n=== Testing get_status_message ===")
    msg1 = get_status_message(5)
    msg2 = get_status_message(15)
    msg3 = get_status_message(25)
    print(f"Level 5: {msg1}")
    print(f"Level 15: {msg2}")
    print(f"Level 25: {msg3}")
    print("Expected: Beginner, Intermediate, Expert")

    print("\n=== Testing double_value ===")
    d1 = double_value(5)
    d2 = double_value(7)
    print(f"Double 5: {d1}")
    print(f"Double 7: {d2}")
    print("Expected: 10, 14")

    # Demonstrate using returned values
    print("\n=== Using Returned Values ===")
    points = calculate_total_points(80, 20)
    doubled = double_value(points)
    print(f"Points: {points}, Doubled: {doubled}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
