# Lesson: Games (While Loops & Random) - Part 3: Simple Guessing Game

> **Module**: module_4_games
> **Part**: 3 of 5
> **Difficulty**: 2
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Create game loops that continue until a condition is met (combining while loops with random)

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| Game loop | A while loop that keeps the game running until win/lose/quit |
| User feedback | Giving hints like "higher/lower" to guide the player |

---

## Lesson Content

### Building on Parts 1-2

We know while loops (repeat until something is true) and random numbers (unpredictable values). Now we combine them to make our first game!

### New Material

The classic number guessing game structure:
```python
import random

secret = random.randint(1, 100)
guess = 0  # Initialize to something that's not the secret

while guess != secret:
    guess = int(input("Guess the number: "))

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it!")
```

Key elements:
1. Computer picks a random number once (before the loop)
2. Loop continues until player guesses correctly
3. Give hints after each wrong guess
4. Get a NEW guess each time through the loop

### Watch For

- **Not updating the guess inside the loop**: The guess must change, or it's an infinite loop
- **Picking a new random number each iteration**: The secret should be set BEFORE the loop, not inside it
- **Not converting input to int**: `input()` returns a string, need `int()` for number comparison

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_guess_number | Core guessing game mechanics - the foundation for other games |
| exercise_4_high_low | Card game variant using comparison and random |

---

## Checkpoint

Ask: "In the guessing game, what should happen after a wrong guess?"
Expected: Ask for another guess (loop continues)

---

## If the Student Struggles

- **If game logic is wrong**: Break it into smaller pieces - get the random number working first, then add the loop
- **If loop never ends**: Check that `guess` is being updated inside the loop
- **If random number keeps changing**: Make sure `random.randint()` is called once, before the while loop
