# =============================================================================
# Hybrid Exercise: The Apprentice - Complete Program
# =============================================================================
# Difficulty: 4-5
# Arc: The Apprentice
# Parts: DISCOVERY -> GUIDANCE -> GROWTH
# Concepts: All Module 0 - variables, strings, numbers, input, f-strings
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.
You will study a complete program, practice with guidance, then build your own!
"""


# ============================================================
# PART 1: DISCOVERY - Study the Master's Program
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Study this complete character creator program.
# Predict what it will do before running it.


def master_program():
    """DO NOT MODIFY - Study and predict"""
    # Character setup
    name = "{{hero}}"
    character_class = "Apprentice"

    # Stats
    health = 100
    strength = 10
    defense = 8

    # Calculated stats
    power = strength + defense

    # Display character sheet
    print(f"=== {name} the {character_class} ===")
    print(f"Health: {health}")
    print(f"Strength: {strength}")
    print(f"Defense: {defense}")
    print(f"Power Rating: {power}")
    print("=" * 30)


def your_predictions():
    # ✏️ YOUR PREDICTIONS HERE ✏️
    #
    # Before running master_program(), predict:
    #
    # 1. How many lines will be printed? ___
    # 2. What will the Power Rating be? ___
    # 3. What type of quotes does the program use for output? ___
    #
    # Run the program to check your predictions!
    pass


# ============================================================
# PART 2: GUIDANCE - Practice with Scaffolding
# ============================================================
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# Complete these functions by filling in the missing parts.


def guided_character_header(name, title):
    """
    Create a character header.

    Args:
        name: The character's name
        title: The character's title

    Returns:
        A formatted header string

    Example:
        >>> guided_character_header("{{hero}}", "Wizard")
        "=== {{hero}} the Wizard ==="
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # Use an f-string to create the header.
    # Pattern: "=== {name} the {title} ==="

    pass


def guided_stat_line(stat_name, stat_value):
    """
    Create a stat display line.

    Args:
        stat_name: Name of the stat (like "Health")
        stat_value: Value of the stat (like 100)

    Returns:
        A formatted stat string

    Example:
        >>> guided_stat_line("Health", 100)
        "Health: 100"
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    #
    # Use an f-string: f"{stat_name}: {stat_value}"

    pass


# ============================================================
# PART 3: GROWTH - Create Your Own
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now create your own character creator from scratch!


def my_character_creator():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create your own character profile program!
    #
    # Requirements:
    # 1. Create at least 5 variables (name, class, and 3+ stats)
    # 2. Calculate at least one derived stat (like power = str + def)
    # 3. Use f-strings for all output
    # 4. Print a header with the character's name and class
    # 5. Print all stats in a formatted way
    # 6. Print a separator line at the end
    #
    # Example output:
    # === Maya the Warrior ===
    # Health: 120
    # Strength: 15
    # Defense: 12
    # Speed: 8
    # Combat Rating: 27
    # ==============================
    #
    # Be creative! Add your own stats and style.

    pass


def my_interactive_creator():
    # ✏️ BONUS CHALLENGE ✏️
    #
    # Make an INTERACTIVE version that asks the user for input!
    #
    # Use input() to ask for:
    # - Character name
    # - Character class
    # - At least one stat value
    #
    # Then display the character sheet using f-strings.
    #
    # Example interaction:
    # Enter character name: Luna
    # Enter character class: Mage
    # Enter magic power: 25
    #
    # === Luna the Mage ===
    # Magic Power: 25
    # (etc...)

    pass


def main():
    print("=" * 50)
    print("PART 1: DISCOVERY - Study the Master's Program")
    print("=" * 50)

    print("\n--- master_program output ---")
    master_program()

    print("\n--- Your Predictions ---")
    your_predictions()

    print("\n" + "=" * 50)
    print("PART 2: GUIDANCE - Practice with Scaffolding")
    print("=" * 50)

    print("\n--- Testing guided_character_header ---")
    result1 = guided_character_header("{{hero}}", "Wizard")
    print("Result:", result1)
    print("Expected: === {{hero}} the Wizard ===")

    print("\n--- Testing guided_stat_line ---")
    result2 = guided_stat_line("Health", 100)
    print("Result:", result2)
    print("Expected: Health: 100")

    print("\n" + "=" * 50)
    print("PART 3: GROWTH - Create Your Own")
    print("=" * 50)

    print("\n--- my_character_creator ---")
    my_character_creator()

    print("\n--- my_interactive_creator (BONUS) ---")
    # Uncomment to test interactive version:
    # my_interactive_creator()
    print("(Uncomment the line above to test!)")

    print("\n" + "=" * 50)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
