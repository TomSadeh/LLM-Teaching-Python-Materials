# =============================================================================
# TEMPLATE: Decode the Error
# =============================================================================
#
# PURPOSE: Students interpret error messages and fix code.
# SKILL: Error literacy, debugging, understanding Python errors
#
# STRUCTURE:
#   - Show an error message (as if from terminal)
#   - Show the code that caused it
#   - Student explains the error and provides the fix
#   - NO running code first - pure interpretation
#
# GUIDELINES:
#   - Use REAL Python error messages (copy exact format)
#   - Error should be SOLVABLE from the message + code
#   - Include line numbers in traceback
#   - Start with common errors, progress to obscure ones
#
# ERROR TYPES TO COVER:
#   - SyntaxError (missing colon, unmatched parenthesis)
#   - NameError (undefined variable, typo)
#   - TypeError (wrong type operations)
#   - ValueError (right type, wrong value)
#   - IndexError (list index out of range)
#   - KeyError (missing dictionary key)
#   - AttributeError (wrong method/attribute)
#   - IndentationError (wrong indentation)
#   - ZeroDivisionError
#   - FileNotFoundError
#
# DIFFICULTY SCALING:
#   - Easy: Error message directly points to problem
#   - Medium: Need to understand the context
#   - Hard: Error is a symptom of a problem elsewhere
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_DECODE_ERROR_INTRO}}   - Main intro for error decoding exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Error:
#   {{ERROR_N_TITLE}}                - Title for error N (1, 2, 3...)
#   {{CONTEXT_ERROR_N_NARRATIVE}}    - Story/context for error N
#   {{CONTEXT_ERROR_HINT_N}}         - Hint for error N
#
# Closing:
#   {{CONTEXT_INVESTIGATION_COMPLETE}} - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
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
  File "[filename].py", line [N], in <module>
    [line of code that errored]
[ErrorType]: [error description]
"""


def buggy_code_a():
    """The code that caused the error"""
    # [CODE WITH THE BUG]
    pass


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_1}}
    #
    # Now write the fixed code:

    # [STUDENT WRITES FIXED VERSION]
    pass


# ============================================================
# {{ERROR_2_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
[Another error message]
"""


def buggy_code_b():
    """The code that caused the error"""
    pass


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_2}}
    pass


# [REPEAT PATTERN FOR MORE ERRORS]


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

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()


# =============================================================================
# ERROR MESSAGE FORMATS:
# =============================================================================
#
# SYNTAX ERROR (shows caret):
#   File "file.py", line 3
#       for i in range(10)
#                        ^
#   SyntaxError: expected ':'
#
# NAME ERROR:
#   Traceback (most recent call last):
#     File "file.py", line 5, in <module>
#       print(mesage)
#   NameError: name 'mesage' is not defined
#
# TYPE ERROR:
#   Traceback (most recent call last):
#     File "file.py", line 3, in <module>
#       result = "hello" + 5
#   TypeError: can only concatenate str (not "int") to str
#
# VALUE ERROR:
#   Traceback (most recent call last):
#     File "file.py", line 2, in <module>
#       num = int("hello")
#   ValueError: invalid literal for int() with base 10: 'hello'
#
# INDEX ERROR:
#   Traceback (most recent call last):
#     File "file.py", line 3, in <module>
#       print(items[5])
#   IndexError: list index out of range
#
# KEY ERROR:
#   Traceback (most recent call last):
#     File "file.py", line 3, in <module>
#       print(data["missing"])
#   KeyError: 'missing'
#
# ATTRIBUTE ERROR:
#   Traceback (most recent call last):
#     File "file.py", line 2, in <module>
#       items.add("new")
#   AttributeError: 'list' object has no attribute 'add'
#
# INDENTATION ERROR:
#   File "file.py", line 3
#       print(x)
#       ^
#   IndentationError: expected an indented block after 'for' statement
#
# =============================================================================
