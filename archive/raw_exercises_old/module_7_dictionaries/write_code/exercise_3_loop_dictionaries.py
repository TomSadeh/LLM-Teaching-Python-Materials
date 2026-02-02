# Exercise 3: Looping Through Dictionaries


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a spellbook dictionary with at least 3 spells and their power:
    # Example: {"{{spell1}}": 10, "{{spell2}}": 25, "{{spell3}}": 50}
    # Loop through and print each spell name (the keys)
    # Hint: for spell in spellbook:
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Using the same spellbook, print both the spell AND its power
    # Like: "{{spell1}} - Power: 10"
    # Hint: for spell in spellbook: print(spell, spellbook[spell])
    # Or: for spell, power in spellbook.items():
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create an inventory dictionary with items and quantities:
    # {"{{item}}": 1, "health potion": 5, "gold coins": 100, "map": 1}
    # Loop through and print items where quantity > 1
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a dictionary of students and their houses:
    # {"{{hero}}": "{{house}}", "{{heroine}}": "{{house}}", "{{friend}}": "{{house}}"}
    # Count how many students are in "{{house}}"
    # Print: "{{house}} has [count] students"
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create a spellbook with spells and power levels
    # Find and print the most powerful spell!
    # Hint: keep track of the highest power you've seen
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Create a price list dictionary:
    # {"{{item}}": 10, "{{pet}}": 50, "potion": 5, "cloak": 25}
    # Calculate and print the total value of buying one of each
    pass


def main():
    print("=== Exercise A: Print All Spells ===")
    exercise_a()

    print("\n=== Exercise B: Spells with Power ===")
    exercise_b()

    print("\n=== Exercise C: Filter Inventory ===")
    exercise_c()

    print("\n=== Exercise D: Count by House ===")
    exercise_d()

    print("\n=== Exercise E: Most Powerful Spell ===")
    exercise_e()

    print("\n=== Exercise F: Shopping Total ===")
    exercise_f()


main()
