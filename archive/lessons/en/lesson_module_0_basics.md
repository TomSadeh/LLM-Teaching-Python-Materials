# Lesson: Python Basics

> **Module**: module_0_basics
> **Difficulty**: 1
> **Duration**: 15-20 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] None - this is the first module!

---

## Learning Objectives

By the end of this lesson, the student will be able to:

1. Use `print()` to display text on the screen
2. Create variables to store text and numbers
3. Perform basic math operations (+, -, *, /)
4. Get user input with `input()` and use it in a program
5. Combine variables and text using f-strings or concatenation

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `print()` | A function that displays text/values on the screen |
| Variable | A named container that stores a value (like a labeled box) |
| String | Text data, written in quotes ("hello") |
| Integer | A whole number without decimals (42) |
| `input()` | A function that waits for the user to type something and returns it as text |

---

## Common Misconceptions

1. **Forgetting quotes around strings**: Students write `print(hello)` instead of `print("hello")`
   **Reality**: Without quotes, Python thinks `hello` is a variable name

2. **Thinking `input()` returns numbers**: Students try `age = input() + 1`
   **Reality**: `input()` always returns a string; use `int()` to convert

3. **Confusing `=` and `==`**: Students use `=` to compare values
   **Reality**: `=` assigns values, `==` compares them (taught later, but good to mention)

4. **Variable name case sensitivity**: Using `Name` and `name` as if they're the same
   **Reality**: Python treats them as completely different variables

---

## Teaching Sequence

### Phase 1: print() - Output to the screen
- Show the simplest form: `print("Hello")`
- Explain that `print()` is a function and quotes define text
- Let them run it immediately - instant success
- Watch for: forgetting quotes, using wrong quote types

### Phase 2: Variables - Storing values
- Introduce the "labeled box" analogy
- Show: `name = "Maya"` then `print(name)`
- Emphasize: no quotes when using a variable
- Watch for: quotes around variable names, typos in variable names

### Phase 3: Math operations
- Show basic math: `2 + 3`, `10 - 4`, `3 * 5`, `10 / 2`
- Combine with variables: `age = 12` then `next_year = age + 1`
- Watch for: trying to do math on strings

### Phase 4: input() - Getting user input
- Show: `name = input("What is your name? ")`
- Combine with print: `print("Hello, " + name)`
- Watch for: not storing input in a variable

### Phase 5: Combining it all
- Build a simple interactive program
- Use variables, input, and print together
- Introduce f-strings as a cleaner way to combine text and variables

---

## Exercises Mapping

| Exercise | Concepts covered | Notes |
|----------|------------------|-------|
| exercise_01_hello | print() basics | Start here - immediate success |
| exercise_02_variables | Variables, strings | Introduces storing values |
| exercise_03_math | Math operations, integers | Numeric calculations |
| exercise_04_input | input(), string concatenation | User interaction |
| exercise_05_calculator | input(), int(), math | Converting input to numbers |
| exercise_06_madlib | Multiple inputs, f-strings | Fun combination exercise |
| exercise_07_counting | Loops (preview) | Optional stretch |
| exercise_08_patterns | Multiple print statements | Pattern recognition |
| exercise_09_sum | input(), int(), addition | Practical math |

---

## Checkpoints

### After Phase 1 (print)
Ask: "What happens if you write print(hello) without quotes?"
Expected: Python looks for a variable named hello and gives an error

### After Phase 2 (variables)
Ask: "If I write name = 'Maya', what does print(name) show?"
Expected: Maya (without quotes)

### After Phase 4 (input)
Ask: "Why do we need to use int() when adding numbers from input?"
Expected: Because input() gives us text/string, not a number

### End of Lesson
Ask: "How would you ask someone for their age and then print it?"
Expected: Something like `age = input("How old are you?")` then `print(age)`

---

## If the Student Struggles

- **If struggling with quotes**: Show the difference between `"Maya"` (text) and `Maya` (variable) side by side
- **If struggling with variables**: Use physical props analogy - sticky notes on boxes
- **If struggling with input()**: Break it into steps - first just show input without storing, then add the variable
- **If struggling with math on strings**: Show the error message and explain what "cannot concatenate" means

---

## Extension Ideas

For students who finish early or want more challenge:

- Create a "character profile" that asks for name, age, and favorite thing, then displays it nicely formatted
- Try making a simple "fortune teller" that gives different responses based on input

---

## Real-World Connection

> "Every app you use - Instagram, Minecraft, YouTube - uses these same concepts: storing information in variables, getting input from users, and showing output on the screen."

---

## Notes for the LLM Teacher

- This is the first lesson - establish that making mistakes is normal and encouraged
- Run code after every small change to build the "experiment and see" habit
- If using themed examples, this is a good place to introduce them casually
- Keep the warm-up trivial - just `print("Hi")` is enough to start with success
