# Module 1: Turtle Art with Loops

## What You'll Learn
- Using `for` loops to repeat actions
- Making the turtle draw shapes
- Creating cool patterns with code

## Lessons

### Lesson 1: Basic Shapes
Before we make art, let's practice drawing shapes with loops!

**Quick reminder - a for loop looks like this:**
```python
for i in range(4):
    print("This prints 4 times!")
```

The turtle understands commands like:
- `t.forward(100)` - move forward 100 pixels
- `t.right(90)` - turn right 90 degrees
- `t.left(45)` - turn left 45 degrees
- `t.penup()` - stop drawing
- `t.pendown()` - start drawing again
- `t.color("red")` - change the pen color

### Lesson 2: Variables Control Everything
You can use variables to change your drawings:
```python
size = 100
for i in range(4):
    t.forward(size)
    t.right(90)
```

Try changing `size` - what happens?

### Lesson 3: Nested Loops (Loops inside Loops!)
Want to draw a shape multiple times? Put a loop inside a loop!

---

## Exercises
Work through the exercises in order:
1. `exercise_1_square.py` - Draw a square
2. `exercise_2_triangle.py` - Draw a triangle
3. `exercise_3_star.py` - Draw a star (challenge!)
4. `exercise_4_creative.py` - Make your own art!

## Tips
- If your turtle window closes too fast, add `turtle.done()` at the end
- Made a mistake? Close the turtle window and run again
- Experiment! Change numbers and see what happens
- Ask Claude for hints if you're stuck (but try first!)
