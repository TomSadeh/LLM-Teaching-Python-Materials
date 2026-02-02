"""
TEMPLATE 8: PROGRESSIVE UNLOCKING
Purpose: Build confidence with gated content that students activate when ready
Complexity: ⭐⭐ Moderate
Best for: Complex multi-stage exercises, building confidence gradually
"""

"""
{{CONTEXT_UNLOCKING_INTRO}}

{{CONTEXT_UNLOCKING_PROGRESSION}}
"""

# ============================================================
# {{STAGE_1_TITLE}} - AVAILABLE NOW
# ============================================================
# {{CONTEXT_STAGE_1_NARRATIVE}}
#
# ✏️ YOUR CODE HERE ✏️


def stage_1():
    """
    {{STAGE_1_DESCRIPTION}}

    Start here. This is the foundation for all later stages.
    """
    pass


# ============================================================
# {{STAGE_2_TITLE}} - UNLOCK AFTER STAGE 1
# ============================================================
# {{CONTEXT_STAGE_2_NARRATIVE}}
#
# {{CONTEXT_UNLOCK_INSTRUCTION_2}}


# def stage_2():
#     """
#     {{STAGE_2_DESCRIPTION}}
#
#     Requires understanding from Stage 1.
#     Uncomment when ready to attempt.
#     """
#     # ✏️ YOUR CODE HERE ✏️
#     pass


# ============================================================
# {{STAGE_3_TITLE}} - UNLOCK AFTER STAGE 2
# ============================================================
# {{CONTEXT_STAGE_3_NARRATIVE}}
#
# {{CONTEXT_UNLOCK_INSTRUCTION_3}}


# def stage_3():
#     """
#     {{STAGE_3_DESCRIPTION}}
#
#     Builds on Stages 1-2. More challenging.
#     Uncomment when ready to attempt.
#     """
#     # ✏️ YOUR CODE HERE ✏️
#     pass


# ============================================================
# {{STAGE_4_TITLE}} - UNLOCK AFTER STAGE 3
# ============================================================
# {{CONTEXT_STAGE_4_NARRATIVE}}
#
# {{CONTEXT_UNLOCK_INSTRUCTION_4}}


# def stage_4():
#     """
#     {{STAGE_4_DESCRIPTION}}
#
#     Advanced challenge. Requires mastery of previous stages.
#     Uncomment when ready to attempt.
#     """
#     # ✏️ YOUR CODE HERE ✏️
#     pass


# ============================================================
# {{STAGE_5_TITLE}} - FINAL STAGE (UNLOCK AFTER STAGE 4)
# ============================================================
# {{CONTEXT_STAGE_5_NARRATIVE}}
#
# {{CONTEXT_UNLOCK_INSTRUCTION_5}}


# def stage_5():
#     """
#     {{STAGE_5_DESCRIPTION}}
#
#     Master level. Only attempt after completing all previous stages.
#     Uncomment when ready for final challenge.
#     """
#     # ✏️ YOUR CODE HERE ✏️
#     pass


# ============================================================
# PROGRESSION TRACKER
# ============================================================


def check_progress():
    """
    {{CONTEXT_PROGRESS_CHECK}}

    Shows which stages are active/completed.
    """
    print("=" * 60)
    print("{{CONTEXT_PROGRESS_TITLE}}")
    print("=" * 60)
    print()

    stages = [
        ("{{STAGE_1_TITLE}}", stage_1, True),  # Always unlocked
        ("{{STAGE_2_TITLE}}", 'stage_2' in dir(), False),  # Check if uncommented
        ("{{STAGE_3_TITLE}}", 'stage_3' in dir(), False),
        ("{{STAGE_4_TITLE}}", 'stage_4' in dir(), False),
        ("{{STAGE_5_TITLE}}", 'stage_5' in dir(), False),
    ]

    for title, available, is_first in stages:
        if available and not isinstance(available, bool):
            status = "✅ {{CONTEXT_STATUS_AVAILABLE}}"
        elif is_first:
            status = "✅ {{CONTEXT_STATUS_AVAILABLE}}"
        else:
            status = "🔒 {{CONTEXT_STATUS_LOCKED}}"
        print(f"{status} {title}")

    print()
    print("{{CONTEXT_PROGRESS_NEXT_STEP}}")
    print("=" * 60)


# ============================================================
# MAIN EXECUTION
# ============================================================


def main():
    """Run all unlocked stages."""
    print("{{CONTEXT_PROGRESSION_START}}")
    print("=" * 60)
    print()

    # Stage 1 - Always runs
    print("{{STAGE_1_LABEL}}")
    print("-" * 60)
    stage_1()
    print("{{CONTEXT_STAGE_1_COMPLETE}}")
    print()

    # {{CONTEXT_UNLOCK_REMINDER}}
    # Uncomment stages below as you complete them:

    # Stage 2 - Uncomment when ready
    # print("{{STAGE_2_LABEL}}")
    # print("-" * 60)
    # stage_2()
    # print("{{CONTEXT_STAGE_2_COMPLETE}}")
    # print()

    # Stage 3 - Uncomment when ready
    # print("{{STAGE_3_LABEL}}")
    # print("-" * 60)
    # stage_3()
    # print("{{CONTEXT_STAGE_3_COMPLETE}}")
    # print()

    # Stage 4 - Uncomment when ready
    # print("{{STAGE_4_LABEL}}")
    # print("-" * 60)
    # stage_4()
    # print("{{CONTEXT_STAGE_4_COMPLETE}}")
    # print()

    # Stage 5 - Uncomment when ready
    # print("{{STAGE_5_LABEL}}")
    # print("-" * 60)
    # stage_5()
    # print("{{CONTEXT_STAGE_5_COMPLETE}}")
    # print()

    print("=" * 60)
    print("{{CONTEXT_PROGRESSION_STATUS}}")
    print()

    # Check overall progress
    check_progress()


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_UNLOCKING_INTRO}}          - Why progressive unlocking
# {{CONTEXT_UNLOCKING_PROGRESSION}}    - Overall journey description
#
# For each stage (1-5):
# {{STAGE_N_TITLE}}                    - Stage heading
# {{CONTEXT_STAGE_N_NARRATIVE}}        - What this stage unlocks (narrative)
# {{STAGE_N_DESCRIPTION}}              - What this stage does (technical)
# {{CONTEXT_UNLOCK_INSTRUCTION_N}}     - How to activate this stage
# {{STAGE_N_LABEL}}                    - Label for output section
# {{CONTEXT_STAGE_N_COMPLETE}}         - Message when stage completes
#
# Progression tracking:
# {{CONTEXT_UNLOCK_REMINDER}}          - Reminder about unlocking
# {{CONTEXT_PROGRESSION_START}}        - Message when starting
# {{CONTEXT_PROGRESSION_STATUS}}       - Current progress message
# {{CONTEXT_PROGRESS_CHECK}}           - Purpose of progress check
# {{CONTEXT_PROGRESS_TITLE}}           - Title for progress display
# {{CONTEXT_STATUS_AVAILABLE}}         - Label for available stages
# {{CONTEXT_STATUS_LOCKED}}            - Label for locked stages
# {{CONTEXT_PROGRESS_NEXT_STEP}}       - What to do next
#
# Note: Can have more or fewer than 5 stages. Adjust as needed.
