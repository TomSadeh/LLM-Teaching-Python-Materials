# =============================================================================
# Hybrid Exercise: The Apprentice - Variables and Strings
# =============================================================================
# Difficulty: 3
# Arc: The Apprentice
# Parts: DISCOVERY -> GUIDANCE -> GROWTH
# Concepts: variables, strings, concatenation, printing
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: DISCOVERY - Study the Master's Work
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Study how {{hero}}'s mentor uses variables and strings.
# Predict the output before running the code.


def master_code_1():
    """DO NOT MODIFY - Study and predict"""
    title = "Apprentice"
    name = "{{hero}}"
    full_title = title + " " + name
    print(full_title)


def master_code_2():
    """DO NOT MODIFY - Study and predict"""
    school = "{{school}}"
    year = 1
    print(school, "- Year", year)


def master_code_3():
    """DO NOT MODIFY - Study and predict"""
    item = "{{item}}"
    owner = "{{hero}}"
    description = "The " + item + " belongs to " + owner
    print(description)


def your_predictions():
    # ✏️ YOUR PREDICTIONS HERE ✏️
    #
    # Write EXACTLY what each master_code function will print.
    #
    # master_code_1 output: _______________
    # master_code_2 output: _______________
    # master_code_3 output: _______________
    #
    # Hint: Pay attention to spaces - where do they come from?
    pass


# ============================================================
# PART 2: GUIDANCE - Practice with Support
# ============================================================
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# Now practice with some scaffolding to help you.


def guided_exercise_a():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Create and use variables like the master did.
    #
    # role = "Guardian"
    # hero = "{{hero}}"
    # title = role ___ " " ___ hero     # Fill in the operator to join strings
    # print(title)
    #
    # Hint: Use + to concatenate (join) strings.
    pass


def guided_exercise_b():
    # ✏️ FILL IN THE BLANKS ✏️
    #
    # Print multiple items with automatic spacing.
    #
    # location = "{{school}}"
    # status = "training"
    # print(___,  "is now", ___)        # Fill in the variable names
    #
    # Hint: Print the location and status variables.
    pass


# ============================================================
# PART 3: GROWTH - Create Your Own
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now create your own code using what you've learned!


def your_creation_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a character introduction.
    #
    # Step 1: Create a variable `hero_name` with value "{{hero}}"
    # Step 2: Create a variable `class_type` with value "{{ROLE_TITLE}}"
    # Step 3: Create a variable `intro` that combines:
    #         hero_name + " the " + class_type
    # Step 4: Print the intro
    #
    # Expected output: {{hero}} the {{ROLE_TITLE}}
    pass


def your_creation_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a status report for {{hero}}.
    #
    # Step 1: Create `location` with value "{{school}}"
    # Step 2: Create `health` with value 100 (a number!)
    # Step 3: Create `gold` with value 50 (a number!)
    # Step 4: Print using commas: "Location:", location
    # Step 5: Print using commas: "Health:", health, "Gold:", gold
    #
    # Expected output:
    # Location: {{school}}
    # Health: 100 Gold: 50
    pass


def main():
    print("=" * 50)
    print("PART 1: DISCOVERY - Study the Master's Work")
    print("=" * 50)

    print("\n--- master_code_1 ---")
    master_code_1()

    print("\n--- master_code_2 ---")
    master_code_2()

    print("\n--- master_code_3 ---")
    master_code_3()

    print("\n--- Your Predictions ---")
    your_predictions()

    print("\n" + "=" * 50)
    print("PART 2: GUIDANCE - Practice with Support")
    print("=" * 50)

    print("\n--- guided_exercise_a ---")
    # guided_exercise_a()  # Uncomment when blanks are filled

    print("\n--- guided_exercise_b ---")
    # guided_exercise_b()

    print("\n" + "=" * 50)
    print("PART 3: GROWTH - Create Your Own")
    print("=" * 50)

    print("\n--- your_creation_a ---")
    your_creation_a()

    print("\n--- your_creation_b ---")
    your_creation_b()

    print("\n" + "=" * 50)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
