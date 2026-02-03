# =============================================================================
# Hybrid Exercise: The Upgrade - Cleaner List Code
# =============================================================================
# Difficulty: 4
# Arc: Upgrade (EVALUATION -> IMPROVEMENT) - 2-part variant
# Concepts: Code comparison, simplification, Pythonic patterns
# =============================================================================

"""
{{CONTEXT_EVALUATION_INTRO}}

This is a multi-part exercise. Complete each part in order.
"""


# ============================================================
# PART 1: EVALUATION - Compare Approaches
# ============================================================
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Two developers wrote code to solve the same problem.
# Analyze which approach is better and why.


# --- COMPARISON 1: Summing a List ---


def sum_verbose(numbers):
    """Version A: Manual loop"""
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    return total


def sum_pythonic(numbers):
    """Version B: Direct iteration"""
    total = 0
    for num in numbers:
        total = total + num
    return total


def analysis_sum():
    # YOUR ANALYSIS
    #
    # Both produce the same result. Which is better?
    # Consider: readability, simplicity, risk of bugs.

    analysis = {
        "better_version": "?",  # "A" or "B"
        "reason": "Because...",
        "what_makes_B_simpler": "...",
    }

    return analysis


# --- COMPARISON 2: Building a New List ---


def double_verbose(numbers):
    """Version A: Manual indexing"""
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i] * 2)
    return result


def double_simple(numbers):
    """Version B: Direct element iteration"""
    result = []
    for num in numbers:
        result.append(num * 2)
    return result


def analysis_double():
    # YOUR ANALYSIS
    #
    # Which approach is cleaner for transforming list elements?

    analysis = {
        "better_version": "?",  # "A" or "B"
        "reason": "Because...",
        "when_might_A_be_needed": "...",  # When DO you need the index?
    }

    return analysis


# --- COMPARISON 3: Counting Matches ---


def count_verbose(items, target):
    """Version A: Manual loop and counter"""
    count = 0
    for i in range(len(items)):
        if items[i] == target:
            count = count + 1
    return count


def count_builtin(items, target):
    """Version B: Using list's count method"""
    return items.count(target)


def analysis_count():
    # YOUR ANALYSIS
    #
    # Version B is just one line! Is simpler always better?

    analysis = {
        "better_version": "?",  # "A" or "B"
        "reason": "Because...",
        "advantage_of_A": "...",  # What can you learn from the verbose version?
    }

    return analysis


# ============================================================
# PART 2: IMPROVEMENT - Simplify Verbose Code
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Now apply what you learned. Simplify these verbose functions.


def original_1(names):
    """ORIGINAL: Find all names starting with a specific letter"""
    # This code finds names starting with "A"
    result = []
    for i in range(len(names)):
        name = names[i]
        if name[0] == "A":
            result.append(names[i])
    return result


def simplified_1(names):
    # SIMPLIFY THIS
    #
    # Improvements to make:
    # 1. Iterate directly over names (no need for range/index)
    # 2. Use the loop variable directly in append
    #
    # Hint: for name in names: if name[0] == "A": result.append(name)

    pass  # Replace with simplified version


def original_2(numbers):
    """ORIGINAL: Get the largest number"""
    if len(numbers) == 0:
        return None
    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest


def simplified_2(numbers):
    # SIMPLIFY THIS
    #
    # Improvements to make:
    # 1. Iterate directly over elements
    # 2. Use "for num in numbers:" instead of range
    #
    # Keep the empty list check!
    # Alternative: Python has max() built-in, but practice the loop first.

    pass  # Replace with simplified version


def original_3(items):
    """ORIGINAL: Check if any item is "special" """
    found = False
    for i in range(len(items)):
        if items[i] == "special":
            found = True
    return found


def simplified_3(items):
    # SIMPLIFY THIS
    #
    # Improvements to make:
    # 1. Iterate directly
    # 2. Return immediately when found (no need to keep looping!)
    # 3. Alternative: use "in" operator
    #
    # Two valid simplifications:
    # Option A: Loop with early return
    # Option B: return "special" in items

    pass  # Replace with simplified version


def verify_simplifications():
    """Test that simplified versions produce same results as originals"""
    test_names = ["Alice", "Bob", "Anna", "Charlie", "Alex"]
    test_numbers = [5, 2, 9, 1, 7]
    test_items = ["normal", "special", "normal"]

    print("Testing original_1 vs simplified_1:")
    print(f"  Original: {original_1(test_names)}")
    print(f"  Simplified: {simplified_1(test_names)}")

    print("\nTesting original_2 vs simplified_2:")
    print(f"  Original: {original_2(test_numbers)}")
    print(f"  Simplified: {simplified_2(test_numbers)}")

    print("\nTesting original_3 vs simplified_3:")
    print(f"  Original: {original_3(test_items)}")
    print(f"  Simplified: {simplified_3(test_items)}")


def main():
    print("=" * 60)
    print("THE UPGRADE: Cleaner List Code")
    print("=" * 60)

    print("\n--- PART 1: EVALUATION ---")
    print("{{CONTEXT_EVALUATION_INTRO}}")

    print("\n=== Comparison 1: Summing ===")
    test_nums = [10, 20, 30, 40]
    print(f"sum_verbose({test_nums}): {sum_verbose(test_nums)}")
    print(f"sum_pythonic({test_nums}): {sum_pythonic(test_nums)}")
    print(f"Your analysis: {analysis_sum()}")

    print("\n=== Comparison 2: Doubling ===")
    print(f"double_verbose({test_nums}): {double_verbose(test_nums)}")
    print(f"double_simple({test_nums}): {double_simple(test_nums)}")
    print(f"Your analysis: {analysis_double()}")

    print("\n=== Comparison 3: Counting ===")
    test_items = ["a", "b", "a", "c", "a"]
    print(f"count_verbose({test_items}, 'a'): {count_verbose(test_items, 'a')}")
    print(f"count_builtin({test_items}, 'a'): {count_builtin(test_items, 'a')}")
    print(f"Your analysis: {analysis_count()}")

    print("\n--- PART 2: IMPROVEMENT ---")
    print("{{CONTEXT_IMPROVEMENT_INTRO}}")
    # verify_simplifications()  # Uncomment after implementing

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")


main()
