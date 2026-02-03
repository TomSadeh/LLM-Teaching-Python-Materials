"""
{{CONTEXT_ERROR_HANDLING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Topic: Handling ModuleNotFoundError
Difficulty: 3

When importing modules, things can go wrong: the module might not exist,
be misspelled, or not be installed. Learn to handle these gracefully.
"""


# ============================================================
# {{HANDLING_1_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# This function crashes if the module doesn't exist.


def original_import_helper():
    """ORIGINAL: Crashes if module doesn't exist"""
    import nonexistent_module  # This will crash!
    return nonexistent_module.some_function()


def safe_import_optional_module(module_name):
    """
    Try to import a module, return None if not available.

    Args:
        module_name: Name of module to import

    Returns:
        The module object, or None if import failed

    Should handle:
    - ModuleNotFoundError -> print message and return None
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_1}}
    #
    # Step 1: Use try/except to catch ModuleNotFoundError
    #
    # Step 2: Inside try:
    #         Use __import__(module_name) to dynamically import
    #         This is equivalent to: import module_name
    #
    # Step 3: If successful, return the module
    #
    # Step 4: In except block:
    #         Print: f"Module '{module_name}' not found"
    #         Return None
    #
    # Example:
    #   try:
    #       module = __import__(module_name)
    #       return module
    #   except ModuleNotFoundError:
    #       print(f"Module '{module_name}' not found")
    #       return None
    pass


# ============================================================
# {{HANDLING_2_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# Sometimes you want to use optional features if available.


def original_use_optional_feature():
    """ORIGINAL: Crashes if colorama isn't installed"""
    import colorama  # Optional third-party module
    colorama.init()
    return colorama.Fore.RED + "Error!" + colorama.Style.RESET_ALL


def use_colors_if_available(text, color="red"):
    """
    Return colored text if colorama is available, plain text otherwise.

    Args:
        text: The text to potentially color
        color: Color name (ignored if colorama unavailable)

    Returns:
        str: Colored text if possible, plain text otherwise
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_2}}
    #
    # Step 1: Try to import colorama
    #
    # Step 2: If successful, use it to color the text
    #
    # Step 3: If ModuleNotFoundError, just return the plain text
    #
    # Pattern:
    #   try:
    #       import colorama
    #       colorama.init()
    #       # ... use colorama ...
    #   except ModuleNotFoundError:
    #       return text  # Return plain text
    pass


# ============================================================
# {{HANDLING_3_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# Handle typos in module names gracefully.


def original_import_with_typo():
    """ORIGINAL: Crashes due to typo in module name"""
    import maht  # Typo! Should be 'math'
    return maht.sqrt(16)


def safe_math_sqrt(value):
    """
    Calculate square root with import error handling.

    Args:
        value: Number to find square root of

    Returns:
        float: The square root, or None if import fails
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_3}}
    #
    # Step 1: Try to import math and calculate sqrt
    #
    # Step 2: Handle ModuleNotFoundError (shouldn't happen with math,
    #         but demonstrates the pattern)
    #
    # Step 3: Handle ValueError for negative numbers
    #
    # Example:
    #   try:
    #       import math
    #       return math.sqrt(value)
    #   except ModuleNotFoundError:
    #       print("Math module not available")
    #       return None
    #   except ValueError:
    #       print("Cannot calculate square root of negative number")
    #       return None
    pass


# ============================================================
# {{HANDLING_4_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# Create a flexible import function for {{school}}.


def try_import_modules(module_names, fallback_value=None):
    """
    Try to import from a list of modules, return first success.

    Args:
        module_names: List of module names to try
        fallback_value: Value to return if all imports fail

    Returns:
        First successfully imported module, or fallback_value
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_4}}
    #
    # Step 1: Loop through module_names
    #
    # Step 2: For each name, try to import it
    #
    # Step 3: If import succeeds, return the module immediately
    #
    # Step 4: If import fails (ModuleNotFoundError), continue to next
    #
    # Step 5: After the loop, return fallback_value
    #
    # Example:
    #   for name in module_names:
    #       try:
    #           return __import__(name)
    #       except ModuleNotFoundError:
    #           continue
    #   return fallback_value
    pass


def main():
    print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
    print("=" * 50)

    print("\n=== {{HANDLING_1_TITLE}} ===")
    print("Testing optional module import:")
    # Uncomment to test:
    # result = safe_import_optional_module("math")
    # if result:
    #     print(f"  math imported: sqrt(16) = {result.sqrt(16)}")
    # result = safe_import_optional_module("fake_module")
    # print(f"  fake_module result: {result}")

    print("\n=== {{HANDLING_2_TITLE}} ===")
    print("Testing optional colors:")
    # Uncomment to test:
    # text = use_colors_if_available("Warning message", "yellow")
    # print(f"  Result: {text}")

    print("\n=== {{HANDLING_3_TITLE}} ===")
    print("Testing safe sqrt:")
    # Uncomment to test:
    # print(f"  sqrt(16) = {safe_math_sqrt(16)}")
    # print(f"  sqrt(-4) = {safe_math_sqrt(-4)}")

    print("\n=== {{HANDLING_4_TITLE}} ===")
    print("Testing flexible import:")
    # Uncomment to test:
    # modules_to_try = ["fake1", "fake2", "math", "fake3"]
    # result = try_import_modules(modules_to_try)
    # if result:
    #     print(f"  Found module: {result.__name__}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")


main()
