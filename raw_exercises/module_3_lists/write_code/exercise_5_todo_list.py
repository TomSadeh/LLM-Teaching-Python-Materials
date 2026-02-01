# Exercise 5: Todo List Manager

def show_todos(todos):
    # ✏️ YOUR CODE HERE ✏️
    # Print all todos with numbers
    # If the list is empty, print "No todos yet!"
    #
    # Example output:
    # 1. Buy milk
    # 2. Do homework
    # 3. Walk the dog
    pass


def add_todo(todos, item):
    # ✏️ YOUR CODE HERE ✏️
    # Add the item to the todos list
    # Hint: use the .append() method
    pass


def remove_todo(todos, number):
    # ✏️ YOUR CODE HERE ✏️
    # Remove the todo at position 'number' (1-based, not 0-based!)
    # Hint: lists are 0-indexed, so item 1 is at index 0
    # Hint: use the .pop() method with an index
    pass


def main():
    todos = []

    while True:
        print("\n--- Todo List ---")
        show_todos(todos)
        print("\nCommands: add, remove, quit")
        command = input("What do you want to do? ").lower()

        if command == "add":
            item = input("What do you need to do? ")
            add_todo(todos, item)
            print("Added!")
        elif command == "remove":
            number = int(input("Which number to remove? "))
            remove_todo(todos, number)
            print("Removed!")
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("I don't understand that command.")


main()
