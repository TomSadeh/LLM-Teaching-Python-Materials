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
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_COMPLETE_FUNCTION_INTRO}} - Main intro for completion exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}      - What student will learn
#
# Per-Function:
#   {{FUNCTION_N_TITLE}}                - Title for function N (1, 2, 3...)
#   {{CONTEXT_FUNCTION_N_NARRATIVE}}    - Story/context for function N
#   {{CONTEXT_FUNCTION_HINT_N}}         - Hint for function N
#
# Closing:
#   {{CONTEXT_FINAL_ASSEMBLY}}          - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{FUNCTION_1_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}

def function_a(param1, param2):
    """
    [Clear description of what function does]

    Args:
        param1: [Description and type]
        param2: [Description and type]

    Returns:
        [Description of return value and type]

    Examples:
        >>> function_a(example_input_1)
        expected_output_1
        >>> function_a(example_input_2)
        expected_output_2
    """
    # Started for you:
    # [SETUP CODE - variable initialization, etc.]

    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # {{CONTEXT_FUNCTION_HINT_1}}

    pass  # Replace with implementation


# ============================================================
# {{FUNCTION_2_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}

def function_b(param):
    """
    [Description]

    Examples:
        >>> function_b(input1)
        output1
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # {{CONTEXT_FUNCTION_HINT_2}}

    pass


# [REPEAT PATTERN FOR MORE FUNCTIONS]


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
    # [CALL FUNCTION WITH TEST INPUTS]
    # [PRINT RESULTS]
    # [COMPARE TO EXPECTED]

    print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
    # [TEST CALLS]

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


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
