# =============================================================================
# Write Code: Functions with Parameters
# =============================================================================
# Difficulty: 2
# Concepts: Parameters, arguments, positional arguments, multiple parameters
# =============================================================================

"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Create a function that accepts one parameter.
    #
    # Step 1: Define a function called greet_person that takes one parameter: name
    # Step 2: Inside, print f"Hello, {name}!"
    # Step 3: Call greet_person with "{{hero}}"
    # Step 4: Call greet_person with "{{heroine}}"
    #
    # Hint: def function_name(parameter):
    #
    # Expected output:
    #   Hello, {{hero}}!
    #   Hello, {{heroine}}!
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Create a function that uses its parameter multiple times.
    #
    # Step 1: Define a function called celebrate that takes one parameter: winner
    # Step 2: Inside, print f"Congratulations, {winner}!"
    # Step 3: Inside, print f"{winner} is the champion!"
    # Step 4: Inside, print f"Everyone applauds {winner}!"
    # Step 5: Call celebrate with "{{hero}}"
    #
    # Expected output:
    #   Congratulations, {{hero}}!
    #   {{hero}} is the champion!
    #   Everyone applauds {{hero}}!
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Create a function with two parameters.
    #
    # Step 1: Define a function called introduce that takes two parameters:
    #         person and role
    # Step 2: Inside, print f"{person} is the {role}."
    # Step 3: Call introduce with "{{hero}}" and "leader"
    # Step 4: Call introduce with "{{mentor}}" and "advisor"
    # Step 5: Call introduce with "{{heroine}}" and "strategist"
    #
    # Expected output:
    #   {{hero}} is the leader.
    #   {{mentor}} is the advisor.
    #   {{heroine}} is the strategist.
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Create a function with three parameters.
    #
    # Step 1: Define a function called describe_mission that takes three
    #         parameters: leader, location, goal
    # Step 2: Inside, print f"Mission Briefing:"
    # Step 3: Inside, print f"  Leader: {leader}"
    # Step 4: Inside, print f"  Location: {location}"
    # Step 5: Inside, print f"  Goal: {goal}"
    # Step 6: Call the function with "{{hero}}", "{{location}}", "{{spell1}}"
    #
    # Expected output:
    #   Mission Briefing:
    #     Leader: {{hero}}
    #     Location: {{location}}
    #     Goal: {{spell1}}
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Create and use multiple functions with parameters.
    #
    # Step 1: Define a function called print_header that takes one parameter:
    #         title, and prints f"=== {title} ==="
    # Step 2: Define a function called print_member that takes two parameters:
    #         name and status, and prints f"  {name}: {status}"
    # Step 3: Call print_header with "Team {{house}}"
    # Step 4: Call print_member with "{{hero}}" and "Ready"
    # Step 5: Call print_member with "{{heroine}}" and "Ready"
    # Step 6: Call print_member with "{{friend}}" and "Preparing"
    #
    # Expected output:
    #   === Team {{house}} ===
    #     {{hero}}: Ready
    #     {{heroine}}: Ready
    #     {{friend}}: Preparing
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    exercise_c()

    print("\n=== {{PHASE_4_TITLE}} ===")
    exercise_d()

    print("\n=== {{PHASE_5_TITLE}} ===")
    exercise_e()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
