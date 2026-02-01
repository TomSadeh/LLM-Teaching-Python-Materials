# Reference Materials Catalog

Curriculum analysis from popular Python teaching resources and pedagogy research.

---

## Textbook Curricula

### Think Python (Allen Downey)

**Focus:** CS fundamentals, recursion, OOP

| Ch | Topic | Our Module |
|----|-------|------------|
| 1 | Programming as thinking | - |
| 2 | Variables and statements | module_0 |
| 3 | Functions | module_5 |
| 4 | Turtle, interface design | module_1 |
| 5 | Conditionals, recursion | module_2 |
| 6 | Return values | module_5 |
| 7 | Iteration, search | module_4 |
| 8 | Strings, regex | module_8 |
| 9 | Lists | module_3 |
| 10 | Dictionaries, memoization | module_7 |
| 11 | Tuples | - |
| 12 | Text analysis | - |
| 13 | Files, databases | - |
| 14-17 | OOP | module_9 |
| 18-19 | Advanced topics | - |

**Key differences:** Functions earlier, recursion emphasis, covers tuples/files.

**Files:**
- [curriculum.md](../references/think-python/curriculum.md)
- [exercises.md](../references/think-python/exercises.md)
- [gap-analysis.md](../references/think-python/gap-analysis.md)

---

### Python for Everybody (Dr. Chuck)

**Focus:** Data processing, web, databases

| Ch | Topic | Our Module |
|----|-------|------------|
| 1 | Introduction | - |
| 2 | Variables | module_0 |
| 3 | Conditionals, try/except | module_2 |
| 4 | Functions | module_5 |
| 5 | Iterations | module_1, module_4 |
| 6 | Strings | module_0 |
| 7 | Files | - |
| 8 | Lists | module_3 |
| 9 | Dictionaries | module_7 |
| 10 | Tuples | - |
| 11 | Regex | - |
| 12 | Web scraping | - |
| 13 | Web services, APIs | - |
| 14 | OOP | module_9 |
| 15 | Databases | - |
| 16 | Data visualization | - |

**Key differences:** Data-focused examples, try/except early, web/API chapters.

**Files:**
- [curriculum.md](../references/python-for-everybody/curriculum.md)
- [exercises.md](../references/python-for-everybody/exercises.md)
- [gap-analysis.md](../references/python-for-everybody/gap-analysis.md)

---

### Automate the Boring Stuff (Al Sweigart)

**Focus:** Practical automation projects

| Ch | Topic | Our Module |
|----|-------|------------|
| 1-2 | Python basics | module_0 |
| 3 | Flow control | module_2 |
| 4 | Loops | module_1, module_4 |
| 5 | Functions | module_5 |
| 6 | Debugging | - |
| 7 | Lists | module_3 |
| 8 | Dictionaries | module_7 |
| 9 | Strings | module_0 |
| 10 | Regex | - |
| 11-12 | Files | - |
| 13-25 | Automation projects | - |

**Key differences:** Dedicated debugging chapter, no OOP, massive automation section.

**Files:**
- [curriculum.md](../references/automate-boring-stuff/curriculum.md)
- [exercises.md](../references/automate-boring-stuff/exercises.md)
- [gap-analysis.md](../references/automate-boring-stuff/gap-analysis.md)

---

## Pedagogy Research

### Learning Science

Research-backed teaching principles.

| Topic | Key Insight |
|-------|-------------|
| Cognitive Load | Working memory holds ~4 chunks; reduce extraneous load |
| Worked Examples | Beginners learn better from studying solutions first |
| Deliberate Practice | Specific goals + immediate feedback + repetition |
| Transfer | Varied contexts help apply learning in new situations |
| Motivation | Autonomy, competence, relatedness drive engagement |
| Spacing | Spread practice over time for better retention |

**File:** [learning-science.md](../references/pedagogy/learning-science.md)

---

### Common Struggles

Universal beginner pain points and teaching strategies.

| Struggle | Exercise Response |
|----------|-------------------|
| Syntax errors | decode_error |
| Variable confusion | code_tracing, output_prediction |
| Loop mental models | Turtle visualization, code_tracing |
| Function confusion | complete_function |
| Off-by-one errors | bug_hunt |
| Boolean logic | output_prediction |
| State/mutability | code_tracing |
| Debugging mindset | bug_hunt, decode_error |

**File:** [common-struggles.md](../references/pedagogy/common-struggles.md)

---

### Exercise Types

Taxonomy of programming exercises by cognitive load and skill target.

| Category | Types | Skills |
|----------|-------|--------|
| Reading | output_prediction, code_tracing, match_output | Comprehension |
| Scaffolded | fill_blanks, code_ordering, complete_function | Guided writing |
| Debugging | bug_hunt, decode_error | Error handling |
| Improvement | fix_style, simplify_code, add_error_handling | Code quality |
| Analysis | which_is_better, spot_difference | Evaluation |
| Free Writing | write_code, blank_page | Full creation |

**Progression:** Read → Fill blanks → Fix bugs → Write code

**File:** [exercise-types.md](../references/pedagogy/exercise-types.md)

---

### Progression Patterns

How to sequence topics effectively.

| Approach | Order | Philosophy |
|----------|-------|------------|
| Academic | Variables → Functions → Loops → Recursion | Functions fundamental |
| Practical | Variables → Loops → Data → Functions → Files | Build useful things |
| Visual (ours) | Basics → Turtle/Loops → Lists → Games → Functions | Engagement first |

**Key decisions:**
- Functions early vs late (we: late)
- For vs while first (we: for)
- Lists vs dicts first (we: lists)

**File:** [progression-patterns.md](../references/pedagogy/progression-patterns.md)

---

## Topics We Don't Cover (Gaps)

From all three curricula:

| Topic | Source | Priority |
|-------|--------|----------|
| File I/O | All three | Medium |
| Try/except basics | PY4E, ATBS | Medium |
| Tuples | Think Python, PY4E | Low |
| Regex | All three | Low |
| Debugging techniques | ATBS | Medium |
| Recursion | Think Python | Low |
| Web/APIs | PY4E | Low |
| Databases | Think Python, PY4E | Low |

---

## Quick Lookup

### By Module Topic

| If writing for... | Consult... |
|-------------------|------------|
| module_0 (basics) | Think Python ch 1-2, ATBS ch 1-2 |
| module_1 (turtle) | Think Python ch 4 |
| module_2 (decisions) | PY4E ch 3, ATBS ch 3 |
| module_3 (lists) | All three - ch 7-9 |
| module_4 (games/while) | Think Python ch 7, ATBS ch 4 |
| module_5 (functions) | Think Python ch 3,6, PY4E ch 4 |
| module_7 (dicts) | All three - ch 8-10 |
| module_9 (OOP) | Think Python ch 14-17 |

### By Exercise Type

| If creating... | Consult... |
|----------------|------------|
| Bug hunt | common-struggles.md, exercise-types.md |
| Code tracing | exercise-types.md |
| Output prediction | exercise-types.md, learning-science.md |
| Any new type | exercise-types.md, EXERCISE_TYPE_MODULE_MAPPING.md |

### By Skill Target

| Teaching... | Consult... |
|-------------|------------|
| Syntax | common-struggles.md (Syntax Errors) |
| Debugging | common-struggles.md (Debugging Mindset), ATBS ch 6 |
| Functions | common-struggles.md (Function Confusion) |
| Loops | common-struggles.md (Loop Mental Models) |
