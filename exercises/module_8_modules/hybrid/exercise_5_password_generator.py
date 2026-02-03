"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part exercise where {{hero}} builds secure password
and code generators using the string and random modules together.

Programming concepts: string module, random module, function design
Difficulty: 2-3
"""

import string
import random


# ============================================================
# PART 1: Growth - Basic Code Generation
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Learn to use string constants for character pools.


def generate_numeric_code(length):
    """
    Generate a numeric code (digits only).

    Args:
        length: How many digits

    Returns:
        str: A string of random digits

    Example:
        >>> generate_numeric_code(6)
        "847291"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Get digit characters: string.digits = "0123456789"
    #
    # Step 2: Build the code using a loop:
    #         code = ""
    #         for i in range(length):
    #             code = code + random.choice(string.digits)
    #
    # Step 3: Return the code
    pass


def generate_alpha_code(length, case="upper"):
    """
    Generate an alphabetic code.

    Args:
        length: How many characters
        case: "upper", "lower", or "mixed"

    Returns:
        str: A string of random letters

    Example:
        >>> generate_alpha_code(4, "upper")
        "XKCD"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Select the right character set based on case:
    #         if case == "upper":
    #             chars = string.ascii_uppercase
    #         elif case == "lower":
    #             chars = string.ascii_lowercase
    #         else:
    #             chars = string.ascii_letters
    #
    # Step 2: Build and return the code
    pass


def generate_alphanumeric_code(length):
    """
    Generate a code with letters and numbers.

    Args:
        length: How many characters

    Returns:
        str: A string of random letters and digits

    Example:
        >>> generate_alphanumeric_code(8)
        "A3bK9mZ2"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Combine character sets:
    #         chars = string.ascii_letters + string.digits
    #
    # Step 2: Build and return the code
    pass


# ============================================================
# PART 2: Growth - Combining Modules for Passwords
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Create more sophisticated password generators.


def generate_password(length, include_special=True):
    """
    Generate a random password.

    Args:
        length: Password length (minimum 4)
        include_special: Whether to include punctuation

    Returns:
        str: A random password
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Build character pool:
    #         chars = string.ascii_letters + string.digits
    #         if include_special:
    #             chars = chars + string.punctuation
    #
    # Step 2: Generate password using loop or sample
    #
    # Step 3: Return the password
    pass


def generate_memorable_password(word_count=3):
    """
    Generate a password from random words (more memorable).

    Args:
        word_count: Number of words to use

    Returns:
        str: Words joined with numbers

    Example:
        >>> generate_memorable_password(3)
        "apple7banana3cherry"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create a word list:
    #         words = ["flame", "river", "stone", "cloud", "star",
    #                  "moon", "sun", "wind", "wave", "tree"]
    #
    # Step 2: Use random.sample() to pick words
    #
    # Step 3: Join words with random digits between them:
    #         result = ""
    #         for i, word in enumerate(selected_words):
    #             result = result + word
    #             if i < len(selected_words) - 1:
    #                 result = result + random.choice(string.digits)
    #
    # Step 4: Return the result
    pass


def generate_passphrase(word_count=4, separator="-"):
    """
    Generate a passphrase (words separated by a character).

    Args:
        word_count: Number of words
        separator: Character between words

    Returns:
        str: A passphrase like "correct-horse-battery-staple"
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create a larger word list
    #
    # Step 2: Use random.sample() to pick words
    #
    # Step 3: Join with separator: separator.join(selected_words)
    #
    # Step 4: Return the result
    pass


# ============================================================
# PART 3: Improvement - Validation and Security
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Add validation to ensure passwords meet requirements.


def validate_password(password):
    """
    Check if a password meets security requirements.

    Requirements:
    - At least 8 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit

    Args:
        password: The password to check

    Returns:
        tuple: (is_valid: bool, message: str)
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Check length >= 8
    #
    # Step 2: Check for uppercase (any char in string.ascii_uppercase)
    #         has_upper = False
    #         for char in password:
    #             if char in string.ascii_uppercase:
    #                 has_upper = True
    #                 break
    #
    # Step 3: Similarly check for lowercase and digit
    #
    # Step 4: Return appropriate tuple:
    #         (True, "Password meets all requirements")
    #         (False, "Password must be at least 8 characters")
    #         etc.
    pass


def generate_secure_password(length=12):
    """
    Generate a password guaranteed to meet requirements.

    Args:
        length: Minimum 8, default 12

    Returns:
        str: A secure password
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Ensure minimum length
    #         if length < 8:
    #             length = 8
    #
    # Step 2: Start with required characters:
    #         password = [
    #             random.choice(string.ascii_uppercase),
    #             random.choice(string.ascii_lowercase),
    #             random.choice(string.digits),
    #         ]
    #
    # Step 3: Fill remaining with random chars:
    #         all_chars = string.ascii_letters + string.digits
    #         for i in range(length - 3):
    #             password.append(random.choice(all_chars))
    #
    # Step 4: Shuffle so required chars aren't always first:
    #         random.shuffle(password)
    #
    # Step 5: Convert list to string and return:
    #         return "".join(password)
    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("Password Generator for {{school}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Basic Code Generation")
    print("-" * 40)
    # Uncomment to test:
    # print(f"Numeric (6): {generate_numeric_code(6)}")
    # print(f"Alpha upper (4): {generate_alpha_code(4, 'upper')}")
    # print(f"Alpha lower (4): {generate_alpha_code(4, 'lower')}")
    # print(f"Alpha mixed (4): {generate_alpha_code(4, 'mixed')}")
    # print(f"Alphanumeric (8): {generate_alphanumeric_code(8)}")
    print()

    print(">>> PART 2: Password Generation")
    print("-" * 40)
    # Uncomment to test:
    # print(f"Password (12): {generate_password(12)}")
    # print(f"Password (12, no special): {generate_password(12, False)}")
    # print(f"Memorable: {generate_memorable_password(3)}")
    # print(f"Passphrase: {generate_passphrase(4, '-')}")
    print()

    print(">>> PART 3: Validation")
    print("-" * 40)
    # Uncomment to test:
    # test_passwords = ["abc", "abcdefgh", "Abcdefgh", "Abcdefg1"]
    # for pwd in test_passwords:
    #     valid, msg = validate_password(pwd)
    #     status = "PASS" if valid else "FAIL"
    #     print(f"  '{pwd}': {status} - {msg}")
    # print()
    # print(f"Secure password: {generate_secure_password(12)}")
    print()

    print("=" * 60)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
