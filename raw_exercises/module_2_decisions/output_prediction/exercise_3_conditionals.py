# Exercise 3: Output Prediction - Conditionals
#
# Read the code carefully and predict what it will print.
# Do NOT run the code - practice mental execution!
#
# Theme: {{hero}}'s decisions at {{school}}


# --- PREDICTION CHALLENGE A ---
# Simple if statement

def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    points = 75
    if points >= 50:
        print("You passed!")


def challenge_a_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Is 75 >= 50?
    pass


# --- PREDICTION CHALLENGE B ---
# if-else

def challenge_b_code():
    """DO NOT MODIFY - Just read and predict"""
    password = "{{password}}"
    guess = "magic"
    if guess == password:
        print("Access granted!")
    else:
        print("Access denied!")


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Is "magic" equal to "{{password}}"?
    pass


# --- PREDICTION CHALLENGE C ---
# if-elif-else chain

def challenge_c_code():
    """DO NOT MODIFY - Just read and predict"""
    score = 85
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("F")


def challenge_c_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Which condition is checked first that's True?
    pass


# --- PREDICTION CHALLENGE D ---
# Multiple conditions with and

def challenge_d_code():
    """DO NOT MODIFY - Just read and predict"""
    age = 15
    has_permission = True
    if age >= 13 and has_permission:
        print("Welcome, young wizard!")
    else:
        print("Sorry, not allowed.")


def challenge_d_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Both conditions must be True for 'and'
    pass


# --- PREDICTION CHALLENGE E ---
# Multiple conditions with or

def challenge_e_code():
    """DO NOT MODIFY - Just read and predict"""
    is_weekend = False
    is_holiday = False
    if is_weekend or is_holiday:
        print("No class today!")
    else:
        print("Time for class!")


def challenge_e_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: At least one must be True for 'or'
    pass


# --- PREDICTION CHALLENGE F ---
# Nested if statements

def challenge_f_code():
    """DO NOT MODIFY - Just read and predict"""
    has_wand = True
    spell_power = 30
    if has_wand:
        if spell_power > 50:
            print("Powerful spell!")
        else:
            print("Weak spell...")
    else:
        print("No wand!")


def challenge_f_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Check the outer if first, then the inner if
    pass


# --- PREDICTION CHALLENGE G ---
# Tricky: multiple prints possible

def challenge_g_code():
    """DO NOT MODIFY - Just read and predict"""
    level = 5
    if level >= 1:
        print("Beginner badge!")
    if level >= 3:
        print("Intermediate badge!")
    if level >= 5:
        print("Advanced badge!")


def challenge_g_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: These are separate if statements, not if-elif!
    # How many will print?
    pass


# --- PREDICTION CHALLENGE H ---
# Comparing strings

def challenge_h_code():
    """DO NOT MODIFY - Just read and predict"""
    house = "{{house}}"
    if house == "{{house}}":
        print("Welcome home!")
    if house != "Slytherin":
        print("Not in Slytherin!")


def challenge_h_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Both if statements are checked independently
    pass


def main():
    print("=== Output Prediction: Conditionals ===")
    print()
    print("For each challenge:")
    print("1. Read the code in challenge_X_code()")
    print("2. Write your prediction in challenge_X_prediction()")
    print("3. Then run to check your answers!")
    print()
    print("="*40)

    print("\n--- Challenge A: Actual Output ---")
    challenge_a_code()
    print("--- Your Prediction ---")
    challenge_a_prediction()

    print("\n--- Challenge B: Actual Output ---")
    challenge_b_code()
    print("--- Your Prediction ---")
    challenge_b_prediction()

    print("\n--- Challenge C: Actual Output ---")
    challenge_c_code()
    print("--- Your Prediction ---")
    challenge_c_prediction()

    print("\n--- Challenge D: Actual Output ---")
    challenge_d_code()
    print("--- Your Prediction ---")
    challenge_d_prediction()

    print("\n--- Challenge E: Actual Output ---")
    challenge_e_code()
    print("--- Your Prediction ---")
    challenge_e_prediction()

    print("\n--- Challenge F: Actual Output ---")
    challenge_f_code()
    print("--- Your Prediction ---")
    challenge_f_prediction()

    print("\n--- Challenge G: Actual Output ---")
    challenge_g_code()
    print("--- Your Prediction ---")
    challenge_g_prediction()

    print("\n--- Challenge H: Actual Output ---")
    challenge_h_code()
    print("--- Your Prediction ---")
    challenge_h_prediction()

    print("\n" + "="*40)
    print("Compare your predictions with the actual output!")


main()
