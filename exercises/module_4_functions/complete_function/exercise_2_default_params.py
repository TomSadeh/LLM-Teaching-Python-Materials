# =============================================================================
# Complete the Function: Default Parameters
# =============================================================================
# Difficulty: 3
# Concepts: Default parameter values, optional arguments, parameter ordering
# =============================================================================

"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# Function 1: Single Default Parameter
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}

def greet(name, greeting="Hello"):
    """
    Create a greeting message.

    Args:
        name: The person to greet.
        greeting: The greeting word (default: "Hello").

    Returns:
        A formatted greeting string.

    Examples:
        >>> greet("{{hero}}")
        'Hello, {{hero}}!'
        >>> greet("{{heroine}}", "Welcome")
        'Welcome, {{heroine}}!'
    """
    # COMPLETE THIS FUNCTION
    #
    # Return a formatted string: "{greeting}, {name}!"
    #
    # Hint: The greeting parameter already has a default value.
    #       If the caller doesn't provide it, "Hello" is used.

    pass  # Replace with implementation


# ============================================================
# Function 2: Multiple Default Parameters
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}

def format_profile(name, title="Member", level=1):
    """
    Format a profile display.

    Args:
        name: The person's name (required).
        title: Their title (default: "Member").
        level: Their level (default: 1).

    Returns:
        A formatted profile string.

    Examples:
        >>> format_profile("{{hero}}")
        '{{hero}} - Member (Level 1)'
        >>> format_profile("{{heroine}}", "Leader")
        '{{heroine}} - Leader (Level 1)'
        >>> format_profile("{{mentor}}", "Advisor", 10)
        '{{mentor}} - Advisor (Level 10)'
    """
    # COMPLETE THIS FUNCTION
    #
    # Return: "{name} - {title} (Level {level})"
    #
    # Hint: All the parameters are available, just format them.

    pass


# ============================================================
# Function 3: Required Before Optional
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}

def calculate_score(base, bonus=0, multiplier=1):
    """
    Calculate a final score with optional modifiers.

    Args:
        base: The base score (required).
        bonus: Extra points to add (default: 0).
        multiplier: Score multiplier (default: 1).

    Returns:
        The calculated score: (base + bonus) * multiplier

    Examples:
        >>> calculate_score(100)
        100
        >>> calculate_score(100, 20)
        120
        >>> calculate_score(100, 20, 2)
        240
    """
    # COMPLETE THIS FUNCTION
    #
    # Calculate and return: (base + bonus) * multiplier
    #
    # Hint: Do the addition first, then multiply.

    pass


# ============================================================
# Function 4: Default with Condition
# ============================================================
# {{CONTEXT_FUNCTION_4_NARRATIVE}}

def get_message(name, is_new=True):
    """
    Get an appropriate message based on membership status.

    Args:
        name: The person's name.
        is_new: Whether they are new (default: True).

    Returns:
        A welcome message for new members, or a greeting for returning ones.

    Examples:
        >>> get_message("{{hero}}")
        'Welcome to {{school}}, {{hero}}!'
        >>> get_message("{{heroine}}", False)
        'Welcome back, {{heroine}}!'
    """
    # COMPLETE THIS FUNCTION
    #
    # If is_new is True, return: "Welcome to {{school}}, {name}!"
    # If is_new is False, return: "Welcome back, {name}!"
    #
    # Hint: Use an if/else statement.

    pass


# ============================================================
# Function 5: Flexible Formatting
# ============================================================
# {{CONTEXT_FUNCTION_5_NARRATIVE}}

def create_header(text, width=40, char="="):
    """
    Create a formatted header with customizable appearance.

    Args:
        text: The header text (required).
        width: Total width of the header line (default: 40).
        char: Character to use for the border (default: "=").

    Returns:
        A formatted header string with border above and below.

    Examples:
        >>> create_header("News")
        '========================================\\nNews\\n========================================'
        >>> create_header("Alert", 20, "-")
        '--------------------\\nAlert\\n--------------------'
    """
    # COMPLETE THIS FUNCTION
    #
    # Create a header with:
    # - A line of {char} repeated {width} times
    # - The text
    # - Another line of {char} repeated {width} times
    #
    # Hint: Use char * width to create the border line.
    #       Use \n to join the parts, or return them combined.

    pass


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing greet ===")
    print(greet("{{hero}}"))
    print(greet("{{heroine}}", "Welcome"))
    print(greet("{{friend}}", "Greetings"))

    print("\n=== Testing format_profile ===")
    print(format_profile("{{hero}}"))
    print(format_profile("{{heroine}}", "Leader"))
    print(format_profile("{{mentor}}", "Advisor", 10))

    print("\n=== Testing calculate_score ===")
    print(f"Base only: {calculate_score(100)}")
    print(f"With bonus: {calculate_score(100, 20)}")
    print(f"With multiplier: {calculate_score(100, 20, 2)}")

    print("\n=== Testing get_message ===")
    print(get_message("{{hero}}"))
    print(get_message("{{heroine}}", False))
    print(get_message("{{friend}}", True))

    print("\n=== Testing create_header ===")
    header1 = create_header("{{school}} News")
    print(header1)
    print()
    header2 = create_header("Alert", 30, "-")
    print(header2)

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
