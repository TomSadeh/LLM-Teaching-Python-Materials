# Exercise 2: O.W.L. Exam Grading (Harry Potter Style!)


def get_owl_grade(score):
    # ✏️ YOUR CODE HERE ✏️
    # Return the O.W.L. grade based on score!
    # (These are the Hogwarts exam grades)
    #
    # 95 and above = "O" (Outstanding)
    # 85-94 = "E" (Exceeds Expectations)
    # 70-84 = "A" (Acceptable)
    # 55-69 = "P" (Poor)
    # 40-54 = "D" (Dreadful)
    # Below 40 = "T" (Troll)
    #
    # Use if/elif/else!
    pass


def main():
    print("🦉 O.W.L. EXAMINATION RESULTS 🦉")
    print("=" * 35)
    score = int(input("Enter your exam score: "))
    grade = get_owl_grade(score)
    print("Your O.W.L. grade is:", grade)

    # Bonus: Can you add what each grade means?
    # Example: if grade == "O": print("Outstanding! Hermione would be proud!")


main()
