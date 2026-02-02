# Exercise 1: Code Ordering - Function Calls
#
# The lines of code are scrambled! Put them in the correct order
# to make the functions work properly.
#
# Theme: Creating and calling magical helper functions


# ============================================================
# ORDERING CHALLENGE A: Define Before Call
# ============================================================
#
# A function must be DEFINED before it can be CALLED.
# Put these lines in the correct order.
#
# SCRAMBLED LINES:
#   greet_hero("{{hero}}")
#   def greet_hero(name):
#       print(f"Welcome, {name}!")

def challenge_a():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: Python reads top to bottom - define first!

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE B: Return Before Use
# ============================================================
#
# To use a function's result, you must call it AND
# store the return value before using it.
#
# SCRAMBLED LINES:
#   print(f"Power level: {power}")
#   def calculate_power(level, multiplier):
#       return level * multiplier
#   power = calculate_power(10, 5)

def challenge_b():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: define → call and store → use result

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE C: Multiple Functions
# ============================================================
#
# When functions call each other, define helper functions first.
#
# SCRAMBLED LINES:
#   def create_title(name):
#       upper_name = make_uppercase(name)
#       return f"=== {upper_name} ==="
#
#   print(create_title("{{hero}}"))
#
#   def make_uppercase(text):
#       return text.upper()

def challenge_c():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Hint: create_title uses make_uppercase, so which must be defined first?

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE D: Function with Loop
# ============================================================
#
# A function that builds and returns a result.
# The accumulator must be initialized before the loop.
#
# SCRAMBLED LINES:
#   def count_letters(word):
#       for letter in word:
#           count = count + 1
#       count = 0
#       return count
#
#   result = count_letters("{{spell1}}")
#   print(f"Letter count: {result}")

def challenge_d():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: initialize → loop → return (inside function)
    # Then: call function → use result (outside function)

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE E: Full Program Structure
# ============================================================
#
# A complete program with helper functions and main.
# This is a common pattern in real programs!
#
# SCRAMBLED LINES:
#   main()
#
#   def format_spell(spell):
#       return f"*{spell}*"
#
#   def main():
#       spell = "{{spell2}}"
#       formatted = format_spell(spell)
#       display_spell(formatted)
#
#   def display_spell(text):
#       print(f"Casting: {text}")

def challenge_e():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Pattern: helper functions → main function → call main
    # Hint: main uses format_spell and display_spell

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE F: Building a List
# ============================================================
#
# Create a function that builds a list using append.
# The empty list must exist before appending!
#
# SCRAMBLED LINES:
#   def create_team():
#       return team
#       team.append("{{friend}}")
#       team = []
#       team.append("{{hero}}")
#       team.append("{{heroine}}")
#
#   heroes = create_team()
#   print(heroes)

def challenge_f():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: create list → append items → return list

    pass  # Delete this and add the correctly ordered lines


def main():
    print("=== Challenge A: Define Before Call ===")
    challenge_a()

    print("\n=== Challenge B: Return Before Use ===")
    challenge_b()

    print("\n=== Challenge C: Multiple Functions ===")
    challenge_c()

    print("\n=== Challenge D: Function with Loop ===")
    challenge_d()

    print("\n=== Challenge E: Full Program Structure ===")
    challenge_e()

    print("\n=== Challenge F: Building a List ===")
    challenge_f()

    print("\nReorder each challenge, then run to test!")


main()
