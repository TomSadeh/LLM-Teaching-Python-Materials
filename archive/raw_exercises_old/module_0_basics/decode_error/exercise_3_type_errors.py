# Exercise 3: Decode the Error - Type Errors
#
# Each exercise shows an error message and the code that caused it.
# Your job: Understand the error and fix the code WITHOUT running it first.
#
# Theme: {{hero}}'s magical calculations at {{school}}


# ============================================================
# ERROR DECODE A: Concatenating String and Number
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "points.py", line 2, in <module>
    print("You earned " + 100 + " points!")
TypeError: can only concatenate str (not "int") to str
"""


def buggy_code_a():
    """The code that caused the error"""
    print("You earned " + 100 + " points!")


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: You can't use + to combine text and numbers directly)
    #
    # Write the fixed code below:
    # Method 1: Convert number to string with str()
    # Method 2: Use commas in print() instead of +
    pass


# ============================================================
# ERROR DECODE B: Math on a String
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "potion.py", line 3, in <module>
    total = ingredients + 5
TypeError: can only concatenate str (not "int") to str
"""


def buggy_code_b():
    """The code that caused the error"""
    ingredients = input("How many ingredients? ")
    total = ingredients + 5
    print(total)


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: input() always returns a string, even if you type a number!)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE C: Multiplying Incompatible Types
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "spellpower.py", line 3, in <module>
    power = strength * boost
TypeError: can't multiply sequence by non-int of type 'str'
"""


def buggy_code_c():
    """The code that caused the error"""
    strength = "50"
    boost = "2"
    power = strength * boost
    print(power)


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: "50" is text, not a number. 50 is a number!)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE D: Wrong Type for len()
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "count.py", line 2, in <module>
    length = len(count)
TypeError: object of type 'int' has no len()
"""


def buggy_code_d():
    """The code that caused the error"""
    count = 12345
    length = len(count)
    print(f"Number has {length} digits")


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: len() works on strings and lists, not numbers!)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE E: Calling a Non-Callable
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "spell.py", line 2, in <module>
    print(spell())
TypeError: 'str' object is not callable
"""


def buggy_code_e():
    """The code that caused the error"""
    spell = "{{spell1}}"
    print(spell())


def fix_code_e():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: () after a name tries to call it like a function!)
    #
    # Write the fixed code below:
    pass


# ============================================================
# BONUS: Multiple Type Errors
# ============================================================
"""
This code has 2 different type errors. Find and fix them all!

age = input("Enter your age: ")
next_year = age + 1
print("Next year you'll be " + next_year)
"""


def fix_all_type_errors():
    # ✏️ FIND AND FIX ALL 2 ERRORS ✏️
    #
    # Error 1: _______________
    # Error 2: _______________
    #
    # Write the fully fixed code below:
    pass


def main():
    print("=== Decode the Error: Type Errors ===")
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()
    print("Tip: TypeError means you're mixing incompatible types!")
    print("     Common fixes: str(), int(), float()")
    print()

    # Uncomment each to test after fixing:
    # print("Testing A:"); fix_code_a()
    # print("Testing B:"); fix_code_b()
    # print("Testing C:"); fix_code_c()
    # print("Testing D:"); fix_code_d()
    # print("Testing E:"); fix_code_e()
    # print("Testing Bonus:"); fix_all_type_errors()


main()
