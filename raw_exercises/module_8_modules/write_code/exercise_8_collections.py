# Exercise 8: The Collections Module (Counter and More!)

from collections import Counter


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Use Counter to count items in a list!
    spells_used = ["{{spell1}}", "{{spell2}}", "{{spell1}}", "{{spell3}}",
                   "{{spell1}}", "{{spell2}}", "{{spell4}}"]
    # spell_counts = Counter(spells_used)
    # Print which spell was used most often
    # Hint: .most_common(1) returns the top item
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Count characters in a string!
    # Count how many of each letter in "{{school}}"
    # Print the 3 most common letters
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Word frequency counter!
    # Ask user for a sentence
    # Count how many times each word appears
    # (Hint: split into words first, then use Counter)
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Battle log analyzer!
    # Given a list of battle actions:
    actions = ["attack", "defend", "attack", "spell", "attack",
               "heal", "spell", "attack", "defend"]
    # Count and display what actions were used most
    # Show a simple bar chart using * characters!
    # Example: attack: ****
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Inventory collector!
    # Two adventurers combine their loot:
    loot1 = Counter({"gold": 50, "potion": 3, "{{item}}": 1})
    loot2 = Counter({"gold": 30, "potion": 2, "gem": 5})
    # Add them together and display total inventory
    # Hint: combined = loot1 + loot2
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Vote counter!
    # Create a voting system for "Best Character"
    # Ask multiple users to vote (loop until they type "done")
    # Count votes and announce the winner!
    pass


def dice_statistics():
    # ✏️ YOUR CODE HERE ✏️
    # Roll dice 100 times and analyze!
    # Use Counter to track how often each number appears
    # Print a histogram showing the distribution
    # (Should be roughly even for a fair die!)
    pass


def main():
    print("=== Exercise A: Count Spells ===")
    exercise_a()

    print("\n=== Exercise B: Letter Frequency ===")
    exercise_b()

    print("\n=== Exercise C: Word Frequency ===")
    exercise_c()

    print("\n=== Exercise D: Battle Log ===")
    exercise_d()

    print("\n=== Exercise E: Combine Inventories ===")
    exercise_e()

    print("\n=== Exercise F: Voting System ===")
    exercise_f()

    print("\n=== Dice Statistics ===")
    dice_statistics()


main()
