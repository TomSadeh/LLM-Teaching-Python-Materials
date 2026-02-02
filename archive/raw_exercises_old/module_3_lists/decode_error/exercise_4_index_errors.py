# Exercise 4: Decode the Error - Index Errors
#
# Each exercise shows an error message and the code that caused it.
# Your job: Understand the error and fix the code WITHOUT running it first.
#
# Theme: {{hero}}'s collection of magical items at {{school}}


# ============================================================
# ERROR DECODE A: Index Out of Range
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "inventory.py", line 2, in <module>
    print(items[3])
IndexError: list index out of range
"""


def buggy_code_a():
    """The code that caused the error"""
    items = ["wand", "potion", "cloak"]
    print(items[3])


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: List indexes start at 0! A 3-item list has indexes 0, 1, 2)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE B: Negative Index Too Far
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "spells.py", line 2, in <module>
    print(spells[-4])
IndexError: list index out of range
"""


def buggy_code_b():
    """The code that caused the error"""
    spells = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    print(spells[-4])


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: Negative indexes go from -1 (last) to -len(list))
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE C: Empty List Access
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "collection.py", line 2, in <module>
    print(treasures[0])
IndexError: list index out of range
"""


def buggy_code_c():
    """The code that caused the error"""
    treasures = []
    print(treasures[0])


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: An empty list has no items to access!)
    #
    # Write the fixed code below (add an item first, or check if list is empty):
    pass


# ============================================================
# ERROR DECODE D: Off-by-One in Loop
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "roster.py", line 3, in <module>
    print(students[i])
IndexError: list index out of range
"""


def buggy_code_d():
    """The code that caused the error"""
    students = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    for i in range(4):
        print(students[i])


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: range(4) gives 0,1,2,3 but the list only has indexes 0,1,2)
    #
    # Write the fixed code below:
    pass


# ============================================================
# ERROR DECODE E: String Index Error
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "name.py", line 2, in <module>
    print(name[10])
IndexError: string index out of range
"""


def buggy_code_e():
    """The code that caused the error"""
    name = "{{hero}}"
    print(name[10])


def fix_code_e():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # (Hint: Strings work like lists - indexes start at 0!)
    #
    # Write the fixed code below:
    pass


# ============================================================
# BONUS: Multiple Index Errors
# ============================================================
"""
This code has 2 different index errors. Find and fix them all!

members = ["{{hero}}", "{{heroine}}"]
print("First member:", members[1])
print("Third member:", members[2])
print("All members:", members[0], members[1], members[2])
"""


def fix_all_index_errors():
    # ✏️ FIND AND FIX ALL 2 ERRORS ✏️
    #
    # Error 1: _______________
    # Error 2: _______________
    #
    # Write the fully fixed code below:
    pass


def main():
    print("=== Decode the Error: Index Errors ===")
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()
    print("Tip: IndexError means you're trying to access a position")
    print("     that doesn't exist! Remember: indexes start at 0.")
    print()

    # Uncomment each to test after fixing:
    # print("Testing A:"); fix_code_a()
    # print("Testing B:"); fix_code_b()
    # print("Testing C:"); fix_code_c()
    # print("Testing D:"); fix_code_d()
    # print("Testing E:"); fix_code_e()
    # print("Testing Bonus:"); fix_all_index_errors()


main()
