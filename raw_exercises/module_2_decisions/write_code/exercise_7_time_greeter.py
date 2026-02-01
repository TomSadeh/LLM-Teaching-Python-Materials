# Exercise 7: Time of Day Greeter

def get_greeting(hour):
    # ✏️ YOUR CODE HERE ✏️
    # Return a greeting based on the hour (0-23):
    # 5-11: "Good morning!"
    # 12-16: "Good afternoon!"
    # 17-20: "Good evening!"
    # 21-4: "Good night!"
    #
    # Hint: Use if/elif/else
    pass


def main():
    hour = int(input("What hour is it? (0-23): "))

    if hour < 0 or hour > 23:
        print("That's not a valid hour!")
    else:
        greeting = get_greeting(hour)
        print(greeting)


main()
