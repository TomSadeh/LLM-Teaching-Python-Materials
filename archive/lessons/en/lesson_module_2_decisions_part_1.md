# Lesson: Decisions (if/elif/else) - Part 1: Simple if Statement

> **Module**: module_2_decisions
> **Part**: 1 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Variables and basic data types (strings, integers)
- [ ] Using `input()` to get user data
- [ ] Basic comparison concepts (bigger, smaller, equal)

---

## Learning Objective

By the end of this part, the student will be able to:

- Write `if` statements to execute code conditionally

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `if` | Runs the indented code only when the condition is True |
| Comparison operators | `==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=` |
| Boolean | A value that's either `True` or `False` |

---

## Lesson Content

### Getting Started
- Start with the simplest case: `if condition:`
- Use a concrete example: checking if a password matches
- Show what happens when condition is True vs False

```python
password = input("Enter password: ")
if password == "{{password}}":
    print("Access granted!")
```

### The Structure of an if Statement
1. The keyword `if`
2. A condition (something that's True or False)
3. A colon `:`
4. Indented code that runs only when condition is True

### Watch For
- **Missing colon**: `if x == 5` without the `:` causes an error
- **No indentation**: Python uses indentation to know what's "inside" the if
- **Using `=` instead of `==`**: `=` assigns values, `==` compares them

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_password | Classic "access granted" - practice writing a simple if statement |

---

## Checkpoint

Ask: "What's the difference between `=` and `==`?"
Expected: `=` puts a value in a variable, `==` checks if two things are equal

---

## If the Student Struggles

- **If struggling with the concept**: Use real-world analogies - "if it's raining, take an umbrella"
- **If getting syntax errors**: Check for the colon and proper indentation
- **If nothing happens**: The condition might be False - add a print before the if to see the value

---

## Real-World Connection

> "Every app makes decisions constantly - websites check if your password is correct before letting you in."

---

## Notes for the LLM Teacher

- The `= vs ==` confusion is very common - address it explicitly
- Use interactive examples where students predict the output before running
- Make sure they understand that the indented code only runs when the condition is True
