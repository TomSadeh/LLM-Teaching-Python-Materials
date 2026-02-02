"""
TEMPLATE 7: PREDICTION CHALLENGER
Purpose: Test understanding by predicting code output before running
Complexity: ⭐ Simple
Best for: output_prediction exercise type
"""

"""
{{CONTEXT_PREDICTION_INTRO}}

{{CONTEXT_PREDICTION_PURPOSE}}
"""

# ============================================================
# {{CHALLENGE_1_TITLE}}
# ============================================================
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}
#
# ✏️ YOUR PREDICTION ✏️
# What will this code print? Write your answer below BEFORE running it:
#
# Predicted output:
# Line 1:
# Line 2:
# Line 3:
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}


def challenge_1():
    """
    {{CHALLENGE_1_DESCRIPTION}}

    Read the code carefully. Predict the output.
    """
    data = {"name": "{{hero}}", "level": 5}
    print(f"Welcome, {data['name']}!")
    data["level"] = 10
    print(f"Level up! New level: {data['level']}")
    print(f"Status: {data}")


# ============================================================
# {{CHALLENGE_2_TITLE}}
# ============================================================
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}
#
# ✏️ YOUR PREDICTION ✏️
# What will this code print? Write your answer below BEFORE running it:
#
# Predicted output:
# Line 1:
# Line 2:
# Line 3:
# Line 4:
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}


def challenge_2():
    """
    {{CHALLENGE_2_DESCRIPTION}}

    Pay attention to how values change.
    """
    items = ["{{item}}", "{{item_2}}", "{{item_3}}"]
    print(f"Inventory: {items}")
    items.append("{{item_4}}")
    print(f"Added item! Now: {items}")
    first_item = items[0]
    print(f"First item: {first_item}")
    print(f"Total items: {len(items)}")


# ============================================================
# {{CHALLENGE_3_TITLE}}
# ============================================================
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}
#
# ✏️ YOUR PREDICTION ✏️
# What will this code print? Write your answer below BEFORE running it:
#
# Predicted output:
# Line 1:
# Line 2:
# Line 3:
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}


def challenge_3():
    """
    {{CHALLENGE_3_DESCRIPTION}}

    Think about conditionals carefully.
    """
    power = 15
    if power > 10:
        print("{{CONTEXT_CONDITION_TRUE}}")
    else:
        print("{{CONTEXT_CONDITION_FALSE}}")

    power = power + 5
    print(f"Current power: {power}")

    if power >= 20:
        print("{{CONTEXT_THRESHOLD_MET}}")


# ============================================================
# {{CHALLENGE_4_TITLE}}
# ============================================================
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}
#
# ✏️ YOUR PREDICTION ✏️
# What will this code print? Write your answer below BEFORE running it:
#
# Predicted output:
# Line 1:
# Line 2:
# Line 3:
# Line 4:
#
# {{CONTEXT_PREDICTION_GUIDANCE_4}}


def challenge_4():
    """
    {{CHALLENGE_4_DESCRIPTION}}

    Loops can be tricky - trace carefully!
    """
    for i in range(3):
        print(f"{{CONTEXT_LOOP_MESSAGE}} {i}")

    count = 0
    while count < 2:
        print(f"Count: {count}")
        count += 1


# ============================================================
# VERIFICATION
# ============================================================
# {{CONTEXT_VERIFICATION_PROMPT}}


def verify_predictions():
    """
    {{CONTEXT_VERIFICATION_NARRATIVE}}

    Compare your predictions with actual output.
    """
    print("=" * 60)
    print("{{CONTEXT_VERIFICATION_START}}")
    print("=" * 60)
    print()

    print("{{CHALLENGE_1_LABEL}}")
    print("-" * 60)
    challenge_1()
    print()
    print("{{CONTEXT_REFLECTION_1}}")
    print()

    print("{{CHALLENGE_2_LABEL}}")
    print("-" * 60)
    challenge_2()
    print()
    print("{{CONTEXT_REFLECTION_2}}")
    print()

    print("{{CHALLENGE_3_LABEL}}")
    print("-" * 60)
    challenge_3()
    print()
    print("{{CONTEXT_REFLECTION_3}}")
    print()

    print("{{CHALLENGE_4_LABEL}}")
    print("-" * 60)
    challenge_4()
    print()
    print("{{CONTEXT_REFLECTION_4}}")
    print()

    print("=" * 60)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")
    print("=" * 60)


def main():
    """Run verification after making predictions."""
    # Step 1: Read all challenges and write predictions
    # Step 2: Uncomment the line below to see actual output
    # verify_predictions()
    print("{{CONTEXT_VERIFICATION_INSTRUCTION}}")


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_PREDICTION_INTRO}}         - Why prediction matters
# {{CONTEXT_PREDICTION_PURPOSE}}       - Skill being developed
#
# For each challenge (1-4):
# {{CHALLENGE_N_TITLE}}                - Challenge heading
# {{CONTEXT_CHALLENGE_N_NARRATIVE}}    - Story context for challenge
# {{CONTEXT_PREDICTION_GUIDANCE_N}}    - Hints for thinking through it
# {{CHALLENGE_N_DESCRIPTION}}          - Technical description
# {{CHALLENGE_N_LABEL}}                - Label for verification output
# {{CONTEXT_REFLECTION_N}}             - Reflection prompt after seeing result
#
# Special context for challenge 3 (conditionals):
# {{CONTEXT_CONDITION_TRUE}}           - Message when condition is true
# {{CONTEXT_CONDITION_FALSE}}          - Message when condition is false
# {{CONTEXT_THRESHOLD_MET}}            - Message when threshold reached
#
# Special context for challenge 4 (loops):
# {{CONTEXT_LOOP_MESSAGE}}             - Message printed in loop
#
# Verification:
# {{CONTEXT_VERIFICATION_PROMPT}}      - Instructions for checking work
# {{CONTEXT_VERIFICATION_NARRATIVE}}   - How verification works
# {{CONTEXT_VERIFICATION_START}}       - Message when verification begins
# {{CONTEXT_VERIFICATION_COMPLETE}}    - All predictions checked
# {{CONTEXT_VERIFICATION_INSTRUCTION}} - How to activate verification
#
# Note: Can have more or fewer than 4 challenges. Adjust as needed.
