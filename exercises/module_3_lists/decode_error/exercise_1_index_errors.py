# =============================================================================
# Decode the Error: Index Errors
# =============================================================================
# Difficulty: 2
# Concepts: IndexError, list bounds, understanding error messages
# =============================================================================

"""
{{CONTEXT_DECODE_ERROR_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{ERROR_1_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_1_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "inventory.py", line 4, in <module>
    print(items[3])
IndexError: list index out of range
"""


def buggy_code_a():
    """The code that caused the error"""
    items = ["{{item}}", "potion", "key"]
    print(items[3])  # BUG: Index 3 doesn't exist!


def fix_code_a():
    # FIX THE CODE
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # Hint: The list has 3 items. What are the valid indices?
    # Count them: index 0, index 1, index 2 (that's it!)
    #
    # Now write the fixed code to print the LAST item:

    pass


# ============================================================
# {{ERROR_2_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "team.py", line 5, in <module>
    print(team[team_size])
IndexError: list index out of range
"""


def buggy_code_b():
    """The code that caused the error"""
    team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    team_size = len(team)  # team_size = 3
    print(team[team_size])  # BUG: team[3] doesn't exist!


def fix_code_b():
    # FIX THE CODE
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # Hint: len() returns 3, but indices go from 0 to 2.
    # To get the last element, use len() - 1.
    #
    # Now write the fixed code:

    pass


# ============================================================
# {{ERROR_3_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_3_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "empty.py", line 3, in <module>
    print(inventory[0])
IndexError: list index out of range
"""


def buggy_code_c():
    """The code that caused the error"""
    inventory = []  # Empty list!
    print(inventory[0])  # BUG: Can't access index 0 of empty list


def fix_code_c():
    # FIX THE CODE
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # Hint: An empty list has NO valid indices.
    # You can check if a list is empty with: if len(list) > 0:
    #
    # Fix by checking if the list has items before accessing:

    pass


# ============================================================
# {{ERROR_4_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_4_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "loop.py", line 4, in <module>
    print(f"Item {i}: {items[i]}")
IndexError: list index out of range
"""


def buggy_code_d():
    """The code that caused the error"""
    abilities = ["{{spell1}}", "{{spell2}}"]
    for i in range(3):  # BUG: range goes 0, 1, 2 but list only has indices 0, 1
        print(f"Item {i}: {abilities[i]}")


def fix_code_d():
    # FIX THE CODE
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # Hint: range(3) gives [0, 1, 2] but the list only has indices 0 and 1.
    # Use len(items) to get the correct range.
    #
    # Now write the fixed code:

    pass


def main():
    print("{{CONTEXT_DECODE_ERROR_INTRO}}")
    print("=" * 50)
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()

    print("=== {{ERROR_1_TITLE}} ===")
    # Uncomment to test after fixing:
    # fix_code_a()

    print("\n=== {{ERROR_2_TITLE}} ===")
    # fix_code_b()

    print("\n=== {{ERROR_3_TITLE}} ===")
    # fix_code_c()

    print("\n=== {{ERROR_4_TITLE}} ===")
    # fix_code_d()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
