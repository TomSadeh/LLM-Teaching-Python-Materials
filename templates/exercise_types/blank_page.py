# =============================================================================
# TEMPLATE: Write From Scratch (Blank Page)
# =============================================================================
#
# PURPOSE: Students implement functions with minimal guidance.
# SKILL: Full problem-solving, translating requirements to code
#
# STRUCTURE:
#   - Provide ONLY: function signature + docstring with examples
#   - No starter code, no hints, no structure
#   - Student writes complete implementation
#   - Tests to verify correctness
#
# GUIDELINES:
#   - Docstring is the ONLY guidance
#   - Examples should clarify edge cases
#   - Progress from easy to hard within the exercise set
#   - This is the most challenging format - use for assessment or advanced practice
#
# DOCSTRING REQUIREMENTS:
#   - Clear description of what function does
#   - Parameter descriptions with types
#   - Return value description with type
#   - 2-4 examples showing input → output
#   - Edge cases in examples where relevant
#
# DIFFICULTY SCALING:
#   - Easy: Single operation, obvious approach
#   - Medium: Requires loop or condition, one "trick"
#   - Hard: Multiple steps, data structure knowledge needed
#   - Expert: Algorithm knowledge, optimization, complex logic
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_BLANK_PAGE_INTRO}}     - Main intro for blank page exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Challenge:
#   {{BLANK_N_TITLE}}                - Title for challenge N (1, 2, 3...)
#   {{CONTEXT_BLANK_N_NARRATIVE}}    - Story/context for challenge N
#
# Closing:
#   {{CONTEXT_MASTERY_COMPLETE}}     - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# NOTE: Blank page exercises have MINIMAL narrative by design.
# The docstring IS the specification. Use context blocks sparingly.
#
# =============================================================================

"""
{{CONTEXT_BLANK_PAGE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{BLANK_1_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_1_NARRATIVE}}

def function_a(parameters):
    """
    [Clear, concise description of what to do]

    Args:
        param1: [Type and description]
        param2: [Type and description]

    Returns:
        [Type]: [Description of return value]

    Examples:
        >>> function_a(example_input_1)
        expected_output_1
        >>> function_a(example_input_2)
        expected_output_2
        >>> function_a(edge_case_input)
        edge_case_output
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{BLANK_2_TITLE}}
# ============================================================
# {{CONTEXT_BLANK_2_NARRATIVE}}

def function_b(parameters):
    """
    [Description]

    Examples:
        >>> function_b(input1)
        output1
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# [REPEAT PATTERN FOR MORE CHALLENGES]
# [ORGANIZE BY DIFFICULTY: EASY → MEDIUM → HARD → EXPERT]


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Run tests for all functions."""
    print("Testing your implementations...\n")

    # Test function_a
    print("{{BLANK_1_TITLE}}")
    # assert function_a(test_input) == expected_output, "Description of test"
    print("   ✓ Passed!\n")

    # Test function_b
    print("{{BLANK_2_TITLE}}")
    # assert function_b(test_input) == expected_output, "Description of test"
    print("   ✓ Passed!\n")

    print("=" * 40)
    print("All tests passed!")


def main():
    print("{{CONTEXT_BLANK_PAGE_INTRO}}")
    print("=" * 50)
    print()
    print("Implement each function based on its docstring.")
    print("When ready, run the tests to check your work.")
    print()

    # Uncomment to run tests after implementing:
    # run_tests()

    print("{{CONTEXT_MASTERY_COMPLETE}}")


main()


# =============================================================================
# CHALLENGE IDEAS BY DIFFICULTY:
# =============================================================================
#
# EASY (single concept):
#   - Return a value doubled/tripled
#   - Check if number is even/odd
#   - Return string in uppercase with punctuation
#   - Get first/last element of list
#   - Check if list is empty
#
# MEDIUM (combine concepts):
#   - Count occurrences of character in string
#   - Find largest/smallest in list
#   - Filter list by condition
#   - Reverse a string/list
#   - Check if palindrome (simple)
#
# HARD (algorithm required):
#   - FizzBuzz variations
#   - Find duplicates in list
#   - Group items by property
#   - Merge sorted lists
#   - Calculate running average
#
# EXPERT (complex logic):
#   - Validate balanced brackets
#   - Implement binary search
#   - Parse simple expressions
#   - Flatten nested structures
#   - Implement caching/memoization
#
# DOCSTRING BEST PRACTICES:
#   - Be specific about input types
#   - Show examples that cover normal + edge cases
#   - Mention if order matters in output
#   - Specify behavior for empty input
#   - Clarify if case-sensitive
#
# =============================================================================
