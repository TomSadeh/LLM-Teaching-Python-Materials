# Lesson: Object-Oriented Programming - Part 5: Putting It All Together

> **Module**: module_9_oop
> **Part**: 5 of 5
> **Difficulty**: 3
> **Duration**: 6-8 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Create complete classes with `__init__` and multiple methods, and understand how objects maintain state

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| State | The current values of an object's attributes at any moment |
| Object interaction | Objects can work together, calling methods on each other |

---

## Lesson Content

### Building on Part 4

We know all the pieces. Now let's build complete, useful classes.

### A Complete Character Class

```python
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_alive = True

    def attack(self, target):
        if self.is_alive:
            damage = self.strength
            print(f"{self.name} attacks {target.name} for {damage} damage!")
            target.take_damage(damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} has {self.health} health remaining.")
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        if self.is_alive:
            self.health += amount
            print(f"{self.name} heals for {amount}. Health: {self.health}")

    def status(self):
        status = "alive" if self.is_alive else "defeated"
        print(f"{self.name}: {self.health} HP, {status}")
```

### Objects Interacting

```python
hero = Character("{{hero}}", 100, 25)
villain = Character("{{villain}}", 80, 30)

hero.attack(villain)    # Hero attacks villain
villain.attack(hero)    # Villain fights back

hero.status()
villain.status()
```

### Objects Maintain State

The power of OOP: objects remember their state between method calls:

```python
# Each call changes the object's state
hero.take_damage(20)    # health is now 80
hero.take_damage(15)    # health is now 65
hero.heal(10)           # health is now 75
```

### Multiple Instances, Independent State

```python
hero = Character("{{hero}}", 100, 20)
friend = Character("{{friend}}", 80, 15)

hero.take_damage(30)    # hero's health: 70
friend.take_damage(10)  # friend's health: 70

# They have separate health values!
```

### Watch For

- **Confusing class-level vs instance-level**: Each object has its own attributes
- **Objects affecting each other unintentionally**: Make sure students understand which object is being modified
- **Forgetting to use self in methods**: Review if they're still making this mistake

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_4_character | Complete character class - RPG-style example |
| exercise_5_pet_sim | State changes - Interactive object |
| exercise_7_bank_account | Multiple methods, validation - Real-world model |
| exercise_8_text_adventure | Objects interacting - Complex application |
| exercise_9_game_objects | Multiple classes - Full project |

---

## Checkpoint

Ask: "When would you use a class instead of just a dictionary?"
Expected: When you want to bundle data with behavior/functions that operate on that data, and when objects need to maintain and change state over time

---

## If the Student Struggles

- **If object interaction is confusing**: Walk through each method call step by step, showing what changes
- **If state changes are unclear**: Print out attribute values after each operation to show how they change
- **If forgetting syntax**: Provide a minimal template they can copy and modify

---

## Extension Ideas

For students who finish early or want more challenge:

- Create a simple text-based game with Player and Enemy classes
- Build a virtual pet that has needs (hunger, happiness) that change over time
- Make a Card class and build a simple card game

---

## Notes for the LLM Teacher

- This is the culmination of the OOP lesson - make sure all previous concepts are solid before complex examples
- Don't introduce inheritance in this lesson - focus on the basics
- The character/RPG context works well since students understand stats and actions
- Encourage students to experiment with creating their own classes
- `self` is the hardest concept - if they're still struggling, review it again
- Consider not using the term "constructor" - just call it "the init method"
