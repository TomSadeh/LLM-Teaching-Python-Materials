"""
{{CONTEXT_DECODE_ERROR_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to understand and fix KeyError,
one of the most common errors when working with dictionaries.
"""


# ============================================================
# {{ERROR_1_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_1_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "registry.py", line 8, in <module>
    print(registry["{{spell3}}"])
KeyError: '{{spell3}}'
"""


def buggy_code_a():
    """The code that caused the error."""
    registry = {
        "{{spell1}}": "basic",
        "{{spell2}}": "intermediate"
    }

    # This line causes the error
    print(registry["{{spell3}}"])


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_1}}
    #
    # Fix option 1: Add the missing key to the dictionary
    # Fix option 2: Check if the key exists before accessing
    # Fix option 3: Use .get() method with a default value
    #
    # Choose one approach and write the fixed code:

    pass


# ============================================================
# {{ERROR_2_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "scores.py", line 6, in <module>
    print(f"Score: {scores[player_name]}")
KeyError: 'unknown_player'
"""


def buggy_code_b():
    """The code that caused the error."""
    scores = {
        "{{hero}}": 100,
        "{{heroine}}": 150
    }

    player_name = "unknown_player"  # This name isn't in the dictionary
    print(f"Score: {scores[player_name]}")


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_2}}
    #
    # This is a common pattern: accessing a dictionary with user input.
    # The key might not exist! Write code that handles this gracefully.
    #
    # Hint: Use `in` to check if a key exists: if key in dictionary:
    #       Or use .get(key, default_value)

    pass


# ============================================================
# {{ERROR_3_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_3_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "inventory.py", line 9, in <module>
    inventory[item] += 1
KeyError: '{{item}}'
"""


def buggy_code_c():
    """The code that caused the error."""
    inventory = {}

    items_found = ["{{spell1}}", "{{item}}", "{{spell1}}"]

    for item in items_found:
        # Trying to increment, but key doesn't exist yet!
        inventory[item] += 1

    print(inventory)


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_3}}
    #
    # This is the "counting pattern" - you need to handle
    # the first occurrence of each item specially.
    #
    # Fix using .get(): inventory[item] = inventory.get(item, 0) + 1
    # This returns 0 if the key doesn't exist, then adds 1.

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

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
