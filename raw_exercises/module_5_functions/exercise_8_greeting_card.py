# Exercise 8: Greeting Card Maker

def make_border(width, char="*"):
    # ✏️ YOUR CODE HERE ✏️
    # Return a string of 'char' repeated 'width' times
    # Example: make_border(5, "*") returns "*****"
    #
    # Hint: You can multiply strings! "*" * 3 = "***"
    pass


def center_text(text, width):
    # ✏️ YOUR CODE HERE ✏️
    # Return the text centered in a line of the given width
    #
    # Example: center_text("Hi", 10) returns "    Hi    "
    #
    # Hint: Use the .center() string method
    # Or calculate spaces needed on each side
    pass


def make_card(recipient, message, width=30):
    # ✏️ YOUR CODE HERE ✏️
    # Create and print a greeting card!
    #
    # It should look something like this:
    # ******************************
    # *                            *
    # *        Happy Birthday      *
    # *           Sarah!           *
    # *                            *
    # *   Wishing you a great day  *
    # *                            *
    # ******************************
    #
    # Use make_border() and center_text() to help!
    #
    # Hint: For middle lines, you need a * at start and end
    # with the centered text in between
    pass


def main():
    print("=== Greeting Card Maker ===\n")

    recipient = input("Who is this card for? ")
    print("\nChoose a greeting:")
    print("1. Happy Birthday")
    print("2. Congratulations")
    print("3. Thank You")
    print("4. Custom message")

    choice = input("Your choice: ")

    if choice == "1":
        greeting = "Happy Birthday"
    elif choice == "2":
        greeting = "Congratulations"
    elif choice == "3":
        greeting = "Thank You"
    else:
        greeting = input("Enter your greeting: ")

    message = input("Add a short message: ")

    print("\n")
    make_card(recipient, greeting + " " + recipient + "!\n" + message)


main()
