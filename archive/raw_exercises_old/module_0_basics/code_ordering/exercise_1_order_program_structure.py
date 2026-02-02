# Exercise 1: Code Ordering - Program Structure
#
# The lines of code are scrambled! Put them in the correct order
# to make the program work properly.
#
# Theme: Organizing magical spells and hero greetings


# ============================================================
# ORDERING CHALLENGE A: Simple Greeting
# ============================================================
#
# Create a program that greets a hero by name.
# The program should:
# 1. Store the hero's name
# 2. Create a greeting message
# 3. Print the greeting
#
# SCRAMBLED LINES:
#   print(greeting)
#   greeting = f"Welcome, {hero_name}!"
#   hero_name = "{{hero}}"

def challenge_a():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: You must define a variable BEFORE using it!

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE B: Calculate and Display
# ============================================================
#
# Calculate how many spells a student learns per year.
# The program should work correctly when lines are in order.
#
# SCRAMBLED LINES:
#   spells_per_year = total_spells // years
#   years = 7
#   print(f"That's {spells_per_year} spells per year!")
#   total_spells = 49

def challenge_b():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: Both values must exist before division!

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE C: Input and Process
# ============================================================
#
# Get a spell name from the user and cast it.
# The program needs to: get input, format it, display it.
#
# SCRAMBLED LINES:
#   print(f"Casting {spell_upper}!")
#   spell_name = input("Enter a spell: ")
#   spell_upper = spell_name.upper()

def challenge_c():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: input → process → output

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# ORDERING CHALLENGE D: Full Program Structure
# ============================================================
#
# This is a complete mini-program with multiple steps.
# Put ALL lines in the correct order.
#
# SCRAMBLED LINES:
#   print(f"{hero} from {house} says: {exclamation}")
#   house = "{{house}}"
#   message = f"{hero} from {house} says: {exclamation}"
#   hero = "{{hero}}"
#   exclamation = "{{exclamation}}"

def challenge_d():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Hint: Variables hero, house, and exclamation must all exist
    # before creating the message. The print line uses 'message'.

    pass  # Delete this and add the correctly ordered lines


def main():
    print("=== Challenge A: Simple Greeting ===")
    challenge_a()

    print("\n=== Challenge B: Calculate and Display ===")
    challenge_b()

    print("\n=== Challenge C: Input and Process ===")
    challenge_c()

    print("\n=== Challenge D: Full Program Structure ===")
    challenge_d()

    print("\nReorder each challenge, then run to test!")


main()
