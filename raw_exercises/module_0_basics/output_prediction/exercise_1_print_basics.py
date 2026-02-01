# Exercise 1: Output Prediction - Print Basics
#
# Read the code carefully and predict what it will print.
# Do NOT run the code - practice mental execution!
#
# Theme: Messages from {{school}}


# --- PREDICTION CHALLENGE A ---
# What happens when you print multiple things?

def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    print("{{greeting}}")
    print("Welcome to", "{{school}}")
    print("Your" + " " + "adventure" + " " + "begins!")


def challenge_a_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    # How many lines? What's on each line?
    #
    # Hint: print() with commas adds spaces between items
    pass


# --- PREDICTION CHALLENGE B ---
# What happens with numbers in print?

def challenge_b_code():
    """DO NOT MODIFY - Just read and predict"""
    print(5 + 3)
    print("5 + 3")
    print("5" + "3")


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Think about what quotes do
    pass


# --- PREDICTION CHALLENGE C ---
# Variables and printing

def challenge_c_code():
    """DO NOT MODIFY - Just read and predict"""
    hero = "{{hero}}"
    house = "{{house}}"
    print(hero)
    print("hero")
    print(hero, "is in", house)


def challenge_c_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: What's the difference between hero and "hero"?
    pass


# --- PREDICTION CHALLENGE D ---
# String multiplication

def challenge_d_code():
    """DO NOT MODIFY - Just read and predict"""
    print("*" * 5)
    print("{{spell1}} " * 3)
    spell = "{{spell2}}"
    print(spell * 2)


def challenge_d_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: What does * do with strings?
    pass


# --- PREDICTION CHALLENGE E ---
# Counting with range

def challenge_e_code():
    """DO NOT MODIFY - Just read and predict"""
    for i in range(3):
        print(i)


def challenge_e_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: What number does range(3) start at? End at?
    pass


# --- PREDICTION CHALLENGE F ---
# Loop with a message

def challenge_f_code():
    """DO NOT MODIFY - Just read and predict"""
    for i in range(1, 4):
        print("{{exclamation}}!")
    print("Done!")


def challenge_f_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: How many times does the loop run? Is "Done!" inside the loop?
    pass


def main():
    print("=== Output Prediction: Print Basics ===")
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

    print("\n" + "="*40)
    print("Compare your predictions with the actual output!")


main()
