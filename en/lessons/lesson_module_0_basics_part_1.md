# Lesson: Python Basics - Part 1: Hello World with print()

> **Module**: module_0_basics
> **Part**: 1 of 5
> **Difficulty**: 1
> **Duration**: 3-5 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] None - this is the first module!

---

## Learning Objective

By the end of this part, the student will be able to:

- Use `print()` to display text on the screen

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `print()` | A function that displays text/values on the screen |
| String | Text data, written in quotes ("hello") |

---

## Lesson Content

### Getting Started

Show the simplest form: `print("Hello")`

Explain that `print()` is a function - a command that does something. The text inside the quotes is what gets displayed.

```python
print("Hello!")
print("Welcome to Python!")
```

Let the student run it immediately - instant success is key for the first lesson.

### Key Points

- `print()` is a function - notice the parentheses
- Text must be in quotes (either `"double"` or `'single'`)
- Without quotes, Python thinks you're referring to a variable

### Watch For

- **Forgetting quotes**: `print(hello)` instead of `print("hello")`
- **Using wrong quote types**: mixing `"` and `'` incorrectly
- **Missing parentheses**: `print "Hello"` instead of `print("Hello")`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_01_hello | Start here - immediate success with print() |

---

## Checkpoint

Ask: "What happens if you write print(hello) without quotes?"
Expected: Python looks for a variable named hello and gives an error

---

## If the Student Struggles

- **If forgetting quotes**: Show the error message and explain that quotes tell Python "this is text, not a variable name"
- **If confused about parentheses**: Explain that parentheses are how we "call" or "use" a function

---

## Real-World Connection

> "Every app you use - Instagram, Minecraft, YouTube - uses print-like functions to display text on your screen."

---

## Notes for the LLM Teacher

- This is the first lesson - establish that making mistakes is normal and encouraged
- Run code after every small change to build the "experiment and see" habit
- Keep it trivial - just `print("Hi")` is enough to start with success
