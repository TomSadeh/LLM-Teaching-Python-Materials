# Plan: Module 9 - Object-Oriented Programming

Recreation plan for module_9_oop using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_9_oop |
| **Topic** | Classes, objects, methods, inheritance |
| **Prerequisites** | module_0_basics through module_8_modules |
| **Target Hybrid Ratio** | 60-70% |

### Learning Objectives

By the end of this module, students will be able to:

1. Define classes using the `class` keyword
2. Write `__init__` methods to initialize object state
3. Use `self` to access and modify instance attributes
4. Define instance methods that operate on object state
5. Distinguish between class attributes and instance attributes
6. Implement `__str__` for human-readable object representation
7. Use inheritance to create specialized subclasses
8. Override methods in subclasses
9. Use `super()` to call parent class methods
10. Design classes to model real-world entities
11. Compare OOP and procedural approaches for the same problem

### Curriculum Constraints

| Available Concepts | NOT Available (later modules / advanced) |
|--------------------|------------------------------------------|
| **From Modules 0-8:** | |
| print(), variables, strings, numbers | file I/O (open/read/write) |
| input(), type conversion, f-strings | third-party packages (pip) |
| for loops, range(), while loops | async/await |
| if/elif/else, comparisons, boolean ops | decorators (@property, @classmethod) |
| lists, indexing, slicing, list methods | generators, iterators |
| functions (def, parameters, return) | context managers (with) |
| break, continue | multiple inheritance |
| import, standard library (math, datetime, random, string) | metaclasses |
| dictionaries, .get(), nested dicts | abstract base classes |
| try/except for error handling | class decorators |
| **New in Module 9:** | |
| `class ClassName:` syntax | |
| `__init__(self, ...)` constructor | |
| `self` parameter and instance attributes | |
| Instance methods `def method(self):` | |
| Class vs instance attributes | |
| `__str__(self)` for string representation | |
| Inheritance `class Child(Parent):` | |
| Method overriding | |
| `super()` for parent method calls | |
| Object interaction (methods taking other objects) | |

### Why OOP is Challenging

Based on pedagogy research and common struggles:

| Challenge | Why It's Hard | Our Response |
|-----------|---------------|--------------|
| **Understanding `self`** | Implicit first parameter is unintuitive | Explicit tracing, fill-in exercises |
| **Class vs Instance** | Abstract distinction | Visual metaphors (blueprint vs house) |
| **When to use classes** | Design decision with no clear rule | which_is_better comparisons |
| **Inheritance mental model** | "is-a" relationships are abstract | Progressive building from simple |
| **Object state** | State changes through method calls | code_tracing exercises |
| **Method vs function** | When to put logic inside class | Explicit comparison exercises |

### Mental Models to Build

| Concept | Metaphor | Exercise Strategy |
|---------|----------|-------------------|
| Class | Blueprint/template | Show class, then create multiple instances |
| Instance | Individual house from blueprint | Create several objects from same class |
| `self` | "This specific object" reference | Trace through method calls |
| `__init__` | Birth/creation moment | Initialize with different values |
| Methods | Actions the object can perform | Build behavior incrementally |
| Inheritance | Family tree / specialization | Start with parent, add child features |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [EXERCISE_TYPE_MODULE_MAPPING.md](../../templates/EXERCISE_TYPE_MODULE_MAPPING.md) | Valid types for Module 9 |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |
| Think Python chapters 14-17 | OOP pedagogy reference |

---

## 2. Exercise Distribution

### Available Exercise Types (5 total)

| Category | Types |
|----------|-------|
| **Core** | write_code, complete_function, blank_page |
| **Improvement** | fix_style |
| **Analysis** | which_is_better |

**Advantage over Module 8:** We have 5 exercise types vs Module 8's 2, enabling richer hybrid combinations.

### Target Distribution

| Type | Count | Rationale |
|------|:-----:|-----------|
| write_code | 4 | Core class building, method implementation |
| complete_function | 3 | Method completion with signature guidance |
| blank_page | 2 | Advanced independent class design |
| fix_style | 1 | OOP naming conventions and structure |
| which_is_better | 2 | OOP vs procedural, design comparisons |
| **hybrid** | 8 | Multi-part projects (62% of total) |
| **TOTAL** | **20** | |

### Hybrid Ratio Calculation

- Total exercises: 20
- Hybrid exercises: 8
- Ratio: **62%** (meets 60-70% target)

---

## 3. Exercise Inventory

### Concept Progression

Exercises are organized into concept clusters, progressing from simple to complex.

| Cluster | Concepts | Difficulty |
|---------|----------|:----------:|
| A | Class definition, `__init__`, `self`, attributes | 1-2 |
| B | Instance methods, calling methods | 2 |
| C | `__str__`, object representation | 2-3 |
| D | Multiple instances, object interaction | 3 |
| E | Inheritance basics, extending classes | 3 |
| F | Method overriding, `super()` | 3-4 |
| G | Class design, OOP vs procedural | 4 |
| H | Integration projects | 4-5 |

### Isolated Exercises

#### Cluster A: Class Basics (Difficulty 1-2)

| # | Type | Concept Focus |
|---|------|---------------|
| 1 | write_code | Define first class with `__init__` and attributes |
| 2 | complete_function | Complete `__init__` method with given attributes |

#### Cluster B: Instance Methods (Difficulty 2)

| # | Type | Concept Focus |
|---|------|---------------|
| 3 | write_code | Add methods that use and modify `self` attributes |
| 4 | complete_function | Complete method bodies using `self` |

#### Cluster C: Object Representation (Difficulty 2-3)

| # | Type | Concept Focus |
|---|------|---------------|
| 5 | write_code | Implement `__str__` for readable output |

#### Cluster D: Object Interaction (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 6 | write_code | Methods that take other objects as parameters |

#### Cluster E: Inheritance Basics (Difficulty 3)

| # | Type | Concept Focus |
|---|------|---------------|
| 7 | write_code | Create subclass that extends parent class |
| 8 | complete_function | Complete subclass `__init__` using `super()` |

#### Cluster F: Method Overriding (Difficulty 3-4)

| # | Type | Concept Focus |
|---|------|---------------|
| 9 | write_code | Override parent methods with specialized behavior |

#### Cluster G: Design and Analysis (Difficulty 4)

| # | Type | Concept Focus |
|---|------|---------------|
| 10 | which_is_better | Compare two class designs for same problem |
| 11 | which_is_better | Compare OOP vs procedural implementation |
| 12 | fix_style | Apply OOP naming conventions (PascalCase, etc.) |

### Hybrid Exercises

#### Hybrid 1: The Character Builder (Apprentice Arc)

**Story:** Learn to create characters for the {{school}} by following {{mentor}}'s examples.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GUIDANCE | complete_function | Study existing class, complete a method |
| 2 | GROWTH | write_code | Add new methods to the class |
| 3 | OWNERSHIP | write_code | Create your own character class |

**Placement:** After Cluster A-B (class basics + methods)
**Difficulty:** 2
**Arc:** Apprentice (adapted - no output_prediction, uses complete_function)

#### Hybrid 2: The Creature Collection (World Builder)

**Story:** Build a {{creature}} management system with classes.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Create base creature class |
| 2 | GROWTH | write_code | Add `__str__` for display |
| 3 | GROWTH | write_code | Create collection class that manages creatures |
| 4 | OWNERSHIP | write_code | Add interaction between creatures |

**Placement:** After Cluster C-D (representation + interaction)
**Difficulty:** 3
**Arc:** World Builder (build interconnected class system)

#### Hybrid 3: The Inheritance Journey (Inheritance Arc)

**Story:** {{hero}} discovers legacy code from {{mentor}} and must extend it.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | DISCOVERY | complete_function | Understand parent class by completing methods |
| 2 | GROWTH | write_code | Create first subclass |
| 3 | GROWTH | write_code | Create second subclass with different behavior |
| 4 | OWNERSHIP | write_code | Add shared functionality via inheritance |

**Placement:** After Cluster E (inheritance basics)
**Difficulty:** 3-4
**Arc:** Inheritance (study → extend → own)

#### Hybrid 4: The Method Override Challenge (Competition Arc)

**Story:** Two {{school}} students solved the same problem differently - which is better?

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Compare base class implementations |
| 2 | GROWTH | write_code | Implement override in subclass |
| 3 | EVALUATION | which_is_better | Compare override strategies |

**Placement:** After Cluster F (method overriding)
**Difficulty:** 3-4
**Arc:** Competition (evaluate → build → evaluate)

#### Hybrid 5: The Style Refactor (Upgrade Arc)

**Story:** Legacy code works but violates OOP conventions - clean it up.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Identify what's wrong |
| 2 | IMPROVEMENT | fix_style | Apply naming conventions |
| 3 | GROWTH | write_code | Reorganize into proper class structure |

**Placement:** Cluster G (design and analysis)
**Difficulty:** 4
**Arc:** Upgrade (evaluate → fix → rebuild)

#### Hybrid 6: OOP vs Procedural (Competition Arc)

**Story:** The great debate at {{school}} - when is OOP worth it?

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | EVALUATION | which_is_better | Compare dict-based vs class-based |
| 2 | GROWTH | write_code | Convert procedural to OOP |
| 3 | OWNERSHIP | blank_page | Design your own system, justify approach |

**Placement:** Cluster G (design and analysis)
**Difficulty:** 4
**Arc:** Competition (compare → implement → create)

#### Hybrid 7: The Game Entity System (World Builder)

**Story:** Build a complete game entity hierarchy for {{school}}.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Create base Entity class |
| 2 | GROWTH | write_code | Create Player subclass |
| 3 | GROWTH | write_code | Create Enemy subclass |
| 4 | GROWTH | write_code | Implement combat interaction |
| 5 | OWNERSHIP | blank_page | Add your own entity type |

**Placement:** Cluster H (integration)
**Difficulty:** 4-5
**Arc:** World Builder (build complex interconnected system)

#### Hybrid 8: The {{school}} Management System (Capstone)

**Story:** Design and build a complete system using OOP principles.

| Part | Beat | Type | Focus |
|------|------|------|-------|
| 1 | GROWTH | write_code | Design core class hierarchy |
| 2 | GROWTH | complete_function | Implement required methods |
| 3 | GROWTH | write_code | Add inheritance for specialization |
| 4 | IMPROVEMENT | fix_style | Ensure production-ready code |
| 5 | OWNERSHIP | blank_page | Extend with your own feature |

**Placement:** End of module (capstone)
**Difficulty:** 5
**Arc:** Custom (DESIGN → IMPLEMENT → INHERIT → POLISH → CREATE)

---

## 4. Difficulty Progression Map

```
Difficulty:  1 -----> 2 -----> 3 -----> 4 -----> 5
             |       |        |        |        |
Exercises:   1,2     3,4,5    6,7,8,9  10,11,12 -
             |       H1       H2,H3    H4,H5,H6 H7,H8
```

H1-H8 = Hybrid exercises

---

## 5. File Structure

```
exercises/
└── module_9_oop/
    ├── write_code/
    │   ├── exercise_1_first_class.py
    │   ├── exercise_2_methods.py
    │   ├── exercise_3_str_method.py
    │   ├── exercise_4_object_interaction.py
    │   ├── exercise_5_inheritance.py
    │   └── exercise_6_method_override.py
    ├── complete_function/
    │   ├── exercise_1_init_completion.py
    │   ├── exercise_2_method_completion.py
    │   └── exercise_3_super_completion.py
    ├── blank_page/
    │   ├── exercise_1_design_class.py
    │   └── exercise_2_design_hierarchy.py
    ├── fix_style/
    │   └── exercise_1_oop_conventions.py
    ├── which_is_better/
    │   ├── exercise_1_class_design.py
    │   └── exercise_2_oop_vs_procedural.py
    └── hybrid/
        ├── exercise_1_character_builder.py
        ├── exercise_2_creature_collection.py
        ├── exercise_3_inheritance_journey.py
        ├── exercise_4_override_challenge.py
        ├── exercise_5_style_refactor.py
        ├── exercise_6_oop_vs_procedural.py
        ├── exercise_7_game_entities.py
        └── exercise_8_school_management.py
```

---

## 6. Implementation Phases

### Phase 1: Class Fundamentals (Clusters A, B)

**Exercises:** 1, 2, 3, 4, Hybrid 1
**Difficulty:** 1-2
**Estimated Files:** 5

| # | Type | File |
|---|------|------|
| 1 | write_code | `write_code/exercise_1_first_class.py` |
| 2 | complete_function | `complete_function/exercise_1_init_completion.py` |
| 3 | write_code | `write_code/exercise_2_methods.py` |
| 4 | complete_function | `complete_function/exercise_2_method_completion.py` |
| H1 | hybrid | `hybrid/exercise_1_character_builder.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| write_code | [templates/exercise_types/write_code.py](../../templates/exercise_types/write_code.py) |
| complete_function | [templates/exercise_types/complete_function.py](../../templates/exercise_types/complete_function.py) |
| World Builder | [templates/activity_patterns/template_9_world_builder.py](../../templates/activity_patterns/template_9_world_builder.py) |

---

### Phase 2: Representation and Interaction (Clusters C, D)

**Exercises:** 5, 6, Hybrid 2
**Difficulty:** 2-3
**Estimated Files:** 3

| # | Type | File |
|---|------|------|
| 5 | write_code | `write_code/exercise_3_str_method.py` |
| 6 | write_code | `write_code/exercise_4_object_interaction.py` |
| H2 | hybrid | `hybrid/exercise_2_creature_collection.py` |

---

### Phase 3: Inheritance (Clusters E, F)

**Exercises:** 7, 8, 9, Hybrid 3, Hybrid 4
**Difficulty:** 3-4
**Estimated Files:** 5

| # | Type | File |
|---|------|------|
| 7 | write_code | `write_code/exercise_5_inheritance.py` |
| 8 | complete_function | `complete_function/exercise_3_super_completion.py` |
| 9 | write_code | `write_code/exercise_6_method_override.py` |
| H3 | hybrid | `hybrid/exercise_3_inheritance_journey.py` |
| H4 | hybrid | `hybrid/exercise_4_override_challenge.py` |

---

### Phase 4: Design and Analysis (Cluster G)

**Exercises:** 10, 11, 12, Hybrid 5, Hybrid 6
**Difficulty:** 4
**Estimated Files:** 5

| # | Type | File |
|---|------|------|
| 10 | which_is_better | `which_is_better/exercise_1_class_design.py` |
| 11 | which_is_better | `which_is_better/exercise_2_oop_vs_procedural.py` |
| 12 | fix_style | `fix_style/exercise_1_oop_conventions.py` |
| H5 | hybrid | `hybrid/exercise_5_style_refactor.py` |
| H6 | hybrid | `hybrid/exercise_6_oop_vs_procedural.py` |

**Read Before This Phase:**
| Template | Path |
|----------|------|
| which_is_better | [templates/exercise_types/which_is_better.py](../../templates/exercise_types/which_is_better.py) |
| fix_style | [templates/exercise_types/fix_style.py](../../templates/exercise_types/fix_style.py) |
| blank_page | [templates/exercise_types/blank_page.py](../../templates/exercise_types/blank_page.py) |

---

### Phase 5: Integration Projects (Cluster H)

**Exercises:** blank_page 1, blank_page 2, Hybrid 7, Hybrid 8
**Difficulty:** 4-5
**Estimated Files:** 4

| # | Type | File |
|---|------|------|
| 13 | blank_page | `blank_page/exercise_1_design_class.py` |
| 14 | blank_page | `blank_page/exercise_2_design_hierarchy.py` |
| H7 | hybrid | `hybrid/exercise_7_game_entities.py` |
| H8 | hybrid | `hybrid/exercise_8_school_management.py` |

---

### Phase Summary

| Phase | Cluster | Exercises | Files | New Templates |
|:-----:|---------|-----------|:-----:|---------------|
| 1 | Class Fundamentals | 1-4, H1 | 5 | write_code, complete_function |
| 2 | Representation + Interaction | 5-6, H2 | 3 | *(none)* |
| 3 | Inheritance | 7-9, H3, H4 | 5 | *(none)* |
| 4 | Design and Analysis | 10-12, H5, H6 | 5 | which_is_better, fix_style, blank_page |
| 5 | Integration | 13-14, H7, H8 | 4 | *(none)* |
| **Total** | | **20** | **22** | |

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every exercise contains at least one `{{placeholder}}`
- [ ] NO concepts from later modules (file I/O, decorators, multiple inheritance)
- [ ] All 11 learning objectives covered
- [ ] Progressive difficulty (1 to 5)
- [ ] Only uses approved exercise types (write_code, complete_function, blank_page, fix_style, which_is_better)

### Format Requirements

- [ ] All functions/methods use `pass` placeholder
- [ ] Instructions use `# YOUR CODE HERE` marker
- [ ] Each file has `main()` that calls all exercises
- [ ] PEP 8 compliant (including PascalCase for class names)
- [ ] Follows templates from `templates/exercise_types/`

### OOP-Specific Requirements

- [ ] Class names use PascalCase
- [ ] Method names use snake_case
- [ ] `self` is always first parameter of instance methods
- [ ] `__init__` properly initializes all attributes
- [ ] Docstrings explain class purpose and methods
- [ ] Examples show creating instances and calling methods

### Curriculum Compliance

| Concept | Covered In |
|---------|------------|
| `class` keyword | Exercises 1, H1 |
| `__init__` method | Exercises 1, 2, H1 |
| `self` parameter | Exercises 1-9, all hybrids |
| Instance attributes | Exercises 1-6, H1, H2 |
| Instance methods | Exercises 3, 4, H1, H2 |
| Class vs instance attributes | Exercise 4, H2 |
| `__str__` method | Exercise 5, H2 |
| Inheritance | Exercises 7, 8, H3 |
| `super()` | Exercise 8, H3 |
| Method overriding | Exercise 9, H3, H4 |
| OOP design principles | Exercises 10, 11, H5, H6 |
| Complex class hierarchies | H7, H8 |

---

## 8. Implementation Notes

### Key Constraints

1. **No file I/O** - Objects exist only in memory
2. **No decorators** - No @property, @classmethod, @staticmethod
3. **No multiple inheritance** - Single parent only
4. **No abstract classes** - Just concrete implementations
5. **Students HAVE all prior concepts** - Functions, dicts, loops, etc.

### OOP Concepts to Teach

| Concept | Priority | Teaching Approach |
|---------|:--------:|-------------------|
| `class` definition | High | Blueprint metaphor |
| `__init__` | High | Birth/creation moment |
| `self` | High | "This specific object" |
| Instance attributes | High | Object's personal data |
| Instance methods | High | Object's abilities |
| `__str__` | Medium | How object introduces itself |
| Inheritance | High | Specialization/family tree |
| `super()` | Medium | Calling parent's version |
| Method overriding | Medium | Customizing inherited behavior |
| Class attributes | Low | Shared by all instances |

### OOP Concepts NOT to Teach (Too Advanced)

| Concept | Reason |
|---------|--------|
| `@property` | Decorator syntax not introduced |
| `@classmethod` / `@staticmethod` | Too advanced |
| Multiple inheritance | Complex, rarely needed |
| Abstract base classes | Requires abc module |
| Dunder methods beyond `__init__`/`__str__` | Too many, too abstract |
| Metaclasses | Graduate-level topic |
| Composition vs inheritance | Advanced design pattern |

### Pedagogical Considerations

**Why OOP is challenging:**

- `self` is mandatory but feels redundant
- Class vs instance distinction is abstract
- When to use OOP vs functions/dicts is unclear
- Inheritance can feel like "magic"
- Object state changes are harder to trace

**Building mental models:**

- Class = "cookie cutter" or "blueprint"
- Instance = "actual cookie" or "house built from blueprint"
- `self` = "me" - the object talking about itself
- `__init__` = "when I was born, I was given these things"
- Methods = "things I can do"
- Inheritance = "I'm like my parent, but with extras"

### Placeholder Usage Ideas

- `{{hero}}` as a Character class
- `{{creature}}` as base class for creatures
- `{{spell1}}`, `{{spell2}}` as Ability class instances
- `{{school}}` management system with Student/Teacher classes
- `{{item}}` as Item class in inventory system
- `{{mentor}}` provides the parent class
- `{{villain}}` as Enemy subclass
- `{{location}}` as Location class hierarchy

### Code Patterns to Demonstrate

**Basic class:**
```python
class {{ROLE_TITLE}}:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def introduce(self):
        return f"I am {self.name}, level {self.level}"
```

**Inheritance:**
```python
class {{creature}}(BaseCreature):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def attack(self):
        return f"{self.name} attacks with power {self.power}!"
```

**Object interaction:**
```python
def battle(self, other):
    if self.power > other.power:
        return f"{self.name} defeats {other.name}!"
```

---

## 9. Concept-Specific Teaching Notes

### Class Basics (Cluster A)

**Introducing `class`:**
```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
```

**Key points:**
- `class` keyword starts definition
- Class names use PascalCase
- `__init__` is called automatically when creating object
- `self` refers to the object being created

**Common errors:**
- Forgetting `self` in method signatures
- Not calling `super().__init__()` in subclasses
- Confusing class definition with instance creation

### Methods (Cluster B)

**Instance methods:**
```python
def take_damage(self, amount):
    self.health -= amount
    if self.health < 0:
        self.health = 0

def is_alive(self):
    return self.health > 0
```

**Key points:**
- Methods always have `self` as first parameter
- Methods can access and modify attributes via `self`
- Methods can return values or modify state

### Special Methods (Cluster C)

**`__str__` for display:**
```python
def __str__(self):
    return f"{self.name} (HP: {self.health})"
```

**Key points:**
- `__str__` is called by `print()` and `str()`
- Should return a human-readable string
- Makes debugging much easier

### Object Interaction (Cluster D)

**Methods with other objects:**
```python
def attack(self, target):
    damage = self.strength
    target.take_damage(damage)
    return f"{self.name} dealt {damage} damage to {target.name}"
```

**Key points:**
- Methods can take other objects as parameters
- Objects can call methods on other objects
- This enables complex interactions

### Inheritance (Clusters E, F)

**Creating subclasses:**
```python
class Wizard(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} casts a spell!"
        return f"{self.name} has no mana!"
```

**Key points:**
- `class Child(Parent):` creates inheritance
- `super().__init__()` calls parent's initializer
- Child can add new attributes and methods
- Child can override parent methods

### Design Analysis (Cluster G)

**OOP vs Procedural comparison:**

Procedural (with dicts):
```python
def create_character(name, health):
    return {"name": name, "health": health}

def take_damage(character, amount):
    character["health"] -= amount
```

OOP:
```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
```

**When OOP is better:**
- Complex state with many interacting pieces
- Behavior closely tied to data
- Need for inheritance/specialization
- Modeling real-world entities

**When dicts/functions are fine:**
- Simple data with few operations
- Configuration or settings
- Quick prototypes

---

## 10. Arc Adaptations for Module 9

Module 9's 5 exercise types enable richer hybrid combinations than Module 8.

| Standard Arc | Adaptation for Module 9 |
|--------------|------------------------|
| Apprentice | complete_function → write_code → write_code |
| Inheritance | complete_function → write_code → write_code → write_code |
| Competition | which_is_better → write_code → which_is_better |
| Upgrade | which_is_better → fix_style → write_code |
| World Builder | write_code → write_code → write_code → blank_page |

### Custom Arcs for OOP

**BUILD → EXTEND → SPECIALIZE:**
1. Build base class (write_code)
2. Add methods (write_code)
3. Create subclasses (write_code)
4. Override for specialization (write_code)

**COMPARE → CONVERT → CREATE:**
1. Compare OOP vs procedural (which_is_better)
2. Convert to OOP (write_code)
3. Design your own (blank_page)

---

## 11. Comparison with Adjacent Modules

| Aspect | Module 8 (Modules) | Module 9 (OOP) | Module 10 (Mega) |
|--------|-------------------|----------------|------------------|
| Exercise types | 2 | **5** | TBD |
| Total exercises | 18 | 20 | TBD |
| Hybrid count | 9 | 8 | TBD |
| Hybrid ratio | 60% | 62% | TBD |
| Key challenge | Import/namespace | Object orientation | Full integration |
| Arc diversity | Low (constrained) | **Medium-High** | TBD |

**Module 9 advantages:**
1. More exercise types enable varied pedagogy
2. `which_is_better` perfect for OOP design questions
3. `blank_page` enables independent class design
4. Rich opportunities for World Builder pattern

---

## 12. Success Criteria

A successful Module 9 implementation will:

1. **Demystify `self`** - Students understand why `self` is needed
2. **Build class intuition** - Students know when classes help vs hurt
3. **Enable inheritance** - Students can create and extend class hierarchies
4. **Develop design sense** - Students can compare OOP vs procedural approaches
5. **Prepare for projects** - Students ready for Module 10 mega project

### Measurable Outcomes

| Objective | How We'll Know |
|-----------|----------------|
| Can create classes | Exercises 1-4 completed |
| Understands `self` | Method completion exercises correct |
| Can use inheritance | Exercises 7-9, H3 completed |
| Can evaluate design | which_is_better exercises show reasoning |
| Can design independently | blank_page exercises produce valid classes |

---

## 13. Transition Notes

### From Module 8 (Modules)

Students arrive knowing:
- How to import standard library
- How to create custom modules
- `__name__ == "__main__"` pattern
- Error handling with try/except

**Bridge concepts:**
- Classes are like modules that hold both data AND functions
- `self` is like the module's internal state
- Methods are like module functions that know about the module's data

### To Module 10 (Mega Project)

Students should leave ready to:
- Design multi-class systems
- Use inheritance for code reuse
- Model real-world domains with objects
- Integrate all concepts from Modules 0-9

**Capstone prep:**
- Hybrid 8 (school management) is explicit capstone prep
- Complex interactions between classes
- Full OOP design exercise

---

## 14. References

### Think Python Chapters (OOP coverage)

| Chapter | Topic | Our Coverage |
|---------|-------|--------------|
| 14 | Classes and Functions | Cluster A |
| 15 | Classes and Methods | Clusters B, C |
| 16 | Classes and Objects | Cluster D |
| 17 | Inheritance | Clusters E, F |

### Pedagogy Sources

- Common struggles: `references/pedagogy/common-struggles.md`
- Exercise types: `references/pedagogy/exercise-types.md`
- Progression patterns: `references/pedagogy/progression-patterns.md`
