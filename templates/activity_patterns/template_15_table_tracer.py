"""
TEMPLATE 15: TABLE TRACER
Purpose: Track variable state changes in structured table format
Complexity: ⭐⭐ Moderate
Best for: code_tracing exercise type, debugging, state monitoring
"""

"""
{{CONTEXT_TRACE_INTRO}}

{{CONTEXT_TRACE_PURPOSE}}
"""

# ============================================================
# {{TRACE_SCENARIO_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_NARRATIVE}}
#
# ✏️ FILL IN THE TRACING TABLE ✏️
# {{CONTEXT_TRACE_TABLE}}
#
# {{CONTEXT_TRACE_INSTRUCTIONS}}
#
# TRACING TABLE:
# | Line | Code | {{VAR_1_NAME}} | {{VAR_2_NAME}} | {{VAR_3_NAME}} | Notes |
# |------|------|{{TRACE_HEADER_DASHES}}|
# | 1 | {{TRACE_LINE_1_CODE}} | {{TRACE_STEP_1_VAR1}} | {{TRACE_STEP_1_VAR2}} | {{TRACE_STEP_1_VAR3}} | {{TRACE_NOTE_1}} |
# | 2 | {{TRACE_LINE_2_CODE}} | {{TRACE_STEP_2_VAR1}} | {{TRACE_STEP_2_VAR2}} | {{TRACE_STEP_2_VAR3}} | {{TRACE_NOTE_2}} |
# | 3 | {{TRACE_LINE_3_CODE}} | {{TRACE_STEP_3_VAR1}} | {{TRACE_STEP_3_VAR2}} | {{TRACE_STEP_3_VAR3}} | {{TRACE_NOTE_3}} |
# | 4 | {{TRACE_LINE_4_CODE}} | {{TRACE_STEP_4_VAR1}} | {{TRACE_STEP_4_VAR2}} | {{TRACE_STEP_4_VAR3}} | {{TRACE_NOTE_4}} |
# | 5 | {{TRACE_LINE_5_CODE}} | {{TRACE_STEP_5_VAR1}} | {{TRACE_STEP_5_VAR2}} | {{TRACE_STEP_5_VAR3}} | {{TRACE_NOTE_5}} |
#
# {{CONTEXT_TRACE_GUIDANCE}}


def trace_scenario_1():
    """
    {{TRACE_SCENARIO_1_DESCRIPTION}}

    This is the code you'll trace through.
    """
    # Line 1
    data = {"name": "{{hero}}", "level": 1}

    # Line 2
    data["level"] = 5

    # Line 3
    data["power"] = 10

    # Line 4
    current_level = data["level"]

    # Line 5
    data["level"] = current_level + 3

    return data


# ============================================================
# {{TRACE_SCENARIO_2_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_2_NARRATIVE}}
#
# ✏️ FILL IN THE TRACING TABLE ✏️
#
# TRACING TABLE:
# | Line | Code | {{VAR2_1_NAME}} | {{VAR2_2_NAME}} | {{VAR2_3_NAME}} | Notes |
# |------|------|{{TRACE_2_HEADER_DASHES}}|
# | 1 | {{TRACE_2_LINE_1_CODE}} | {{TRACE_2_STEP_1_VAR1}} | {{TRACE_2_STEP_1_VAR2}} | {{TRACE_2_STEP_1_VAR3}} | {{TRACE_2_NOTE_1}} |
# | 2 | {{TRACE_2_LINE_2_CODE}} | {{TRACE_2_STEP_2_VAR1}} | {{TRACE_2_STEP_2_VAR2}} | {{TRACE_2_STEP_2_VAR3}} | {{TRACE_2_NOTE_2}} |
# | 3 | {{TRACE_2_LINE_3_CODE}} | {{TRACE_2_STEP_3_VAR1}} | {{TRACE_2_STEP_3_VAR2}} | {{TRACE_2_STEP_3_VAR3}} | {{TRACE_2_NOTE_3}} |
# | 4 | {{TRACE_2_LINE_4_CODE}} | {{TRACE_2_STEP_4_VAR1}} | {{TRACE_2_STEP_4_VAR2}} | {{TRACE_2_STEP_4_VAR3}} | {{TRACE_2_NOTE_4}} |
#
# {{CONTEXT_TRACE_2_GUIDANCE}}


def trace_scenario_2():
    """
    {{TRACE_SCENARIO_2_DESCRIPTION}}

    Another scenario to trace.
    """
    # Line 1
    items = ["{{item}}", "{{item_2}}"]

    # Line 2
    items.append("{{item_3}}")

    # Line 3
    first_item = items[0]

    # Line 4
    items[1] = "{{item_4}}"

    return items, first_item


# ============================================================
# {{TRACE_SCENARIO_3_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_3_NARRATIVE}}
#
# ✏️ FILL IN THE TRACING TABLE ✏️
#
# TRACING TABLE:
# | Line | Code | {{VAR3_1_NAME}} | {{VAR3_2_NAME}} | {{VAR3_3_NAME}} | Output | Notes |
# |------|------|{{TRACE_3_HEADER_DASHES}}|
# | 1 | {{TRACE_3_LINE_1_CODE}} | {{TRACE_3_STEP_1_VAR1}} | {{TRACE_3_STEP_1_VAR2}} | {{TRACE_3_STEP_1_VAR3}} | {{TRACE_3_STEP_1_OUT}} | {{TRACE_3_NOTE_1}} |
# | 2 | {{TRACE_3_LINE_2_CODE}} | {{TRACE_3_STEP_2_VAR1}} | {{TRACE_3_STEP_2_VAR2}} | {{TRACE_3_STEP_2_VAR3}} | {{TRACE_3_STEP_2_OUT}} | {{TRACE_3_NOTE_2}} |
# | 3 | {{TRACE_3_LINE_3_CODE}} | {{TRACE_3_STEP_3_VAR1}} | {{TRACE_3_STEP_3_VAR2}} | {{TRACE_3_STEP_3_VAR3}} | {{TRACE_3_STEP_3_OUT}} | {{TRACE_3_NOTE_3}} |
# | 4 | {{TRACE_3_LINE_4_CODE}} | {{TRACE_3_STEP_4_VAR1}} | {{TRACE_3_STEP_4_VAR2}} | {{TRACE_3_STEP_4_VAR3}} | {{TRACE_3_STEP_4_OUT}} | {{TRACE_3_NOTE_4}} |
# | 5 | {{TRACE_3_LINE_5_CODE}} | {{TRACE_3_STEP_5_VAR1}} | {{TRACE_3_STEP_5_VAR2}} | {{TRACE_3_STEP_5_VAR3}} | {{TRACE_3_STEP_5_OUT}} | {{TRACE_3_NOTE_5}} |
#
# {{CONTEXT_TRACE_3_GUIDANCE}}


def trace_scenario_3():
    """
    {{TRACE_SCENARIO_3_DESCRIPTION}}

    This one includes conditionals and output.
    """
    # Line 1
    score = 10

    # Line 2
    print(f"Starting score: {score}")

    # Line 3
    if score > 5:
        # Line 4
        score = score * 2
        # Line 5
        print(f"Bonus applied! New score: {score}")

    return score


# ============================================================
# VERIFICATION
# ============================================================
# {{CONTEXT_VERIFICATION}}


def verify_traces():
    """
    {{CONTEXT_VERIFICATION_NARRATIVE}}

    Run all scenarios and show actual execution.
    """
    print("=" * 60)
    print("{{CONTEXT_VERIFICATION_START}}")
    print("=" * 60)
    print()

    print("{{CONTEXT_VERIFICATION_INSTRUCTIONS}}")
    print()

    # Scenario 1
    print("{{TRACE_SCENARIO_1_LABEL}}")
    print("-" * 60)
    result1 = trace_scenario_1()
    print(f"{{CONTEXT_FINAL_STATE}}: {result1}")
    print()
    print("{{CONTEXT_REFLECTION_1}}")
    print()

    # Scenario 2
    print("{{TRACE_SCENARIO_2_LABEL}}")
    print("-" * 60)
    result2a, result2b = trace_scenario_2()
    print(f"{{CONTEXT_FINAL_STATE}}: items={result2a}, first_item={result2b}")
    print()
    print("{{CONTEXT_REFLECTION_2}}")
    print()

    # Scenario 3
    print("{{TRACE_SCENARIO_3_LABEL}}")
    print("-" * 60)
    result3 = trace_scenario_3()
    print(f"{{CONTEXT_FINAL_STATE}}: {result3}")
    print()
    print("{{CONTEXT_REFLECTION_3}}")
    print()

    print("=" * 60)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")
    print("=" * 60)


# ============================================================
# TRACING PRACTICE
# ============================================================


def practice_tracing():
    """
    {{CONTEXT_PRACTICE_DESCRIPTION}}

    Interactive practice mode.
    """
    print("=" * 60)
    print("{{CONTEXT_PRACTICE_START}}")
    print("=" * 60)
    print()

    print("{{CONTEXT_PRACTICE_INSTRUCTIONS}}")
    print()

    scenarios = [
        ("{{TRACE_SCENARIO_TITLE}}", trace_scenario_1),
        ("{{TRACE_SCENARIO_2_TITLE}}", trace_scenario_2),
        ("{{TRACE_SCENARIO_3_TITLE}}", trace_scenario_3)
    ]

    for i, (title, func) in enumerate(scenarios, 1):
        print(f"\n{i}. {title}")

    choice = input("\n{{CONTEXT_PRACTICE_PROMPT}} ")

    try:
        idx = int(choice) - 1
        if 0 <= idx < len(scenarios):
            title, func = scenarios[idx]
            print(f"\n{{CONTEXT_PRACTICE_SELECTED}}: {title}")
            print("-" * 60)
            print("{{CONTEXT_PRACTICE_TRACE_NOW}}")
            input("{{CONTEXT_PRACTICE_READY_PROMPT}}")

            print("\n{{CONTEXT_PRACTICE_EXECUTING}}")
            result = func()
            print(f"\n{{CONTEXT_FINAL_STATE}}: {result}")

            print("\n{{CONTEXT_PRACTICE_REFLECTION}}")
        else:
            print("{{CONTEXT_INVALID_CHOICE}}")
    except ValueError:
        print("{{CONTEXT_INVALID_INPUT}}")


def main():
    """Run tracing exercise."""
    print("{{CONTEXT_MAIN_WELCOME}}")
    print()
    print("1. {{CONTEXT_MODE_VERIFY}}")
    print("2. {{CONTEXT_MODE_PRACTICE}}")
    print()

    mode = input("{{CONTEXT_MODE_PROMPT}} ")

    if mode == "1":
        verify_traces()
    elif mode == "2":
        practice_tracing()
    else:
        print("{{CONTEXT_INVALID_MODE}}")


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_TRACE_INTRO}}              - Why tracing matters
# {{CONTEXT_TRACE_PURPOSE}}            - Skill being developed
#
# For each scenario (1-3):
# {{TRACE_SCENARIO_N_TITLE}}           - Scenario heading
# {{CONTEXT_TRACE_N_NARRATIVE}}        - Story behind scenario
# {{TRACE_SCENARIO_N_DESCRIPTION}}     - Technical description
# {{TRACE_SCENARIO_N_LABEL}}           - Label for verification output
# {{CONTEXT_TRACE_N_GUIDANCE}}         - Hints for tracing
# {{CONTEXT_REFLECTION_N}}             - Reflection prompt
#
# Table structure (per scenario):
# {{CONTEXT_TRACE_TABLE}}              - Instructions for table
# {{CONTEXT_TRACE_INSTRUCTIONS}}       - How to fill in table
# {{VAR_N_X_NAME}}                     - Variable names (columns)
# {{TRACE_N_HEADER_DASHES}}            - Dashes for table header
# {{TRACE_N_LINE_X_CODE}}              - Code being executed
# {{TRACE_N_STEP_X_VARY}}              - Variable value at step
# {{TRACE_N_STEP_X_OUT}}               - Output at step (if applicable)
# {{TRACE_N_NOTE_X}}                   - Note about what happened
#
# Verification:
# {{CONTEXT_VERIFICATION}}             - Instructions for verification
# {{CONTEXT_VERIFICATION_NARRATIVE}}   - How verification works
# {{CONTEXT_VERIFICATION_START}}       - Opening message
# {{CONTEXT_VERIFICATION_INSTRUCTIONS}} - How to use verification
# {{CONTEXT_FINAL_STATE}}              - Label for final state
# {{CONTEXT_VERIFICATION_COMPLETE}}    - Closing message
#
# Practice mode:
# {{CONTEXT_PRACTICE_DESCRIPTION}}     - What practice mode does
# {{CONTEXT_PRACTICE_START}}           - Opening message
# {{CONTEXT_PRACTICE_INSTRUCTIONS}}    - How to use practice mode
# {{CONTEXT_PRACTICE_PROMPT}}          - Prompt for selection
# {{CONTEXT_PRACTICE_SELECTED}}        - Selected message
# {{CONTEXT_PRACTICE_TRACE_NOW}}       - Instructions to trace
# {{CONTEXT_PRACTICE_READY_PROMPT}}    - Ready prompt
# {{CONTEXT_PRACTICE_EXECUTING}}       - Execution message
# {{CONTEXT_PRACTICE_REFLECTION}}      - Reflection prompt
#
# Main:
# {{CONTEXT_MAIN_WELCOME}}             - Welcome message
# {{CONTEXT_MODE_VERIFY}}              - Verify mode description
# {{CONTEXT_MODE_PRACTICE}}            - Practice mode description
# {{CONTEXT_MODE_PROMPT}}              - Mode selection prompt
# {{CONTEXT_INVALID_CHOICE}}           - Invalid choice message
# {{CONTEXT_INVALID_INPUT}}            - Invalid input message
# {{CONTEXT_INVALID_MODE}}             - Invalid mode message
#
# Note: This template has the most context blocks due to detailed table structure.
# Can simplify by using fewer scenarios or less detailed tables.
