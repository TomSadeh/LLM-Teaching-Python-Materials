"""
{{CONTEXT_DECODE_ERROR_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to understand and fix errors
that occur when working with nested dictionaries.
"""


# ============================================================
# {{ERROR_1_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_1_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "config.py", line 8, in <module>
    volume = settings["audio"]["volume"]
KeyError: 'audio'
"""


def buggy_code_a():
    """The code that caused the error."""
    settings = {
        "display": {"brightness": 80, "resolution": "1080p"},
        "controls": {"sensitivity": 5}
    }

    # Trying to access audio settings that don't exist
    volume = settings["audio"]["volume"]
    print(f"Volume: {volume}")


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_1}}
    #
    # Option 1: Add the missing "audio" key to settings
    # Option 2: Check if "audio" exists before accessing
    # Option 3: Use .get() with a default value
    #
    # Write a version that handles missing nested keys gracefully:

    pass


# ============================================================
# {{ERROR_2_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "profile.py", line 7, in <module>
    health = characters["{{hero}}"]["stats"]["health"]
TypeError: 'NoneType' object is not subscriptable
"""


def buggy_code_b():
    """The code that caused the error."""
    characters = {
        "{{hero}}": None,  # Character data not loaded yet!
        "{{heroine}}": {"stats": {"health": 100, "mana": 50}}
    }

    # This crashes because characters["{{hero}}"] is None
    health = characters["{{hero}}"]["stats"]["health"]
    print(f"Health: {health}")


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_2}}
    #
    # The error message says "NoneType object is not subscriptable"
    # This means we tried to use ["stats"] on None.
    #
    # Fix by checking if the character data exists before accessing:

    pass


# ============================================================
# {{ERROR_3_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_3_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "inventory.py", line 10, in <module>
    player_data["inventory"]["{{item}}"] += 1
KeyError: '{{item}}'
"""


def buggy_code_c():
    """The code that caused the error."""
    player_data = {
        "name": "{{hero}}",
        "inventory": {
            "{{spell1}}": 3
        }
    }

    # Trying to add to an item that doesn't exist in inventory
    player_data["inventory"]["{{item}}"] += 1
    print(player_data["inventory"])


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_3}}
    #
    # The nested dictionary exists (inventory), but the key
    # "{{item}}" doesn't exist within it.
    #
    # Use .get() on the inner dictionary:
    # player_data["inventory"]["{{item}}"] = player_data["inventory"].get("{{item}}", 0) + 1

    pass


# ============================================================
# {{ERROR_4_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_4_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "game.py", line 8, in <module>
    abilities["{{hero}}"]["{{spell1}}"]["power"] = 20
KeyError: '{{spell1}}'
"""


def buggy_code_d():
    """The code that caused the error."""
    abilities = {
        "{{hero}}": {},  # Empty dict - no abilities yet!
        "{{heroine}}": {"{{spell1}}": {"power": 10}}
    }

    # Trying to set a value in a nested dict that doesn't exist
    abilities["{{hero}}"]["{{spell1}}"]["power"] = 20


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_4}}
    #
    # {{hero}}'s abilities dict is empty - "{{spell1}}" doesn't exist.
    # We need to create the entire nested structure.
    #
    # One approach: Check and create each level
    # Another approach: Assign the whole nested dict at once

    pass


def main():
    print("{{CONTEXT_DECODE_ERROR_INTRO}}")
    print("=" * 50)
    print()
    print("Nested dictionary errors are trickier because the problem")
    print("might be at any level of the nesting!")
    print()
    print("For each exercise:")
    print("1. Identify WHICH key caused the error")
    print("2. Understand WHY that key is problematic")
    print("3. Fix the code to handle missing data gracefully")
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
