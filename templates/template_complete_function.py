# =============================================================================
# TEMPLATE: Complete the Function
# =============================================================================
#
# PURPOSE: Students finish partially-written functions.
# SKILL: Implementation, working with existing code structure
#
# STRUCTURE:
#   - Provide function signature and docstring
#   - Provide some starter code (setup, structure)
#   - Student completes the implementation
#   - Include tests to verify correctness
#
# GUIDELINES:
#   - Docstring should clearly specify expected behavior
#   - Starter code should establish the PATTERN/APPROACH
#   - Leave the CORE LOGIC for student to complete
#   - Include 2-3 examples in docstring
#   - Tests at bottom should verify all examples work
#
# HOW MUCH TO PROVIDE:
#   - Always: function signature, docstring with examples
#   - Usually: initial variable setup (empty list, counter = 0)
#   - Sometimes: loop structure without body
#   - Never: the actual logic/solution
#
# DIFFICULTY SCALING:
#   - Easy: Most structure given, just fill in 1-3 lines
#   - Medium: Structure suggested, student writes core loop/logic
#   - Hard: Only signature and docstring, student designs approach
#
# =============================================================================

# Exercise N: Complete the Function - [TOPIC]
#
# Each function is partially written. Read the docstring and
# the started code, then complete the implementation.
#
# Theme: [THEMED CONTEXT USING {{placeholders}}]


def function_name(param1, param2):
    """
    [Clear description of what function does]

    Args:
        param1: [Description and type]
        param2: [Description and type]

    Returns:
        [Description of return value and type]

    Examples:
        >>> function_name(example_input_1)
        expected_output_1
        >>> function_name(example_input_2)
        expected_output_2
    """
    # Started for you:
    # [SETUP CODE - variable initialization, etc.]

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: [GUIDANCE ON APPROACH]

    # [STRUCTURE HINTS IF APPROPRIATE]
    # for item in param1:
    #     [student fills this in]

    pass  # Replace with implementation

    # return [appropriate value]


# [REPEAT PATTERN FOR MORE FUNCTIONS]


def main():
    # Test [function_name]
    print("=== Test: [function_name] ===")
    # [CALL FUNCTION WITH TEST INPUTS]
    # [PRINT RESULTS]
    # [COMPARE TO EXPECTED]

    # [REPEAT FOR EACH FUNCTION]


main()


# =============================================================================
# STARTER CODE PATTERNS:
# =============================================================================
#
# ACCUMULATOR PATTERN:
#   result = 0  # or [] or ""
#   for item in collection:
#       # ✏️ YOUR CODE HERE - update result
#   return result
#
# FILTER PATTERN:
#   matches = []
#   for item in collection:
#       # ✏️ YOUR CODE HERE - check condition, append if match
#   return matches
#
# TRANSFORM PATTERN:
#   transformed = []
#   for item in collection:
#       # ✏️ YOUR CODE HERE - transform item, append
#   return transformed
#
# SEARCH PATTERN:
#   for item in collection:
#       # ✏️ YOUR CODE HERE - check condition
#       # return item if found
#   return None  # or default
#
# BUILD DICTIONARY PATTERN:
#   result = {}
#   for item in collection:
#       # ✏️ YOUR CODE HERE - add to dict
#   return result
#
# =============================================================================
