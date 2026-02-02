# Exercise 1: Decode the Error - Dictionary Errors
#
# Each exercise shows an error message and the code that caused it.
# Your job: Understand the error and fix the code WITHOUT running it first.
#
# Theme: Debugging {{school}}'s magical record system


# ============================================================
# ERROR DECODE A: Missing Key (KeyError)
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "student_records.py", line 5, in <module>
    print(student["grade"])
KeyError: 'grade'
"""

def buggy_code_a():
    """The code that caused the error"""
    student = {
        "name": "{{hero}}",
        "house": "{{house}}",
        "year": 3
    }
    print(student["grade"])  # 'grade' key doesn't exist!


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Option 1: Add the missing key to the dictionary
    # Option 2: Use .get() to provide a default value
    # Option 3: Check if key exists before accessing
    #
    # The fix:
    student = {
        "name": "{{hero}}",
        "house": "{{house}}",
        "year": 3
    }
    pass  # Access safely or add the key


# ============================================================
# ERROR DECODE B: Unhashable Type (List as Key)
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "spellbook.py", line 4, in <module>
    spells[ingredients] = "Healing Potion"
TypeError: unhashable type: 'list'
"""

def buggy_code_b():
    """The code that caused the error"""
    spells = {}
    ingredients = ["moonstone", "fairy wings"]
    spells[ingredients] = "Healing Potion"  # Lists can't be dict keys!


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # Hint: Lists are mutable, so they can't be dictionary keys.
    #       Tuples are immutable and CAN be keys.
    #
    # The fix:
    spells = {}
    ingredients = ["moonstone", "fairy wings"]
    pass  # Convert to a type that can be a key


# ============================================================
# ERROR DECODE C: Modifying During Iteration
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "cleanup.py", line 6, in <module>
    for student in students:
RuntimeError: dictionary changed size during iteration
"""

def buggy_code_c():
    """The code that caused the error"""
    students = {
        "{{hero}}": 95,
        "{{friend}}": 60,
        "{{villain}}": 45
    }

    # Remove failing students while iterating - NOT allowed!
    for student in students:
        if students[student] < 70:
            del students[student]


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # Hint: Create a list of keys to delete first,
    #       OR create a new dictionary with passing students
    #
    # The fix:
    students = {
        "{{hero}}": 95,
        "{{friend}}": 60,
        "{{villain}}": 45
    }
    pass  # Remove without modifying during iteration


# ============================================================
# ERROR DECODE D: Wrong Method (AttributeError)
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "inventory.py", line 5, in <module>
    items.append("map")
AttributeError: 'dict' object has no attribute 'append'
"""

def buggy_code_d():
    """The code that caused the error"""
    items = {"wand": 1, "cloak": 1}
    items.append("map")  # Dictionaries don't have append!


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # Hint: To add to a dictionary, use dict[key] = value
    #
    # The fix:
    items = {"wand": 1, "cloak": 1}
    pass  # Add "map" to the dictionary correctly


# ============================================================
# ERROR DECODE E: None is Not Subscriptable
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "lookup.py", line 8, in <module>
    print(result["power"])
TypeError: 'NoneType' object is not subscriptable
"""

def buggy_code_e():
    """The code that caused the error"""
    spells = {"{{spell1}}": {"power": 10, "type": "attack"}}

    # .get() returns None when key not found
    result = spells.get("{{spell3}}")
    print(result["power"])  # None["power"] = error!


def fix_code_e():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # Hint: Check if result is not None before accessing
    #
    # The fix:
    spells = {"{{spell1}}": {"power": 10, "type": "attack"}}

    result = spells.get("{{spell3}}")
    pass  # Handle the None case


# ============================================================
# ERROR DECODE F: Wrong Key Type
# ============================================================
"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "scores.py", line 5, in <module>
    print(scores["1"])
KeyError: '1'
"""

def buggy_code_f():
    """The code that caused the error"""
    scores = {1: "First", 2: "Second", 3: "Third"}
    print(scores["1"])  # Key is int 1, not string "1"!


def fix_code_f():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    # Hint: The key type must match exactly: 1 != "1"
    #
    # The fix:
    scores = {1: "First", 2: "Second", 3: "Third"}
    pass  # Use the correct key type


def main():
    print("=== Decode the Error: Dictionary Errors ===")
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()
    print("="*50)
    print()
    print("Error Types Covered:")
    print("  A: KeyError - accessing missing key")
    print("  B: TypeError - unhashable type (list as key)")
    print("  C: RuntimeError - modifying dict during iteration")
    print("  D: AttributeError - wrong method for dict")
    print("  E: TypeError - None is not subscriptable")
    print("  F: KeyError - wrong key type (int vs str)")
    print()

    # Uncomment each to test after fixing:
    # print("\nTesting A:"); fix_code_a()
    # print("\nTesting B:"); fix_code_b()
    # print("\nTesting C:"); fix_code_c()
    # print("\nTesting D:"); fix_code_d()
    # print("\nTesting E:"); fix_code_e()
    # print("\nTesting F:"); fix_code_f()


main()
