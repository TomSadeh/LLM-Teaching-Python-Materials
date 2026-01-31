# Exercise 9: Word Collector

def count_words(words):
    # ✏️ YOUR CODE HERE ✏️
    # Return how many words are in the list
    # Hint: use len()
    pass


def find_longest(words):
    # ✏️ YOUR CODE HERE ✏️
    # Return the longest word in the list
    #
    # Hint: Start by assuming the first word is longest
    # Hint: Loop through and compare lengths using len()
    # Hint: If you find a longer word, update your answer
    pass


def find_shortest(words):
    # ✏️ YOUR CODE HERE ✏️
    # Return the shortest word in the list
    # Same idea as find_longest, but opposite!
    pass


def main():
    print("=== Word Collector ===")
    print("Enter words one at a time. Type 'done' when finished.\n")

    words = []

    # Collect words
    while True:
        word = input("Enter a word: ")
        if word.lower() == "done":
            break
        words.append(word)

    # Show results
    if len(words) == 0:
        print("You didn't enter any words!")
    else:
        print("\n--- Results ---")
        print("You entered", count_words(words), "words")
        print("All your words:", words)
        print("Longest word:", find_longest(words))
        print("Shortest word:", find_shortest(words))


main()
