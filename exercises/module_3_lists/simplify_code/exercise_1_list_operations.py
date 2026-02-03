# =============================================================================
# Simplify This: List Operations
# =============================================================================
# Difficulty: 4
# Concepts: Pythonic patterns, cleaner list code
# =============================================================================

"""
{{CONTEXT_SIMPLIFY_CODE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{SIMPLIFY_1_TITLE}}
# ============================================================
# {{CONTEXT_SIMPLIFY_1_NARRATIVE}}


def original_1():
    """ORIGINAL: Build a list by iterating with indices"""
    names = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]

    uppercase_names = []
    for i in range(len(names)):
        uppercase_names.append(names[i].upper())

    print(f"Result: {uppercase_names}")
    return uppercase_names


def simplified_1():
    # SIMPLIFY THIS
    #
    # Improvement: Iterate directly over elements, not indices.
    # Change: for i in range(len(names)) -> for name in names
    #
    # Hint: You don't need the index at all!

    names = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]

    # YOUR SIMPLIFIED CODE HERE
    pass


# ============================================================
# {{SIMPLIFY_2_TITLE}}
# ============================================================
# {{CONTEXT_SIMPLIFY_2_NARRATIVE}}


def original_2():
    """ORIGINAL: Check if item exists with a loop"""
    inventory = ["{{item}}", "potion", "key", "map"]
    target = "potion"

    found = False
    for i in range(len(inventory)):
        if inventory[i] == target:
            found = True

    if found == True:
        print(f"{target} is in inventory")
    else:
        print(f"{target} is NOT in inventory")

    return found


def simplified_2():
    # SIMPLIFY THIS
    #
    # Improvements:
    # 1. Use "in" operator instead of loop
    # 2. Use "if found:" instead of "if found == True:"
    #
    # Hint: found = target in inventory

    inventory = ["{{item}}", "potion", "key", "map"]
    target = "potion"

    # YOUR SIMPLIFIED CODE HERE
    pass


# ============================================================
# {{SIMPLIFY_3_TITLE}}
# ============================================================
# {{CONTEXT_SIMPLIFY_3_NARRATIVE}}


def original_3():
    """ORIGINAL: Count items manually"""
    scores = [85, 42, 91, 67, 38, 95, 73, 88]
    passing_threshold = 60

    passing_count = 0
    for i in range(len(scores)):
        if scores[i] >= passing_threshold:
            passing_count = passing_count + 1

    print(f"Passing scores: {passing_count} out of {len(scores)}")
    return passing_count


def simplified_3():
    # SIMPLIFY THIS
    #
    # Improvements:
    # 1. Iterate directly over scores
    # 2. Use += instead of count = count + 1
    #
    # Hint: for score in scores: if score >= threshold: count += 1

    scores = [85, 42, 91, 67, 38, 95, 73, 88]
    passing_threshold = 60

    # YOUR SIMPLIFIED CODE HERE
    pass


# ============================================================
# {{SIMPLIFY_4_TITLE}}
# ============================================================
# {{CONTEXT_SIMPLIFY_4_NARRATIVE}}


def original_4():
    """ORIGINAL: Get first N items verbose way"""
    items = ["{{spell1}}", "{{spell2}}", "{{spell3}}", "{{spell4}}"]
    n = 2

    first_n = []
    for i in range(n):
        first_n.append(items[i])

    print(f"First {n} items: {first_n}")
    return first_n


def simplified_4():
    # SIMPLIFY THIS
    #
    # Improvement: Use slicing instead of loop
    #
    # Hint: first_n = items[:n]

    items = ["{{spell1}}", "{{spell2}}", "{{spell3}}", "{{spell4}}"]
    n = 2

    # YOUR SIMPLIFIED CODE HERE
    pass


# ============================================================
# {{SIMPLIFY_5_TITLE}}
# ============================================================
# {{CONTEXT_SIMPLIFY_5_NARRATIVE}}


def original_5():
    """ORIGINAL: Reverse a list manually"""
    original = [1, 2, 3, 4, 5]

    reversed_list = []
    for i in range(len(original) - 1, -1, -1):
        reversed_list.append(original[i])

    print(f"Original: {original}")
    print(f"Reversed: {reversed_list}")
    return reversed_list


def simplified_5():
    # SIMPLIFY THIS
    #
    # Improvement: Use slice with step -1
    #
    # Hint: reversed_list = original[::-1]

    original = [1, 2, 3, 4, 5]

    # YOUR SIMPLIFIED CODE HERE
    pass


# ============================================================
# {{SIMPLIFY_6_TITLE}}
# ============================================================
# {{CONTEXT_SIMPLIFY_6_NARRATIVE}}


def original_6():
    """ORIGINAL: Copy a list manually"""
    original = ["{{item}}", "potion", "key"]

    copy = []
    for i in range(len(original)):
        copy.append(original[i])

    # Verify it's a copy
    original.append("map")
    print(f"Original: {original}")
    print(f"Copy: {copy}")

    return copy


def simplified_6():
    # SIMPLIFY THIS
    #
    # Improvement: Use slicing or list() to copy
    #
    # Options:
    # 1. copy = original[:]
    # 2. copy = list(original)
    # 3. copy = original.copy()

    original = ["{{item}}", "potion", "key"]

    # YOUR SIMPLIFIED CODE HERE
    pass


def main():
    print("{{CONTEXT_SIMPLIFY_CODE_INTRO}}")
    print("=" * 50)

    print("\n=== {{SIMPLIFY_1_TITLE}} ===")
    print("Original:")
    original_1()
    print("Simplified:")
    # simplified_1()

    print("\n=== {{SIMPLIFY_2_TITLE}} ===")
    print("Original:")
    original_2()
    print("Simplified:")
    # simplified_2()

    print("\n=== {{SIMPLIFY_3_TITLE}} ===")
    print("Original:")
    original_3()
    print("Simplified:")
    # simplified_3()

    print("\n=== {{SIMPLIFY_4_TITLE}} ===")
    print("Original:")
    original_4()
    print("Simplified:")
    # simplified_4()

    print("\n=== {{SIMPLIFY_5_TITLE}} ===")
    print("Original:")
    original_5()
    print("Simplified:")
    # simplified_5()

    print("\n=== {{SIMPLIFY_6_TITLE}} ===")
    print("Original:")
    original_6()
    print("Simplified:")
    # simplified_6()

    print("\n" + "=" * 50)
    print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")


main()
