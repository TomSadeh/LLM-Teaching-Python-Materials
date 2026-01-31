# Exercise 9: Magical Contact Book


def create_contact_book():
    # ✏️ YOUR CODE HERE ✏️
    # Create a contact book where each contact has:
    # - name (as the key)
    # - house, year, owl_name (as a nested dictionary)
    #
    # Start with a few contacts:
    contacts = {
        "{{hero}}": {
            "house": "{{house}}",
            "year": 5,
            "pet": "{{pet}}"
        },
        "{{heroine}}": {
            "house": "{{house}}",
            "year": 5,
            "pet": "{{pet}}"
        }
    }
    return contacts


def add_contact(contacts):
    # ✏️ YOUR CODE HERE ✏️
    # Ask for: name, house, year, pet name
    # Add to the contacts dictionary
    # Print confirmation: "Added [name] to your contacts!"
    pass


def find_contact(contacts):
    # ✏️ YOUR CODE HERE ✏️
    # Ask for a name to search
    # If found, print all their info nicely
    # If not found, print "Contact not found!"
    # Bonus: allow partial name matching!
    pass


def list_by_house(contacts):
    # ✏️ YOUR CODE HERE ✏️
    # Ask which house to filter by
    # Print all contacts in that house
    pass


def delete_contact(contacts):
    # ✏️ YOUR CODE HERE ✏️
    # Ask for a name to delete
    # Remove from contacts if found
    # Print confirmation or "not found" message
    pass


def contact_menu():
    # ✏️ YOUR CODE HERE ✏️
    # Create an interactive menu:
    # 1. View all contacts
    # 2. Add new contact
    # 3. Search for contact
    # 4. List by house
    # 5. Delete contact
    # 6. Exit
    #
    # Keep running until user chooses Exit!
    contacts = create_contact_book()

    while True:
        print("\n--- MAGICAL CONTACT BOOK ---")
        print("1. View all contacts")
        print("2. Add new contact")
        print("3. Search for contact")
        print("4. List by house")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "6":
            print("{{greeting}}")
            break
        # Add the rest of the menu options here!


def main():
    print("=" * 40)
    print("   MAGICAL CONTACT BOOK")
    print("   {{school}} Edition")
    print("=" * 40)

    contact_menu()


main()
