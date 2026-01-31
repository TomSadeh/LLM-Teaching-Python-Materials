# Lesson: Turtle Graphics & Loops - Part 1: Meet the Turtle

> **Module**: module_1_turtle_loops
> **Part**: 1 of 5
> **Difficulty**: 1
> **Duration**: 4-6 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Using `print()` to display output
- [ ] Creating and using variables
- [ ] Basic understanding of functions (calling them with parentheses)

---

## Learning Objective

By the end of this part, the student will be able to:

- Create a turtle and move it on the screen using `forward()` and `right()`

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Turtle | An on-screen "pen" you can program to draw by moving |
| `forward(n)` | Moves the turtle forward n pixels, drawing a line |
| `right(n)` | Turns the turtle clockwise by n degrees (doesn't move) |

---

## Lesson Content

### Getting Started

The turtle is like a little robot with a pen. When it moves, it draws a line. We can tell it to go forward, turn left, or turn right.

First, we need to import the turtle module and create our turtle:

```python
import turtle

t = turtle.Turtle()
```

### Basic Movement

Now we can give commands to our turtle:

```python
t.forward(100)  # Move forward 100 pixels, drawing a line
t.right(90)     # Turn right 90 degrees (but don't move)
t.forward(100)  # Move forward again
```

The turtle starts facing up. After `right(90)`, it faces right (east).

### Watch For

- Running code without `turtle.done()` at the end (window closes immediately)
- Confusion about which way is left vs right
- Expecting the turtle to move when turning

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_square (first steps only) | Have student draw just one line and one turn |

---

## Checkpoint

Ask: "If the turtle is facing up and you do right(90), which way is it facing now?"
Expected: Right (east)

---

## If the Student Struggles

- **If confused about direction**: Stand up and demonstrate - face "up" (forward), then turn right 90 degrees
- **If code runs but nothing appears**: They likely forgot `turtle.done()` at the end

---

## Real-World Connection

> "Game characters move the same way - they have a position and a direction they're facing. When you press the arrow keys in a game, you're giving commands just like we give to the turtle!"

---

## Notes for the LLM Teacher

- Turtle graphics provides immediate visual feedback - use this to keep engagement high
- Let students experiment with different values for forward() to see what happens
- Keep this phase short - the goal is just to understand basic movement before introducing repetition
