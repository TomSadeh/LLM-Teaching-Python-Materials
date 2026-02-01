# Exercise 8: RPG Inventory System


def display_inventory(inventory):
    # ✏️ YOUR CODE HERE ✏️
    # Print the inventory in a nice format:
    # ========== INVENTORY ==========
    # {{item}}: 1
    # health potion: 5
    # gold: 100
    # ================================
    pass


def add_item(inventory, item, quantity):
    # ✏️ YOUR CODE HERE ✏️
    # If item exists, add to quantity
    # If item doesn't exist, create it with the quantity
    # Return the updated inventory
    pass


def remove_item(inventory, item, quantity):
    # ✏️ YOUR CODE HERE ✏️
    # Subtract quantity from item
    # If quantity becomes 0 or less, remove the item entirely
    # If item doesn't exist, print "You don't have that item!"
    # Return the updated inventory
    pass


def use_item(inventory, item):
    # ✏️ YOUR CODE HERE ✏️
    # "Use" an item (remove 1 of it)
    # Print what was used: "You used [item]!"
    # Special effects:
    # - If "health potion": print "Health restored!"
    # - If "{{item}}": print "{{spell1}}!"
    # Return the updated inventory
    pass


def shop(inventory, gold):
    # ✏️ YOUR CODE HERE ✏️
    # Create a shop with items and prices
    shop_items = {
        "health potion": 10,
        "mana potion": 15,
        "{{item}}": 50,
        "{{pet}}": 100
    }
    # Display shop items
    # Ask what they want to buy
    # Check if they have enough gold
    # Add item to inventory, subtract gold
    # Return updated inventory and gold
    pass


def main():
    print("=" * 40)
    print("   {{hero}}'s INVENTORY SYSTEM")
    print("=" * 40)
    print()

    # Starting inventory
    inventory = {
        "{{item}}": 1,
        "health potion": 3,
        "gold": 50
    }

    print("=== Starting Inventory ===")
    display_inventory(inventory)

    print("\n=== Adding Items ===")
    inventory = add_item(inventory, "health potion", 2)
    inventory = add_item(inventory, "map", 1)
    display_inventory(inventory)

    print("\n=== Using an Item ===")
    inventory = use_item(inventory, "health potion")
    display_inventory(inventory)

    print("\n=== Removing Items ===")
    inventory = remove_item(inventory, "health potion", 2)
    display_inventory(inventory)

    print("\n=== Shopping ===")
    gold = inventory.get("gold", 0)
    inventory, gold = shop(inventory, gold)
    inventory["gold"] = gold
    display_inventory(inventory)


main()
