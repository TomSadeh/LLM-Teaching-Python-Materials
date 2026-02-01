# Exercise 1: Decode the Error - Syntax Errors
#
# Each exercise shows an error message and the code that caused it.
# Your job: Understand the error and fix the code WITHOUT running it first.
#
# Theme: {{hero}}'s first day learning magic at {{school}}


# ============================================================
# ERROR DECODE A: Missing Quotes
# ============================================================
"""
ERROR MESSAGE:
--------------
  File "spell_practice.py", line 2
    spell_name = {{spell1}}
                 ^
SyntaxError: invalid syntax
"""


def buggy_code_a():
    """The code that caused the error"""
    spell_name = {{spell1}}
    print(spell_name)


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: Text needs to be wrapped in something special)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE B: Missing Colon
# ============================================================
"""
ERROR MESSAGE:
--------------
  File "counting.py", line 1
    for i in range(5)
                    ^
SyntaxError: expected ':'
"""


def buggy_code_b():
    """The code that caused the error"""
    for i in range(5)
        print(i)


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: What's missing at the end of the for line?)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE C: Unmatched Parenthesis
# ============================================================
"""
ERROR MESSAGE:
--------------
  File "greeting.py", line 1
    print("{{greeting}}, {{hero}}!"
         ^
SyntaxError: '(' was never closed
"""


def buggy_code_c():
    """The code that caused the error"""
    print("{{greeting}}, {{hero}}!"


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: Count the parentheses)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE D: Indentation Error
# ============================================================
"""
ERROR MESSAGE:
--------------
  File "loop.py", line 2
    print(i)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
"""


def buggy_code_d():
    """The code that caused the error"""
    for i in range(3):
    print(i)


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: What should happen after a colon?)
    #
    # Write the fixed code below:
    pass


# ============================================================
# BONUS: Multiple Syntax Errors
# ============================================================
"""
This code has 3 different syntax errors. Find and fix them all!

def introduce_wizard()
    name = {{hero}}
    print("I am " + name
"""


def fix_all_syntax_errors():
    # ✏️ FIND AND FIX ALL 3 ERRORS ✏️
    #
    # Error 1: _______________
    # Error 2: _______________
    # Error 3: _______________
    #
    # Write the fully fixed code below:
    pass


def main():
    print("=== Decode the Error: Syntax Errors ===")
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()

    # Uncomment each to test after fixing:
    # print("Testing A:"); fix_code_a()
    # print("Testing B:"); fix_code_b()
    # print("Testing C:"); fix_code_c()
    # print("Testing D:"); fix_code_d()
    # print("Testing Bonus:"); fix_all_syntax_errors()


main()
