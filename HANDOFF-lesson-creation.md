# Handoff: Lesson Document Creation

## Context

We've established a framework for teaching Python to preteens/teens (ages 10-16) via an LLM teacher. The methodology documents have been updated with 12 core teaching principles, and lesson templates have been created.

## What Was Done

### Updated Methodology Documents
- `en/teaching_methodology.md` - English version
- `he/teaching_methodology.md` - Hebrew version

Both now include:
- Target audience definition (preteens/teens, smart, capable of understanding tradeoffs)
- 12 core teaching principles (treat as intelligent, proper coding practices, progressive isolation, etc.)
- Lesson structure (15-40 min: warm-up → intro → guided practice → independent practice → wrap-up)
- Adaptive teaching signals
- What NOT to do

### Created Lesson Templates
- `en/lessons/TEMPLATE.md`
- `he/lessons/TEMPLATE.md`

## What Needs to Be Done

Create lesson documents for each module. The modules are:

| Module | Topic | Difficulty | Priority |
|--------|-------|------------|----------|
| `module_0_basics` | Print, variables, math, input/output | 1 | High |
| `module_1_turtle_loops` | Turtle graphics, for loops | 1 | High |
| `module_2_decisions` | if/elif/else, comparisons | 2 | High |
| `module_3_lists` | Lists, iteration, list methods | 2 | High |
| `module_4_games` | While loops, random, game logic | 2 | Medium |
| `module_5_functions` | Functions, parameters, return values | 3 | High |
| `module_6_final_project` | Integration project | 3 | Low |
| `module_7_dictionaries` | Dictionaries, key-value pairs | 2 | Medium |
| `module_8_modules` | Built-in modules (datetime, json, etc.) | 3 | Medium |
| `module_9_oop` | Classes, objects, inheritance | 3 | Medium |

## How to Create a Lesson Document

1. **Copy the template** from `en/lessons/TEMPLATE.md` (or `he/lessons/`)
2. **Name it** `lesson_[topic].md` (e.g., `lesson_lists.md`)
3. **Fill in each section** using the guidance below

### Section-by-Section Guidance

#### Prerequisites
Look at what modules come before this one. What concepts must they already know?

#### Learning Objectives
Be specific and measurable. "Understand lists" is bad. "Create a list with 3+ items" is good.

#### Key Concepts
List the 3-5 core terms/concepts. One sentence each. These are vocabulary words.

#### Common Misconceptions
Think about what confuses beginners:
- Off-by-one errors in loops
- Mutable vs immutable confusion
- Scope issues with variables
- Forgetting `return` in functions

#### Teaching Sequence
Follow the "progressive isolation" principle:
1. Concept alone (no variables, simplest form)
2. Add one element (introduce variables)
3. Add another (type conversion, edge cases)
4. Combine with previous knowledge

#### Exercises Mapping
Look at the actual exercises in `raw_exercises/module_X_*/`. Map which exercises cover which concepts. This helps the LLM know when to assign what.

#### Checkpoints
Write simple questions that test understanding. Not trick questions—just verification that they got it.

#### If Student Struggles
Provide alternative explanations or analogies specific to this topic.

#### Real-World Connection
One sentence about where this appears in apps/games they know. Don't overthink it.

## Key Principles to Remember

1. **No code examples in lesson docs** - The LLM will generate appropriate examples based on student context and theme preferences

2. **Keep it brief** - These are guidelines for the LLM, not student-facing content. The LLM improvises.

3. **Focus on the "what" and "why"** - The LLM handles the "how" dynamically

4. **Progressive complexity** - Each phase builds on the previous

5. **Lesson duration guide**:
   - Simple topics (basics, simple loops): 15-20 min
   - Medium topics (lists, conditions): 25-30 min
   - Complex topics (functions, OOP): 35-40 min

## File Structure After Completion

```
en/
├── teaching_methodology.md
└── lessons/
    ├── TEMPLATE.md
    ├── lesson_basics.md
    ├── lesson_turtle_loops.md
    ├── lesson_decisions.md
    ├── lesson_lists.md
    ├── lesson_games.md
    ├── lesson_functions.md
    ├── lesson_dictionaries.md
    ├── lesson_modules.md
    └── lesson_oop.md

he/
├── teaching_methodology.md
└── lessons/
    ├── TEMPLATE.md
    ├── lesson_basics.md
    ├── lesson_turtle_loops.md
    ... (same structure)
```

## Reference: Exercise Files Per Module

For mapping exercises to concepts, here are the exercise counts:

- `module_0_basics`: 18 exercises (hello, variables, math, input, calculator, madlib, etc.)
- `module_1_turtle_loops`: 10 exercises (square, triangle, star, hexagon, circle, etc.)
- `module_2_decisions`: 9 exercises (password, grades, number_game, quiz, etc.)
- `module_3_lists`: 9 exercises (favorites, loop_list, magic_8ball, todo_list, etc.)
- `module_4_games`: 9 exercises (guess_number, rock_paper_scissors, dice, trivia, etc.)
- `module_5_functions`: 9 exercises (shapes, helper_functions, temperature, etc.)
- `module_6_final_project`: 3 templates (app, art, game)
- `module_7_dictionaries`: 9 exercises (spellbook, character_stats, nested_data, etc.)
- `module_8_modules`: 9 exercises (datetime, random, json, math, string, etc.)
- `module_9_oop`: 9 exercises (first_class, init, methods, inheritance, etc.)

## Notes

- Create English versions first, then translate to Hebrew
- Use `{{placeholder}}` syntax in any themed examples (see `theme_variables.json`)
- The LLM teacher will read both `teaching_methodology.md` AND the relevant lesson doc when teaching
