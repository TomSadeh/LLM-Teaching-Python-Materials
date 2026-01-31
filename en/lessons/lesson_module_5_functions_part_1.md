# Lesson: Functions - Part 1: Why Functions?

> **Module**: module_5_functions
> **Part**: 1 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] All basic concepts: variables, types, operators
- [ ] Control flow: if/else, loops
- [ ] Lists and iteration
- [ ] Calling built-in functions like `print()`, `len()`, `input()`

---

## Learning Objective

By the end of this part, the student will be able to:

- Define a simple function using `def` with a descriptive name and call it

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Function | A named block of reusable code that performs a specific task |
| `def` keyword | The keyword used to define (create) a new function |
| Function call | Using the function name with parentheses to run the code inside |

---

## Lesson Content

### The Problem: Repetitive Code

Show code that repeats the same pattern multiple times:

```python
# Drawing three squares - lots of repetition!
import turtle
t = turtle.Turtle()

# Square 1
for i in range(4):
    t.forward(50)
    t.right(90)

t.penup()
t.forward(100)
t.pendown()

# Square 2
for i in range(4):
    t.forward(50)
    t.right(90)

t.penup()
t.forward(100)
t.pendown()

# Square 3
for i in range(4):
    t.forward(50)
    t.right(90)
```

Ask: "What happens if we want to change the square size? We'd have to change it in three places!"

### The Solution: A Reusable Recipe

Introduce the concept: "A function is like a recipe you can use multiple times"

```python
# Define the function - create the recipe
def draw_square():
    for i in range(4):
        t.forward(50)
        t.right(90)

# Call the function - use the recipe
draw_square()
t.penup()
t.forward(100)
t.pendown()
draw_square()
t.penup()
t.forward(100)
t.pendown()
draw_square()
```

### The Simplest Function

Start with the absolute simplest function - no parameters, no return:

```python
def say_hello():
    print("Hello!")
    print("Welcome to Python!")

# Nothing happens until we CALL it
say_hello()  # Now it runs!
say_hello()  # We can call it again!
```

Emphasize: `def` creates the function, but the code inside only runs when you call it.

### Watch For

- **Forgetting the parentheses**: `say_hello` vs `say_hello()` - the parentheses are required to call the function
- **Forgetting the colon**: `def say_hello():` needs the colon at the end
- **Indentation errors**: All code inside the function must be indented

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_shapes | Create simple turtle drawing functions with no parameters |

---

## Checkpoint

Ask: "What's the difference between defining a function and calling a function?"
Expected: Defining (with `def`) creates the function but doesn't run it. Calling (with parentheses) actually runs the code inside.

---

## If the Student Struggles

- **If confused about def vs call**: Use a recipe book analogy - writing a recipe in the book (def) vs actually cooking it (call)
- **If forgetting to call functions**: Add a checklist - "Did I define it? Did I call it?"
- **If indentation errors**: Show how all lines inside the function must be indented the same amount

---

## Real-World Connection

> "Every app is built from functions. When you tap 'post' on Instagram, a function runs. When you jump in a game, a jump function runs. Functions are how programmers organize complex behavior into manageable pieces."

---

## Notes for the LLM Teacher

- This is the foundation for one of the most important programming concepts
- Start with visual examples (turtle) to make the concept concrete
- Emphasize the "recipe" analogy - it makes the concept accessible
- Make sure students understand that `def` doesn't run the code - this is a common source of confusion
- Have students predict what will happen before running code
