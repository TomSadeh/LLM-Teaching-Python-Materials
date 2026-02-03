# =============================================================================
# Hybrid Exercise: The Competition - Design Showdown
# =============================================================================
# Difficulty: 4
# Arc: Competition (EVALUATION -> GROWTH -> EVALUATION)
# Concepts: Function design, comparing approaches, building better solutions
# =============================================================================

"""
{{CONTEXT_EVALUATION_INTRO}}

This is a multi-part exercise. Complete each part in order.

Two developers have submitted their code solutions. You'll evaluate both,
then build your own improved version.
"""


# ============================================================
# PART 1: EVALUATION - Compare Two Designs
# ============================================================
# {{CONTEXT_EVALUATION_INTRO}}
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Compare these two approaches to the same problem.

# PROBLEM: Create a system to display formatted profile cards.


def approach_1_monolithic():
    """
    Developer A's Approach: One large function that does everything.
    """
    def display_profile(name, role, level, location, status):
        print("+" + "-" * 38 + "+")
        print(f"| Name: {name:<30} |")
        print(f"| Role: {role:<30} |")
        print(f"| Level: {level:<29} |")
        print(f"| Location: {location:<26} |")
        print(f"| Status: {status:<28} |")
        print("+" + "-" * 38 + "+")

    display_profile("{{hero}}", "Leader", 25, "{{location}}", "Active")
    print()
    display_profile("{{heroine}}", "Strategist", 22, "{{school}}", "Active")


def approach_2_modular():
    """
    Developer B's Approach: Multiple small functions working together.
    """
    def create_border():
        return "+" + "-" * 38 + "+"

    def format_field(label, value, width=30):
        return f"| {label}: {value:<{width - len(label) - 2}} |"

    def build_profile_card(name, role, level, location, status):
        lines = [
            create_border(),
            format_field("Name", name),
            format_field("Role", role),
            format_field("Level", level),
            format_field("Location", location),
            format_field("Status", status),
            create_border()
        ]
        return "\n".join(lines)

    def display_card(card):
        print(card)

    card1 = build_profile_card("{{hero}}", "Leader", 25, "{{location}}", "Active")
    display_card(card1)
    print()
    card2 = build_profile_card("{{heroine}}", "Strategist", 22, "{{school}}", "Active")
    display_card(card2)


def part_1_evaluate():
    # YOUR EVALUATION
    #
    # Compare the two approaches:

    evaluation = """
    APPROACH 1 (Monolithic):
    Pros:
    - Simpler to understand at first glance
    - Everything in one place

    Cons:
    - Hard to reuse parts (like the border)
    - Hard to test individual components
    - Changes require modifying the whole function

    APPROACH 2 (Modular):
    Pros:
    - Each function has one job
    - Easy to reuse components
    - Easy to test each part
    - Easy to modify one aspect without breaking others

    Cons:
    - More functions to understand
    - Slightly more code

    Which is better for:
    - A quick script? Approach 1 might be fine
    - A larger project? Approach 2 is better
    - Code that will be modified? Approach 2

    My verdict: _______________
    """
    return evaluation


# ============================================================
# PART 2: GROWTH - Build Your Own Version
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now create your own improved version.


def my_profile_system():
    # BUILD YOUR OWN PROFILE CARD SYSTEM
    #
    # Requirements:
    # 1. Create a function to generate border lines (customizable character)
    # 2. Create a function to format a single field
    # 3. Create a function to build a complete profile card
    # 4. Create a function to display the card
    # 5. Use default parameters where appropriate
    #
    # Bonus features to consider:
    # - Customizable border character
    # - Customizable width
    # - Option to add a title to the card

    def create_border(char="-", width=40):
        """Create a border line."""
        # YOUR CODE HERE
        pass

    def format_field(label, value, width=40):
        """Format a label: value pair."""
        # YOUR CODE HERE
        pass

    def build_card(name, role, level, status="Active", width=40):
        """Build a complete profile card."""
        # YOUR CODE HERE
        #
        # Use create_border and format_field
        pass

    def display_card(card):
        """Display a card to the screen."""
        # YOUR CODE HERE
        pass

    # Test your system
    print("My Profile System:")
    print()

    # Create and display cards
    # YOUR CODE HERE
    #
    # Create at least 2 profile cards and display them


# ============================================================
# PART 3: EVALUATION - Reflect on Your Design
# ============================================================
# {{CONTEXT_EVALUATION_INTRO}}
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Compare your design to the original approaches.


def part_3_reflection():
    # YOUR REFLECTION
    #
    # How does your design compare?

    reflection = """
    MY DESIGN CHOICES:

    1. Functions I created:
       -
       -
       -

    2. Default parameters I used:
       -
       -

    3. What makes my design better/different:
       -
       -

    4. What I would improve if I had more time:
       -
       -

    5. Key lesson learned about function design:
       -
    """
    return reflection


# ============================================================
# BONUS: Extend Your System
# ============================================================

def extended_profile_system():
    # EXTEND YOUR SYSTEM
    #
    # Add these features to your profile system:
    #
    # 1. A function to create a "mini card" (just name and status)
    # 2. A function to compare two profiles (show side by side)
    # 3. A function to create a team roster (multiple profiles)

    # YOUR CODE HERE
    pass


def main():
    print("=" * 60)
    print("THE COMPETITION: Design Showdown")
    print("=" * 60)

    print("\n--- PART 1: EVALUATE THE COMPETITORS ---")
    print("{{CONTEXT_EVALUATION_INTRO}}")

    print("\nApproach 1 (Monolithic):")
    approach_1_monolithic()

    print("\nApproach 2 (Modular):")
    approach_2_modular()

    print(f"\nYour evaluation:{part_1_evaluate()}")

    print("\n--- PART 2: YOUR VERSION ---")
    print("{{CONTEXT_GROWTH_INTRO}}")
    my_profile_system()

    print("\n--- PART 3: REFLECTION ---")
    print(f"\nYour reflection:{part_3_reflection()}")

    print("\n--- BONUS: EXTENDED SYSTEM ---")
    extended_profile_system()

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("\nKey Principles of Good Function Design:")
    print("1. Single Responsibility: Each function does one thing")
    print("2. Reusability: Functions can be used in multiple places")
    print("3. Configurability: Default parameters add flexibility")
    print("4. Separation of Concerns: Build vs Display vs Format")


main()
