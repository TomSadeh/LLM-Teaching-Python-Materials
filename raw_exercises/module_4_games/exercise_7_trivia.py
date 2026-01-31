# Exercise 7: Book Trivia Quiz Game!

def ask_question(question, choices, correct_index):
    # ✏️ YOUR CODE HERE ✏️
    # 1. Print the question
    # 2. Print all the choices with letters (A, B, C, D)
    # 3. Get the player's answer
    # 4. Return True if correct, False if wrong
    #
    # Hint: choices is a list like ["{{house}}", "{{house}}", "{{house}}", "{{house}}"]
    # Hint: correct_index tells you which one is right (0 = A, 1 = B, etc.)
    pass


def main():
    print("📚 Ultimate Book Trivia Quiz! 📚\n")

    # Questions: (question, choices, correct_index)
    # Mix of {{hero}}, {{hero}}, Hunger Games, and {{school}} series!
    questions = [
        # {{hero}}
        ("What house is {{hero}} sorted into?",
         ["{{house}}", "{{house}}", "{{house}}", "{{house}}"], 1),

        # {{school}} series
        ("What is {{heroine}}'s main ability?",
         ["{{spell2}}", "{{spell1}}", "{{spell1}}", "{{spell2}}"], 1),

        # {{hero}}
        ("Who is {{hero}}'s mentor?",
         ["{{mentor}}", "{{mentor}}", "{{mentor}}", "{{mentor}}"], 2),

        # Hunger Games
        ("What district is {{heroine}} from?",
         ["{{school}}", "{{school}}", "{{school}}", "{{school}}"], 3),

        # {{hero}}
        ("What is the name of the spell that produces light?",
         ["{{spell2}}", "{{spell1}}", "{{spell4}}", "{{spell3}}"], 1),

        # {{school}} series
        ("What school do students attend in {{school}} series?",
         ["{{school}}", "{{school}}", "{{school}}", "{{school}}"], 2),

        # {{hero}}
        ("What is the name of the camp for heroes?",
         ["{{school}}", "{{school}}", "{{school}}", "{{school}}"], 1),

        # Hunger Games
        ("What is {{heroine}}'s weapon of choice?",
         ["{{item}}", "{{item}}", "{{item}}", "{{item}}"], 2),
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
