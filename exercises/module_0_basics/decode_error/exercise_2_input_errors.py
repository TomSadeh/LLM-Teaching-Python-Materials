# =============================================================================
# Decode the Error: Input Errors
# =============================================================================
# Difficulty: 3-4
# Concepts: TypeError with input, ValueError, type conversion
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
    total = price + 10
TypeError: can only concatenate str (not "int") to str
"""


def buggy_code_a():
    """The code that caused the error"""
    price = input("Enter price: ")
    total = price + 10
    print("With tax:", total)


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Hint: What type does input() return? What type do we need for math?
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
Traceback (most recent call last):
  File "program.py", line 2, in <module>
    age = int(age_text)
ValueError: invalid literal for int() with base 10: 'twenty'
"""


def buggy_code_b():
    """The code that caused the error"""
    age_text = "twenty"  # Simulating user typing "twenty"
    age = int(age_text)
    print("Age:", age)


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Hint: int() can only convert strings that contain digits like "20".
    # The word "twenty" cannot be converted to a number.
    #
    # Note: This error happens when a user types text instead of numbers.
    # For this exercise, change the input to a valid number string.
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
  File "program.py", line 4, in <module>
    result = num1 + num2
TypeError: can only concatenate str (not "str") to str
"""


def buggy_code_c():
    """The code that caused the error"""
    num1 = input("First number: ")
    num2 = input("Second number: ")
    result = num1 + num2
    print("Sum:", result)


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Hint: If user types 5 and 3, the current code would print "53"
    # because it concatenates strings instead of adding numbers!
    #
    # Write the fixed code below:

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
