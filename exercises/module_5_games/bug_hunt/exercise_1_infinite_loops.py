"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}

Topic: Finding infinite loop bugs
Difficulty: 1-2

Infinite loops are one of the most common bugs when learning while loops.
In this exercise, you'll find and fix loops that never end.
"""


# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# {{hero}} wrote this code to count items, but it runs forever!
#
# EXPECTED BEHAVIOR:
# Print numbers 1 through 5, then stop
#
# ACTUAL BEHAVIOR:
# Prints 1 forever without stopping
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}


def buggy_counter():
    """This code has exactly ONE bug. Find it!"""
    count = 1
    while count <= 5:
        print(count)
        # The counter never changes! Loop runs forever.


def fix_counter():
    """
    Fix the infinite loop.

    Expected output:
        1
        2
        3
        4
        5
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# This countdown should go from 5 to 1, but something's wrong.
#
# EXPECTED BEHAVIOR:
# Print 5, 4, 3, 2, 1, "Done!"
#
# ACTUAL BEHAVIOR:
# Counts the wrong direction and never reaches 0
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}


def buggy_countdown():
    """This code has exactly ONE bug. Find it!"""
    num = 5
    while num > 0:
        print(num)
        num += 1  # Oops! Going the wrong way!


def fix_countdown():
    """
    Fix the countdown direction.

    Expected output:
        5
        4
        3
        2
        1
        Done!
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# This loop should process a list, but it never terminates.
#
# EXPECTED BEHAVIOR:
# Process each item and stop when list is empty
#
# ACTUAL BEHAVIOR:
# The list never gets shorter
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}


def buggy_list_processor():
    """This code has exactly ONE bug. Find it!"""
    items = ["{{item}}", "{{pet}}", "{{creature}}"]
    index = 0
    while index < len(items):
        print(f"Processing: {items[index]}")
        # Forgot to move to next item!


def fix_list_processor():
    """
    Fix the list processor.

    Expected output:
        Processing: {{item}}
        Processing: {{pet}}
        Processing: {{creature}}
        All items processed!
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# This accumulator should add up numbers, but it loops forever.
#
# EXPECTED BEHAVIOR:
# Add numbers until total exceeds 20, then stop
#
# ACTUAL BEHAVIOR:
# Total never changes, condition never becomes False
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}


def buggy_accumulator():
    """This code has exactly ONE bug. Find it!"""
    total = 0
    amount = 5
    while total < 20:
        print(f"Adding {amount}, total would be {total + amount}")
        # total + amount doesn't save the result!


def fix_accumulator():
    """
    Fix the accumulator.

    Expected output:
        Adding 5, total is now 5
        Adding 5, total is now 10
        Adding 5, total is now 15
        Adding 5, total is now 20
        Final total: 20
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Buggy version (DON'T RUN - infinite loop):")
    print("# buggy_counter()")
    print("\nFixed version:")
    fix_counter()

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Buggy version (DON'T RUN - infinite loop):")
    print("# buggy_countdown()")
    print("\nFixed version:")
    fix_countdown()

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Buggy version (DON'T RUN - infinite loop):")
    print("# buggy_list_processor()")
    print("\nFixed version:")
    fix_list_processor()

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Buggy version (DON'T RUN - infinite loop):")
    print("# buggy_accumulator()")
    print("\nFixed version:")
    fix_accumulator()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
