# Exercise 7: Shopping List Total

def calculate_total(prices):
    # ✏️ YOUR CODE HERE ✏️
    # Add up all the prices and return the total
    #
    # Hint: Start with total = 0
    # Hint: Loop through the prices and add each one to total
    pass


def main():
    print("=== Shopping Calculator ===\n")

    prices = []
    items = []

    # Collect items and prices
    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item.lower() == "done":
            break
        price = float(input("Enter price for " + item + ": $"))
        items.append(item)
        prices.append(price)

    # Show the receipt
    print("\n--- Your Receipt ---")
    for i in range(len(items)):
        print(items[i] + ": $" + str(prices[i]))

    print("-------------------")
    total = calculate_total(prices)
    print("Total: $" + str(total))


main()
