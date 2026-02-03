"""
{{CONTEXT_DECODE_ERROR_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to understand and fix JSON-related errors,
especially JSONDecodeError which occurs when parsing invalid JSON.

Topic: JSON error interpretation
Difficulty: 3
"""

import json


# ============================================================
# {{ERROR_1_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_1_NARRATIVE}}
#
# The most common JSON error: malformed JSON syntax.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "load_config.py", line 3, in <module>
    config = json.load(f)
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 2 column 5 (char 6)
"""


def buggy_code_a():
    """The JSON file that caused the error."""
    # The file "config.json" contains:
    # {
    #     name: "{{hero}}"
    # }
    # Notice: 'name' should be "name" (double quotes required!)

    with open("config.json", "r") as f:
        config = json.load(f)


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_1}}
    #
    # JSON REQUIRES double quotes for all strings and keys!
    # Unlike Python, you cannot use single quotes or unquoted keys.
    #
    # Wrong: {name: "value"}      - unquoted key
    # Wrong: {"name": 'value'}    - single quotes
    # Right: {"name": "value"}    - double quotes everywhere
    #
    # Fix: Correct the JSON file content, or handle the error:
    #   try:
    #       with open("config.json", "r") as f:
    #           config = json.load(f)
    #   except json.JSONDecodeError as e:
    #       print(f"Invalid JSON: {e}")
    #       config = {"default": "settings"}

    pass


# ============================================================
# {{ERROR_2_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# Trailing commas cause JSON errors (unlike Python).

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "load_list.py", line 3, in <module>
    data = json.load(f)
json.decoder.JSONDecodeError: Expecting value: line 5 column 1 (char 42)
"""


def buggy_code_b():
    """The JSON file that caused the error."""
    # The file "items.json" contains:
    # {
    #     "items": [
    #         "{{spell1}}",
    #         "{{spell2}}",
    #     ]
    # }
    # Notice: Trailing comma after "{{spell2}}" is not allowed!

    with open("items.json", "r") as f:
        data = json.load(f)


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_2}}
    #
    # JSON does NOT allow trailing commas (Python does).
    #
    # Wrong: ["a", "b", "c",]   - trailing comma
    # Right: ["a", "b", "c"]    - no trailing comma
    #
    # This is a common mistake when copy-pasting from Python code!

    pass


# ============================================================
# {{ERROR_3_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# Empty or truncated files cause JSON errors.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "load_save.py", line 3, in <module>
    save_data = json.load(f)
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
"""


def buggy_code_c():
    """The code that caused the error."""
    # The file "save.json" is empty or corrupted (incomplete write)

    with open("save.json", "r") as f:
        save_data = json.load(f)


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_3}}
    #
    # The file is empty or contains no valid JSON.
    # This can happen if:
    # - File was never written to
    # - Write operation was interrupted
    # - File was accidentally cleared
    #
    # Fix: Check for empty file or handle the error:
    #   try:
    #       with open("save.json", "r") as f:
    #           content = f.read()
    #           if not content.strip():
    #               save_data = {}  # Default for empty file
    #           else:
    #               save_data = json.loads(content)
    #   except json.JSONDecodeError:
    #       save_data = {}  # Default for corrupt file

    pass


# ============================================================
# {{ERROR_4_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_4_NARRATIVE}}
#
# Type errors when working with JSON data.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "process_data.py", line 6, in <module>
    level = data["level"] + 1
TypeError: can only concatenate str (not "int") to str
"""


def buggy_code_d():
    """The code that caused the error."""
    json_string = '{"name": "{{hero}}", "level": "5"}'  # Note: "5" is a string!

    data = json.loads(json_string)
    level = data["level"] + 1  # Error: "5" + 1 doesn't work


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_4}}
    #
    # The JSON had "5" (string) instead of 5 (number).
    # JSON preserves types, so if it's a string in JSON, it's a string in Python.
    #
    # Fix option 1: Fix the JSON source
    #   json_string = '{"name": "{{hero}}", "level": 5}'  # No quotes around 5
    #
    # Fix option 2: Convert when using
    #   level = int(data["level"]) + 1

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
    print("JSONDecodeError - missing quotes on keys")
    # Uncomment to test after fixing:
    # fix_code_a()

    print("\n=== {{ERROR_2_TITLE}} ===")
    print("JSONDecodeError - trailing comma")
    # fix_code_b()

    print("\n=== {{ERROR_3_TITLE}} ===")
    print("JSONDecodeError - empty/corrupt file")
    # fix_code_c()

    print("\n=== {{ERROR_4_TITLE}} ===")
    print("TypeError - wrong data type from JSON")
    # fix_code_d()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
    print()
    print("Key differences between JSON and Python:")
    print("  1. JSON keys MUST be double-quoted strings")
    print("  2. JSON strings MUST use double quotes")
    print("  3. JSON does NOT allow trailing commas")
    print("  4. JSON has: true, false, null (not True, False, None)")
    print("  5. JSON numbers can be strings - watch for type issues!")


main()
