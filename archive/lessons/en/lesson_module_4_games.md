# Lesson: Games (While Loops & Random)

> **Module**: module_4_games
> **Difficulty**: 2
> **Duration**: 25-30 minutes

---

## Prerequisites

What the student should already know before this lesson:

- [ ] Variables and input/output
- [ ] if/elif/else statements
- [ ] Lists and for loops
- [ ] Basic comparison operators

---

## Learning Objectives

By the end of this lesson, the student will be able to:

1. Use `while` loops for indefinite repetition
2. Generate random numbers with `random.randint()`
3. Create game loops that continue until a condition is met
4. Track game state using variables (score, attempts, etc.)
5. Use `break` to exit a loop early

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `while` loop | Repeats as long as a condition is True (unlike `for` which repeats a set number of times) |
| `random.randint(a, b)` | Returns a random integer between a and b, inclusive |
| Game loop | A while loop that keeps the game running until win/lose/quit |
| `break` | Immediately exits the current loop |
| State variable | A variable that tracks something across multiple iterations (like score) |

---

## Common Misconceptions

1. **Infinite loops**: Forgetting to update the condition variable
   **Reality**: The loop condition must eventually become False, or use `break`

2. **Off-by-one with randint**: Thinking `randint(1, 10)` excludes 10
   **Reality**: `randint` includes both endpoints (unlike `range`)

3. **Confusing break and continue**: Using break when they want to skip to next iteration
   **Reality**: `break` exits the loop entirely; `continue` skips to the next iteration

4. **Not importing random**: Trying to use random functions without `import random`
   **Reality**: Always need `import random` at the top of the file

---

## Teaching Sequence

### Phase 1: While loop basics
- Compare to for loop: "do this while something is true"
- Simple example: counting down from 5
- Emphasize: the condition is checked before each iteration
- Watch for: infinite loops, forgetting to update counter

### Phase 2: Random numbers
- `import random` - explain imports briefly
- `random.randint(1, 10)` - random number from 1 to 10
- Show that it gives different results each time
- Watch for: forgetting the import, wrong syntax

### Phase 3: Simple guessing game
- Computer picks a random number
- Player guesses until correct
- Give "higher/lower" hints
- Classic application of while + random + conditionals
- Watch for: not updating the guess inside the loop

### Phase 4: Game state and scoring
- Track number of attempts
- Add a score system
- Limit number of guesses
- Watch for: resetting score inside the loop instead of before

### Phase 5: Break and menu loops
- Using `break` to exit when player quits
- Creating a menu that loops until "exit" is chosen
- Watch for: using break outside a loop, break vs return confusion

---

## Exercises Mapping

| Exercise | Concepts covered | Notes |
|----------|------------------|-------|
| exercise_1_guess_number | while, randint, conditionals | Core game mechanics |
| exercise_2_rock_paper_scissors | random.choice, conditionals | Classic game |
| exercise_3_dice | randint, accumulating scores | Simple random |
| exercise_4_high_low | randint, comparison, loops | Card game variant |
| exercise_5_word_scramble | random.shuffle, lists | String manipulation |
| exercise_6_slots | Multiple randint, matching | Visual game |
| exercise_7_trivia | Lists, conditionals, score | Quiz game |
| exercise_8_hangman | String iteration, state | Classic word game |
| exercise_9_adventure | Nested loops, state | Text adventure |

---

## Checkpoints

### After Phase 1 (while loop)
Ask: "What happens if the while condition is never False?"
Expected: The loop runs forever (infinite loop)

### After Phase 2 (random)
Ask: "What do you need at the top of your file to use random?"
Expected: `import random`

### After Phase 3 (guessing game)
Ask: "In the guessing game, what should happen after a wrong guess?"
Expected: Ask for another guess (loop continues)

### End of Lesson
Ask: "How would you let the player play again after winning?"
Expected: Wrap the game in another while loop with a "play again?" prompt

---

## If the Student Struggles

- **If creating infinite loops**: Add print statements to show what's happening each iteration
- **If confused about while vs for**: "for = known number of times; while = until something happens"
- **If game logic is wrong**: Break it into smaller pieces - get the random number working first, then add the loop
- **If not getting randomness**: Explain that `randint` is truly random - can't predict it

---

## Extension Ideas

For students who finish early or want more challenge:

- Add difficulty levels (easy = fewer numbers, hard = more)
- Create a two-player game
- Make a "best of 3" wrapper around a game
- Add a high score system that persists across games

---

## Real-World Connection

> "Every game you play has a game loop running - Minecraft checks your inputs, updates the world, and redraws the screen many times per second, all in a while loop."

---

## Notes for the LLM Teacher

- Games are highly motivating - let students customize and add features
- Start with the simplest possible version and add complexity gradually
- Infinite loops can freeze the environment - teach Ctrl+C early
- Encourage "what if" experimentation with random ranges and game rules
- Celebrate when games work - this is often a breakthrough moment for engagement
