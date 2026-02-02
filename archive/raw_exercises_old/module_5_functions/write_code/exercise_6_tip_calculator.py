# Exercise 6: Tip Calculator

def calculate_tip(bill_amount, tip_percent):
    # ✏️ YOUR CODE HERE ✏️
    # Calculate the tip amount and return it
    # Example: bill is $50, tip is 20% -> return 10.0
    #
    # Hint: tip_percent is a whole number like 15 or 20
    # You need to divide by 100 to get the decimal
    pass


def calculate_total(bill_amount, tip_amount):
    # ✏️ YOUR CODE HERE ✏️
    # Add the bill and tip together and return the total
    pass


def split_bill(total, num_people):
    # ✏️ YOUR CODE HERE ✏️
    # Divide the total by the number of people and return it
    # This tells each person how much they owe
    pass


def main():
    print("=== Tip Calculator ===\n")

    bill = float(input("Enter the bill amount: $"))
    tip_percent = int(input("Tip percentage (e.g., 15, 18, 20): "))

    tip = calculate_tip(bill, tip_percent)
    total = calculate_total(bill, tip)

    print("\n--- Receipt ---")
    print("Bill:  $" + str(bill))
    print("Tip:   $" + str(tip))
    print("Total: $" + str(total))

    split = input("\nSplit the bill? (y/n): ")
    if split.lower() == "y":
        people = int(input("How many people? "))
        each = split_bill(total, people)
        print("Each person pays: $" + str(round(each, 2)))


main()
