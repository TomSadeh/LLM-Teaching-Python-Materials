# =============================================================================
# Complete the Function: Format Output
# =============================================================================
# Difficulty: 4
# Concepts: f-strings, string formatting, return values
# =============================================================================

"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{FUNCTION_1_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}


def format_greeting(name, location):
    """
    Create a formatted greeting message.

    Args:
        name: The person's name (string)
        location: Where they are (string)

    Returns:
        A greeting string in the format: "Hello, NAME! Welcome to LOCATION."

    Examples:
        >>> format_greeting("{{hero}}", "{{school}}")
        "Hello, {{hero}}! Welcome to {{school}}."
        >>> format_greeting("Maya", "Python Academy")
        "Hello, Maya! Welcome to Python Academy."
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # Use an f-string to create the greeting.
    # f-strings let you put variables inside curly braces: f"Hello, {name}!"
    #
    # Hint: The f goes BEFORE the opening quote.

    pass  # Replace with: return f"..."


# ============================================================
# {{FUNCTION_2_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}


def format_stats(hero_name, health, gold):
    """
    Create a formatted stats display.

    Args:
        hero_name: The character's name (string)
        health: Current health points (integer)
        gold: Amount of gold (integer)

    Returns:
        A stats string with the hero's name, health, and gold.

    Examples:
        >>> format_stats("{{hero}}", 100, 50)
        "{{hero}} - HP: 100 | Gold: 50"
        >>> format_stats("Alex", 75, 200)
        "Alex - HP: 75 | Gold: 200"
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # Use an f-string with multiple variables.
    # You can put any variable inside {braces}.
    #
    # Hint: Numbers work inside f-strings too!

    pass


# ============================================================
# {{FUNCTION_3_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}


def format_calculation(num1, num2):
    """
    Create a formatted calculation result.

    Args:
        num1: First number (integer)
        num2: Second number (integer)

    Returns:
        A string showing the calculation and result.

    Examples:
        >>> format_calculation(10, 5)
        "10 + 5 = 15"
        >>> format_calculation(3, 7)
        "3 + 7 = 10"
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # You can do math INSIDE the f-string braces!
    # Example: f"{a} + {b} = {a + b}"
    #
    # Hint: The calculation happens when the f-string is created.

    pass


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
    result1 = format_greeting("{{hero}}", "{{school}}")
    print("Result:", result1)
    print("Expected: Hello, {{hero}}! Welcome to {{school}}.")

    print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
    result2 = format_stats("{{hero}}", 100, 50)
    print("Result:", result2)
    print("Expected: {{hero}} - HP: 100 | Gold: 50")

    print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
    result3 = format_calculation(10, 5)
    print("Result:", result3)
    print("Expected: 10 + 5 = 15")

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
