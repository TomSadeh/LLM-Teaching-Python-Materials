# Lesson: Turtle Graphics & Loops - Part 5: Adding Color and Style

> **Module**: module_1_turtle_loops
> **Part**: 5 of 5
> **Difficulty**: 1
> **Duration**: 4-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Change turtle properties (color, speed) and create more complex patterns with nested loops

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `color()` | Changes the color of the lines the turtle draws |
| `speed()` | Controls how fast the turtle moves (1=slow, 10=fast) |
| Nested loops | A loop inside another loop - for complex patterns |

---

## Lesson Content

### Building on Part 4

Now that we can draw shapes, let's make them colorful and more interesting!

### Changing Colors

```python
t.color("red")      # Now the turtle draws in red
t.forward(100)

t.color("blue")     # Switch to blue
t.forward(100)
```

Common colors: "red", "blue", "green", "yellow", "purple", "orange", "pink"

### Changing Speed

```python
t.speed(1)   # Slow - good for watching what happens
t.speed(5)   # Medium
t.speed(10)  # Fast
t.speed(0)   # Fastest (no animation)
```

### Colors in a Loop

We can use a list of colors and loop through them:

```python
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in colors:
    t.color(color)
    t.forward(100)
    t.right(60)
```

### Nested Loops for Complex Patterns

Want to draw multiple squares? Put a loop inside a loop:

```python
for i in range(6):           # Do this 6 times
    for j in range(4):       # Draw a square
        t.forward(100)
        t.right(90)
    t.right(60)              # Turn before the next square
```

This draws 6 squares, each rotated 60 degrees!

### Watch For

- Color names must be in quotes ("red" not red)
- Forgetting which loop level they're in with nested loops
- Indentation becomes critical with nested loops

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_7_rainbow | Colors in loops - combining loops with color changes |
| exercise_8_nested_squares | Nested loops - multiple squares in a pattern |
| exercise_9_flower | Multiple shapes combined - integration exercise |

---

## Checkpoint

Ask: "Why is using a loop better than writing forward/right many times?"
Expected: Less code, easier to change, fewer mistakes

---

## If the Student Struggles

- **If confused about nested loops**: Draw it step by step - first show ONE square, then show how we repeat that
- **If colors aren't working**: Check for spelling and quotes
- **If patterns look wrong**: Slow down the turtle with `t.speed(1)` to see what's happening
