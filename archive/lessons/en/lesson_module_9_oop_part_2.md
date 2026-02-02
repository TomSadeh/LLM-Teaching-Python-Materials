# Lesson: Object-Oriented Programming - Part 2: Creating a Simple Class

> **Module**: module_9_oop
> **Part**: 2 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Define a class with the `class` keyword and create instances (objects) of it

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `class` keyword | How you define a new class in Python |
| Instance | A specific object created from a class blueprint |
| Dot notation | How you access attributes on an object (e.g., `hero.name`) |

---

## Lesson Content

### Building on Part 1

We learned WHY classes are useful - now let's see HOW to create one.

### Your First Class

The simplest possible class:

```python
class Character:
    pass

# Create an instance (object) from the class
hero = Character()
villain = Character()
```

### Adding Attributes

You can add attributes to an object using dot notation:

```python
hero = Character()
hero.name = "{{hero}}"
hero.health = 100

villain = Character()
villain.name = "{{villain}}"
villain.health = 80
```

### Accessing Attributes

```python
print(hero.name)        # Prints: {{hero}}
print(villain.health)   # Prints: 80
```

### Key Insight: Class vs Instance

- `Character` is the **class** (the blueprint)
- `hero` and `villain` are **instances** (specific objects)
- Each instance has its own separate attributes

```python
# This shows they are different objects:
print(hero.name)      # {{hero}}
print(villain.name)   # {{villain}}
```

### Watch For

- **Missing parentheses**: `Character` is the class, `Character()` creates an instance
- Students trying to access attributes on the class itself instead of an instance
- Confusion between the class name and variable names

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_first_class | Simplest possible class - define and create instances |

---

## Checkpoint

Ask: "What's the difference between a class and an object?"
Expected: A class is the blueprint/template, an object is a specific instance made from it

---

## If the Student Struggles

- **If class vs instance is unclear**: Use tangible examples - "Dog" is the class, "my dog Fluffy" is an instance
- **If forgetting parentheses**: Emphasize that `Character` is like a recipe, `Character()` is like following the recipe to make something
- **If dot notation is confusing**: Compare to how you access items in a dictionary with brackets, but objects use dots
