# =============================================================================
# Hybrid Exercise: The Rescue - List Processing Functions
# =============================================================================
# Difficulty: 4
# Arc: Rescue (SETBACK -> INVESTIGATION -> IMPROVEMENT)
# Concepts: Functions with list parameters, edge cases, error handling
# =============================================================================

"""
{{CONTEXT_SETBACK_INTRO}}

This is a multi-part exercise. Complete each part in order.

The list processing system at {{school}} is failing. Students are getting
errors when they try to analyze their data. You need to fix it!
"""


# ============================================================
# PART 1: SETBACK - Understand the Error
# ============================================================
# {{CONTEXT_SETBACK_INTRO}}
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# The system is crashing. Decode what went wrong.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "processor.py", line 15, in <module>
    result = get_first(empty_list)
  File "processor.py", line 5, in get_first
    return items[0]
IndexError: list index out of range

The code that caused this:
    def get_first(items):
        return items[0]

    empty_list = []
    result = get_first(empty_list)  # Crashes!
"""


def part_1_understand_error():
    """
    SETBACK: Understand why the code crashed.
    """
    print("Demonstrating the problem:\n")

    # This function doesn't handle empty lists
    def buggy_get_first(items):
        return items[0]  # Crashes if items is empty!

    # Works fine with data
    print("With data:")
    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    first = buggy_get_first(team)
    print(f"First of {team}: {first}")

    # Crashes with empty list
    print("\nWith empty list:")
    print("This would crash: buggy_get_first([])")
    print("IndexError: list index out of range")

    # YOUR UNDERSTANDING
    #
    # Why does this error occur?
    # - Lists use 0-based indexing
    # - An empty list has no index 0
    # - Accessing a non-existent index raises IndexError


# ============================================================
# PART 2: INVESTIGATION - Fix the Functions
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Here are the broken functions. Fix each one to handle edge cases.


def part_2_fix_functions():
    """
    INVESTIGATION: Fix the functions to handle edge cases.
    """

    # FIX 1: get_first - Handle empty lists
    def get_first(items, default=None):
        """
        Return the first item in a list, or default if empty.

        Args:
            items: A list of items.
            default: Value to return if list is empty (default: None).

        Returns:
            The first item, or default if list is empty.
        """
        # YOUR FIX HERE
        #
        # Check if the list has items before accessing index 0
        pass

    # FIX 2: get_last - Handle empty lists
    def get_last(items, default=None):
        """
        Return the last item in a list, or default if empty.
        """
        # YOUR FIX HERE
        pass

    # FIX 3: get_average - Handle empty lists
    def get_average(numbers):
        """
        Return the average of a list of numbers.
        Return 0 if the list is empty (can't divide by zero!).
        """
        # YOUR FIX HERE
        #
        # Check length before dividing
        pass

    # FIX 4: get_item_at - Handle invalid indices
    def get_item_at(items, index, default=None):
        """
        Return the item at the given index, or default if invalid.
        """
        # YOUR FIX HERE
        #
        # Check if index is valid before accessing
        pass

    # Test the fixed functions
    print("Testing fixed functions:\n")

    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    empty = []
    scores = [85, 90, 78]

    print("get_first:")
    print(f"  Team: {get_first(team)}")
    print(f"  Empty: {get_first(empty)}")
    print(f"  Empty with default: {get_first(empty, 'No one')}")

    print("\nget_last:")
    print(f"  Team: {get_last(team)}")
    print(f"  Empty: {get_last(empty)}")

    print("\nget_average:")
    print(f"  Scores {scores}: {get_average(scores)}")
    print(f"  Empty []: {get_average([])}")

    print("\nget_item_at:")
    print(f"  Team[1]: {get_item_at(team, 1)}")
    print(f"  Team[10]: {get_item_at(team, 10)}")
    print(f"  Team[10] with default: {get_item_at(team, 10, 'Invalid')}")


# ============================================================
# PART 3: IMPROVEMENT - Build Robust List Functions
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Create a complete set of safe list processing functions.


def part_3_improved_functions():
    """
    IMPROVEMENT: Create robust list processing functions.
    """

    # FUNCTION 1: safe_sum
    def safe_sum(numbers):
        """
        Return the sum of numbers, or 0 if empty or invalid.
        """
        # YOUR CODE HERE
        pass

    # FUNCTION 2: find_max
    def find_max(numbers, default=None):
        """
        Return the maximum value in a list.
        Return default if list is empty.

        Note: Don't use the built-in max() function.
              Use a loop to find the maximum.
        """
        # YOUR CODE HERE
        #
        # Hint: Start with the first element as max_value
        #       Then compare each element
        pass

    # FUNCTION 3: find_min
    def find_min(numbers, default=None):
        """
        Return the minimum value in a list.
        Return default if list is empty.
        """
        # YOUR CODE HERE
        pass

    # FUNCTION 4: count_matches
    def count_matches(items, target):
        """
        Count how many items match the target.
        Return 0 if list is empty.
        """
        # YOUR CODE HERE
        pass

    # FUNCTION 5: filter_above
    def filter_above(numbers, threshold):
        """
        Return a new list with only numbers above threshold.
        Return empty list if input is empty.
        """
        # YOUR CODE HERE
        #
        # Create a new list and add items that meet the condition
        pass

    # FUNCTION 6: transform_all
    def transform_all(items, prefix=""):
        """
        Return a new list with prefix added to each item.
        """
        # YOUR CODE HERE
        #
        # Create a new list with transformed items
        pass

    # Test the improved functions
    print("Testing improved functions:\n")

    scores = [85, 90, 78, 92, 88]
    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    empty = []

    print("safe_sum:")
    print(f"  Scores: {safe_sum(scores)}")
    print(f"  Empty: {safe_sum(empty)}")

    print("\nfind_max:")
    print(f"  Scores: {find_max(scores)}")
    print(f"  Empty: {find_max(empty)}")

    print("\nfind_min:")
    print(f"  Scores: {find_min(scores)}")
    print(f"  Empty: {find_min(empty, 0)}")

    print("\ncount_matches:")
    numbers = [1, 2, 2, 3, 2, 4]
    print(f"  Count of 2 in {numbers}: {count_matches(numbers, 2)}")

    print("\nfilter_above:")
    print(f"  Scores above 85: {filter_above(scores, 85)}")

    print("\ntransform_all:")
    print(f"  Team with prefix: {transform_all(team, '>> ')}")


# ============================================================
# FINAL: Complete List Utility
# ============================================================

def final_list_utility():
    """
    FINAL: Put it all together with a list analyzer.
    """

    def analyze_scores(scores, name="Data"):
        """
        Analyze a list of scores and return a summary.

        Args:
            scores: A list of numeric scores.
            name: A label for the data.

        Returns:
            A formatted summary string.
        """
        # YOUR CODE HERE
        #
        # Use your functions to:
        # 1. Handle empty list case
        # 2. Calculate count, sum, average, min, max
        # 3. Return a formatted summary
        pass

    # Test the analyzer
    print("=" * 40)
    print("Score Analyzer")
    print("=" * 40)

    print(analyze_scores([85, 90, 78, 92, 88], "{{hero}}'s scores"))
    print()
    print(analyze_scores([100, 95, 98], "{{heroine}}'s scores"))
    print()
    print(analyze_scores([], "Empty data"))


def main():
    print("=" * 60)
    print("THE RESCUE: List Processing Functions")
    print("=" * 60)
    print("{{CONTEXT_SETBACK_INTRO}}")

    print("\n--- PART 1: SETBACK - Understand the Error ---")
    part_1_understand_error()

    print("\n--- PART 2: INVESTIGATION - Fix the Functions ---")
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    part_2_fix_functions()

    print("\n--- PART 3: IMPROVEMENT - Build Robust Functions ---")
    print("{{CONTEXT_IMPROVEMENT_INTRO}}")
    part_3_improved_functions()

    print("\n--- FINAL: List Analyzer ---")
    final_list_utility()

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("\nKey Lessons:")
    print("1. Always handle empty lists before accessing elements")
    print("2. Use default parameters for flexible error handling")
    print("3. Check indices before accessing list positions")
    print("4. Functions make error handling reusable")


main()
