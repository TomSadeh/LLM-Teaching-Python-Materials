# Lesson: Decisions (if/elif/else) - Part 4: Combining Conditions

> **Module**: module_2_decisions
> **Part**: 4 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Combine conditions with `and`, `or`, and `not`

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `and` | Both conditions must be True for the whole thing to be True |
| `or` | At least one condition must be True for the whole thing to be True |
| `not` | Flips True to False and False to True |

---

## Lesson Content

### Building on Part 3
- Sometimes a single condition isn't enough
- What if we need to check multiple things at once?

### New Material

#### Using `and` - Both Must Be True
```python
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 13 and has_ticket == "yes":
    print("Welcome to the movie!")
else:
    print("Sorry, you can't enter.")
```

#### Using `or` - At Least One Must Be True
```python
day = input("What day is it? ")

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")
```

#### Using `not` - Flip the Condition
```python
is_raining = False

if not is_raining:
    print("Let's go outside!")
```

### Combining Multiple Operators
```python
# Check if age is between 13 and 19 (teenager)
age = int(input("Enter age: "))
if age >= 13 and age <= 19:
    print("You're a teenager!")

# Python also allows this cleaner syntax:
if 13 <= age <= 19:
    print("You're a teenager!")
```

### Watch For
- **Forgetting that `and` requires BOTH to be True**: If either is False, the whole thing is False
- **Using English words instead of Python keywords**: Must use lowercase `and`, `or`, `not`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_5_age_checker | Practice combining conditions for age ranges |
| exercise_9_validation | Use multiple conditions for input validation |

---

## Checkpoint

Ask: "How would you check if a number is between 10 and 20?"
Expected: `if number >= 10 and number <= 20:` or `if 10 <= number <= 20:`

---

## If the Student Struggles

- **If struggling with and/or**: Use truth tables with simple examples
- **If confused about when to use and vs or**: "and" = both must be true (stricter), "or" = either can be true (looser)
