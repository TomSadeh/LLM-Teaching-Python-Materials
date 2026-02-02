"""
TEMPLATE 13: DECISION TREE
Purpose: Branch through multiple conditional paths based on choices/conditions
Complexity: ⭐⭐ Moderate
Best for: Conditionals, dialog trees, RPG choice systems, classification logic
"""

"""
{{CONTEXT_DECISION_INTRO}}

{{CONTEXT_DECISION_SCENARIO}}
"""

# ============================================================
# {{DECISION_POINT_1_TITLE}}
# ============================================================
# {{CONTEXT_DECISION_POINT_1_NARRATIVE}}


def decision_point_1(choice):
    """
    {{DECISION_POINT_1_DESCRIPTION}}

    Args:
        choice (str): {{DECISION_POINT_1_CHOICE_PARAM}}

    Returns:
        str: {{DECISION_POINT_1_RETURN}}

    {{CONTEXT_DECISION_POINT_1_OPTIONS}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Use if/elif/else to handle different choices
    # Return outcome based on choice
    pass


# ============================================================
# {{DECISION_POINT_2_TITLE}}
# ============================================================
# {{CONTEXT_DECISION_POINT_2_NARRATIVE}}


def decision_point_2(choice, previous_outcome):
    """
    {{DECISION_POINT_2_DESCRIPTION}}

    Args:
        choice (str): {{DECISION_POINT_2_CHOICE_PARAM}}
        previous_outcome (str): {{DECISION_POINT_2_PREVIOUS_PARAM}}

    Returns:
        str: {{DECISION_POINT_2_RETURN}}

    {{CONTEXT_DECISION_POINT_2_OPTIONS}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # This decision may depend on previous outcome
    # Use nested conditionals if needed
    pass


# ============================================================
# {{DECISION_POINT_3_TITLE}}
# ============================================================
# {{CONTEXT_DECISION_POINT_3_NARRATIVE}}


def decision_point_3(choice, previous_outcomes):
    """
    {{DECISION_POINT_3_DESCRIPTION}}

    Args:
        choice (str): {{DECISION_POINT_3_CHOICE_PARAM}}
        previous_outcomes (list): {{DECISION_POINT_3_PREVIOUS_PARAM}}

    Returns:
        str: {{DECISION_POINT_3_RETURN}}

    {{CONTEXT_DECISION_POINT_3_OPTIONS}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Final decision may consider all previous outcomes
    pass


# ============================================================
# {{FINAL_OUTCOME_TITLE}}
# ============================================================
# {{CONTEXT_FINAL_OUTCOME_NARRATIVE}}


def determine_final_outcome(all_outcomes):
    """
    {{FINAL_OUTCOME_DESCRIPTION}}

    Args:
        all_outcomes (list): {{FINAL_OUTCOME_PARAM}}

    Returns:
        str: {{FINAL_OUTCOME_RETURN}}

    {{CONTEXT_FINAL_OUTCOME_LOGIC}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Analyze all decisions made
    # Determine final result/classification
    # Return final outcome
    pass


# ============================================================
# DECISION TREE TRAVERSAL
# ============================================================


def traverse_decision_tree():
    """
    {{CONTEXT_TRAVERSAL_DESCRIPTION}}

    Walk through the complete decision tree with user input.
    """
    print("=" * 60)
    print("{{CONTEXT_TRAVERSAL_START}}")
    print("=" * 60)
    print()

    outcomes = []

    # Decision Point 1
    print("{{DECISION_POINT_1_PROMPT}}")
    print("-" * 60)
    print("{{CONTEXT_DECISION_1_CHOICES}}")
    choice1 = input("{{CONTEXT_DECISION_1_INPUT_PROMPT}} ")
    outcome1 = decision_point_1(choice1)
    if outcome1:
        print(f"\n{{CONTEXT_OUTCOME_LABEL}}: {outcome1}")
        outcomes.append(outcome1)
    print()

    # Decision Point 2
    print("{{DECISION_POINT_2_PROMPT}}")
    print("-" * 60)
    print("{{CONTEXT_DECISION_2_CHOICES}}")
    choice2 = input("{{CONTEXT_DECISION_2_INPUT_PROMPT}} ")
    outcome2 = decision_point_2(choice2, outcomes[0] if outcomes else None)
    if outcome2:
        print(f"\n{{CONTEXT_OUTCOME_LABEL}}: {outcome2}")
        outcomes.append(outcome2)
    print()

    # Decision Point 3
    print("{{DECISION_POINT_3_PROMPT}}")
    print("-" * 60)
    print("{{CONTEXT_DECISION_3_CHOICES}}")
    choice3 = input("{{CONTEXT_DECISION_3_INPUT_PROMPT}} ")
    outcome3 = decision_point_3(choice3, outcomes)
    if outcome3:
        print(f"\n{{CONTEXT_OUTCOME_LABEL}}: {outcome3}")
        outcomes.append(outcome3)
    print()

    # Final Outcome
    print("=" * 60)
    print("{{CONTEXT_FINAL_OUTCOME_LABEL}}")
    print("=" * 60)
    final = determine_final_outcome(outcomes)
    if final:
        print(final)

    print()
    print("{{CONTEXT_TRAVERSAL_COMPLETE}}")


# ============================================================
# AUTOMATED TEST PATH
# ============================================================


def test_decision_path(path):
    """
    Test a specific decision path without user input.

    Args:
        path (list): List of choices to make at each decision point

    {{CONTEXT_TEST_PATH_PURPOSE}}
    """
    print(f"Testing path: {path}")
    print("-" * 60)

    outcomes = []

    if len(path) >= 1:
        outcome1 = decision_point_1(path[0])
        if outcome1:
            outcomes.append(outcome1)
            print(f"Decision 1 ({path[0]}): {outcome1}")

    if len(path) >= 2:
        outcome2 = decision_point_2(path[1], outcomes[0] if outcomes else None)
        if outcome2:
            outcomes.append(outcome2)
            print(f"Decision 2 ({path[1]}): {outcome2}")

    if len(path) >= 3:
        outcome3 = decision_point_3(path[2], outcomes)
        if outcome3:
            outcomes.append(outcome3)
            print(f"Decision 3 ({path[2]}): {outcome3}")

    final = determine_final_outcome(outcomes)
    if final:
        print(f"\nFinal outcome: {final}")

    print()


def main():
    """Run decision tree traversal or tests."""
    print("{{CONTEXT_TREE_WELCOME}}")
    print()

    mode = input("{{CONTEXT_MODE_PROMPT}}")

    if mode == "1":
        # Interactive mode
        traverse_decision_tree()
    else:
        # Test mode - run predefined paths
        print("\n{{CONTEXT_TEST_MODE_START}}")
        print("=" * 60)
        print()

        test_paths = [
            ["{{TEST_PATH_1_C1}}", "{{TEST_PATH_1_C2}}", "{{TEST_PATH_1_C3}}"],
            ["{{TEST_PATH_2_C1}}", "{{TEST_PATH_2_C2}}", "{{TEST_PATH_2_C3}}"],
            ["{{TEST_PATH_3_C1}}", "{{TEST_PATH_3_C2}}", "{{TEST_PATH_3_C3}}"],
        ]

        for i, path in enumerate(test_paths, 1):
            print(f"{{CONTEXT_TEST_PATH_LABEL}} {i}")
            test_decision_path(path)


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_DECISION_INTRO}}           - Why decision trees matter
# {{CONTEXT_DECISION_SCENARIO}}        - The scenario/story setup
#
# For each decision point (1-3):
# {{DECISION_POINT_N_TITLE}}           - Decision heading
# {{CONTEXT_DECISION_POINT_N_NARRATIVE}} - Story behind decision
# {{DECISION_POINT_N_DESCRIPTION}}     - Technical description
# {{DECISION_POINT_N_CHOICE_PARAM}}    - Choice parameter description
# {{DECISION_POINT_N_PREVIOUS_PARAM}}  - Previous outcome parameter (if applicable)
# {{DECISION_POINT_N_RETURN}}          - Return value description
# {{CONTEXT_DECISION_POINT_N_OPTIONS}} - Available options/choices
# {{DECISION_POINT_N_PROMPT}}          - Prompt shown to user
# {{CONTEXT_DECISION_N_CHOICES}}       - Display of available choices
# {{CONTEXT_DECISION_N_INPUT_PROMPT}}  - Input prompt text
#
# Final outcome:
# {{FINAL_OUTCOME_TITLE}}              - Final outcome heading
# {{CONTEXT_FINAL_OUTCOME_NARRATIVE}}  - Story behind final determination
# {{FINAL_OUTCOME_DESCRIPTION}}        - Technical description
# {{FINAL_OUTCOME_PARAM}}              - All outcomes parameter
# {{FINAL_OUTCOME_RETURN}}             - Return value description
# {{CONTEXT_FINAL_OUTCOME_LOGIC}}      - Logic for determining outcome
# {{CONTEXT_FINAL_OUTCOME_LABEL}}      - Label for final outcome display
#
# Traversal:
# {{CONTEXT_TRAVERSAL_DESCRIPTION}}    - What traversal does
# {{CONTEXT_TRAVERSAL_START}}          - Opening message
# {{CONTEXT_OUTCOME_LABEL}}            - Label for each outcome
# {{CONTEXT_TRAVERSAL_COMPLETE}}       - Closing message
#
# Testing:
# {{CONTEXT_TEST_PATH_PURPOSE}}        - Purpose of automated testing
# {{CONTEXT_TREE_WELCOME}}             - Welcome message
# {{CONTEXT_MODE_PROMPT}}              - Prompt for selecting mode
# {{CONTEXT_TEST_MODE_START}}          - Test mode opening
# {{CONTEXT_TEST_PATH_LABEL}}          - Label for test path
# {{TEST_PATH_N_CX}}                   - Test path choices (3 paths, 3 choices each)
#
# Note: Can have more or fewer decision points. Adjust as needed.
