# Exercise 2: Output Prediction - Loops
#
# Read the code carefully and predict what it will print.
# Do NOT run the code - practice mental execution!
#
# Theme: {{hero}}'s training sessions at {{school}}


# --- PREDICTION CHALLENGE A ---
# Basic counting loop

def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    for i in range(5):
        print(i)


def challenge_a_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    # How many lines? What number is on each line?
    #
    # Hint: range(5) gives how many numbers? Starting from?
    pass


# --- PREDICTION CHALLENGE B ---
# Range with start and stop

def challenge_b_code():
    """DO NOT MODIFY - Just read and predict"""
    for i in range(2, 6):
        print(i)


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: range(start, stop) - does it include the stop value?
    pass


# --- PREDICTION CHALLENGE C ---
# Range with step

def challenge_c_code():
    """DO NOT MODIFY - Just read and predict"""
    for i in range(0, 10, 2):
        print(i)


def challenge_c_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: The third number in range() is the step
    pass


# --- PREDICTION CHALLENGE D ---
# Loop with accumulator

def challenge_d_code():
    """DO NOT MODIFY - Just read and predict"""
    total = 0
    for i in range(1, 4):
        total = total + i
        print(total)


def challenge_d_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Track both i and total as the loop runs
    # i=1: total = 0+1 = ?
    # i=2: total = ?+2 = ?
    # i=3: total = ?+3 = ?
    pass


# --- PREDICTION CHALLENGE E ---
# Countdown loop

def challenge_e_code():
    """DO NOT MODIFY - Just read and predict"""
    for i in range(3, 0, -1):
        print(i)
    print("{{exclamation}}!")


def challenge_e_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: Negative step means counting down. What's the last value?
    pass


# --- PREDICTION CHALLENGE F ---
# Nested print in loop

def challenge_f_code():
    """DO NOT MODIFY - Just read and predict"""
    for i in range(3):
        print("*" * (i + 1))


def challenge_f_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: When i=0, i+1=1, so "*"*1 = ?
    # When i=1, i+1=2, so "*"*2 = ?
    pass


# --- PREDICTION CHALLENGE G ---
# Loop variable after loop ends

def challenge_g_code():
    """DO NOT MODIFY - Just read and predict"""
    for i in range(5):
        pass
    print(i)


def challenge_g_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: The loop variable still exists after the loop!
    # What's the LAST value i had?
    pass


# --- PREDICTION CHALLENGE H ---
# Loop with condition inside

def challenge_h_code():
    """DO NOT MODIFY - Just read and predict"""
    count = 0
    for i in range(5):
        if i % 2 == 0:
            count = count + 1
    print(count)


def challenge_h_prediction():
    # ✏️ YOUR PREDICTION ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Hint: % 2 == 0 checks if a number is even
    # Which numbers in 0,1,2,3,4 are even?
    pass


def main():
    print("=== Output Prediction: Loops ===")
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
