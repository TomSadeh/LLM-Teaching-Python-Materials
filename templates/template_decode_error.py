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

# Exercise N: Decode the Error - [TOPIC]
#
# Each exercise shows an error message and the code that caused it.
# Your job: Understand the error and fix the code WITHOUT running it first.
#
# Theme: [THEMED CONTEXT USING {{placeholders}}]


# ============================================================
# ERROR DECODE [LETTER]: [ERROR TYPE]
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "[filename].py", line [N], in <module>
    [line of code that errored]
[ErrorType]: [error description]
"""

def buggy_code_X():
    """The code that caused the error"""
    # [CODE WITH THE BUG]
    pass


def fix_code_X():
    # ✏️ FIX THE CODE ✏️
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # Now write the fixed code:

    # [STUDENT WRITES FIXED VERSION]
    pass


# [REPEAT PATTERN FOR MORE EXERCISES]


# ============================================================
# BONUS: Multiple Errors
# ============================================================
"""
This code has [N] different errors. Find and fix them all.

[SHOW CODE WITH MULTIPLE BUGS]
"""

def fix_all_errors():
    # ✏️ FIND AND FIX ALL ERRORS ✏️
    #
    # Error 1: _______________
    # Error 2: _______________
    # [ETC.]
    #
    # Fixed code:
    pass


def main():
    print("=== Error Decode Exercises ===")
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()

    # Uncomment each to test after fixing:
    # print("Testing [LETTER]:"); fix_code_X()


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
