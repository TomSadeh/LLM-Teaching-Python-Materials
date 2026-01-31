# Exercise 2: Calculator with Functions


def add(a, b):
    # ✏️ YOUR CODE HERE ✏️
    # Return a + b
    pass


def subtract(a, b):
    # ✏️ YOUR CODE HERE ✏️
    # Return a - b
    pass


def multiply(a, b):
    # ✏️ YOUR CODE HERE ✏️
    # Return a * b
    pass


def divide(a, b):
    # ✏️ YOUR CODE HERE ✏️
    # Return a / b
    # Bonus: what if b is 0? Handle that case!
    pass


def calculate(num1, num2, operation):
    # ✏️ YOUR CODE HERE ✏️
    # Based on operation (+, -, *, /), call the right function
    # and return the result
    #
    # Example: calculate(5, 3, "+") should return 8
    pass


def main():
    print("🔢 Calculator 🔢")
    print("================")

    num1 = float(input("First number: "))
    operation = input("Operation (+, -, *, /): ")
    num2 = float(input("Second number: "))

    result = calculate(num1, num2, operation)
    print("Result:", result)


main()
