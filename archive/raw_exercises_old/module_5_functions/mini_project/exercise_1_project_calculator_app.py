# Exercise 1: Mini Project - Calculator App
#
# Build a calculator application! Some helper functions are provided,
# you need to complete them and build the main calculator logic.
#
# Theme: {{hero}}'s Magical Calculator


# ============================================================
# PART 1: Basic Operation Functions (PROVIDED - STUDY THESE)
# ============================================================

def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """
    Divide a by b.
    Returns None if b is zero.
    """
    if b == 0:
        return None
    return a / b


# ============================================================
# PART 2: Additional Operations (YOU IMPLEMENT THESE)
# ============================================================

def power(base, exponent):
    """
    Calculate base raised to exponent.

    Examples:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
        >>> power(10, 2)
        100
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def modulo(a, b):
    """
    Calculate remainder of a divided by b.
    Returns None if b is zero.

    Examples:
        >>> modulo(10, 3)
        1
        >>> modulo(15, 5)
        0
        >>> modulo(7, 0)
        None
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def square_root(n):
    """
    Calculate square root of n.
    Returns None if n is negative.

    Examples:
        >>> square_root(16)
        4.0
        >>> square_root(2)
        1.4142...
        >>> square_root(-1)
        None
    """
    # ✏️ YOUR CODE HERE ✏️
    # Hint: You can use n ** 0.5 or import math
    pass


def absolute(n):
    """
    Return absolute value of n.

    Examples:
        >>> absolute(-5)
        5
        >>> absolute(3)
        3
        >>> absolute(0)
        0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 3: Input Handling (YOU IMPLEMENT THESE)
# ============================================================

def parse_number(text):
    """
    Convert text to a number (int or float).
    Returns None if conversion fails.

    Examples:
        >>> parse_number("42")
        42
        >>> parse_number("3.14")
        3.14
        >>> parse_number("abc")
        None
    """
    # ✏️ YOUR CODE HERE ✏️
    # Hint: Use try/except with float()
    pass


def get_operation_function(symbol):
    """
    Return the function for a given operation symbol.
    Returns None if symbol is not recognized.

    Supported symbols: +, -, *, /, ^, %

    Examples:
        >>> func = get_operation_function("+")
        >>> func(2, 3)
        5
        >>> get_operation_function("?")
        None
    """
    # ✏️ YOUR CODE HERE ✏️
    # Hint: Use a dictionary to map symbols to functions
    operations = {
        "+": add,
        "-": subtract,
        # Add the rest...
    }
    pass


# ============================================================
# PART 4: Calculation Engine (YOU IMPLEMENT THESE)
# ============================================================

def calculate(num1, operator, num2):
    """
    Perform a calculation with two numbers and an operator.

    Args:
        num1: First number
        operator: Operation symbol (+, -, *, /, ^, %)
        num2: Second number

    Returns:
        The result, or None if operation fails

    Examples:
        >>> calculate(10, "+", 5)
        15
        >>> calculate(10, "/", 0)
        None
        >>> calculate(2, "^", 8)
        256
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def calculate_expression(expression):
    """
    Parse and calculate a simple expression like "5 + 3".

    Args:
        expression: String with format "num1 operator num2"

    Returns:
        The result, or None if expression is invalid

    Examples:
        >>> calculate_expression("5 + 3")
        8
        >>> calculate_expression("10 * 2")
        20
        >>> calculate_expression("invalid")
        None
    """
    # ✏️ YOUR CODE HERE ✏️
    # Hint: Split by space, validate parts, call calculate()
    pass


# ============================================================
# PART 5: History Feature (YOU IMPLEMENT THESE)
# ============================================================

def create_history():
    """
    Create an empty calculation history.

    Returns:
        list: Empty list to store calculations
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def add_to_history(history, expression, result):
    """
    Add a calculation to history.

    Args:
        history: The history list
        expression: The expression that was calculated
        result: The result of the calculation

    Example:
        >>> h = create_history()
        >>> add_to_history(h, "5 + 3", 8)
        >>> h
        [{'expression': '5 + 3', 'result': 8}]
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_history(history, count=5):
    """
    Get the last 'count' calculations from history.

    Args:
        history: The history list
        count: Number of recent calculations to return

    Returns:
        list: Last 'count' history entries
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def clear_history(history):
    """
    Clear all history.

    Args:
        history: The history list
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 6: Interactive Calculator (PROVIDED - STUDY AND EXTEND)
# ============================================================

def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 40)
    print(f"  {{hero}}'s Magical Calculator")
    print("=" * 40)
    print("Operations: + - * / ^ %")
    print("Commands: history, clear, quit")
    print("=" * 40)


def run_calculator():
    """Run the interactive calculator."""
    display_menu()
    history = create_history()

    while True:
        print()
        user_input = input("Enter calculation (or command): ").strip().lower()

        if user_input == "quit":
            print("Goodbye!")
            break

        elif user_input == "history":
            recent = get_history(history)
            if recent:
                print("\nRecent calculations:")
                for entry in recent:
                    print(f"  {entry['expression']} = {entry['result']}")
            else:
                print("No history yet.")

        elif user_input == "clear":
            clear_history(history)
            print("History cleared.")

        else:
            result = calculate_expression(user_input)
            if result is not None:
                print(f"= {result}")
                add_to_history(history, user_input, result)
            else:
                print("Invalid expression. Try: 5 + 3")


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Test all calculator functions."""
    print("Testing Calculator Functions...\n")

    # Test basic operations
    print("Testing basic operations...")
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 4) == 12
    assert divide(10, 2) == 5
    assert divide(10, 0) is None
    print("   ✓ Basic operations passed!\n")

    # Test additional operations
    print("Testing additional operations...")
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert modulo(10, 3) == 1
    assert modulo(10, 0) is None
    assert square_root(16) == 4.0
    assert square_root(-1) is None
    assert absolute(-5) == 5
    print("   ✓ Additional operations passed!\n")

    # Test input handling
    print("Testing input handling...")
    assert parse_number("42") == 42
    assert parse_number("3.14") == 3.14
    assert parse_number("abc") is None
    assert get_operation_function("+") is not None
    assert get_operation_function("?") is None
    print("   ✓ Input handling passed!\n")

    # Test calculation
    print("Testing calculation...")
    assert calculate(10, "+", 5) == 15
    assert calculate(10, "-", 3) == 7
    assert calculate(4, "*", 5) == 20
    assert calculate(20, "/", 4) == 5
    assert calculate(2, "^", 3) == 8
    assert calculate(10, "%", 3) == 1
    print("   ✓ Calculation passed!\n")

    # Test expression parsing
    print("Testing expression parsing...")
    assert calculate_expression("5 + 3") == 8
    assert calculate_expression("10 * 2") == 20
    assert calculate_expression("invalid") is None
    print("   ✓ Expression parsing passed!\n")

    # Test history
    print("Testing history...")
    h = create_history()
    add_to_history(h, "5 + 3", 8)
    add_to_history(h, "10 * 2", 20)
    recent = get_history(h, 2)
    assert len(recent) == 2
    clear_history(h)
    assert len(h) == 0
    print("   ✓ History passed!\n")

    print("=" * 40)
    print("All tests passed! 🎉")


def main():
    print("=== Calculator Mini Project ===")
    print()
    print("Complete all the functions marked with ✏️")
    print("Then choose an option below:")
    print()

    # Uncomment ONE of these:
    # run_tests()        # Test your implementation
    # run_calculator()   # Run interactive calculator


main()
