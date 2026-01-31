# Lesson: Object-Oriented Programming - Part 3: The __init__ Method

> **Module**: module_9_oop
> **Part**: 3 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use `__init__` to set up object attributes when an object is created

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `__init__` | Special method that runs automatically when creating a new object |
| `self` | Reference to the current object being created or used |
| Attribute | A variable that belongs to an object (e.g., `self.name`) |

---

## Lesson Content

### Building on Part 2

We created objects and added attributes afterward. But there's a better way - set up attributes at creation time.

### The Problem with Adding Attributes Later

```python
hero = Character()
hero.name = "{{hero}}"
hero.health = 100

# What if you forget one?
sidekick = Character()
sidekick.name = "{{friend}}"
# Oops! Forgot to set health!
print(sidekick.health)  # Error!
```

### The Solution: __init__

```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Now you MUST provide name and health when creating
hero = Character("{{hero}}", 100)
sidekick = Character("{{friend}}", 80)
```

### Understanding self

`self` refers to the specific object being created:

```python
def __init__(self, name, health):
    self.name = name    # Store name ON THIS OBJECT
    self.health = health  # Store health ON THIS OBJECT
```

When you call `Character("{{hero}}", 100)`:
- Python creates a new object
- `self` refers to that new object
- `self.name = name` stores "{{hero}}" on that object

### Different Instances, Different Values

```python
hero = Character("{{hero}}", 100)
villain = Character("{{villain}}", 120)

print(hero.name)     # {{hero}}
print(villain.name)  # {{villain}}
```

Each object stores its own values!

### Watch For

- **Not using self.**: Writing just `name = name` creates a local variable, not an attribute
- **Forgetting self parameter**: `def __init__(name, health):` won't work
- **Confusing parameter and attribute**: The parameter `name` and the attribute `self.name` are different things

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_2_init | Practice writing __init__ methods to set up objects |

---

## Checkpoint

Ask: "What is `__init__` for?"
Expected: It runs when you create a new object and sets up its initial values

---

## If the Student Struggles

- **If __init__ is mysterious**: Call it "the setup function" that runs automatically when you create an object
- **If self is confusing**: Explain it as "this object right here" - like saying your own name when referring to yourself
- **If not storing with self.**: Draw a diagram showing the difference between local variable `name` and object attribute `self.name`
