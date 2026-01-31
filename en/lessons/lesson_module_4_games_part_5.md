# Lesson: Games (While Loops & Random) - Part 5: Break and Menu Loops

> **Module**: module_4_games
> **Part**: 5 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use `break` to exit a loop early and create menu-driven game loops

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `break` | Immediately exits the current loop |
| Menu loop | A while True loop that shows options and exits when the user chooses to quit |
| `while True` | A common pattern for loops that exit via break rather than a condition |

---

## Lesson Content

### Building on Part 4

Sometimes we want to exit a loop immediately, not wait until the condition is checked. That's what `break` does.

### New Material

Using `break` for quitting:
```python
while True:
    choice = input("Play again? (yes/quit): ")
    if choice == "quit":
        print("Thanks for playing!")
        break
    print("Starting new game...")
```

Menu-driven game:
```python
while True:
    print("\n=== GAME MENU ===")
    print("1. Play Game")
    print("2. View High Score")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        print("Playing game...")
        # Game code here
    elif choice == "2":
        print("High Score: 100")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
```

Key point: `break` only exits the innermost loop. If you have nested loops, break only exits the inner one.

### Watch For

- **Using break outside a loop**: `break` must be inside a while or for loop
- **Confusing break and return**: `break` exits the loop; `return` exits the function
- **Confusing break and continue**: `break` exits entirely; `continue` skips to the next iteration

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_2_rock_paper_scissors | Classic game with play-again loop |
| exercise_5_word_scramble | String manipulation with game loop |
| exercise_6_slots | Slot machine with multiple random numbers |
| exercise_8_hangman | Classic word game with state tracking |
| exercise_9_adventure | Text adventure with nested loops and state |

---

## Checkpoint

Ask: "How would you let the player play again after winning?"
Expected: Wrap the game in another while loop with a "play again?" prompt, using break when they choose to quit

---

## If the Student Struggles

- **If break isn't working**: Make sure it's inside the loop, not outside
- **If confused about break vs continue**: "break = leave the building; continue = skip this room, go to the next one"
- **If nested loop confusion**: Only the innermost loop is affected by break

---

## Notes for the LLM Teacher

- Games are highly motivating - let students customize and add features
- Celebrate when games work - this is often a breakthrough moment for engagement
- Start with the simplest possible version and add complexity gradually
- Encourage "what if" experimentation with random ranges and game rules
- The exercises in this phase are more complex - guide students to break them into smaller steps
