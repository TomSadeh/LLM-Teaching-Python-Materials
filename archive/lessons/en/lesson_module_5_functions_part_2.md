# Lesson: Functions - Part 2: Adding Parameters

> **Module**: module_5_functions
> **Part**: 2 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Add parameters to functions to make them flexible and reusable with different values

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Parameter | A variable in the function definition that acts as a placeholder for a value |
| Argument | The actual value passed to a function when calling it |

---

## Lesson Content

### Building on Part 1

In Part 1, we created simple functions that always do the exact same thing. But what if we want a function that can do slightly different things depending on what we give it?

### Making Functions Flexible

```python
# This function always says "Hello!" - not very flexible
def say_hello():
    print("Hello!")

# What if we want to greet different people?
```

### Introducing Parameters

Parameters let the function receive input:

```python
def greet(name):
    print(f"Hello, {name}!")

# Now we can greet anyone!
greet("{{hero}}")      # Hello, {{hero}}!
greet("{{heroine}}")   # Hello, {{heroine}}!
greet("{{friend}}")    # Hello, {{friend}}!
```

Explain the terminology:
- `name` in `def greet(name):` is a **parameter** (the placeholder)
- `"{{hero}}"` in `greet("{{hero}}")` is an **argument** (the actual value)

### Multiple Parameters

Functions can accept multiple pieces of information:

```python
def greet_with_title(title, name):
    print(f"Hello, {title} {name}!")

greet_with_title("Professor", "{{mentor}}")  # Hello, Professor {{mentor}}!
greet_with_title("Dr.", "{{villain}}")       # Hello, Dr. {{villain}}!
```

Order matters! Arguments are matched to parameters by position.

### Practical Example: Flexible Drawing

```python
def draw_square(size):
    for i in range(4):
        t.forward(size)  # Use the parameter!
        t.right(90)

# Now we can draw different sized squares
draw_square(50)   # Small square
draw_square(100)  # Medium square
draw_square(200)  # Large square
```

### Watch For

- **Positional confusion**: With multiple parameters, getting the order wrong
- **Missing arguments**: Calling `greet()` without providing a name
- **Confusion between parameter and argument**: Remember - parameter in definition, argument in call

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_2_greetings | Create functions with parameters for personalized output |

---

## Checkpoint

Ask: "What's the difference between a parameter and an argument?"
Expected: Parameter is in the function definition (it's a placeholder), argument is the actual value passed when calling the function.

---

## If the Student Struggles

- **If confused about parameters**: Use a cooking recipe analogy - the recipe says "flour" (parameter) but you provide the actual ingredient when cooking (argument)
- **If mixing up order**: Practice with simple two-parameter functions, have them trace which argument goes to which parameter
- **If forgetting to pass arguments**: Show the error message Python gives and explain what it means
