"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise where you'll learn to create your own
Python modules. You'll understand module structure, build reusable
code, and learn the important __name__ == "__main__" pattern.

Programming concepts: module creation, code organization, __name__ pattern
Difficulty: 3-4
"""


# ============================================================
# PART 1: Discovery - Understanding Module Structure
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# A Python module is simply a .py file containing code.
# When you import it, Python runs that file and makes its
# contents available.


"""
MODULE ANATOMY (study this):

A typical module contains:
1. Module docstring (what the module does)
2. Imports (modules this module depends on)
3. Constants (values that don't change)
4. Functions (reusable code)
5. Classes (later module - not yet!)
6. Main block (code that runs only when executed directly)

Example structure:
    '''Module docstring'''

    import math  # Imports

    PI = 3.14159  # Constants

    def my_function():  # Functions
        pass

    if __name__ == "__main__":  # Main block
        # Only runs when this file is executed directly
        # NOT when imported
        pass
"""


def explain_module_structure():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a docstring explaining what makes a good module.
    #
    # Write a multi-line string explaining:
    # 1. What a Python module is
    # 2. What you can put in a module
    # 3. Why modules are useful
    #
    # Print your explanation
    pass


# ============================================================
# PART 2: Ownership - Create Your Own Module Functions
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Write functions that could be part of a reusable module.
# These functions should be general-purpose and well-documented.


# --- Module Constants ---
DEFAULT_GREETING = "Welcome to {{school}}!"
VERSION = "1.0.0"


def greet(name):
    """
    Generate a greeting for {{school}}.

    Args:
        name: The name of the person to greet

    Returns:
        str: A personalized greeting

    Example:
        >>> greet("{{hero}}")
        "Welcome to {{school}}, {{hero}}!"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create a greeting string using the name
    # Step 2: Return it
    #
    # Format: "Welcome to {{school}}, [name]!"
    pass


def calculate_score(base, multiplier=1.0, bonus=0):
    """
    Calculate a score for {{school}} activities.

    Args:
        base: Base score value
        multiplier: Score multiplier (default 1.0)
        bonus: Bonus points to add (default 0)

    Returns:
        float: Calculated score

    Example:
        >>> calculate_score(100, 1.5, 10)
        160.0
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Formula: (base * multiplier) + bonus
    pass


def format_result(value, label="Result"):
    """
    Format a value with a label for display.

    Args:
        value: The value to format
        label: Label for the value (default "Result")

    Returns:
        str: Formatted string

    Example:
        >>> format_result(42, "Score")
        "Score: 42"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Return: "[label]: [value]"
    pass


# ============================================================
# PART 3: Growth - The __name__ == "__main__" Pattern
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# This pattern is CRUCIAL for making modules work correctly.


"""
THE __name__ VARIABLE:

Python sets __name__ to:
- "__main__" when you run the file directly: python mymodule.py
- The module name when imported: import mymodule

WHY THIS MATTERS:

When you run:
    python mymodule.py

Python sets __name__ = "__main__", and code in the
if __name__ == "__main__": block runs.

When someone imports your module:
    import mymodule

Python sets __name__ = "mymodule", so the code in the
if __name__ == "__main__": block does NOT run.

This lets you:
1. Include test code that only runs when testing
2. Provide a demo when run directly
3. Keep imports clean (no side effects)
"""


def demonstrate_name_variable():
    """
    Show the current value of __name__.

    When called from this file directly: "__main__"
    When called after import: "exercise_6_create_module"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Print the value of __name__
    #
    # Step 2: Explain what it means:
    #         if __name__ == "__main__":
    #             print("This file is being run directly")
    #         else:
    #             print("This file was imported as a module")
    pass


# ============================================================
# PART 4: Ownership - Using Your Module
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Demonstrate how your module would be used.


def module_demo():
    """
    Demonstrate all the module's capabilities.

    This function should:
    1. Show the module version
    2. Demonstrate each function
    3. Show example outputs
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Print module info
    #         print(f"Module Version: {VERSION}")
    #         print(f"Default Greeting: {DEFAULT_GREETING}")
    #
    # Step 2: Demonstrate greet()
    #         print(greet("{{hero}}"))
    #         print(greet("{{heroine}}"))
    #
    # Step 3: Demonstrate calculate_score()
    #         score1 = calculate_score(100)
    #         score2 = calculate_score(100, 1.5)
    #         score3 = calculate_score(100, 1.5, 25)
    #         Print each result
    #
    # Step 4: Demonstrate format_result()
    #         print(format_result(score3, "Final Score"))
    pass


# ============================================================
# MAIN BLOCK - Only runs when file is executed directly
# ============================================================

def main():
    """
    Main function - runs when module is executed directly.

    This is where you put demo code, tests, or a CLI interface.
    """
    print("=" * 60)
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("Creating Your Own Module")
    print("=" * 60)
    print()

    print(">>> PART 1: Understanding Module Structure")
    print("-" * 40)
    explain_module_structure()
    print()

    print(">>> PART 2: Your Module Functions")
    print("-" * 40)
    # Uncomment to test your functions:
    # print(f"Greeting: {greet('{{hero}}')}")
    # print(f"Score: {calculate_score(100, 1.5, 10)}")
    # print(f"Formatted: {format_result(42, 'Points')}")
    print()

    print(">>> PART 3: The __name__ Variable")
    print("-" * 40)
    demonstrate_name_variable()
    print()

    print(">>> PART 4: Module Demo")
    print("-" * 40)
    module_demo()
    print()

    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print()
    print("Key Takeaways:")
    print("  1. A module is just a .py file")
    print("  2. Include docstrings for documentation")
    print("  3. Use __name__ == '__main__' for demo/test code")
    print("  4. Functions should be general and reusable")
    print("=" * 60)


# This is the key pattern - study it!
if __name__ == "__main__":
    main()
