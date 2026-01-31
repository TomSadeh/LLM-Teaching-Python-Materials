# Module 5: Functions - Your Own Commands

## What You'll Learn
- Why functions make code better
- Parameters: giving information to functions
- Return values: getting information back
- Default values for parameters
- Building reusable code

## Lessons

### Lesson 1: Why Functions?
Without functions, you repeat yourself:

```python
# Drawing 3 squares - lots of repeated code!
for i in range(4):
    t.forward(50)
    t.right(90)

t.penup()
t.forward(100)
t.pendown()

for i in range(4):
    t.forward(50)
    t.right(90)

# ... and again and again!
```

With functions - write once, use many times!

### Lesson 2: Functions with Parameters
Parameters let you customize what the function does:

```python
def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)

# Now we can draw different sized squares!
draw_square(t, 50)   # small
draw_square(t, 100)  # big
draw_square(t, 200)  # huge!
```

### Lesson 3: Return Values
Functions can give back a result:

```python
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print(total)  # 8
```

**return** sends a value back. **print** just shows it on screen.

### Lesson 4: Default Parameters
Give parameters a default value:

```python
def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

greet("Maya")              # Hello, Maya!
greet("Maya", "Hi there")  # Hi there, Maya!
```

### Lesson 5: Multiple Returns
Return different things based on conditions:

```python
def check_age(age):
    if age >= 18:
        return "adult"
    elif age >= 13:
        return "teenager"
    else:
        return "child"
```

---

## Exercises
1. `exercise_1_shapes.py` - Create shape-drawing functions
2. `exercise_2_calculator.py` - Build a calculator with functions
3. `exercise_3_helper_functions.py` - Useful functions you can reuse
4. `exercise_4_turtle_art.py` - Turtle art with custom functions!

## Tips
- If you write the same code twice, make it a function!
- Give functions clear names that describe what they do
- Keep functions short - one job per function
