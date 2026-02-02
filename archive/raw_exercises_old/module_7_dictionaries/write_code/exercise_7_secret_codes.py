# Exercise 7: Secret Codes with Dictionaries (Cipher Fun!)


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a simple substitution cipher dictionary:
    # Each letter maps to a different letter
    cipher = {
        "a": "z", "b": "y", "c": "x", "d": "w", "e": "v",
        "f": "u", "g": "t", "h": "s", "i": "r", "j": "q",
        "k": "p", "l": "o", "m": "n", "n": "m", "o": "l",
        "p": "k", "q": "j", "r": "i", "s": "h", "t": "g",
        "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"
    }
    # Encode the word "hello" using the cipher
    # Hint: loop through each letter and look it up in cipher
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Ask the user for a word
    # Encode it using the cipher from exercise_a
    # Print the secret message!
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create a number cipher (A=1, B=2, etc.)
    # Encode a word as numbers
    # Example: "cat" becomes "3 1 20"
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # DECODE a message!
    # Create the reverse cipher (z=a, y=b, etc.)
    # Or use the same cipher since it's symmetric!
    # Decode: "svool" (what word is it?)
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create your own secret code!
    # Maybe use symbols: {"a": "@", "e": "3", "i": "!", ...}
    # Or {{school}}-themed codes!
    # Encode a secret message about {{hero}}
    pass


def encoder_decoder():
    # ✏️ YOUR CODE HERE ✏️
    # Build a complete encoder/decoder program!
    # 1. Ask: "Do you want to (E)ncode or (D)ecode?"
    # 2. Ask for the message
    # 3. Encode or decode based on choice
    # 4. Print the result
    #
    # Hint: for decoding, you need the reverse mapping!
    # You can create it with: {v: k for k, v in cipher.items()}
    pass


def main():
    print("=" * 35)
    print("   SECRET CODE HEADQUARTERS")
    print("=" * 35)
    print()

    print("=== Exercise A: Basic Cipher ===")
    exercise_a()

    print("\n=== Exercise B: Encode User Input ===")
    exercise_b()

    print("\n=== Exercise C: Number Cipher ===")
    exercise_c()

    print("\n=== Exercise D: Decode Message ===")
    exercise_d()

    print("\n=== Exercise E: Custom Code ===")
    exercise_e()

    print("\n=== Full Encoder/Decoder ===")
    encoder_decoder()


main()
