# Lesson: Turtle Graphics & Loops - Part 4: Different Shapes

> **Module**: module_1_turtle_loops
> **Part**: 4 of 5
> **Difficulty**: 1
> **Duration**: 4-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Apply the angle formula (360 / sides) to draw different shapes (triangle, hexagon, etc.)

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Angle formula | Turn angle = 360 / number of sides |
| Regular polygon | A shape where all sides and angles are equal |

---

## Lesson Content

### Building on Part 3

We used 90 degrees for a square because it has 4 sides. But what about other shapes?

### New Material: The Angle Formula

There's a pattern! The turn angle depends on how many sides the shape has:

**Turn angle = 360 / number of sides**

| Shape | Sides | Turn Angle |
|-------|-------|------------|
| Triangle | 3 | 360/3 = 120 degrees |
| Square | 4 | 360/4 = 90 degrees |
| Pentagon | 5 | 360/5 = 72 degrees |
| Hexagon | 6 | 360/6 = 60 degrees |

### Drawing a Triangle

```python
for i in range(3):
    t.forward(100)
    t.right(120)  # 360 / 3 = 120
```

### Drawing a Hexagon

```python
for i in range(6):
    t.forward(50)
    t.right(60)  # 360 / 6 = 60
```

### Why Does This Work?

When the turtle draws a shape and returns to the start, it has turned a full circle (360 degrees). If it makes 4 turns, each turn is 360/4 = 90 degrees.

### Drawing a Circle (Many-Sided Polygon)

A circle is just a polygon with MANY small sides:

```python
for i in range(36):
    t.forward(10)
    t.right(10)  # 360 / 36 = 10
```

### Watch For

- Using 90 degrees for all shapes (common mistake)
- Forgetting to change both the range AND the angle
- Getting the formula backwards

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_2_triangle | 3 sides, 120-degree turns |
| exercise_3_star | 5-point star uses 144 degrees (different formula) |
| exercise_5_hexagon | 6 sides, 60-degree turns - reinforces the formula |
| exercise_6_circle | Many small steps - circle as a polygon |

---

## Checkpoint

Ask: "What angle do you need for a pentagon (5 sides)?"
Expected: 72 degrees (360 / 5)

---

## If the Student Struggles

- **If struggling with angles**: Use a physical demonstration - stand up and turn, showing that a full spin is 360 degrees
- **If applying the pattern incorrectly**: Go back to the square (which they know works) and verify 360/4 = 90
