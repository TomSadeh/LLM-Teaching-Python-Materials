"""
TEMPLATE 10: QUALITY AUDITOR
Purpose: Identify and fix style/quality issues in working code
Complexity: ⭐⭐ Moderate
Best for: fix_style and simplify_code exercise types
"""

"""
{{CONTEXT_AUDIT_INTRO}}

{{CONTEXT_AUDIT_STANDARDS}}
"""

# ============================================================
# {{CODE_SAMPLE_1_TITLE}} - NEEDS IMPROVEMENT
# ============================================================
# {{CONTEXT_CODE_SAMPLE_1_NARRATIVE}}
#
# {{CONTEXT_ISSUES_FOUND_1}}
#
# Issues to fix:
# 1. {{ISSUE_1_1}} - {{ISSUE_1_1_EXPLANATION}}
# 2. {{ISSUE_1_2}} - {{ISSUE_1_2_EXPLANATION}}
# 3. {{ISSUE_1_3}} - {{ISSUE_1_3_EXPLANATION}}
# 4. {{ISSUE_1_4}} - {{ISSUE_1_4_EXPLANATION}}


def original_code_1():
    """
    {{ORIGINAL_CODE_1_DESCRIPTION}}

    This code WORKS but has style/quality issues.
    """
    # Poorly styled code here (but functional!)
    x = {"name": "{{hero}}", "p": 10}  # Bad: unclear variable names
    print(x["name"] + " has power " + str(x["p"]))  # Bad: string concatenation
    if x["p"] > 5:  # Bad: magic number
        print("strong")


# ✏️ YOUR IMPROVED VERSION ✏️
# {{CONTEXT_IMPROVEMENT_GUIDANCE_1}}


def improved_code_1():
    """
    {{IMPROVED_CODE_1_DESCRIPTION}}

    Same functionality, better style.
    """
    pass


# ============================================================
# {{CODE_SAMPLE_2_TITLE}} - NEEDS IMPROVEMENT
# ============================================================
# {{CONTEXT_CODE_SAMPLE_2_NARRATIVE}}
#
# {{CONTEXT_ISSUES_FOUND_2}}
#
# Issues to fix:
# 1. {{ISSUE_2_1}} - {{ISSUE_2_1_EXPLANATION}}
# 2. {{ISSUE_2_2}} - {{ISSUE_2_2_EXPLANATION}}
# 3. {{ISSUE_2_3}} - {{ISSUE_2_3_EXPLANATION}}


def original_code_2():
    """
    {{ORIGINAL_CODE_2_DESCRIPTION}}

    Functional but needs refactoring.
    """
    # Verbose/repetitive code (but works!)
    items = ["{{item}}", "{{item_2}}", "{{item_3}}"]

    if "{{item}}" in items:
        print("Found {{item}}")
    else:
        print("{{item}} not found")

    if "{{item_2}}" in items:
        print("Found {{item_2}}")
    else:
        print("{{item_2}} not found")

    if "{{item_3}}" in items:
        print("Found {{item_3}}")
    else:
        print("{{item_3}} not found")


# ✏️ YOUR IMPROVED VERSION ✏️
# {{CONTEXT_IMPROVEMENT_GUIDANCE_2}}


def improved_code_2():
    """
    {{IMPROVED_CODE_2_DESCRIPTION}}

    Same functionality, more concise.
    """
    pass


# ============================================================
# {{CODE_SAMPLE_3_TITLE}} - NEEDS IMPROVEMENT
# ============================================================
# {{CONTEXT_CODE_SAMPLE_3_NARRATIVE}}
#
# {{CONTEXT_ISSUES_FOUND_3}}
#
# Issues to fix:
# 1. {{ISSUE_3_1}} - {{ISSUE_3_1_EXPLANATION}}
# 2. {{ISSUE_3_2}} - {{ISSUE_3_2_EXPLANATION}}
# 3. {{ISSUE_3_3}} - {{ISSUE_3_3_EXPLANATION}}


def original_code_3():
    """
    {{ORIGINAL_CODE_3_DESCRIPTION}}

    Works but has maintainability issues.
    """
    # Hard to maintain code (but functional!)
    data = {"n": "{{hero}}", "l": 5, "h": 100, "m": 50}
    print(data["n"], data["l"], data["h"], data["m"])

    data["l"] = data["l"] + 1
    data["h"] = data["h"] - 10
    data["m"] = data["m"] + 5


# ✏️ YOUR IMPROVED VERSION ✏️
# {{CONTEXT_IMPROVEMENT_GUIDANCE_3}}


def improved_code_3():
    """
    {{IMPROVED_CODE_3_DESCRIPTION}}

    Same functionality, better maintainability.
    """
    pass


# ============================================================
# COMPARISON
# ============================================================
# {{CONTEXT_COMPARISON}}


def compare_versions(sample_num):
    """
    Run both original and improved versions side-by-side.

    Args:
        sample_num (int): Which code sample to compare (1, 2, or 3)
    """
    print("=" * 60)
    print(f"{{CONTEXT_COMPARISON_TITLE}} {sample_num}")
    print("=" * 60)
    print()

    if sample_num == 1:
        print("{{CONTEXT_ORIGINAL_LABEL}}")
        print("-" * 60)
        original_code_1()
        print()

        print("{{CONTEXT_IMPROVED_LABEL}}")
        print("-" * 60)
        improved_code_1()

    elif sample_num == 2:
        print("{{CONTEXT_ORIGINAL_LABEL}}")
        print("-" * 60)
        original_code_2()
        print()

        print("{{CONTEXT_IMPROVED_LABEL}}")
        print("-" * 60)
        improved_code_2()

    elif sample_num == 3:
        print("{{CONTEXT_ORIGINAL_LABEL}}")
        print("-" * 60)
        original_code_3()
        print()

        print("{{CONTEXT_IMPROVED_LABEL}}")
        print("-" * 60)
        improved_code_3()

    print()
    print("{{CONTEXT_COMPARISON_REFLECTION}}")


def main():
    """Compare all original vs improved versions."""
    print("=" * 60)
    print("{{CONTEXT_AUDIT_START}}")
    print("=" * 60)
    print()

    print("{{CONTEXT_AUDIT_INSTRUCTIONS}}")
    print()

    # Uncomment to compare each sample after improving:
    # compare_versions(1)
    # print()
    # compare_versions(2)
    # print()
    # compare_versions(3)

    print("=" * 60)
    print("{{CONTEXT_AUDIT_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_AUDIT_INTRO}}              - Why code quality matters
# {{CONTEXT_AUDIT_STANDARDS}}          - What standards to apply
#
# For each code sample (1-3):
# {{CODE_SAMPLE_N_TITLE}}              - Sample heading
# {{CONTEXT_CODE_SAMPLE_N_NARRATIVE}}  - Where this code came from
# {{CONTEXT_ISSUES_FOUND_N}}           - Overview of problems
# {{ISSUE_N_X}}                        - Issue description (4 issues per sample)
# {{ISSUE_N_X_EXPLANATION}}            - Why it's a problem
# {{ORIGINAL_CODE_N_DESCRIPTION}}      - What original code does
# {{CONTEXT_IMPROVEMENT_GUIDANCE_N}}   - Tips for improvement
# {{IMPROVED_CODE_N_DESCRIPTION}}      - What improved version should do
#
# Comparison:
# {{CONTEXT_COMPARISON}}               - Purpose of comparison
# {{CONTEXT_COMPARISON_TITLE}}         - Comparison heading
# {{CONTEXT_ORIGINAL_LABEL}}           - Label for original code output
# {{CONTEXT_IMPROVED_LABEL}}           - Label for improved code output
# {{CONTEXT_COMPARISON_REFLECTION}}    - Reflection prompt
#
# Audit execution:
# {{CONTEXT_AUDIT_START}}              - Opening message
# {{CONTEXT_AUDIT_INSTRUCTIONS}}       - How to use the exercise
# {{CONTEXT_AUDIT_COMPLETE}}           - Closing message
#
# Note: Can have more or fewer than 3 code samples. Adjust as needed.
