# Exercise 2: Decode the Error - Name Errors
#
# Each exercise shows an error message and the code that caused it.
# Your job: Understand the error and fix the code WITHOUT running it first.
#
# Theme: {{hero}}'s spell casting practice at {{school}}


# ============================================================
# ERROR DECODE A: Undefined Variable
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "spells.py", line 2, in <module>
    print(spell_name)
NameError: name 'spell_name' is not defined
"""


def buggy_code_a():
    """The code that caused the error"""
    print(spell_name)


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: You can't use a variable before creating it!)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE B: Typo in Variable Name
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "greeting.py", line 2, in <module>
    print(heros_name)
NameError: name 'heros_name' is not defined. Did you mean: 'hero_name'?
"""


def buggy_code_b():
    """The code that caused the error"""
    hero_name = "{{hero}}"
    print(heros_name)


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: Python is helpful - look at the suggestion!)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE C: Case Sensitivity
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "magic.py", line 2, in <module>
    print(School)
NameError: name 'School' is not defined. Did you mean: 'school'?
"""


def buggy_code_c():
    """The code that caused the error"""
    school = "{{school}}"
    print(School)


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: Python cares about UPPERCASE and lowercase!)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE D: Using Variable Before Assignment
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "counter.py", line 3, in <module>
    total = total + 10
NameError: name 'total' is not defined
"""


def buggy_code_d():
    """The code that caused the error"""
    total = total + 10
    print(total)


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: You need to have a value BEFORE you can add to it)
    #
    # Write the fixed code below:
    pass


# ============================================================
# BONUS: Multiple Name Errors
# ============================================================
"""
This code has 3 different name errors. Find and fix them all!

wizard_name = "{{hero}}"
spell = "{{spell1}}"
print(wizardname + " casts " + Spell)
print("The spell was: " + magicword)
"""


def fix_all_name_errors():
    # ✏️ FIND AND FIX ALL 3 ERRORS ✏️
    #
    # Error 1: _______________
    # Error 2: _______________
    # Error 3: _______________
    #
    # Write the fully fixed code below:
    pass


def main():
    print("=== Decode the Error: Name Errors ===")
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()
    print("Tip: NameError means Python doesn't recognize a name!")
    print()

    # Uncomment each to test after fixing:
    # print("Testing A:"); fix_code_a()
    # print("Testing B:"); fix_code_b()
    # print("Testing C:"); fix_code_c()
    # print("Testing D:"); fix_code_d()
    # print("Testing Bonus:"); fix_all_name_errors()


main()
