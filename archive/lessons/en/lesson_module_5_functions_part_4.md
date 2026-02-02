# Lesson: Functions - Part 4: Print vs Return

> **Module**: module_5_functions
> **Part**: 4 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Clearly distinguish between `print()` and `return`, and choose the right one for each situation

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `print()` | Displays text on screen for humans to see - the value is "used up" |
| `return` | Sends a value back to the code that called the function - the value can be used |

---

## Lesson Content

### Building on Part 3

This is the most important distinction in this lesson! Many beginners confuse `print` and `return`. Let's make it crystal clear.

### Side-by-Side Comparison

```python
# Version 1: Using print
def double_print(number):
    result = number * 2
    print(result)

# Version 2: Using return
def double_return(number):
    result = number * 2
    return result
```

They look similar, but behave very differently!

### The Critical Difference

```python
# With print - can't use the result
answer1 = double_print(5)
print(f"answer1 is: {answer1}")  # answer1 is: None

# With return - can use the result
answer2 = double_return(5)
print(f"answer2 is: {answer2}")  # answer2 is: 10
```

`double_print(5)` shows "10" on screen, but `answer1` is `None`.
`double_return(5)` gives back 10, so `answer2` is `10`.

### Why This Matters

Try to use a print-only function in a calculation:

```python
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

# This fails!
total = add_print(2, 3) + add_print(4, 5)
# Prints 5, then 9, then crashes: TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# This works!
total = add_return(2, 3) + add_return(4, 5)
print(total)  # 14
```

### When to Use Which

| Use `print()` when... | Use `return` when... |
|-----------------------|----------------------|
| You want to show something to the user | You need to use the result in your code |
| For debugging (seeing what's happening) | For calculations and data processing |
| For final output at the end of a program | When other code needs the value |

### Practical Example: Validators

```python
def is_valid_password(password):
    if len(password) >= 8:
        return True    # Return, not print!
    else:
        return False

# Now we can use it in conditions
user_password = input("Enter password: ")
if is_valid_password(user_password):
    print("Password accepted!")
else:
    print("Password too short!")
```

If we had used `print(True)` instead of `return True`, the `if` statement wouldn't work!

### Watch For

- **Continued confusion**: This concept often takes multiple examples to sink in
- **Printing AND returning**: Some students try to do both - explain when that's useful vs when it's redundant
- **Using printed values**: Trying to store or use the result of a print-only function

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_6_validators | Boolean returning functions - must use return for True/False |

---

## Checkpoint

Ask: "If I write `result = my_function()` and my_function only prints, what is result?"
Expected: None (the printed text just shows on screen, nothing is returned)

---

## If the Student Struggles

- **If print/return confusion persists**: Draw a diagram showing where values "go" with each approach
  - Print: value goes to the screen (displayed and gone)
  - Return: value goes back to the calling code (can be stored and used)
- **If still confused**: Use a physical analogy - print is like shouting an answer out loud (everyone hears it, but it's gone), return is like handing someone a note (they can keep it and use it)
- **If not seeing the practical difference**: Have them try to write a program that needs to check multiple conditions using print-only functions - they'll see it doesn't work
