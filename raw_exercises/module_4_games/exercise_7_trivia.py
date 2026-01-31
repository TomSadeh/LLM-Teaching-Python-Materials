# Exercise 7: Book Trivia Quiz Game!

def ask_question(question, choices, correct_index):
    # ✏️ YOUR CODE HERE ✏️
    # 1. Print the question
    # 2. Print all the choices with letters (A, B, C, D)
    # 3. Get the player's answer
    # 4. Return True if correct, False if wrong
    #
    # Hint: choices is a list like ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
    # Hint: correct_index tells you which one is right (0 = A, 1 = B, etc.)
    pass


def main():
    print("📚 Ultimate Book Trivia Quiz! 📚\n")

    # Questions: (question, choices, correct_index)
    # Mix of Harry Potter, Percy Jackson, Hunger Games, and Keeper of the Lost Cities!
    questions = [
        # Harry Potter
        ("What house is Harry Potter sorted into?",
         ["Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw"], 1),

        # Keeper of the Lost Cities
        ("What is Sophie Foster's main ability?",
         ["Vanisher", "Telepath", "Empath", "Shade"], 1),

        # Percy Jackson
        ("Who is Percy Jackson's godly parent?",
         ["Zeus", "Hades", "Poseidon", "Apollo"], 2),

        # Hunger Games
        ("What district is Katniss Everdeen from?",
         ["District 1", "District 4", "District 11", "District 12"], 3),

        # Harry Potter
        ("What is the name of the spell that produces light?",
         ["Expelliarmus", "Lumos", "Accio", "Patronum"], 1),

        # Keeper of the Lost Cities
        ("What school do elves attend in Keeper of the Lost Cities?",
         ["Hogwarts", "Exillium", "Foxfire", "Camp Half-Blood"], 2),

        # Percy Jackson
        ("What is the name of the camp for demigods?",
         ["Camp Jupiter", "Camp Half-Blood", "Camp Olympus", "Camp Demigod"], 1),

        # Hunger Games
        ("What is Katniss's weapon of choice?",
         ["Sword", "Spear", "Bow and arrow", "Knife"], 2),
    ]

    score = 0

    # ✏️ YOUR CODE HERE ✏️
    # Loop through the questions list
    # For each question, call ask_question() with the right arguments
    # If they got it right, add 1 to score

    print("\n=== Results ===")
    print("You got", score, "out of", len(questions), "correct!")

    if score == len(questions):
        print("🏆 You're a true book expert!")
    elif score >= len(questions) // 2:
        print("📖 Great job, fellow reader!")
    else:
        print("📚 Time to re-read some books!")


main()
