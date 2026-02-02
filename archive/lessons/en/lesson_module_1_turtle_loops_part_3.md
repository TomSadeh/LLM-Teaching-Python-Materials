# Lesson: Turtle Graphics & Loops - Part 3: Introducing the For Loop

> **Module**: module_1_turtle_loops
> **Part**: 3 of 5
> **Difficulty**: 1
> **Duration**: 4-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use a `for` loop with `range()` to repeat turtle commands

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `for` loop | Repeats a block of code a specific number of times |
| `range(n)` | Creates a sequence from 0 to n-1 (so `range(4)` gives 0,1,2,3) |
| Indentation | The spaces before code that show what's "inside" a loop |

---

## Lesson Content

### Building on Part 2

Remember how tedious it was to write the same code 4 times? There's a better way!

### New Material

A `for` loop lets us say "do this 4 times" in just a few lines:

```python
import turtle

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

That's it! The same square, but with much less code.

### How It Works

- `for i in range(4):` means "do the following 4 times"
- The colon `:` at the end is required - it tells Python a loop is starting
- The indented lines (with spaces at the start) are "inside" the loop
- `range(4)` counts 0, 1, 2, 3 - that's 4 numbers

### The Magic of Loops

Now if we want to change the size, we only change ONE number:

```python
for i in range(4):
    t.forward(200)  # Changed from 100 to 200 - just one place!
    t.right(90)
```

### Watch For

- Missing colon after `range(4)`
- No indentation (the forward and right lines must be indented)
- Wrong range number (off by one)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_square | Now have them rewrite using a for loop |
| exercise_2_triangle | Apply the loop concept to a new shape |

---

## Checkpoint

Ask: "How many times does `for i in range(3):` repeat?"
Expected: 3 times

---

## If the Student Struggles

- **If struggling with range()**: Count on fingers: range(4) = 0,1,2,3 = four numbers
- **If struggling with indentation**: Show the error message and explain Python needs to know what's "inside" the loop
- **If confused about what i is**: Explain it's just a counter that keeps track of which repetition we're on (we can ignore it for now)
