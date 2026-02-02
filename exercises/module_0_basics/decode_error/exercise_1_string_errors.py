# =============================================================================
# Decode the Error: String Errors
# =============================================================================
# Difficulty: 3
# Concepts: TypeError, quote matching, string + number errors
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
  File "program.py", line 3, in <module>
    message = "Welcome to " + school_name + ", " + hero_name
TypeError: can only concatenate str (not "int") to str
"""


def buggy_code_a():
    """The code that caused the error"""
    school_name = 42
    hero_name = "{{hero}}"
    message = "Welcome to " + school_name + ", " + hero_name
    print(message)


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Hint: Look at what type school_name is. Can you concatenate (+)
    # a string with a number directly?
    #
    # Write the fixed code below:

    pass


# ============================================================
# {{ERROR_2_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
  File "program.py", line 2
    greeting = "Hello, {{hero}}!
                                ^
SyntaxError: unterminated string literal
"""


def buggy_code_b():
    """The code that caused the error (this is a representation)"""
    # The actual buggy code would be:
    # greeting = "Hello, {{hero}}!
    # print(greeting)
    pass


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Hint: String literals need both an opening and closing quote.
    #
    # Write the fixed code below:

    pass


# ============================================================
# {{ERROR_3_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_3_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "program.py", line 3, in <module>
    print("Score: " + score)
TypeError: can only concatenate str (not "int") to str
"""


def buggy_code_c():
    """The code that caused the error"""
    score = 100
    print("Score: " + score)


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Hint: There are two ways to fix this:
    # 1. Convert score to a string using str()
    # 2. Use a comma instead of + in print()
    #
    # Write the fixed code below (try both solutions!):

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
