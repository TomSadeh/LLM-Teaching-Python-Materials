# =============================================================================
# Hybrid Exercise: The Inheritance - The Utility Library
# =============================================================================
# Difficulty: 4
# Arc: Inheritance (DISCOVERY -> OWNERSHIP -> INVESTIGATION)
# Concepts: Working with existing functions, extending code, debugging
# =============================================================================

"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise. Complete each part in order.

{{mentor}} has retired and left behind a utility library. You've inherited
the code and must understand it, extend it, and fix any issues.
"""


# ============================================================
# THE INHERITED LIBRARY
# ============================================================
# This is the code you've inherited. Study it carefully.


def format_title(text, width=40):
    """Return a centered title with borders."""
    border = "=" * width
    centered = text.center(width)
    return f"{border}\n{centered}\n{border}"


def format_list_item(item, index, prefix="  "):
    """Return a formatted list item with index."""
    return f"{prefix}{index}. {item}"


def calculate_average(numbers):
    """Return the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    total = 0
    for num in numbers:
        total = total + num
    return total / len(numbers)


def get_grade(score):
    """Return a letter grade for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def create_profile_line(label, value, width=30):
    """Return a formatted profile line."""
    return f"{label}: {value}"


# ============================================================
# PART 1: DISCOVERY - Understand the Inherited Code
# ============================================================
# {{CONTEXT_DISCOVERY_INTRO}}
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Study the library functions above. Predict what they do.


def part_1_explore_library():
    """
    DISCOVERY EXERCISE

    Use the inherited functions and observe their behavior.
    """
    print("Exploring the inherited library...\n")

    # Test format_title
    print("Testing format_title:")
    title = format_title("{{school}} Report")
    print(title)
    print()

    # Test format_list_item
    print("Testing format_list_item:")
    print(format_list_item("{{hero}}", 1))
    print(format_list_item("{{heroine}}", 2))
    print(format_list_item("{{friend}}", 3))
    print()

    # Test calculate_average
    print("Testing calculate_average:")
    scores = [85, 90, 78, 92, 88]
    avg = calculate_average(scores)
    print(f"Scores: {scores}")
    print(f"Average: {avg}")
    print()

    # Test get_grade
    print("Testing get_grade:")
    for score in [95, 85, 75, 65, 55]:
        grade = get_grade(score)
        print(f"Score {score} -> Grade {grade}")
    print()

    # YOUR OBSERVATIONS
    #
    # Answer these questions:
    # 1. What does format_title do with the width parameter? _______________
    # 2. What does calculate_average return for an empty list? _______________
    # 3. What grade does a score of 89 get? _______________


# ============================================================
# PART 2: OWNERSHIP - Extend the Library
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Add your own functions to the library.


def part_2_extend_library():
    """
    OWNERSHIP EXERCISE

    Add new functions that complement the existing library.
    """

    # FUNCTION 1: format_header
    # Create a function similar to format_title but with a different style
    def format_header(text, char="-"):
        """
        Return a header with the text and underline.

        Args:
            text: The header text.
            char: The character for the underline (default: "-").

        Returns:
            The text followed by an underline.

        Example:
            format_header("News") returns:
            "News
             ----"
        """
        # YOUR CODE HERE
        pass

    # FUNCTION 2: format_numbered_list
    # Create a function that uses format_list_item to format a whole list
    def format_numbered_list(items):
        """
        Return a formatted numbered list.

        Args:
            items: A list of items to format.

        Returns:
            A string with all items numbered.

        Example:
            format_numbered_list(["a", "b"]) returns:
            "  1. a
               2. b"
        """
        # YOUR CODE HERE
        # Hint: Use a for loop and format_list_item
        pass

    # FUNCTION 3: get_grade_description
    # Extend get_grade to also provide a description
    def get_grade_description(score):
        """
        Return the grade and a description.

        Args:
            score: The numeric score.

        Returns:
            A string like "A - Excellent" or "B - Good"
        """
        # YOUR CODE HERE
        # Hint: Use the existing get_grade function
        pass

    # FUNCTION 4: create_report_card
    # Combine multiple functions to create a report card
    def create_report_card(name, scores):
        """
        Create a formatted report card.

        Args:
            name: The student's name.
            scores: A list of test scores.

        Returns:
            A formatted report card string.
        """
        # YOUR CODE HERE
        # Hint: Use format_title, calculate_average, get_grade
        pass

    # Test your new functions
    print("Testing your new functions:\n")

    print("format_header:")
    print(format_header("Team Members"))
    print()

    print("format_numbered_list:")
    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    print(format_numbered_list(team))
    print()

    print("get_grade_description:")
    print(get_grade_description(95))
    print(get_grade_description(72))
    print()

    print("create_report_card:")
    card = create_report_card("{{hero}}", [85, 90, 78, 92, 88])
    print(card)


# ============================================================
# PART 3: INVESTIGATION - Find and Fix Issues
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# There are some bugs and edge cases in the library. Find and fix them.


def part_3_fix_issues():
    """
    INVESTIGATION EXERCISE

    The library has some issues. Identify and fix them.
    """

    # ISSUE 1: create_profile_line doesn't use width parameter!
    # The width parameter is defined but never used.

    def fixed_create_profile_line(label, value, width=30):
        """
        Return a formatted profile line with proper width.

        Example:
            fixed_create_profile_line("Name", "{{hero}}", 25) returns:
            "Name:                {{hero}}"
        """
        # YOUR FIX HERE
        # Hint: Use string formatting to align the output
        pass

    # ISSUE 2: calculate_average uses manual loop
    # Can be simplified using sum() - but that's more advanced
    # For now, the original is fine for this level

    # ISSUE 3: What if someone passes a non-list to format_numbered_list?
    # Add a safety check

    def safe_format_numbered_list(items):
        """Format a list with safety checks."""
        # YOUR FIX HERE
        # Check if items is actually a list before processing
        # If not a list, return an error message or empty string
        pass

    # ISSUE 4: get_grade has magic numbers
    # Create a version with clearer threshold handling

    def improved_get_grade(score, thresholds=None):
        """
        Get grade with customizable thresholds.

        Args:
            score: The numeric score.
            thresholds: Optional dict with grade thresholds.
                       Default: {"A": 90, "B": 80, "C": 70, "D": 60}
        """
        # YOUR FIX HERE
        # If thresholds is None, use default values
        # This makes the function more flexible
        pass

    # Test your fixes
    print("Testing fixed functions:\n")

    print("fixed_create_profile_line:")
    print(fixed_create_profile_line("Name", "{{hero}}", 25))
    print(fixed_create_profile_line("Role", "Leader", 25))
    print()

    print("safe_format_numbered_list:")
    print(safe_format_numbered_list(["a", "b", "c"]))
    print(safe_format_numbered_list("not a list"))  # Should handle gracefully
    print()

    print("improved_get_grade:")
    print(improved_get_grade(85))
    print(improved_get_grade(85, {"A": 95, "B": 85, "C": 75, "D": 65}))


def main():
    print("=" * 60)
    print("THE INHERITANCE: The Utility Library")
    print("=" * 60)
    print("{{CONTEXT_DISCOVERY_INTRO}}")

    print("\n--- PART 1: DISCOVERY - Explore the Library ---")
    part_1_explore_library()

    print("\n--- PART 2: OWNERSHIP - Extend the Library ---")
    print("{{CONTEXT_OWNERSHIP_INTRO}}")
    part_2_extend_library()

    print("\n--- PART 3: INVESTIGATION - Fix Issues ---")
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    part_3_fix_issues()

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("\nKey Lessons:")
    print("1. Study existing code before modifying it")
    print("2. Build on what exists rather than rewriting")
    print("3. Test edge cases and fix issues carefully")
    print("4. Document your additions for the next developer")


main()
