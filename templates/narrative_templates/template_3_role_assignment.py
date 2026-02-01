"""
TEMPLATE 3: ROLE ASSIGNMENT
Purpose: Place student in specific role with responsibilities
Complexity: ⭐ Simple
Best for: Contextualized tasks, creating engagement through role-play
"""

"""
{{CONTEXT_ROLE_INTRO}}

{{CONTEXT_ROLE_RESPONSIBILITIES}}

{{CONTEXT_ROLE_CHALLENGE}}
"""

# ============================================================
# {{CONTEXT_SITUATION_SETUP}}
# ============================================================


def role_task_1():
    """
    {{TASK_1_DESCRIPTION}}

    First responsibility of your role.
    """
    # {{CONTEXT_TASK_1_GUIDANCE}}
    # ✏️ YOUR CODE HERE ✏️
    pass


def role_task_2():
    """
    {{TASK_2_DESCRIPTION}}

    Second responsibility of your role.
    """
    # {{CONTEXT_TASK_2_GUIDANCE}}
    # ✏️ YOUR CODE HERE ✏️
    pass


def role_task_3():
    """
    {{TASK_3_DESCRIPTION}}

    Third responsibility of your role.
    """
    # {{CONTEXT_TASK_3_GUIDANCE}}
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# EXECUTE YOUR DUTIES
# ============================================================

def main():
    """Perform all role responsibilities."""
    print("=" * 60)
    print("{{CONTEXT_ROLE_START}}")
    print("=" * 60)
    print()

    print("{{CONTEXT_TASK_1_INTRO}}")
    print("-" * 60)
    role_task_1()
    print("{{CONTEXT_TASK_1_COMPLETE}}")
    print()

    print("{{CONTEXT_TASK_2_INTRO}}")
    print("-" * 60)
    role_task_2()
    print("{{CONTEXT_TASK_2_COMPLETE}}")
    print()

    print("{{CONTEXT_TASK_3_INTRO}}")
    print("-" * 60)
    role_task_3()
    print("{{CONTEXT_TASK_3_COMPLETE}}")
    print()

    print("=" * 60)
    print("{{CONTEXT_ROLE_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_ROLE_INTRO}}             - Who the student is in this scenario
# {{CONTEXT_ROLE_RESPONSIBILITIES}}  - What their job entails
# {{CONTEXT_ROLE_CHALLENGE}}         - The problem they need to solve
# {{CONTEXT_SITUATION_SETUP}}        - Current situation details
#
# For each task (1-3):
# {{TASK_N_DESCRIPTION}}             - Technical description of task
# {{CONTEXT_TASK_N_GUIDANCE}}        - Hints/tips for completing task
# {{CONTEXT_TASK_N_INTRO}}           - Message before task executes
# {{CONTEXT_TASK_N_COMPLETE}}        - Message after task completes
#
# Role execution:
# {{CONTEXT_ROLE_START}}             - Opening message when starting duties
# {{CONTEXT_ROLE_COMPLETE}}          - Closing message when finished
#
# Note: Can have more or fewer than 3 tasks. Adjust as needed.
