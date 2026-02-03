"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn about the string module's useful
constants. These are pre-defined character sets that help with
validation, generation, and text processing.

Topic: string module constants
Difficulty: 2
"""

import string


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Explore the string module's character constants.
    #
    # Step 1: Print each constant to see what it contains:
    #
    #         print("Letters:", string.ascii_letters)
    #         print("Lowercase:", string.ascii_lowercase)
    #         print("Uppercase:", string.ascii_uppercase)
    #         print("Digits:", string.digits)
    #         print("Punctuation:", string.punctuation)
    #
    # Step 2: Check the length of each:
    #         print(f"Letters count: {len(string.ascii_letters)}")
    #         print(f"Digits count: {len(string.digits)}")
    #
    # These constants are useful for:
    # - Validating input (is it all letters? all digits?)
    # - Generating random strings (passwords, codes)
    # - Text processing
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use string constants for input validation.
    #
    # Step 1: Create a function to check if text is all letters:
    #
    #         def is_all_letters(text):
    #             for char in text:
    #                 if char not in string.ascii_letters:
    #                     return False
    #             return True
    #
    # Step 2: Test it with different inputs:
    #         print(is_all_letters("Hello"))        # True
    #         print(is_all_letters("Hello123"))     # False
    #         print(is_all_letters("Hello World"))  # False (space)
    #
    # Step 3: Create a similar function for alphanumeric:
    #
    #         def is_alphanumeric(text):
    #             valid_chars = string.ascii_letters + string.digits
    #             for char in text:
    #                 if char not in valid_chars:
    #                     return False
    #             return True
    #
    # Step 4: Test it:
    #         print(is_alphanumeric("User123"))     # True
    #         print(is_alphanumeric("User_123"))    # False (underscore)
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Combine string constants with random for {{school}}.
    #
    # Step 1: Import random at the top of your solution
    #
    # Step 2: Create a simple code generator:
    #
    #         def generate_code(length):
    #             """Generate a random alphanumeric code."""
    #             characters = string.ascii_uppercase + string.digits
    #             code = ""
    #             for i in range(length):
    #                 code = code + random.choice(characters)
    #             return code
    #
    # Step 3: Generate and print several codes:
    #         print(f"Access code: {generate_code(6)}")
    #         print(f"Long code: {generate_code(10)}")
    #
    # Step 4: Create a variant that only uses digits:
    #
    #         def generate_pin(length):
    #             pin = ""
    #             for i in range(length):
    #                 pin = pin + random.choice(string.digits)
    #             return pin
    #
    #         print(f"PIN: {generate_pin(4)}")
    #
    # Step 5: Create one that uses letters only:
    #         Generate a 5-letter "name" using lowercase letters
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    print("Exploring string constants")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    print("Validation with string constants")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    print("Code generation for {{school}}")
    exercise_c()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print()
    print("String Constants Summary:")
    print("  string.ascii_letters  - a-z and A-Z")
    print("  string.ascii_lowercase - a-z")
    print("  string.ascii_uppercase - A-Z")
    print("  string.digits         - 0-9")
    print("  string.punctuation    - !@#$... etc")


main()
