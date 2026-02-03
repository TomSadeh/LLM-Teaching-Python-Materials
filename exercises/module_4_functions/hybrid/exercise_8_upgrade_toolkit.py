# =============================================================================
# Hybrid Exercise: The Upgrade - Function Toolkit
# =============================================================================
# Difficulty: 4-5
# Arc: Upgrade (EVALUATION -> IMPROVEMENT -> GROWTH)
# Concepts: Refactoring, function decomposition, building toolkits
# =============================================================================

"""
{{CONTEXT_EVALUATION_INTRO}}

This is a multi-part exercise. Complete each part in order.

You've found a massive, monolithic program. Time to upgrade it by breaking
it into a clean toolkit of reusable functions.
"""


# ============================================================
# PART 1: EVALUATION - The Monolithic Monster
# ============================================================
# {{CONTEXT_EVALUATION_INTRO}}
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Study this huge function. Can you identify the separate concerns?


def monolithic_processor(members, scores, show_details=True):
    """
    THE MONOLITH: Does everything in one giant function.
    This works, but it's hard to maintain, test, or reuse parts.
    """
    # Part A: Print header
    print("=" * 50)
    print("{{school}} Team Analysis".center(50))
    print("=" * 50)

    # Part B: Process members
    print("\nTeam Roster:")
    print("-" * 30)
    member_count = 0
    for member in members:
        member_count = member_count + 1
        print(f"  {member_count}. {member}")
    print(f"\nTotal members: {member_count}")

    # Part C: Process scores
    if len(scores) > 0:
        print("\nScore Analysis:")
        print("-" * 30)

        # Calculate total
        total = 0
        for score in scores:
            total = total + score

        # Calculate average
        average = total / len(scores)

        # Find highest
        highest = scores[0]
        for score in scores:
            if score > highest:
                highest = score

        # Find lowest
        lowest = scores[0]
        for score in scores:
            if score < lowest:
                lowest = score

        # Count passing (>= 70)
        passing_count = 0
        for score in scores:
            if score >= 70:
                passing_count = passing_count + 1

        if show_details:
            print(f"  Scores: {scores}")
            print(f"  Total: {total}")
            print(f"  Average: {average:.1f}")
            print(f"  Highest: {highest}")
            print(f"  Lowest: {lowest}")
            print(f"  Passing (>=70): {passing_count}/{len(scores)}")

    else:
        print("\nNo scores to analyze.")

    # Part D: Print footer
    print("\n" + "=" * 50)
    print("End of Report")
    print("=" * 50)


def part_1_evaluate():
    """Test the monolith and identify problems."""
    print("Running the monolithic function:\n")

    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    scores = [85, 92, 78, 95, 70, 88]

    monolithic_processor(team, scores)

    # YOUR EVALUATION
    evaluation = """
    Problems with this approach:

    1. Can't reuse the header/footer separately
    2. Can't calculate average without printing everything
    3. Can't test score analysis independently
    4. Hard to modify one part without affecting others
    5. ~60 lines for one function is too long

    What should be separate functions?
    - Header/footer printing
    - List counting and display
    - Score statistics (total, average, max, min)
    - Pass/fail counting
    - Report assembly
    """
    return evaluation


# ============================================================
# PART 2: IMPROVEMENT - Break Into Functions
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Create helper functions to replace the monolith.


def part_2_create_toolkit():
    """Create the function toolkit."""

    # HELPER 1: Print formatted header
    def print_header(title, width=50, char="="):
        """Print a centered header with borders."""
        # YOUR CODE HERE
        pass

    # HELPER 2: Calculate list total
    def calculate_total(numbers):
        """Return the sum of a list of numbers."""
        # YOUR CODE HERE
        pass

    # HELPER 3: Calculate average
    def calculate_average(numbers):
        """Return the average, or 0 if empty."""
        # YOUR CODE HERE
        # Use calculate_total
        pass

    # HELPER 4: Find maximum
    def find_maximum(numbers):
        """Return the maximum value, or None if empty."""
        # YOUR CODE HERE
        pass

    # HELPER 5: Find minimum
    def find_minimum(numbers):
        """Return the minimum value, or None if empty."""
        # YOUR CODE HERE
        pass

    # HELPER 6: Count items matching condition
    def count_passing(scores, threshold=70):
        """Return count of scores >= threshold."""
        # YOUR CODE HERE
        pass

    # HELPER 7: Format numbered list
    def format_numbered_list(items, indent="  "):
        """Return items as a numbered list string."""
        # YOUR CODE HERE
        pass

    # Test the toolkit
    print("Testing individual toolkit functions:\n")

    scores = [85, 92, 78, 95, 70, 88]
    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]

    print_header("Toolkit Test")

    print(f"\nTotal: {calculate_total(scores)}")
    print(f"Average: {calculate_average(scores)}")
    print(f"Maximum: {find_maximum(scores)}")
    print(f"Minimum: {find_minimum(scores)}")
    print(f"Passing: {count_passing(scores)}")

    print("\nNumbered list:")
    print(format_numbered_list(team))

    # Return the functions for use in Part 3
    return {
        'print_header': print_header,
        'calculate_total': calculate_total,
        'calculate_average': calculate_average,
        'find_maximum': find_maximum,
        'find_minimum': find_minimum,
        'count_passing': count_passing,
        'format_numbered_list': format_numbered_list
    }


# ============================================================
# PART 3: GROWTH - Build the Improved Processor
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Use your toolkit to build a clean, modular processor.


def part_3_build_processor():
    """Build the improved processor using the toolkit."""

    # Create the toolkit functions (copy from Part 2 or define here)
    def print_header(title, width=50, char="="):
        """Print a centered header with borders."""
        # YOUR CODE HERE
        pass

    def calculate_total(numbers):
        # YOUR CODE HERE
        pass

    def calculate_average(numbers):
        # YOUR CODE HERE
        pass

    def find_maximum(numbers):
        # YOUR CODE HERE
        pass

    def find_minimum(numbers):
        # YOUR CODE HERE
        pass

    def count_passing(scores, threshold=70):
        # YOUR CODE HERE
        pass

    def format_numbered_list(items, indent="  "):
        # YOUR CODE HERE
        pass

    # MAIN PROCESSOR: Use the toolkit functions
    def process_team_report(members, scores, show_details=True):
        """
        Generate a team report using the toolkit functions.
        This is cleaner and each part is reusable!
        """
        # YOUR CODE HERE
        #
        # Rebuild the report using your toolkit functions:
        # 1. print_header for title
        # 2. format_numbered_list for members
        # 3. calculate_average, find_maximum, etc. for scores
        # 4. print_header for footer
        pass

    # Test the improved processor
    print("Running the improved processor:\n")

    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    scores = [85, 92, 78, 95, 70, 88]

    process_team_report(team, scores)

    print("\nThe same output, but now:")
    print("- Each function can be tested separately")
    print("- Functions can be reused elsewhere")
    print("- Easy to modify one aspect")


# ============================================================
# BONUS: Extend the Toolkit
# ============================================================

def bonus_extended_toolkit():
    """Add more functions to the toolkit."""

    # BONUS 1: get_score_grade
    def get_score_grade(score):
        """Return letter grade for a score."""
        # YOUR CODE HERE
        pass

    # BONUS 2: get_statistics_summary
    def get_statistics_summary(numbers):
        """Return a dict with all statistics."""
        # YOUR CODE HERE
        # Return: {'count': ?, 'total': ?, 'average': ?, 'max': ?, 'min': ?}
        pass

    # BONUS 3: compare_scores
    def compare_scores(scores1, scores2, label1="Group 1", label2="Group 2"):
        """Compare two sets of scores."""
        # YOUR CODE HERE
        pass

    # Test bonus functions
    print("Bonus toolkit functions:\n")

    print("Grades:")
    for score in [95, 85, 75, 65, 55]:
        print(f"  {score} -> {get_score_grade(score)}")

    print("\nStatistics summary:")
    stats = get_statistics_summary([85, 90, 78, 92, 88])
    print(stats)

    print("\nScore comparison:")
    compare_scores([85, 90, 95], [70, 75, 80], "Team A", "Team B")


def main():
    print("=" * 60)
    print("THE UPGRADE: Function Toolkit")
    print("=" * 60)

    print("\n--- PART 1: EVALUATE THE MONOLITH ---")
    print("{{CONTEXT_EVALUATION_INTRO}}")
    part_1_evaluate()
    print(f"\nEvaluation:{part_1_evaluate()}")

    print("\n--- PART 2: CREATE THE TOOLKIT ---")
    print("{{CONTEXT_IMPROVEMENT_INTRO}}")
    part_2_create_toolkit()

    print("\n--- PART 3: BUILD IMPROVED PROCESSOR ---")
    print("{{CONTEXT_GROWTH_INTRO}}")
    part_3_build_processor()

    print("\n--- BONUS: EXTEND THE TOOLKIT ---")
    bonus_extended_toolkit()

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("\nKey Lessons:")
    print("1. Break large functions into smaller, focused ones")
    print("2. Each function should do ONE thing well")
    print("3. Functions can call other functions")
    print("4. Toolkits make code reusable across projects")
    print("5. Easier to test, debug, and maintain")


main()
