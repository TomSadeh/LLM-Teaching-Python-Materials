# Lesson: Decisions (if/elif/else) - Part 5: Nested Conditions

> **Module**: module_2_decisions
> **Part**: 5 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Nest conditional statements when needed

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Nested if | An if statement inside another if statement - for decisions that depend on earlier decisions |

---

## Lesson Content

### Building on Part 4
- We learned to combine conditions with `and`, `or`, `not`
- Sometimes we need decisions that depend on earlier decisions

### New Material

#### An if Inside Another if
```python
print("You enter a dark cave...")
choice1 = input("Go left or right? ")

if choice1 == "left":
    print("You find a treasure chest!")
    choice2 = input("Open it? (yes/no) ")
    if choice2 == "yes":
        print("Gold coins spill out!")
    else:
        print("You leave it alone.")
else:
    print("You find a friendly {{creature}}!")
```

#### When to Nest vs When to Use `and`
```python
# Nested approach
if has_ticket:
    if age >= 13:
        print("Welcome!")

# Using and (often cleaner)
if has_ticket and age >= 13:
    print("Welcome!")
```

**Use nesting when**:
- Different messages/actions for each level
- The inner decision only makes sense if the outer condition is True

**Use `and` when**:
- You just need both conditions to be True
- There's only one outcome you care about

### Watch For
- **Excessive nesting**: More than 2-3 levels deep is hard to read and usually can be simplified
- **Indentation confusion**: Each nested level needs its own indentation

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_8_adventure | Build a branching story with nested decisions |

---

## Checkpoint

Ask: "When would you use nested if statements instead of `and`?"
Expected: When you need different actions at each level, or when the inner decision only makes sense after the outer one

---

## If the Student Struggles

- **If struggling with nesting levels**: Use consistent indentation (4 spaces per level) and trace through the code step by step
- **If getting lost in the logic**: Draw a decision tree showing all possible paths
