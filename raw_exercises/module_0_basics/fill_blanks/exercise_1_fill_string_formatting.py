# Exercise 1: Fill in the Blanks - String Formatting
#
# Complete the code by filling in the blanks (marked with ___).
# Each blank needs a specific piece of code to make the program work.
#
# Theme: Creating messages for {{school}}


# --- FILL THE BLANKS A: F-Strings ---
#
# Complete the f-string to include variable values in the message.

def exercise_a():
    # ✏️ FILL IN THE BLANKS ✏️

    hero_name = "{{hero}}"
    house_name = "{{house}}"

    # Fill in the blanks to create an f-string
    # The output should be: "Welcome, {{hero}} of {{house}}!"
    message = ___"{hero_name} of {house_name}!"  # Hint: What letter goes before the quote?
    print(message)

    # Now make this one work too
    age = 11
    # Output should be: "{{hero}} is 11 years old"
    message2 = ___"{hero_name} is {___} years old"  # Hint: Put the variable name in braces
    print(message2)


# --- FILL THE BLANKS B: String Concatenation ---
#
# Build strings by joining them with +

def exercise_b():
    # ✏️ FILL IN THE BLANKS ✏️

    greeting = "{{greeting}}"
    name = "{{friend}}"

    # Join these strings together
    # Output should be: "{{greeting}}, {{friend}}!"
    full_greeting = greeting ___ ", " ___ name ___ "!"  # Hint: Use + to join strings
    print(full_greeting)


# --- FILL THE BLANKS C: Print with Multiple Items ---
#
# Use print() with commas to display multiple values

def exercise_c():
    # ✏️ FILL IN THE BLANKS ✏️

    spell = "{{spell1}}"
    power = 100

    # Print multiple items (commas add spaces automatically)
    # Output should be: "Casting {{spell1}} with power 100"
    print("Casting"___ spell___ "with power"___ power)  # Hint: Use commas between items


# --- FILL THE BLANKS D: String Methods ---
#
# Use string methods to transform text

def exercise_d():
    # ✏️ FILL IN THE BLANKS ✏️

    whisper = "{{password}}"

    # Make it uppercase
    # Output should be: "{{PASSWORD}}" (in uppercase)
    loud = whisper.___()  # Hint: The method name is similar to "uppercase"
    print(loud)

    # Make it lowercase
    # Output should be: "{{password}}" (in lowercase)
    quiet = whisper.___()  # Hint: The method name is similar to "lowercase"
    print(quiet)


# --- FILL THE BLANKS E: Input and Variables ---
#
# Get input from user and store in variables

def exercise_e():
    # ✏️ FILL IN THE BLANKS ✏️

    # Ask for user's name and store it
    # Hint: input() returns what the user types
    user_name = ___("What is your name? ")  # Hint: Function to get user input
    print(f"Welcome, {user_name}!")

    # Ask for a number and convert it
    # Hint: input() always returns a string, need to convert to int
    age_text = input("How old are you? ")
    age = ___(age_text)  # Hint: Convert string to integer
    next_year = age + 1
    print(f"Next year you will be {next_year}")


def main():
    print("=== Fill in the Blanks: String Formatting ===")
    print()
    print("Fill in the blanks in each exercise, then uncomment to test!")
    print()
    print("="*50)

    # Uncomment each exercise after filling in the blanks:

    # print("\n--- Exercise A: F-Strings ---")
    # exercise_a()

    # print("\n--- Exercise B: String Concatenation ---")
    # exercise_b()

    # print("\n--- Exercise C: Print with Multiple Items ---")
    # exercise_c()

    # print("\n--- Exercise D: String Methods ---")
    # exercise_d()

    # print("\n--- Exercise E: Input and Variables ---")
    # exercise_e()

    print("\nFill in all the blanks, then uncomment to test!")


main()


# =============================================================================
# ANSWER KEY (for reference):
# =============================================================================
#
# Exercise A: f, age
# Exercise B: +, +, +
# Exercise C: ,  ,  ,  (commas)
# Exercise D: upper, lower
# Exercise E: input, int
#
# =============================================================================
