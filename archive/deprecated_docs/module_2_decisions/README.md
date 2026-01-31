# Module 2: Making Decisions (if/else)

## What You'll Learn
- Making your program choose what to do
- Comparing values (equal, bigger, smaller)
- Using `if`, `elif`, and `else`
- Creating interactive programs

## Lessons

### Lesson 1: The if Statement
Programs can make decisions! An `if` statement checks if something is true:

```python
age = 12
if age >= 10:
    print("You can ride the roller coaster!")
```

### Lesson 2: Comparison Operators
Use these to compare values:
- `==` equals (two equals signs!)
- `!=` not equals
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

### Lesson 3: if/else
What if the condition is false? Use `else`:

```python
password = input("Enter password: ")
if password == "secret123":
    print("Welcome!")
else:
    print("Wrong password!")
```

### Lesson 4: elif (else if)
For multiple choices, use `elif`:

```python
grade = 85
if grade >= 90:
    print("A - Excellent!")
elif grade >= 80:
    print("B - Great job!")
elif grade >= 70:
    print("C - Good")
else:
    print("Keep studying!")
```

---

## Exercises
1. `exercise_1_password.py` - Simple password checker
2. `exercise_2_grades.py` - Grade calculator with elif
3. `exercise_3_number_game.py` - Guess if number is big/small
4. `exercise_4_quiz.py` - Create your own quiz!

## Tips
- Remember: `=` assigns a value, `==` compares values
- Indentation matters! Code inside `if` must be indented
- You can combine conditions with `and` / `or`
