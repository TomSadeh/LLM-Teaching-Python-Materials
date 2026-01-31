# Exercise 6: Simple Calculator

def calculate(num1, num2, operation):
    # ✏️ YOUR CODE HERE ✏️
    # Do the math based on the operation:
    # "+" -> add the numbers
    # "-" -> subtract num2 from num1
    # "*" -> multiply the numbers
    # "/" -> divide num1 by num2
    #
    # Return the result
    #
    # Hint: Use if/elif/else to check which operation
    # Bonus: What happens if someone tries to divide by 0?
    pass


def main():
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    result = calculate(num1, num2, operation)
    print("Result:", result)


main()
