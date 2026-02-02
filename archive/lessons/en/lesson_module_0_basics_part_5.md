# Lesson: Python Basics - Part 5: Putting It All Together

> **Module**: module_0_basics
> **Part**: 5 of 5
> **Difficulty**: 1
> **Duration**: 5-7 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Combine variables and text using f-strings or concatenation

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| f-string | A string starting with `f` that can include variables inside `{}` |
| Concatenation | Joining strings together with `+` |

---

## Lesson Content

### Building on Part 4

We can get input and do math. Now let's combine everything into complete programs!

### New Material

**Method 1: Concatenation (joining with +)**
```python
name = "Maya"
print("Hello, " + name + "!")
```

**Method 2: f-strings (recommended)**
```python
name = "Maya"
age = 12
print(f"Hello, {name}! You are {age} years old.")
```

f-strings are cleaner - just put an `f` before the quotes and use `{}` around variables.

**Complete example:**
```python
name = input("What is your name? ")
age = int(input("How old are you? "))
next_year = age + 1

print(f"Hello, {name}!")
print(f"Next year you will be {next_year}.")
```

### Watch For

- **Forgetting the `f`**: `"{name}"` doesn't work without the `f` prefix
- **Missing curly braces**: `f"Hello, name"` prints "name" literally
- **Mixing concatenation types**: Can't do `"Hi " + 5` (need `str(5)` or use f-string)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_06_madlib | Fun combination of multiple inputs and f-strings |
| exercise_08_patterns | Multiple print statements for output patterns |
| exercise_09_sum | Practical application: input, int(), and math |

---

## Checkpoint

Ask: "How would you ask someone for their age and then print it?"
Expected: Something like `age = input("How old are you? ")` then `print(age)` or `print(f"You are {age}")`

---

## If the Student Struggles

- **If f-strings are confusing**: Start with concatenation, then show f-strings as a "shortcut"
- **If forgetting the f**: Practice saying "f-string" and always typing `f"` together

---

## Extension Ideas

For students who finish early or want more challenge:

- Create a "character profile" that asks for name, age, and favorite thing, then displays it nicely formatted
- Try making a simple "fortune teller" that gives different responses based on input

---

## Notes for the LLM Teacher

- If using themed examples, this is a good place to introduce them casually
- Encourage experimentation - try changing the prompts and outputs
- This completes the basics module - celebrate the accomplishment!
