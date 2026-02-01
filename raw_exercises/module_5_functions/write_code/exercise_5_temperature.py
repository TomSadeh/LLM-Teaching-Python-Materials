# Exercise 5: Temperature Converter

def celsius_to_fahrenheit(celsius):
    # ✏️ YOUR CODE HERE ✏️
    # Convert Celsius to Fahrenheit and return the result
    # Formula: F = (C × 9/5) + 32
    pass


def fahrenheit_to_celsius(fahrenheit):
    # ✏️ YOUR CODE HERE ✏️
    # Convert Fahrenheit to Celsius and return the result
    # Formula: C = (F - 32) × 5/9
    pass


def main():
    print("=== Temperature Converter ===\n")

    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("\nYour choice (1 or 2): ")

    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(temp)
        print(temp, "°C =", result, "°F")
    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(temp)
        print(temp, "°F =", result, "°C")
    else:
        print("Invalid choice!")


main()
