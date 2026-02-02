# Exercise 1: Bug Hunt - List Manipulation
#
# {{villain}} has cursed these list spells with bugs!
# Each function has exactly ONE bug hiding in it.
# Read the story, find the bug, and fix it.
#
# DO NOT run the code first - use your detective skills!


# ============================================================
# BUG HUNT A: The Nested Accident
# ============================================================
"""
STORY:
{{hero}} tried to combine two spell lists into one,
but ended up with a list inside a list!

EXPECTED BEHAVIOR:
Combining ["{{spell1}}", "{{spell2}}"] and ["{{spell3}}"]
should give ["{{spell1}}", "{{spell2}}", "{{spell3}}"]

ACTUAL BEHAVIOR:
Result is ["{{spell1}}", "{{spell2}}", ["{{spell3}}"]]
(The second list is nested inside!)
"""

def buggy_combine():
    spells = ["{{spell1}}", "{{spell2}}"]
    more_spells = ["{{spell3}}"]
    spells.append(more_spells)  # BUG IS HERE
    return spells


def fix_combine():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: append() vs extend() - what's the difference?
    #
    # The fix:
    spells = ["{{spell1}}", "{{spell2}}"]
    more_spells = ["{{spell3}}"]

    pass  # Your code here

    return spells


# ============================================================
# BUG HUNT B: The Off-By-One Index
# ============================================================
"""
STORY:
{{friend}} wants to get the THIRD item from the inventory,
but keeps getting the wrong one!

EXPECTED BEHAVIOR:
From ["wand", "cloak", "map", "stone"], get "map" (the third item)

ACTUAL BEHAVIOR:
Gets "stone" instead (the fourth item)
"""

def buggy_get_third():
    items = ["wand", "cloak", "map", "stone"]
    third_item = items[3]  # BUG IS HERE
    return third_item


def fix_get_third():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: Python lists start at index 0!
    #
    # The fix:
    items = ["wand", "cloak", "map", "stone"]

    pass  # Your code here


# ============================================================
# BUG HUNT C: The Vanishing Sum
# ============================================================
"""
STORY:
{{mentor}} wrote a spell to add up all the points,
but it always returns 0!

EXPECTED BEHAVIOR:
Sum of [10, 20, 30] should be 60

ACTUAL BEHAVIOR:
Always returns 0, no matter what numbers are in the list.
"""

def buggy_sum(numbers):
    total = 0
    for num in numbers:
        total = num  # BUG IS HERE
    return total


def fix_sum(numbers):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: We want to ADD to total, not replace it
    #
    # The fix:
    total = 0

    pass  # Your code here

    return total


# ============================================================
# BUG HUNT D: The Backwards Filter
# ============================================================
"""
STORY:
{{hero}} wrote a spell to find all passing scores (60 or above),
but it's returning the FAILING scores instead!

EXPECTED BEHAVIOR:
From [85, 42, 91, 55], return [85, 91]

ACTUAL BEHAVIOR:
Returns [42, 55] (the failing scores)
"""

def buggy_filter_passing(scores):
    passing = []
    for score in scores:
        if score < 60:  # BUG IS HERE
            passing.append(score)
    return passing


def fix_filter_passing(scores):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: We want scores >= 60, not < 60
    #
    # The fix:
    passing = []

    pass  # Your code here

    return passing


# ============================================================
# BUG HUNT E: The Missing Return
# ============================================================
"""
STORY:
{{friend}} wrote a spell to double all numbers in a list,
but it returns None instead of the doubled list!

EXPECTED BEHAVIOR:
double_all([1, 2, 3]) should return [2, 4, 6]

ACTUAL BEHAVIOR:
Returns None (nothing)
"""

def buggy_double_all(numbers):
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    # BUG: Something is missing here!


def fix_double_all(numbers):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: What should happen at the end of the function?
    #
    # The fix:
    doubled = []

    pass  # Your code here


def main():
    print("=== Bug Hunt: List Manipulation ===")
    print()
    print("Each function has exactly ONE bug.")
    print("Find the bug, then write the fix.")
    print()
    print("="*50)

    # Test the buggy versions:
    print("\nBuggy Combine:", buggy_combine())
    print("  Expected: ['{{spell1}}', '{{spell2}}', '{{spell3}}']")

    print("\nBuggy Get Third:", buggy_get_third())
    print("  Expected: map")

    print("\nBuggy Sum [10,20,30]:", buggy_sum([10, 20, 30]))
    print("  Expected: 60")

    print("\nBuggy Filter [85,42,91,55]:", buggy_filter_passing([85, 42, 91, 55]))
    print("  Expected: [85, 91]")

    print("\nBuggy Double All [1,2,3]:", buggy_double_all([1, 2, 3]))
    print("  Expected: [2, 4, 6]")

    print("\n" + "="*50)
    print("Now fix each function and test your fixes!")


main()
