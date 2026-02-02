"""
TEMPLATE 5: COMPARISON ANALYST
Purpose: Compare two approaches and analyze tradeoffs
Complexity: ⭐⭐⭐ Advanced
Best for: which_is_better exercise type, developing critical thinking
"""

"""
{{CONTEXT_COMPARISON_INTRO}}

{{CONTEXT_COMPARISON_DECISION}}
"""

# ============================================================
# {{APPROACH_1_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_1_NARRATIVE}}
#
# {{CONTEXT_APPROACH_1_RATIONALE}}


def approach_1_example():
    """
    {{APPROACH_1_DESCRIPTION}}

    This approach prioritizes [trait 1].
    """
    # Implementation of first approach
    # Should be complete and functional
    data = {
        "item1": "value1",
        "item2": "value2"
    }

    # Demonstrate approach 1 technique
    result = data.get("item1", "default")
    print(f"Result: {result}")

    return data


# ============================================================
# {{APPROACH_2_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_2_NARRATIVE}}
#
# {{CONTEXT_APPROACH_2_RATIONALE}}


def approach_2_example():
    """
    {{APPROACH_2_DESCRIPTION}}

    This approach prioritizes [trait 2].
    """
    # Implementation of second approach
    # Should be complete and functional
    # Accomplishes same goal differently
    data = {
        "items": {
            "item1": "value1",
            "item2": "value2"
        }
    }

    # Demonstrate approach 2 technique
    result = data["items"]["item1"]
    print(f"Result: {result}")

    return data


# ============================================================
# ✏️ YOUR ANALYSIS ✏️
# ============================================================
# {{CONTEXT_ANALYSIS_PROMPT}}
#
# Questions to consider:
#
# 1. {{ANALYSIS_QUESTION_1}}
# {{CONTEXT_QUESTION_1_GUIDANCE}}
#
# 2. {{ANALYSIS_QUESTION_2}}
# {{CONTEXT_QUESTION_2_GUIDANCE}}
#
# 3. {{ANALYSIS_QUESTION_3}}
# {{CONTEXT_QUESTION_3_GUIDANCE}}
#
# 4. {{ANALYSIS_QUESTION_4}}
# {{CONTEXT_QUESTION_4_GUIDANCE}}
#
# Which approach do you prefer and why?
# {{CONTEXT_DECISION_GUIDANCE}}
#
# ✏️ Write your analysis here as comments:
#
# My analysis:
# I prefer [Approach 1 / Approach 2] because...
#
# Strengths of my chosen approach:
# 1.
# 2.
# 3.
#
# Weaknesses of my chosen approach:
# 1.
# 2.
#
# When I might use the OTHER approach instead:
# -
#


# ============================================================
# COMPARISON DEMONSTRATION
# ============================================================
# {{CONTEXT_DEMONSTRATION}}

def demonstrate_both():
    """Run both approaches side-by-side for comparison."""
    print("=" * 60)
    print("{{CONTEXT_DEMONSTRATION_START}}")
    print("=" * 60)
    print()

    print("{{APPROACH_1_LABEL}}")
    print("-" * 60)
    approach_1_example()
    print()

    print("{{APPROACH_2_LABEL}}")
    print("-" * 60)
    approach_2_example()
    print()

    print("=" * 60)
    print("{{CONTEXT_ANALYSIS_REMINDER}}")
    print("=" * 60)


def main():
    """Run demonstration and prompt for analysis."""
    demonstrate_both()

    print("\n{{CONTEXT_REFLECTION_PROMPT}}")


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_COMPARISON_INTRO}}       - Why comparison matters
# {{CONTEXT_COMPARISON_DECISION}}    - What decision needs to be made
#
# For each approach (1-2):
# {{APPROACH_N_NAME}}                - Name of approach
# {{CONTEXT_APPROACH_N_NARRATIVE}}   - Story explaining approach
# {{CONTEXT_APPROACH_N_RATIONALE}}   - Why someone might choose this
# {{APPROACH_N_DESCRIPTION}}         - Technical description
# {{APPROACH_N_LABEL}}               - Label for demonstration output
#
# Analysis:
# {{CONTEXT_ANALYSIS_PROMPT}}        - How to think about tradeoffs
# {{ANALYSIS_QUESTION_N}}            - Specific analysis questions (4 total)
# {{CONTEXT_QUESTION_N_GUIDANCE}}    - Hints for each question
# {{CONTEXT_DECISION_GUIDANCE}}      - Criteria for good decision
#
# Demonstration:
# {{CONTEXT_DEMONSTRATION}}          - Purpose of side-by-side demo
# {{CONTEXT_DEMONSTRATION_START}}    - Opening message
# {{CONTEXT_ANALYSIS_REMINDER}}      - Reminder to complete analysis
# {{CONTEXT_REFLECTION_PROMPT}}      - Final reflection prompt
#
# Note: Can compare more than 2 approaches if needed.
