"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part project where you'll build an interactive quiz game.
You'll create question banks, implement scoring, and add replay functionality.

{{CONTEXT_LEARNING_OBJECTIVE}}
"""

import random


# ============================================================
# PART 1: Question Data Structure
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
#
# A quiz needs questions! You'll design a data structure to store
# questions and their answers. Each question will be a list containing:
# [question_text, correct_answer, list_of_wrong_answers]


def create_question(question_text, correct_answer, wrong_answers):
    """
    Create a question data structure.

    Args:
        question_text: The question string
        correct_answer: The correct answer string
        wrong_answers: A list of 2-3 wrong answer strings

    Returns:
        A list: [question_text, correct_answer, wrong_answers]
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def create_quiz_questions():
    """
    Create a list of quiz questions about {{school}}.

    Returns:
        A list containing at least 5 questions.
        Each question is in the format from create_question().

    Hint: Create questions about {{hero}}, {{creature}}, {{location}}, etc.
    Make sure to have a mix of topics!
    """
    # ✏️ YOUR CODE HERE ✏️
    # Example structure (replace with themed content):
    # questions = [
    #     create_question(
    #         "What is {{hero}}'s special ability?",
    #         "{{spell1}}",
    #         ["{{spell2}}", "{{spell3}}", "running fast"]
    #     ),
    #     # Add more questions...
    # ]
    pass


# ============================================================
# PART 2: Question Display and Answer Checking
# ============================================================
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now create functions to display questions and check answers.


def get_shuffled_answers(question):
    """
    Get all answers for a question in random order.

    Args:
        question: A question list [text, correct, wrong_list]

    Returns:
        A new list with all answers (correct + wrong) shuffled randomly.

    Hint: Combine correct answer with wrong answers, then shuffle.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_question(question, question_number):
    """
    Display a question with numbered answer choices.

    Args:
        question: A question list [text, correct, wrong_list]
        question_number: The question number to display

    Returns:
        A list of the shuffled answers (so we know which is correct)

    Prints:
        Question N: [question text]
        1. [answer option]
        2. [answer option]
        3. [answer option]
        4. [answer option]
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def check_answer(question, user_choice, displayed_answers):
    """
    Check if the user's answer is correct.

    Args:
        question: The question list [text, correct, wrong_list]
        user_choice: The number the user chose (1-4)
        displayed_answers: The list of answers as displayed

    Returns:
        True if correct, False otherwise.

    Prints:
        "Correct! {{exclamation}}" if right
        "Wrong! The answer was: [correct answer]" if wrong
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 3: Scoring and Feedback
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
#
# A good quiz tracks score and gives feedback!


def calculate_percentage(correct, total):
    """
    Calculate the percentage score.

    Args:
        correct: Number of correct answers
        total: Total number of questions

    Returns:
        The percentage as an integer (0-100).
        Return 0 if total is 0.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_grade_message(percentage):
    """
    Get a themed message based on the score.

    Args:
        percentage: Score percentage (0-100)

    Returns:
        A string message based on performance:
        90-100: "Outstanding! {{mentor}} would be proud!"
        70-89: "Good work! Keep practicing at {{school}}!"
        50-69: "Not bad, but more study is needed."
        0-49: "{{villain}} wins this round. Try again!"
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def display_results(correct, total):
    """
    Display the final quiz results.

    Args:
        correct: Number of correct answers
        total: Total number of questions

    Prints:
        === Quiz Complete! ===
        Score: X / Y
        Percentage: Z%
        [Grade message]
        ====================
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# PART 4: Game Loop with Replay
# ============================================================
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Put it all together with a game loop that:
# - Shuffles questions each game
# - Tracks score
# - Offers replay


def get_valid_answer_choice():
    """
    Get a valid answer choice (1-4) from the user.

    Returns:
        An integer 1, 2, 3, or 4.

    Note:
        Keep asking until valid input is received.
        Use .isdigit() to validate.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def play_quiz(questions):
    """
    Play one round of the quiz.

    Args:
        questions: List of question data structures

    Returns:
        A tuple: (correct_count, total_questions)

    This function:
    1. Shuffles the questions
    2. Asks each question
    3. Checks answers and tracks score
    4. Returns the final score
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def ask_play_again():
    """
    Ask if the user wants to play again.

    Returns:
        True if yes, False if no.

    Note:
        Accept 'yes', 'y', 'no', 'n' (case insensitive).
        Keep asking until valid input.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def run_quiz_game():
    """
    Run the complete quiz game with replay option.

    This function:
    1. Welcomes the player to {{school}} Quiz
    2. Creates the questions
    3. Plays rounds until the player quits
    4. Says goodbye
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)
    print()
    print("Complete each part to build the quiz game.")
    print()

    # Uncomment to test individual parts:
    # Part 1 test
    # questions = create_quiz_questions()
    # print(f"Created {len(questions)} questions")

    # Part 2 test
    # questions = create_quiz_questions()
    # if questions:
    #     answers = display_question(questions[0], 1)
    #     print(f"Answers: {answers}")

    # Part 3 test
    # display_results(3, 5)

    # Part 4 - run the full game
    # run_quiz_game()

    print()
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()
