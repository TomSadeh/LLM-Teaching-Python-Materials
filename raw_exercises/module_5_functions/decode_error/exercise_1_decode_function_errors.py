# Exercise 1: Decode the Error - Function Errors
#
# Each exercise shows an error message and the code that caused it.
# Your job: Understand the error and fix the code WITHOUT running it first.
#
# Theme: Debugging {{school}}'s magical function library


# ============================================================
# ERROR DECODE A: Missing Argument
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "spells.py", line 8, in <module>
    cast_spell()
TypeError: cast_spell() missing 1 required positional argument: 'spell_name'
"""

def buggy_code_a():
    """The code that caused the error"""
    def cast_spell(spell_name):
        print(f"Casting {spell_name}!")

    # Oops - forgot to pass the argument!
    cast_spell()


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # The fix:
    def cast_spell(spell_name):
        print(f"Casting {spell_name}!")

    pass  # Call the function correctly


# ============================================================
# ERROR DECODE B: Too Many Arguments
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "potions.py", line 7, in <module>
    brew("healing", "blue", "bubbling")
TypeError: brew() takes 2 positional arguments but 3 were given
"""

def buggy_code_b():
    """The code that caused the error"""
    def brew(potion_name, color):
        print(f"Brewing {color} {potion_name} potion")

    # Passing too many arguments!
    brew("healing", "blue", "bubbling")


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Option 1: Remove the extra argument
    # Option 2: Update the function to accept 3 parameters
    #
    # The fix:
    pass


# ============================================================
# ERROR DECODE C: Return vs Print Confusion
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "math_spells.py", line 8, in <module>
    result = add_power(5, 3) + 10
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
"""

def buggy_code_c():
    """The code that caused the error"""
    def add_power(a, b):
        total = a + b
        print(total)  # This prints, but doesn't RETURN!

    result = add_power(5, 3) + 10  # add_power returns None!
    print(result)


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # Hint: The function prints but doesn't return a value
    #
    # The fix:
    def add_power(a, b):
        total = a + b
        pass  # What should happen here?

    result = add_power(5, 3) + 10
    print(result)


# ============================================================
# ERROR DECODE D: Undefined Variable in Function
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "scores.py", line 9, in <module>
    show_score()
  File "scores.py", line 6, in show_score
    print(f"Score: {scroe}")
NameError: name 'scroe' is not defined. Did you mean: 'score'?
"""

def buggy_code_d():
    """The code that caused the error"""
    score = 100

    def show_score():
        print(f"Score: {scroe}")  # Typo!

    show_score()


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # The fix:
    score = 100

    def show_score():
        pass  # Fix the typo

    show_score()


# ============================================================
# ERROR DECODE E: Wrong Return Type
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "inventory.py", line 10, in <module>
    for item in get_items():
TypeError: 'NoneType' object is not iterable
"""

def buggy_code_e():
    """The code that caused the error"""
    def get_items():
        items = ["wand", "cloak", "map"]
        # Forgot to return!

    for item in get_items():  # get_items() returns None
        print(item)


def fix_code_e():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # The fix:
    def get_items():
        items = ["wand", "cloak", "map"]
        pass  # What's missing?

    for item in get_items():
        print(item)


# ============================================================
# ERROR DECODE F: Calling Before Defining
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "magic.py", line 2, in <module>
    greet_wizard()
NameError: name 'greet_wizard' is not defined
"""

def buggy_code_f():
    """The code that caused the error"""
    # Calling before the function is defined!
    greet_wizard()

    def greet_wizard():
        print("{{greeting}}, wizard!")


def fix_code_f():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # Hint: In Python, functions must be defined before they are called
    #
    # The fix:
    pass  # Reorder the code correctly


def main():
    print("=== Decode the Error: Function Errors ===")
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()
    print("="*50)
    print()
    print("Error Types Covered:")
    print("  A: Missing required argument")
    print("  B: Too many arguments")
    print("  C: Function returns None (print vs return)")
    print("  D: Typo in variable name")
    print("  E: Forgot to return a value")
    print("  F: Calling function before defining it")
    print()

    # Uncomment each to test after fixing:
    # print("\nTesting A:"); fix_code_a()
    # print("\nTesting B:"); fix_code_b()
    # print("\nTesting C:"); fix_code_c()
    # print("\nTesting D:"); fix_code_d()
    # print("\nTesting E:"); fix_code_e()
    # print("\nTesting F:"); fix_code_f()


main()
