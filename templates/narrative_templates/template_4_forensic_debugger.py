"""
TEMPLATE 4: FORENSIC DEBUGGER
Purpose: Debug broken code by investigating error messages and tracing execution
Complexity: ⭐⭐ Moderate
Best for: decode_error and bug_hunt exercise types
"""

"""
{{CONTEXT_INVESTIGATION_INTRO}}

{{CONTEXT_INVESTIGATION_MISSION}}
"""

# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# ERROR MESSAGE:
# {{ERROR_MESSAGE_1}}
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}


def case_1_buggy():
    """
    {{CASE_1_DESCRIPTION}}

    This code has a bug! Don't run it yet - analyze first.
    """
    # 🐛 BUG: {{BUG_1_HINT}}

    # Intentionally buggy code here
    data = {"name": "{{hero}}", "level": 5}
    print(data["power"])  # Bug: key doesn't exist


# ✏️ FIX THE CODE ✏️
# {{CONTEXT_FIX_GUIDANCE_1}}

def case_1_fixed():
    """
    {{CASE_1_FIX_DESCRIPTION}}

    Fixed version of the buggy code above.
    """
    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# ERROR MESSAGE:
# {{ERROR_MESSAGE_2}}
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}


def case_2_buggy():
    """
    {{CASE_2_DESCRIPTION}}

    Another bug to investigate!
    """
    # 🐛 BUG: {{BUG_2_HINT}}

    # Intentionally buggy code here
    items = ["{{item}}", "{{item_2}}", "{{item_3}}"]
    for i in range(5):  # Bug: range too large for list
        print(items[i])


# ✏️ FIX THE CODE ✏️
# {{CONTEXT_FIX_GUIDANCE_2}}

def case_2_fixed():
    """
    {{CASE_2_FIX_DESCRIPTION}}

    Fixed version of the second bug.
    """
    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# ERROR MESSAGE:
# {{ERROR_MESSAGE_3}}
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}


def case_3_buggy():
    """
    {{CASE_3_DESCRIPTION}}

    Final bug to solve!
    """
    # 🐛 BUG: {{BUG_3_HINT}}

    # Intentionally buggy code here
    name = "{{hero}}"
    print(f"Welcome, {nane}!")  # Bug: typo in variable name


# ✏️ FIX THE CODE ✏️
# {{CONTEXT_FIX_GUIDANCE_3}}

def case_3_fixed():
    """
    {{CASE_3_FIX_DESCRIPTION}}

    Fixed version of the third bug.
    """
    pass


# ============================================================
# VERIFICATION
# ============================================================
# {{CONTEXT_VERIFICATION}}

def verify_fixes():
    """Test all fixed versions."""
    print("=" * 60)
    print("{{CONTEXT_VERIFICATION_START}}")
    print("=" * 60)
    print()

    print("{{CASE_1_LABEL}}")
    print("-" * 60)
    try:
        case_1_fixed()
        print("✅ {{CONTEXT_CASE_1_SUCCESS}}")
    except Exception as e:
        print(f"❌ Still has issues: {e}")
    print()

    print("{{CASE_2_LABEL}}")
    print("-" * 60)
    try:
        case_2_fixed()
        print("✅ {{CONTEXT_CASE_2_SUCCESS}}")
    except Exception as e:
        print(f"❌ Still has issues: {e}")
    print()

    print("{{CASE_3_LABEL}}")
    print("-" * 60)
    try:
        case_3_fixed()
        print("✅ {{CONTEXT_CASE_3_SUCCESS}}")
    except Exception as e:
        print(f"❌ Still has issues: {e}")
    print()

    print("=" * 60)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
    print("=" * 60)


def main():
    """Run verification of all fixes."""
    # Note: Don't run buggy versions - they'll crash!
    # Students should analyze, then write fixes, then run verify_fixes()

    # Uncomment when you've fixed all bugs:
    # verify_fixes()
    print("{{CONTEXT_VERIFICATION_INSTRUCTION}}")


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}      - Framing as investigation/debugging
# {{CONTEXT_INVESTIGATION_MISSION}}    - What needs to be fixed
#
# For each case (1-3):
# {{CASE_N_TITLE}}                     - Case heading
# {{CONTEXT_CASE_N_NARRATIVE}}         - Story behind the bug
# {{ERROR_MESSAGE_N}}                  - Actual error message shown
# {{CONTEXT_INVESTIGATION_PROMPT_N}}   - Questions to guide debugging
# {{CASE_N_DESCRIPTION}}               - Technical description of bug
# {{BUG_N_HINT}}                       - Hint about what's wrong
# {{CONTEXT_FIX_GUIDANCE_N}}           - How to approach the fix
# {{CASE_N_FIX_DESCRIPTION}}           - What the fix should do
# {{CASE_N_LABEL}}                     - Label for verification output
# {{CONTEXT_CASE_N_SUCCESS}}           - Success message
#
# Verification:
# {{CONTEXT_VERIFICATION}}             - Instructions for testing fixes
# {{CONTEXT_VERIFICATION_START}}       - Message when verification begins
# {{CONTEXT_INVESTIGATION_COMPLETE}}   - Message when all cases solved
# {{CONTEXT_VERIFICATION_INSTRUCTION}} - How to activate verification
#
# Note: Can have more or fewer than 3 cases. Adjust as needed.
