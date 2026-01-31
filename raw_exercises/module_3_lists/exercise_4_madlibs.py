# Exercise 4: Fantasy Story Generator!

import random


def get_random_word(word_list):
    return random.choice(word_list)


def create_story():
    # Word lists - add more words from your favorite books!
    heroes = ["{{heroine}}", "{{hero}}", "{{heroine}}", "{{hero}}", "{{hero}}", "{{heroine}}"]
    creatures = ["{{creature}}", "{{creature}}", "{{creature}}", "{{creature}}", "{{creature}}", "{{creature}}"]
    abilities = ["{{spell1}}", "water control", "archery", "magic", "{{spell2}}", "fire"]
    places = ["{{school}}", "{{school}}", "{{place}}", "{{school}}", "{{location}}"]
    villains = ["{{villain}}", "{{villain}}", "{{villain}}", "{{villain}}"]

    # ✏️ YOUR CODE HERE ✏️
    # 1. Use get_random_word() to pick words from each list
    # 2. Put them together into an epic story!
    # 3. Print the story!
    #
    # Example:
    # hero = get_random_word(heroes)
    # Then use the variable in your story:
    # print(hero + " discovered a secret...")
    #
    # Make your story at least 3 sentences!
    # Include a hero, a place, an ability, and maybe a villain!
    pass


def main():
    print("📚 Fantasy Story Generator 📚")
    print("=" * 30)
    create_story()
    print()
    print("Run again for a different story!")


main()
