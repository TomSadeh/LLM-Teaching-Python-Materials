# Exercise 4: Fantasy Story Generator!

import random


def get_random_word(word_list):
    return random.choice(word_list)


def create_story():
    # Word lists - add more words from your favorite books!
    heroes = ["Sophie Foster", "Percy Jackson", "Katniss", "Harry Potter", "Keefe", "Annabeth"]
    creatures = ["alicorn", "hippogriff", "hellhound", "Mockingjay", "phoenix", "dragon"]
    abilities = ["telepathy", "water control", "archery", "magic", "vanishing", "fire"]
    places = ["Foxfire Academy", "Camp Half-Blood", "the Capitol", "Hogwarts", "the Forbidden Forest"]
    villains = ["the Neverseen", "Kronos", "President Snow", "Voldemort"]

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
