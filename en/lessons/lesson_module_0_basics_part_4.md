# Lesson: Python Basics - Part 4: Getting User Input

> **Module**: module_0_basics
> **Part**: 4 of 5
> **Difficulty**: 1
> **Duration**: 4-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Get user input with `input()` and use it in a program

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `input()` | A function that waits for the user to type something and returns it as text |
| `int()` | Converts text to a number so you can do math with it |

---

## Lesson Content

### Building on Part 3

We can store values and do math. But what if we want the user to provide the values?

### New Material

The `input()` function asks the user for information:
```python
name = input("What is your name? ")
print("Hello, " + name)
```

Important: `input()` always returns text (a string), even if the user types a number!

To do math with input, convert it using `int()`:
```python
age_text = input("How old are you? ")
age = int(age_text)
next_year = age + 1
print(next_year)
```

Or do it in one line:
```python
age = int(input("How old are you? "))
```

### Watch For

- **Not storing input in a variable**: The input is lost if you don't save it
- **Trying to do math without int()**: `input() + 1` causes an error
- **Forgetting the space in the prompt**: `"What is your name?"` looks better than `"What is your name?"`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_04_input | Basic input() and string concatenation |
| exercise_05_calculator | Converting input to numbers with int() |

---

## Checkpoint

Ask: "Why do we need to use int() when adding numbers from input?"
Expected: Because input() gives us text/string, not a number

---

## If the Student Struggles

- **If confused about input()**: Break it into steps - first just show input without storing, then add the variable
- **If struggling with int()**: Explain that `"5"` is text and `5` is a number - `int()` converts text to number
