# Exercise 9: Leap Year Checker

def is_leap_year(year):
    # ✏️ YOUR CODE HERE ✏️
    # Return True if the year is a leap year, False otherwise
    #
    # Leap year rules:
    # 1. If the year is divisible by 4, it MIGHT be a leap year
    # 2. BUT if it's divisible by 100, it's NOT a leap year
    # 3. UNLESS it's also divisible by 400, then it IS a leap year
    #
    # Examples:
    # 2024 -> leap year (divisible by 4)
    # 1900 -> NOT a leap year (divisible by 100 but not 400)
    # 2000 -> leap year (divisible by 400)
    #
    # Hint: Use the modulo operator % to check divisibility
    # Hint: You'll need to combine conditions with 'and' and 'or'
    pass


def main():
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print(year, "is a leap year!")
    else:
        print(year, "is not a leap year.")


main()
