"""
TEMPLATE 6: SPECIFICATION IMPLEMENTER
Purpose: Implement functionality from comprehensive specifications (like real-world development)
Complexity: ⭐⭐ Moderate
Best for: complete_function and blank_page exercise types
"""

"""
{{CONTEXT_SPEC_INTRO}}

{{CONTEXT_SPEC_SOURCE}}
"""

# ============================================================
# SPECIFICATION: {{COMPONENT_NAME}}
# ============================================================
# {{CONTEXT_SPEC_NARRATIVE}}
#
# Requirements:
# {{REQUIREMENT_1}}
# {{REQUIREMENT_2}}
# {{REQUIREMENT_3}}
# {{REQUIREMENT_4}}
#
# {{CONTEXT_SPEC_CONSTRAINTS}}
#
# {{CONTEXT_SPEC_ACCEPTANCE}}


def implement_spec(param1, param2, param3=None):
    """
    {{SPEC_SUMMARY}}

    Args:
        param1 (type): {{PARAM_1_DESCRIPTION}}
        param2 (type): {{PARAM_2_DESCRIPTION}}
        param3 (type, optional): {{PARAM_3_DESCRIPTION}}. Defaults to None.

    Returns:
        type: {{RETURN_SPEC}}

    Raises:
        ExceptionType: {{EXCEPTION_SPEC}}

    Examples:
        {{EXAMPLE_1}}
        {{EXAMPLE_2}}
        {{EXAMPLE_3}}

    {{CONTEXT_IMPLEMENTATION_GUIDANCE}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Suggested approach:
    # 1. Validate inputs
    # 2. Initialize data structures
    # 3. Perform main logic
    # 4. Return result
    pass


# ============================================================
# SPECIFICATION: {{COMPONENT_NAME_2}}
# ============================================================
# {{CONTEXT_SPEC_NARRATIVE_2}}
#
# Requirements:
# {{REQUIREMENT_2_1}}
# {{REQUIREMENT_2_2}}
# {{REQUIREMENT_2_3}}
#
# {{CONTEXT_SPEC_CONSTRAINTS_2}}


def implement_spec_2(param1):
    """
    {{SPEC_SUMMARY_2}}

    Args:
        param1 (type): {{PARAM_2_1_DESCRIPTION}}

    Returns:
        type: {{RETURN_SPEC_2}}

    Examples:
        {{EXAMPLE_2_1}}
        {{EXAMPLE_2_2}}

    {{CONTEXT_IMPLEMENTATION_GUIDANCE_2}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# TEST CASES
# ============================================================
# {{CONTEXT_TESTING}}


def test_implementations():
    """
    {{CONTEXT_TEST_NARRATIVE}}

    Run this after implementing both functions.
    """
    print("=" * 60)
    print("{{CONTEXT_TEST_START}}")
    print("=" * 60)
    print()

    # Test Case 1: {{TEST_CASE_1_DESCRIPTION}}
    print("{{TEST_CASE_1_LABEL}}")
    print("-" * 60)
    try:
        result1 = implement_spec("test_value_1", "test_value_2")
        print(f"✅ Result: {result1}")
        print(f"{{CONTEXT_TEST_1_EXPECTED}}")
    except Exception as e:
        print(f"❌ Error: {e}")
    print()

    # Test Case 2: {{TEST_CASE_2_DESCRIPTION}}
    print("{{TEST_CASE_2_LABEL}}")
    print("-" * 60)
    try:
        result2 = implement_spec("edge_case_value", "edge_case_value_2")
        print(f"✅ Result: {result2}")
        print(f"{{CONTEXT_TEST_2_EXPECTED}}")
    except Exception as e:
        print(f"❌ Error: {e}")
    print()

    # Test Case 3: {{TEST_CASE_3_DESCRIPTION}}
    print("{{TEST_CASE_3_LABEL}}")
    print("-" * 60)
    try:
        result3 = implement_spec_2("test_value")
        print(f"✅ Result: {result3}")
        print(f"{{CONTEXT_TEST_3_EXPECTED}}")
    except Exception as e:
        print(f"❌ Error: {e}")
    print()

    print("=" * 60)
    print("{{CONTEXT_TEST_COMPLETE}}")
    print("=" * 60)


def main():
    """Run test suite."""
    # Uncomment when ready to test:
    # test_implementations()
    print("{{CONTEXT_TEST_INSTRUCTION}}")


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_SPEC_INTRO}}               - Why specifications matter
# {{CONTEXT_SPEC_SOURCE}}              - Who wrote the spec and why
#
# For each component (1-2):
# {{COMPONENT_NAME}}                   - Name of component/function
# {{CONTEXT_SPEC_NARRATIVE}}           - Story context for component
# {{REQUIREMENT_N}}                    - Individual requirements (4 per component)
# {{CONTEXT_SPEC_CONSTRAINTS}}         - Limitations or considerations
# {{CONTEXT_SPEC_ACCEPTANCE}}          - How success is measured
# {{SPEC_SUMMARY}}                     - One-line technical summary
# {{PARAM_N_DESCRIPTION}}              - Description of each parameter
# {{RETURN_SPEC}}                      - What function returns
# {{EXCEPTION_SPEC}}                   - What exceptions might be raised
# {{EXAMPLE_N}}                        - Usage examples
# {{CONTEXT_IMPLEMENTATION_GUIDANCE}}  - Tips for implementation
#
# Testing:
# {{CONTEXT_TESTING}}                  - Purpose of test suite
# {{CONTEXT_TEST_NARRATIVE}}           - How testing works
# {{CONTEXT_TEST_START}}               - Opening message
# {{TEST_CASE_N_DESCRIPTION}}          - What each test case checks
# {{TEST_CASE_N_LABEL}}                - Label for test output
# {{CONTEXT_TEST_N_EXPECTED}}          - Expected result description
# {{CONTEXT_TEST_COMPLETE}}            - All tests complete message
# {{CONTEXT_TEST_INSTRUCTION}}         - How to activate tests
