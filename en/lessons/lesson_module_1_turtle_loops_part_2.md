# Lesson: Turtle Graphics & Loops - Part 2: Manual Square

> **Module**: module_1_turtle_loops
> **Part**: 2 of 5
> **Difficulty**: 1
> **Duration**: 4-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Draw a square by manually writing forward and right commands four times

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Sequence | Steps that happen one after another in order |
| Repetition | Doing the same action multiple times |

---

## Lesson Content

### Building on Part 1

Now that we know how to move forward and turn, let's draw a complete shape - a square!

### New Material

A square has 4 sides, and each corner is a 90-degree turn. Here's how to draw one:

```python
import turtle

t = turtle.Turtle()

# Side 1
t.forward(100)
t.right(90)

# Side 2
t.forward(100)
t.right(90)

# Side 3
t.forward(100)
t.right(90)

# Side 4
t.forward(100)
t.right(90)

turtle.done()
```

Notice anything? We wrote the same two lines FOUR times! That's a lot of repetition.

### The Problem with Manual Repetition

- It takes a long time to write
- It's easy to make mistakes (typos, forgetting a line)
- If we want to change the size, we have to change it in 4 places
- What if we wanted a shape with 100 sides? We'd need 200 lines!

This is intentionally tedious - and it's exactly why programmers invented loops!

### Watch For

- Wrong angle (using something other than 90 degrees)
- Forgetting a forward or right command
- Getting frustrated with the repetition (good! this motivates Part 3)

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_square | Have student write out all 4 sides manually before Part 3 |

---

## Checkpoint

Ask: "How many times did we write `t.forward(100)` and `t.right(90)`?"
Expected: 4 times each

---

## If the Student Struggles

- **If they skip steps**: Count the sides of a square together - 1, 2, 3, 4
- **If wrong angle**: Remind them that a square corner is like the corner of a book or window - 90 degrees
