"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll explore advanced random module functions
beyond the basic randint() you already know. These are essential
for games, simulations, and any randomized features.

Topic: Extended random module (choice, shuffle, sample)
Difficulty: 2
"""

import random


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn random.choice() - pick a random item from a sequence.
    #
    # Step 1: Create a list of options:
    #         options = ["{{spell1}}", "{{spell2}}", "{{spell3}}", "{{spell4}}"]
    #
    # Step 2: Use random.choice() to pick one:
    #         selected = random.choice(options)
    #
    # Step 3: Print: "Selected: [selected]"
    #
    # Step 4: Make 5 random selections and print each one
    #         Use a for loop: for i in range(5):
    #
    # Note: choice() works with any sequence (list, string, tuple)
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn random.shuffle() - randomize the order of a list.
    #
    # Step 1: Create a list to shuffle:
    #         items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    # Step 2: Print the original list:
    #         print(f"Original: {items}")
    #
    # Step 3: Shuffle the list IN PLACE:
    #         random.shuffle(items)
    #         Note: shuffle() modifies the original list!
    #
    # Step 4: Print the shuffled list:
    #         print(f"Shuffled: {items}")
    #
    # Step 5: Create and shuffle a list of characters:
    #         characters = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
    #         random.shuffle(characters)
    #         print(f"Turn order: {characters}")
    #
    # Note: shuffle() returns None, it changes the list directly
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn random.sample() - pick multiple unique items.
    #
    # Step 1: Create a pool of items:
    #         pool = ["{{item}}", "gold", "gem", "key", "scroll", "potion"]
    #
    # Step 2: Sample 3 unique items (no repeats):
    #         rewards = random.sample(pool, 3)
    #         print(f"You found: {rewards}")
    #
    # Step 3: The difference from choice():
    #         - choice() picks 1 item
    #         - sample(list, n) picks n UNIQUE items
    #         - sample() does NOT modify the original list
    #
    # Step 4: Try sampling from a range:
    #         lottery = random.sample(range(1, 50), 6)
    #         print(f"Lottery numbers: {sorted(lottery)}")
    #
    # Step 5: What happens if you try sample(pool, 10)?
    #         (You can't sample more items than exist - it's an error!)
    #         Just print: "Can't sample 10 from a list of 6 items"
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    print("random.choice() - Pick one random item")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    print("random.shuffle() - Randomize order")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    print("random.sample() - Pick multiple unique items")
    exercise_c()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print()
    print("Summary:")
    print("  choice(seq)      -> 1 random item")
    print("  shuffle(list)    -> reorder in place")
    print("  sample(seq, n)   -> n unique items (new list)")


main()
