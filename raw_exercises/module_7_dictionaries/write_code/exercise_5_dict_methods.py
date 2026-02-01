# Exercise 5: Useful Dictionary Methods


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a character dictionary
    # Use .keys() to print all the keys
    # Use .values() to print all the values
    # Use .items() to print key-value pairs
    character = {"name": "{{hero}}", "house": "{{house}}", "year": 1}
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Check if a spell exists using "in"
    spellbook = {"{{spell1}}": 10, "{{spell2}}": 25}
    spell_to_find = "{{spell3}}"
    # Print whether the spell is in the spellbook or not
    # Hint: if spell_to_find in spellbook:
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Use .get() for safe access
    inventory = {"{{item}}": 1, "potion": 3}
    # Try to get "gold" - if it doesn't exist, default to 0
    # Hint: inventory.get("gold", 0)
    # Print how much gold the player has
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Use .pop() to remove and return an item
    backpack = {"{{item}}": 1, "map": 1, "food": 5, "rope": 1}
    # Remove "food" and store it in a variable
    # Print what was removed and what's left in the backpack
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Combine two dictionaries using .update()
    base_stats = {"health": 100, "mana": 50}
    bonus_stats = {"strength": 10, "health": 120}  # Note: health will be updated!
    # Use base_stats.update(bonus_stats)
    # Print the combined stats
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Create a copy of a dictionary using .copy()
    original = {"name": "{{hero}}", "level": 5}
    # Make a copy, then change the copy's level to 10
    # Print both to show they're different
    pass


def exercise_g():
    # ✏️ YOUR CODE HERE ✏️
    # Interactive spell lookup!
    spells = {
        "{{spell1}}": "Creates light",
        "{{spell2}}": "Disarms opponent",
        "{{spell3}}": "Summons a guardian",
        "{{spell4}}": "Makes things float"
    }
    # Ask user for a spell name
    # Use .get() to find it, with a default message "Spell not found!"
    pass


def main():
    print("=== Exercise A: keys(), values(), items() ===")
    exercise_a()

    print("\n=== Exercise B: Check if Key Exists ===")
    exercise_b()

    print("\n=== Exercise C: Safe Access with .get() ===")
    exercise_c()

    print("\n=== Exercise D: Remove with .pop() ===")
    exercise_d()

    print("\n=== Exercise E: Combine with .update() ===")
    exercise_e()

    print("\n=== Exercise F: Copy a Dictionary ===")
    exercise_f()

    print("\n=== Exercise G: Spell Lookup ===")
    exercise_g()


main()
