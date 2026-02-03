# =============================================================================
# Hybrid Exercise: Mini Project - The Function Workshop
# =============================================================================
# Difficulty: 5
# Arc: Custom (DISCOVERY -> GROWTH -> GROWTH -> IMPROVEMENT)
# Concepts: Function design, implementation, integration, code quality
# =============================================================================

"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part mini project. Complete each part in order.

You're building a complete Team Management System for {{school}} using
functions. This project ties together everything you've learned about
functions: definition, parameters, return values, and good design.
"""


# ============================================================
# PART 1: DISCOVERY - Design Your Functions
# ============================================================
# {{CONTEXT_DISCOVERY_INTRO}}
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Before writing code, design your function signatures.
# Think about what parameters each function needs and what it should return.


def part_1_design_signatures():
    """
    BLANK PAGE: Design your function signatures.

    For each function, think about:
    - What parameters does it need?
    - What should it return?
    - Should any parameters have default values?
    """

    # YOUR DESIGN NOTES
    #
    # Function 1: create_member
    # Purpose: Create a dictionary representing a team member
    # Parameters: ???
    # Returns: ???
    # Signature: def create_member(???):

    # Function 2: format_member_display
    # Purpose: Return a formatted string showing member info
    # Parameters: ???
    # Returns: ???
    # Signature: def format_member_display(???):

    # Function 3: calculate_team_average
    # Purpose: Calculate the average level of team members
    # Parameters: ???
    # Returns: ???
    # Signature: def calculate_team_average(???):

    # Function 4: find_member_by_name
    # Purpose: Find a member in the team by their name
    # Parameters: ???
    # Returns: ???
    # Signature: def find_member_by_name(???):

    # Function 5: get_team_summary
    # Purpose: Generate a summary report of the team
    # Parameters: ???
    # Returns: ???
    # Signature: def get_team_summary(???):

    print("Part 1: Design your function signatures on paper or in comments.")
    print("Think before you code!")
    print()
    print("Questions to consider:")
    print("1. What data does each function need?")
    print("2. What does each function produce?")
    print("3. What's a good default value for optional parameters?")


# ============================================================
# PART 2: GROWTH - Implement Core Functions
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now implement the core functions for your team management system.


def part_2_implement_core():
    """Implement the core functions."""

    # FUNCTION 1: create_member
    def create_member(name, role, level=1, status="Active"):
        """
        Create a dictionary representing a team member.

        Args:
            name: The member's name.
            role: Their role on the team.
            level: Their experience level (default: 1).
            status: Their current status (default: "Active").

        Returns:
            A dictionary with keys: name, role, level, status

        Examples:
            >>> create_member("{{hero}}", "Leader", 10)
            {'name': '{{hero}}', 'role': 'Leader', 'level': 10, 'status': 'Active'}
        """
        # YOUR CODE HERE
        pass

    # FUNCTION 2: format_member_display
    def format_member_display(member, width=40):
        """
        Format a member dictionary for display.

        Args:
            member: A member dictionary from create_member.
            width: Display width (default: 40).

        Returns:
            A formatted string showing the member's info.

        Example output:
            "{{hero}} (Leader) - Level 10 [Active]"
        """
        # YOUR CODE HERE
        pass

    # FUNCTION 3: add_member_to_team
    def add_member_to_team(team, member):
        """
        Add a member to the team list.

        Args:
            team: A list of member dictionaries.
            member: A member dictionary to add.

        Returns:
            The updated team list.

        Note: This modifies the original list and also returns it.
        """
        # YOUR CODE HERE
        pass

    # FUNCTION 4: find_member_by_name
    def find_member_by_name(team, name):
        """
        Find a member in the team by name.

        Args:
            team: A list of member dictionaries.
            name: The name to search for.

        Returns:
            The member dictionary if found, None otherwise.
        """
        # YOUR CODE HERE
        pass

    # Test the core functions
    print("Testing core functions:\n")

    # Create some members
    member1 = create_member("{{hero}}", "Leader", 10)
    member2 = create_member("{{heroine}}", "Strategist", 8)
    member3 = create_member("{{friend}}", "Scout", 5)

    print("Created members:")
    print(f"  {member1}")
    print(f"  {member2}")
    print(f"  {member3}")

    print("\nFormatted display:")
    print(f"  {format_member_display(member1)}")
    print(f"  {format_member_display(member2)}")
    print(f"  {format_member_display(member3)}")

    # Build a team
    team = []
    add_member_to_team(team, member1)
    add_member_to_team(team, member2)
    add_member_to_team(team, member3)

    print(f"\nTeam size: {len(team)}")

    # Find a member
    found = find_member_by_name(team, "{{heroine}}")
    print(f"\nFound {{heroine}}: {found}")

    not_found = find_member_by_name(team, "Unknown")
    print(f"Found Unknown: {not_found}")

    return team  # Return for Part 3


# ============================================================
# PART 3: GROWTH - Build the Main Program
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Use your functions to build the complete team management system.


def part_3_build_program():
    """Build the main program using all the functions."""

    # Copy or redefine your functions here
    def create_member(name, role, level=1, status="Active"):
        # YOUR CODE HERE
        pass

    def format_member_display(member, width=40):
        # YOUR CODE HERE
        pass

    def add_member_to_team(team, member):
        # YOUR CODE HERE
        pass

    def find_member_by_name(team, name):
        # YOUR CODE HERE
        pass

    # NEW: Calculate team average level
    def calculate_team_average(team):
        """
        Calculate the average level of all team members.

        Returns:
            The average level, or 0 if team is empty.
        """
        # YOUR CODE HERE
        pass

    # NEW: Get members by role
    def get_members_by_role(team, role):
        """
        Return a list of members with the specified role.
        """
        # YOUR CODE HERE
        pass

    # NEW: Get team summary
    def get_team_summary(team, title="Team Summary"):
        """
        Generate a complete team summary report.

        Returns:
            A formatted string with the full report.
        """
        # YOUR CODE HERE
        #
        # Include:
        # - Title
        # - Member count
        # - Average level
        # - List of all members
        pass

    # NEW: Print separator
    def print_section(title, char="=", width=50):
        """Print a section header."""
        # YOUR CODE HERE
        pass

    # BUILD THE MAIN PROGRAM
    print_section("{{school}} Team Manager")

    # Create the team
    team = []

    # Add members
    print("\nAdding team members...")
    add_member_to_team(team, create_member("{{hero}}", "Leader", 10))
    add_member_to_team(team, create_member("{{heroine}}", "Strategist", 8))
    add_member_to_team(team, create_member("{{friend}}", "Scout", 5))
    add_member_to_team(team, create_member("{{mentor}}", "Advisor", 15, "Advisory"))

    # Display all members
    print_section("Team Roster", "-")
    for i, member in enumerate(team):
        print(f"{i + 1}. {format_member_display(member)}")

    # Show statistics
    print_section("Team Statistics", "-")
    print(f"Total members: {len(team)}")
    print(f"Average level: {calculate_team_average(team):.1f}")

    # Find specific members
    print_section("Member Lookup", "-")
    target = "{{hero}}"
    found = find_member_by_name(team, target)
    if found:
        print(f"Found {target}:")
        print(f"  {format_member_display(found)}")
    else:
        print(f"{target} not found.")

    # Generate full summary
    print_section("Full Summary", "=")
    summary = get_team_summary(team, "{{school}} Team Report")
    if summary:
        print(summary)

    print_section("End of Program", "=")


# ============================================================
# PART 4: IMPROVEMENT - Polish and Document
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Review your code and improve the quality.


def part_4_polish():
    """Review and improve code quality."""

    # CHECKLIST: Review your code against these standards

    checklist = """
    CODE QUALITY CHECKLIST:

    [ ] Function Naming:
        - All function names are descriptive (not f1, f2)
        - Names use snake_case
        - Names start with verbs (get_, create_, find_, calculate_)

    [ ] Parameter Naming:
        - All parameters have meaningful names
        - No single-letter names (except i in loops)

    [ ] Default Parameters:
        - Used appropriately for optional values
        - Required parameters come before optional ones

    [ ] Return Values:
        - Functions return values (not just print)
        - Proper handling of edge cases (empty lists, not found)

    [ ] Documentation:
        - Each function has a docstring
        - Parameters and return values are described

    [ ] Code Organization:
        - Helper functions are defined before they're used
        - Related functions are grouped together
        - Main program logic is separate from function definitions

    YOUR IMPROVEMENTS:
    List 3 things you would improve in your code:
    1. _______________
    2. _______________
    3. _______________
    """

    print("Part 4: Code Quality Review")
    print(checklist)


# ============================================================
# BONUS: Extend the System
# ============================================================

def bonus_extensions():
    """Optional extensions to the system."""

    print("BONUS CHALLENGES:")
    print()
    print("1. Add a function to promote a member (increase their level)")
    print("2. Add a function to change a member's status")
    print("3. Add a function to remove a member from the team")
    print("4. Add a function to sort the team by level")
    print("5. Add a function to get the highest-level member")
    print()
    print("Try implementing one or more of these!")

    # YOUR BONUS CODE HERE
    pass


def main():
    print("=" * 60)
    print("MINI PROJECT: The Function Workshop")
    print("=" * 60)
    print("{{CONTEXT_PROJECT_INTRO}}")

    print("\n" + "=" * 60)
    print("PART 1: DESIGN YOUR FUNCTIONS")
    print("=" * 60)
    part_1_design_signatures()

    print("\n" + "=" * 60)
    print("PART 2: IMPLEMENT CORE FUNCTIONS")
    print("=" * 60)
    part_2_implement_core()

    print("\n" + "=" * 60)
    print("PART 3: BUILD THE MAIN PROGRAM")
    print("=" * 60)
    part_3_build_program()

    print("\n" + "=" * 60)
    print("PART 4: POLISH AND DOCUMENT")
    print("=" * 60)
    part_4_polish()

    print("\n" + "=" * 60)
    print("BONUS EXTENSIONS")
    print("=" * 60)
    bonus_extensions()

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)
    print()
    print("Congratulations on completing Module 4: Functions!")
    print()
    print("You've learned to:")
    print("  - Define functions with def")
    print("  - Use parameters to pass data in")
    print("  - Use return to send data back")
    print("  - Distinguish return from print")
    print("  - Use default parameters")
    print("  - Understand local scope")
    print("  - Work with functions and lists")
    print("  - Design reusable function toolkits")
    print()
    print("Functions are the building blocks of programs.")
    print("Use them to make your code clean, reusable, and maintainable!")


main()
