# Final Project Template: Useful App

# ==================
# DATA STORAGE
# ==================
items = []  # Store your app's data here


# ==================
# DISPLAY FUNCTIONS
# ==================

def show_menu():
    print("\n📱 My App 📱")
    print("============")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Quit")


def show_all_items():
    if len(items) == 0:
        print("No items yet!")
    else:
        print("\nYour items:")
        counter = 1
        for item in items:
            print(str(counter) + ". " + item)
            counter = counter + 1


# ==================
# ACTION FUNCTIONS
# ==================

def add_item():
    # Add something to the list
    new_item = input("Enter new item: ")
    items.append(new_item)
    print("Added:", new_item)


def remove_item():
    # Remove something from the list
    show_all_items()
    if len(items) > 0:
        choice = int(input("Which number to remove? "))
        if choice >= 1 and choice <= len(items):
            removed = items.pop(choice - 1)
            print("Removed:", removed)


def do_something_special():
    # Your special feature!
    pass


# ==================
# MAIN APP
# ==================

def handle_choice(choice):
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        do_something_special()
    elif choice == "4":
        return False  # Quit
    else:
        print("Invalid choice!")
    return True  # Keep running


def main():
    print("Welcome to My App!")

    running = True
    while running:
        show_menu()
        choice = input("\nYour choice: ")
        running = handle_choice(choice)

    print("Goodbye!")


main()
