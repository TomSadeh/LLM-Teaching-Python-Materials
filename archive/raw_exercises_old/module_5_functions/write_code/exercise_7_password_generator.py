# Exercise 7: Magical Spell Generator!

import random


def generate_spell(length):
    # ✏️ YOUR CODE HERE ✏️
    # Generate a random magical spell name of the given length
    #
    # Steps:
    # 1. Create a string of magical-sounding letters to choose from
    #    Example: characters = "aeioulmnrstvxz"
    #    (Using more vowels makes it easier to pronounce!)
    # 2. Start with an empty spell string
    # 3. Loop 'length' times, each time picking a random character
    #    Hint: use random.choice(characters)
    # 4. Return the spell
    #
    # Bonus: Capitalize the first letter!
    # Bonus: Add a magical suffix like "us", "ium", or "ara"!
    pass


def generate_spells(count, length):
    # ✏️ YOUR CODE HERE ✏️
    # Generate multiple spells and return them in a list
    #
    # Hint: Create an empty list
    # Hint: Loop 'count' times
    # Hint: Each time, generate a spell and append it to the list
    pass


def main():
    print("🪄 Magical Spell Generator 🪄")
    print("Create new spells like a true wizard!\n")

    length = int(input("How long should the spell be? "))
    count = int(input("How many spells to generate? "))

    spells = generate_spells(count, length)

    print("\n✨ Your new spells: ✨")
    print("-" * 20)
    for spell in spells:
        print(spell)

    print("\nTry saying them out loud!")


main()
