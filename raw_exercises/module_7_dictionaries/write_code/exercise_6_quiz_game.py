# Exercise 6: Build a Quiz Game with Dictionaries!


def simple_quiz():
    # ✏️ YOUR CODE HERE ✏️
    # Create a list of question dictionaries. Each question has:
    # - "question": the question text
    # - "answer": the correct answer
    #
    # Example structure:
    # questions = [
    #     {"question": "What house is {{hero}} in?", "answer": "{{house}}"},
    #     {"question": "What spell creates light?", "answer": "{{spell1}}"},
    #     {"question": "Who is {{hero}}'s friend?", "answer": "{{friend}}"}
    # ]
    #
    # Loop through each question:
    # 1. Print the question
    # 2. Get user's answer with input()
    # 3. Check if it matches (use .lower() on both!)
    # 4. Keep track of score
    # 5. Print final score at the end
    pass


def advanced_quiz():
    # ✏️ YOUR CODE HERE ✏️
    # Create questions with multiple choice!
    # Each question has:
    # - "question": the question text
    # - "options": a list of choices ["A. ...", "B. ...", "C. ..."]
    # - "answer": the correct letter ("A", "B", or "C")
    #
    # Example:
    # {
    #     "question": "Where does {{hero}} go to school?",
    #     "options": ["A. {{school}}", "B. Regular School", "C. {{place}}"],
    #     "answer": "A"
    # }
    #
    # Print each question with its options, get answer, check, track score!
    pass


def timed_challenge():
    # ✏️ BONUS CHALLENGE ✏️
    # Same as above, but import the 'time' module
    # Track how long it takes to complete the quiz!
    # Hint:
    # import time
    # start = time.time()
    # ... quiz code ...
    # end = time.time()
    # print(f"Time: {end - start:.1f} seconds")
    pass


def main():
    print("=" * 40)
    print("   WELCOME TO THE TRIVIA CHALLENGE!")
    print("=" * 40)
    print()

    print("--- Simple Quiz ---")
    simple_quiz()

    print("\n--- Multiple Choice Quiz ---")
    advanced_quiz()

    # Uncomment to try the bonus:
    # print("\n--- Timed Challenge ---")
    # timed_challenge()


main()
