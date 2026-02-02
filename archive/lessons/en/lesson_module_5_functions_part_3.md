# Lesson: Functions - Part 3: The Return Statement

> **Module**: module_5_functions
> **Part**: 3 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use `return` to send values back from a function and capture them in variables

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `return` | Sends a value back from the function to where it was called |
| Return value | The value that a function gives back when it finishes |

---

## Lesson Content

### Building on Part 2

We've learned to send information INTO a function using parameters. Now we'll learn to get information BACK from a function using `return`.

### The Need for Return Values

Sometimes we want a function to calculate something and give us the result:

```python
# This function calculates, but we can't use the result!
def add_numbers(a, b):
    result = a + b
    print(result)  # Just shows it, can't use it elsewhere

add_numbers(5, 3)  # Prints 8, but we can't do anything with it
```

### Introducing Return

```python
def add_numbers(a, b):
    result = a + b
    return result  # Send the result back!

# Now we can capture and use the result
total = add_numbers(5, 3)
print(f"The total is {total}")  # The total is 8
print(total * 2)                # 16 - we can use it!
```

### Practical Example: Temperature Conversion

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Use the returned value
temp_f = celsius_to_fahrenheit(25)
print(f"25C is {temp_f}F")  # 25C is 77.0F

# We can use it in conditions too
if celsius_to_fahrenheit(30) > 80:
    print("It's hot!")
```

### What Happens Without Return?

```python
def no_return_example():
    x = 5 + 3
    # No return statement

result = no_return_example()
print(result)  # None - nothing was returned!
```

If a function has no `return` statement, it returns `None` by default.

### Return Ends the Function

Code after `return` doesn't run:

```python
def example():
    return 42
    print("This never runs!")  # This line is never reached

value = example()  # value is 42
```

### Watch For

- **Forgetting return**: Calculating a value but not returning it
- **Code after return**: Putting code after the return statement (it won't run)
- **Not capturing the return value**: Calling the function but not storing the result

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_4_temperature | Temperature conversion functions using return |
| exercise_5_calculator_func | Math operation functions with parameters and return |

---

## Checkpoint

Ask: "What does a function return if it has no return statement?"
Expected: None

---

## If the Student Struggles

- **If forgetting to capture return value**: Show side by side - `add(2, 3)` vs `result = add(2, 3)`
- **If confused about where the value goes**: Trace through the code step by step, showing the value "traveling" back
- **If putting code after return**: Explain that return is like an exit door - once you leave, you can't do more in that room
