# Exercise 6: String Methods and the String Module

import string


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Explore the string module constants!
    # Print string.ascii_lowercase (all lowercase letters)
    # Print string.ascii_uppercase (all uppercase letters)
    # Print string.digits (all digits)
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Title case converter!
    # Ask for a book title (like "{{hero}} and the chamber of secrets")
    # Convert to title case using .title()
    # Print the formatted title
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Spell validator!
    # A valid spell must:
    # - Start with a capital letter (.istitle() or check first char)
    # - Contain only letters (.isalpha())
    # - Be at least 4 characters long
    # Ask user for a spell and check if it's valid
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Word counter!
    # Ask for a sentence
    # Count: words (.split()), characters (len), and spaces (.count(" "))
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Find and replace!
    # Start with: "{{hero}} went to {{school}}. {{hero}} saw {{friend}}."
    # Replace all "{{hero}}" with a name the user enters
    # Hint: sentence.replace(old, new)
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Password strength checker!
    # A strong password has:
    # - At least 8 characters
    # - At least 1 uppercase letter (any(c.isupper() for c in password))
    # - At least 1 lowercase letter
    # - At least 1 digit
    # - At least 1 special character (check against string.punctuation)
    # Rate the password: Weak, Medium, Strong
    pass


def exercise_g():
    # ✏️ YOUR CODE HERE ✏️
    # Name formatter!
    # Ask for: first name, last name
    # Print in different formats:
    # - "First Last"
    # - "Last, First"
    # - "F. Last"
    # - "first.last" (all lowercase, good for usernames)
    pass


def acronym_maker():
    # ✏️ YOUR CODE HERE ✏️
    # Create an acronym from a phrase!
    # Example: "{{group}}" becomes "DA" (if that was the input)
    # 1. Split the phrase into words
    # 2. Take the first letter of each word
    # 3. Make them uppercase
    # 4. Join them together
    pass


def main():
    print("=== Exercise A: String Constants ===")
    exercise_a()

    print("\n=== Exercise B: Title Case ===")
    exercise_b()

    print("\n=== Exercise C: Spell Validator ===")
    exercise_c()

    print("\n=== Exercise D: Word Counter ===")
    exercise_d()

    print("\n=== Exercise E: Find and Replace ===")
    exercise_e()

    print("\n=== Exercise F: Password Checker ===")
    exercise_f()

    print("\n=== Exercise G: Name Formatter ===")
    exercise_g()

    print("\n=== Acronym Maker ===")
    acronym_maker()


main()
