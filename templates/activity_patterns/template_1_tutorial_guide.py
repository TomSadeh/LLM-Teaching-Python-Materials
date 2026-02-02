"""
TEMPLATE 1: TUTORIAL GUIDE
Purpose: Teach new concept by showing complete example, then asking student to replicate
Complexity: ⭐ Simple
Best for: Introducing new concepts, first exercises in a module
"""

# {{CONTEXT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}

# ============================================================
# EXAMPLE: {{EXAMPLE_TITLE}}
# ============================================================
# {{CONTEXT_EXAMPLE_NARRATIVE}}
#
# Study this complete working example:

def example_function():
    """
    Complete working example demonstrating the concept.

    This docstring should explain WHAT the code does (technical),
    not the narrative context (that's in CONTEXT_EXAMPLE_NARRATIVE).
    """
    # Example implementation here
    # Shows best practices for the concept
    example_data = {
        "key1": "value1",
        "key2": "value2"
    }

    # Demonstrate the technique
    for key, value in example_data.items():
        print(f"{key}: {value}")

    return example_data


# ============================================================
# ✏️ YOUR TURN ✏️
# ============================================================
# {{CONTEXT_STUDENT_TASK}}
#
# {{CONTEXT_SUCCESS_CRITERIA}}

def student_function():
    """
    {{TASK_DESCRIPTION}}

    Args:
        (if applicable)

    Returns:
        (if applicable)

    Example:
        >>> student_function()
        (expected behavior)
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# VERIFICATION
# ============================================================
# {{CONTEXT_VERIFICATION}}

def main():
    """Run both example and student solution."""
    print("=" * 50)
    print("{{CONTEXT_EXAMPLE_LABEL}}")
    print("=" * 50)
    example_function()

    print("\n" + "=" * 50)
    print("{{CONTEXT_STUDENT_LABEL}}")
    print("=" * 50)
    student_function()

    print("\n{{CONTEXT_COMPLETION_MESSAGE}}")


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# The following context blocks should be defined in theme_variables.json:
#
# {{CONTEXT_INTRO}}                - Opening that places student in learning situation
# {{CONTEXT_LEARNING_OBJECTIVE}}   - What they'll learn from this exercise
# {{EXAMPLE_TITLE}}                - Name/title of the example being shown
# {{CONTEXT_EXAMPLE_NARRATIVE}}    - Story explaining the example's context
# {{CONTEXT_STUDENT_TASK}}         - Instructions for student's replication task
# {{CONTEXT_SUCCESS_CRITERIA}}     - How student knows they succeeded
# {{TASK_DESCRIPTION}}             - Technical description of what to implement
# {{CONTEXT_VERIFICATION}}         - How to check if solution is correct
# {{CONTEXT_EXAMPLE_LABEL}}        - Label for example output section
# {{CONTEXT_STUDENT_LABEL}}        - Label for student output section
# {{CONTEXT_COMPLETION_MESSAGE}}   - Closing message when exercise complete
#
# Plus standard entity placeholders:
# {{hero}}, {{mentor}}, {{school}}, {{item}}, {{spell1}}, etc.
