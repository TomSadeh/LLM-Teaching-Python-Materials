# Lesson: Object-Oriented Programming - Part 4: Adding Methods

> **Module**: module_9_oop
> **Part**: 4 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Define methods that operate on object data and understand why `self` is needed

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Method | A function that belongs to a class and can access the object's data |
| `self` in methods | Lets the method access and modify the specific object it was called on |

---

## Lesson Content

### Building on Part 3

We can create objects with attributes. Now let's add behavior - things the object can DO.

### Methods Are Functions Inside Classes

```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        print(f"I am {self.name}!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! Health: {self.health}")
```

### Calling Methods

Use dot notation, just like attributes:

```python
hero = Character("{{hero}}", 100)
hero.introduce()           # Prints: I am {{hero}}!
hero.take_damage(20)       # Prints: {{hero}} takes 20 damage! Health: 80
```

### Why self is Required

Every method needs `self` as its first parameter:

```python
def introduce(self):       # self is required!
    print(f"I am {self.name}!")  # self.name accesses THIS object's name

# When you call:
hero.introduce()
# Python automatically passes hero as self
```

Think of `self` as telling the method "which object are you working with?"

### Methods Can Modify State

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

counter = Counter()
counter.increment()
counter.increment()
print(counter.get_count())  # Prints: 2
```

### Watch For

- **Forgetting self in definition**: `def introduce():` won't work
- **Not using self to access attributes**: `print(name)` looks for a local variable, not `self.name`
- **Forgetting to call with parentheses**: `hero.introduce` vs `hero.introduce()`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_3_methods | Adding methods to a class |
| exercise_6_counter | Simple class with state - practical example |

---

## Checkpoint

Ask: "Why do methods always have `self` as the first parameter?"
Expected: So the method knows which object it's working with - it can access that object's attributes

---

## If the Student Struggles

- **If forgetting self**: Have them always write `self` first, then add other parameters
- **If self.x vs x is confusing**: Explain that `self.name` is "the name stored on this object" while `name` alone looks for a local variable
- **If methods vs functions unclear**: Methods are functions that "belong to" an object and can access its data
