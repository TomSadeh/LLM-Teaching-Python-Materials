"""
{{CONTEXT_ERROR_HANDLING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Topic: Adding input validation loops
Difficulty: 3

Input validation ensures users provide valid data before proceeding.
Use while loops with string checking to validate input.

NOTE: We use while loops and string methods (like .isdigit()) for validation,
not try/except blocks. This teaches the fundamental pattern of validation loops.
"""


# ============================================================
# {{HANDLING_1_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# This function accepts any input and crashes on invalid numbers.


def original_get_number():
    """ORIGINAL: Crashes if user enters non-numeric text"""
    user_input = input("Enter a number: ")
    number = int(user_input)  # Crashes on "abc"!
    return number


def safe_get_number():
    """
    Get a valid integer from the user.
    Keep asking until they enter a valid number.

    Returns:
        int: A valid integer entered by the user

    Validation:
    - If input is not numeric, print "Please enter a valid number."
    - Keep asking until valid
    - Handle negative numbers (starts with '-')
    """
    # ✏️ ADD VALIDATION LOOP ✏️
    #
    # {{CONTEXT_HANDLING_HINT_1}}
    #
    # Step 1: Start while True loop
    # Step 2: Get input
    # Step 3: Check if valid:
    #         - For positive: input.isdigit()
    #         - For negative: input.startswith('-') and input[1:].isdigit()
    # Step 4: If valid, convert and return
    # Step 5: If invalid, print error message (loop continues)
    pass


# ============================================================
# {{HANDLING_2_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# This function accepts numbers outside the valid range.


def original_get_score():
    """ORIGINAL: Accepts any number, even invalid scores"""
    score = int(input("Enter score (0-100): "))
    return score


def safe_get_score():
    """
    Get a valid score from 0 to 100.
    Keep asking until input is valid.

    Returns:
        int: A score between 0 and 100 (inclusive)

    Validation:
    - Must be a number
    - Must be between 0 and 100
    """
    # ✏️ ADD VALIDATION LOOP ✏️
    #
    # {{CONTEXT_HANDLING_HINT_2}}
    #
    # Step 1: Start while True loop
    # Step 2: Get input
    # Step 3: Check if numeric (handle with .isdigit())
    #         If not, print "Please enter a number." and continue
    # Step 4: Convert to int
    # Step 5: Check if in range 0-100
    #         If not, print "Score must be between 0 and 100." and continue
    # Step 6: Return valid score
    pass


# ============================================================
# {{HANDLING_3_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# This function accepts any text, even empty strings.


def original_get_name():
    """ORIGINAL: Accepts empty names"""
    name = input("Enter your name: ")
    return name


def safe_get_name():
    """
    Get a non-empty name from the user.
    Keep asking until they enter something.

    Returns:
        str: A non-empty, stripped name

    Validation:
    - Must not be empty after stripping whitespace
    - Strip leading/trailing whitespace from result
    """
    # ✏️ ADD VALIDATION LOOP ✏️
    #
    # {{CONTEXT_HANDLING_HINT_3}}
    #
    # Step 1: Start while True loop
    # Step 2: Get input and strip whitespace
    # Step 3: If empty string, print "Name cannot be empty." and continue
    # Step 4: Return the stripped name
    pass


# ============================================================
# {{HANDLING_4_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# This function accepts any choice, not just valid options.


def original_get_choice():
    """ORIGINAL: Accepts any choice, even invalid ones"""
    print("Choose: (a) {{spell1}}, (b) {{spell2}}, (c) {{spell3}}")
    choice = input("Your choice: ")
    return choice


def safe_get_choice():
    """
    Get a valid choice from the user (a, b, or c).
    Keep asking until valid.

    Returns:
        str: 'a', 'b', or 'c'

    Validation:
    - Must be exactly 'a', 'b', or 'c' (case insensitive)
    - Show valid options in error message
    """
    # ✏️ ADD VALIDATION LOOP ✏️
    #
    # {{CONTEXT_HANDLING_HINT_4}}
    #
    # Step 1: Define valid_choices = ['a', 'b', 'c']
    # Step 2: Print the menu
    # Step 3: Start while True loop
    # Step 4: Get input and convert to lowercase
    # Step 5: If choice in valid_choices, return it
    # Step 6: Otherwise print "Invalid choice. Please enter a, b, or c."
    pass


# ============================================================
# {{HANDLING_5_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_5_NARRATIVE}}
#
# This yes/no function accepts any input.


def original_confirm():
    """ORIGINAL: Accepts any response as yes"""
    response = input("Confirm? (yes/no): ")
    return response == "yes"


def safe_confirm(prompt):
    """
    Get a yes/no confirmation from the user.
    Keep asking until they enter yes or no.

    Args:
        prompt: The question to ask

    Returns:
        bool: True for yes, False for no

    Validation:
    - Accept 'yes', 'y', 'no', 'n' (case insensitive)
    - Keep asking for other inputs
    """
    # ✏️ ADD VALIDATION LOOP ✏️
    #
    # {{CONTEXT_HANDLING_HINT_5}}
    #
    # Step 1: Start while True loop
    # Step 2: Print prompt and get input (lowercase, stripped)
    # Step 3: If response is 'yes' or 'y', return True
    # Step 4: If response is 'no' or 'n', return False
    # Step 5: Otherwise print "Please enter yes or no."
    pass


def main():
    print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
    print("=" * 50)

    print("\n=== {{HANDLING_1_TITLE}} ===")
    print("Getting a valid number:")
    # number = safe_get_number()
    # print(f"You entered: {number}")

    print("\n=== {{HANDLING_2_TITLE}} ===")
    print("Getting a valid score:")
    # score = safe_get_score()
    # print(f"Score recorded: {score}")

    print("\n=== {{HANDLING_3_TITLE}} ===")
    print("Getting a valid name:")
    # name = safe_get_name()
    # print(f"Hello, {name}!")

    print("\n=== {{HANDLING_4_TITLE}} ===")
    print("Getting a valid choice:")
    # choice = safe_get_choice()
    # print(f"You chose: {choice}")

    print("\n=== {{HANDLING_5_TITLE}} ===")
    print("Getting confirmation:")
    # if safe_confirm("Do you want to continue? (yes/no): "):
    #     print("Continuing...")
    # else:
    #     print("Cancelled.")

    print("\n" + "=" * 50)
    print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")


main()
