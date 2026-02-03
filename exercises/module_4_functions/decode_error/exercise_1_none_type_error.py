# =============================================================================
# Decode the Error: None Type Errors
# =============================================================================
# Difficulty: 2-3
# Concepts: Return values, None, TypeError when using None
# =============================================================================

"""
{{CONTEXT_DECODE_ERROR_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# Error 1: Missing Return Statement
# ============================================================
# {{CONTEXT_ERROR_1_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "exercise.py", line 8, in <module>
    total = result + 10
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
"""


def buggy_code_a():
    """The code that caused the error"""
    def add_five(number):
        total = number + 5
        print(total)  # Prints the value but doesn't return it!

    result = add_five(10)
    total = result + 10  # This crashes because result is None
    print(total)


def fix_code_a():
    # FIX THE CODE
    #
    # First, explain what caused the error:
    # The error occurred because: The function prints the result but doesn't
    # return it. Without a return statement, functions return None.
    # Then result + 10 tries to add None + 10, which fails.
    #
    # Hint: Change print() to return

    # Write the fixed code:
    pass


# ============================================================
# Error 2: Using None in String Formatting
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "exercise.py", line 7, in <module>
    message = "Result: " + result
TypeError: can only concatenate str (not "NoneType") to str
"""


def buggy_code_b():
    """The code that caused the error"""
    def get_status():
        status = "Active"
        # Forgot to return status!

    result = get_status()
    message = "Result: " + result  # Crashes because result is None
    print(message)


def fix_code_b():
    # FIX THE CODE
    #
    # The error occurred because: _______________
    #
    # Hint: Make sure to return the status value

    # Write the fixed code:
    pass


# ============================================================
# Error 3: Calling Methods on None
# ============================================================
# {{CONTEXT_ERROR_3_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "exercise.py", line 7, in <module>
    upper_name = name.upper()
AttributeError: 'NoneType' object has no attribute 'upper'
"""


def buggy_code_c():
    """The code that caused the error"""
    def get_hero_name():
        hero = "{{hero}}"
        print(f"Hero is: {hero}")
        # Missing return!

    name = get_hero_name()
    upper_name = name.upper()  # Crashes because name is None
    print(upper_name)


def fix_code_c():
    # FIX THE CODE
    #
    # The error occurred because: _______________
    #
    # Hint: Return the hero name so it can be used outside the function

    # Write the fixed code:
    pass


# ============================================================
# Error 4: Using None in a Calculation
# ============================================================
# {{CONTEXT_ERROR_4_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "exercise.py", line 9, in <module>
    final_score = score * 2
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
"""


def buggy_code_d():
    """The code that caused the error"""
    def calculate_score(base, bonus):
        total = base + bonus
        print(f"Score calculated: {total}")
        # Missing return - just prints instead

    score = calculate_score(100, 50)
    final_score = score * 2  # Crashes because score is None
    print(f"Final: {final_score}")


def fix_code_d():
    # FIX THE CODE
    #
    # The error occurred because: _______________
    #
    # Hint: The function prints the total but should return it instead

    # Write the fixed code:
    pass


# ============================================================
# Error 5: Chaining Functions with None
# ============================================================
# {{CONTEXT_ERROR_5_NARRATIVE}}

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "exercise.py", line 13, in <module>
    final = add_bonus(base)
  File "exercise.py", line 7, in add_bonus
    return score + 50
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
"""


def buggy_code_e():
    """The code that caused the error"""
    def get_base_score():
        base = 100
        print(base)  # Prints but doesn't return!

    def add_bonus(score):
        return score + 50

    base = get_base_score()  # base is None
    final = add_bonus(base)  # Passes None to add_bonus, which crashes
    print(final)


def fix_code_e():
    # FIX THE CODE
    #
    # The error occurred because: _______________
    #
    # Hint: The first function needs to return its value

    # Write the fixed code:
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
    print("KEY CONCEPT: When a function doesn't have a return statement,")
    print("it returns None. Using None in operations causes errors!")
    print()

    print("=== Error 1: Missing Return Statement ===")
    print("Original code (has bug):")
    # buggy_code_a()  # Don't run - it will crash
    print("\nYour fix:")
    fix_code_a()

    print("\n=== Error 2: None in String Concatenation ===")
    print("\nYour fix:")
    fix_code_b()

    print("\n=== Error 3: Calling Methods on None ===")
    print("\nYour fix:")
    fix_code_c()

    print("\n=== Error 4: None in Calculation ===")
    print("\nYour fix:")
    fix_code_d()

    print("\n=== Error 5: Chaining Functions ===")
    print("\nYour fix:")
    fix_code_e()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
