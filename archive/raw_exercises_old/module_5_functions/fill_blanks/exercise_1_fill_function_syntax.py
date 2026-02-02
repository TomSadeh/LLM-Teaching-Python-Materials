# Exercise 1: Fill in the Blanks - Function Syntax
#
# Complete the code by filling in the blanks (marked with ___).
# Each blank needs a specific piece of code to make the program work.
#
# Theme: Creating magical spells at {{school}}


# --- FILL THE BLANKS A: Basic Function Definition ---
#
# Complete the function definition

def exercise_a():
    # ✏️ FILL IN THE BLANKS ✏️

    # Define a simple function that prints a greeting
    ___ say_hello():  # Hint: What keyword starts a function definition?
        print("{{greeting}}!")

    # Call the function
    say_hello()


# --- FILL THE BLANKS B: Function with Parameter ---
#
# Create a function that takes an input

def exercise_b():
    # ✏️ FILL IN THE BLANKS ✏️

    # Define a function that greets someone by name
    def greet(___):  # Hint: What should we call the input variable?
        print(f"Hello, {name}!")

    # Call the function with different names
    greet("{{hero}}")
    greet("{{friend}}")


# --- FILL THE BLANKS C: Function with Return Value ---
#
# Make a function that gives back a result

def exercise_c():
    # ✏️ FILL IN THE BLANKS ✏️

    # Define a function that calculates spell power
    def calculate_power(level):
        power = level * 10
        ___ power  # Hint: What keyword sends a value back?

    # Use the returned value
    result = calculate_power(5)
    print(f"Power level: {result}")


# --- FILL THE BLANKS D: Function with Multiple Parameters ---
#
# Create a function that takes more than one input

def exercise_d():
    # ✏️ FILL IN THE BLANKS ✏️

    # Define a function that combines two ingredients
    def mix_potion(ingredient1___ ingredient2):  # Hint: What separates parameters?
        print(f"Mixing {ingredient1} with {ingredient2}")
        return f"{ingredient1}-{ingredient2} potion"

    # Call the function
    result = mix_potion("moonstone", "dragon scale")
    print(f"Created: {result}")


# --- FILL THE BLANKS E: Function with Default Parameter ---
#
# Set a default value for a parameter

def exercise_e():
    # ✏️ FILL IN THE BLANKS ✏️

    # Define a function with a default power level
    def cast_spell(spell_name, power___10):  # Hint: What assigns a default value?
        print(f"Casting {spell_name} with power {power}")

    # Call with and without the optional parameter
    cast_spell("{{spell1}}")  # Uses default power of 10
    cast_spell("{{spell2}}", 50)  # Uses specified power of 50


# --- FILL THE BLANKS F: Function Calling Function ---
#
# Have one function use another

def exercise_f():
    # ✏️ FILL IN THE BLANKS ✏️

    def double(n):
        return n * 2

    def quadruple(n):
        # Call double twice to get 4x the original
        doubled = ___(n)  # Hint: Call the double function
        return double(doubled)

    result = quadruple(5)
    print(f"5 quadrupled is {result}")


def main():
    print("=== Fill in the Blanks: Function Syntax ===")
    print()
    print("Fill in the blanks in each exercise, then uncomment to test!")
    print()
    print("="*50)

    # Uncomment each exercise after filling in the blanks:

    # print("\n--- Exercise A: Basic Function Definition ---")
    # exercise_a()

    # print("\n--- Exercise B: Function with Parameter ---")
    # exercise_b()

    # print("\n--- Exercise C: Function with Return Value ---")
    # exercise_c()

    # print("\n--- Exercise D: Function with Multiple Parameters ---")
    # exercise_d()

    # print("\n--- Exercise E: Function with Default Parameter ---")
    # exercise_e()

    # print("\n--- Exercise F: Function Calling Function ---")
    # exercise_f()

    print("\nFill in all the blanks, then uncomment to test!")


main()


# =============================================================================
# ANSWER KEY (for reference):
# =============================================================================
#
# Exercise A: def
# Exercise B: name
# Exercise C: return
# Exercise D: , (comma)
# Exercise E: = (equals sign)
# Exercise F: double
#
# =============================================================================
