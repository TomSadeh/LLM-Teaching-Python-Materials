# Plan: Module 10 - Mega Project (Capstone)

Final capstone module for the curriculum using the universal template system.

---

## 1. Overview

### Module Identity

| Field | Value |
|-------|-------|
| **Module ID** | module_10_mega_project |
| **Topic** | Capstone integration project |
| **Prerequisites** | module_0_basics through module_9_oop |
| **Target Hybrid Ratio** | 100% (capstone projects) |
| **Format** | Multi-file guided projects (not exercise collections) |

### What Makes This Different

| Aspect | Modules 0-9 | Module 10 |
|--------|-------------|-----------|
| Structure | Collection of exercises | Guided multi-file projects |
| Files | Single .py per exercise | Multiple .py files per project |
| Scope | Practice one concept | Integrate ALL concepts |
| Output | Working functions | Complete working application |
| Time | 15-45 min per exercise | 2-4 hours per project |

### Learning Objectives

By the end of this module, students will be able to:

1. Design and implement a multi-file Python application
2. Organize code using custom modules and packages
3. Design class hierarchies for real-world domains
4. Implement data persistence with JSON (save/load state)
5. Generate reports and export data to CSV
6. Handle errors gracefully throughout an application
7. Integrate all concepts from modules 0-9 cohesively
8. Follow software development practices (separation of concerns, documentation)

### Curriculum Constraints

| Available Concepts (ALL) | Still NOT Available |
|--------------------------|---------------------|
| **Everything from Modules 0-9:** | |
| print(), variables, strings, numbers, f-strings | third-party packages (pip install) |
| for loops, range(), while loops, break, continue | async/await, threading |
| if/elif/else, comparisons, boolean ops | decorators (@property, etc.) |
| lists, indexing, slicing, list methods | generators, iterators |
| functions (def, parameters, return, defaults) | multiple inheritance |
| dictionaries, .get(), nested dicts | abstract base classes |
| import, standard library (math, datetime, random, string) | database (sqlite, etc.) |
| file I/O with context managers (with open) | web frameworks |
| json module (load, dump) | GUI libraries |
| csv module (reader, writer) | |
| classes, __init__, self, methods | |
| inheritance, super(), method overriding | |
| __str__ for object representation | |
| try/except for error handling | |

### READ BEFORE STARTING

| Document | Purpose |
|----------|---------|
| [META_PLAN_MODULE_RECREATION.md](META_PLAN_MODULE_RECREATION.md) | Overall strategy |
| [TEMPLATE.md](../../TEMPLATE.md) | Placeholder reference |
| [WRITING_GUIDE_EXERCISES.md](WRITING_GUIDE_EXERCISES.md) | Exercise format standards |
| Module 8 Plan | File I/O patterns |
| Module 9 Plan | OOP patterns |

---

## 2. Project Structure

### Overview

Module 10 contains **2 guided capstone projects**. Each project:
- Spans multiple Python files (3-5 files)
- Requires all major concepts from the curriculum
- Has clear milestones with checkpoints
- Produces a working application

### Project Selection

| Project | Theme Focus | Primary Concepts |
|---------|-------------|------------------|
| **Project 1: Entity Manager** | Management/Simulation | OOP, JSON persistence, reports |
| **Project 2: Data Tracker** | Data analysis | CSV, dicts, functions, file I/O |

Students complete **both projects** (or instructor can choose one based on time).

---

## 3. Project 1: The {{school}} Entity Manager

### Concept

Build a complete entity management system where users can create, manage, and persist entities (characters, creatures, items, etc.) with full OOP architecture.

### Architecture

```
project_1_entity_manager/
├── main.py              # Entry point, main menu loop
├── models.py            # Entity classes (Base, specialized types)
├── storage.py           # JSON save/load functionality
├── reports.py           # CSV export and statistics
└── utils.py             # Helper functions (validation, formatting)
```

### Milestones

#### Milestone 1: Core Models (models.py)

**Goal:** Create the class hierarchy for entities.

| Task | Concepts Used |
|------|---------------|
| Create base `Entity` class with common attributes | class, __init__, self |
| Implement `__str__` for display | dunder methods |
| Create 2-3 specialized subclasses | inheritance, super() |
| Add methods for entity actions | instance methods |

**Checkpoint:** Can create and display entities in Python REPL.

#### Milestone 2: Main Application Loop (main.py)

**Goal:** Build the interactive menu system.

| Task | Concepts Used |
|------|---------------|
| Create main menu with options | while loop, input |
| Implement add/remove/list operations | lists, functions |
| Connect menu to model operations | function calls, imports |
| Add input validation | conditionals, try/except |

**Checkpoint:** Can add, list, and remove entities (not persisted yet).

#### Milestone 3: Data Persistence (storage.py)

**Goal:** Save and load entity data.

| Task | Concepts Used |
|------|---------------|
| Convert objects to dict for JSON | dict comprehension, __dict__ |
| Implement save_data() function | json.dump, with open |
| Implement load_data() function | json.load, error handling |
| Reconstruct objects from dicts | class instantiation |

**Checkpoint:** Data persists between application runs.

#### Milestone 4: Reports and Export (reports.py)

**Goal:** Generate statistics and CSV exports.

| Task | Concepts Used |
|------|---------------|
| Calculate statistics (counts, averages) | loops, math operations |
| Generate summary report | f-strings, formatting |
| Export entity list to CSV | csv.writer, with open |
| Add filtering options | conditionals, list comprehension |

**Checkpoint:** Can export data and view statistics.

#### Milestone 5: Polish and Integration (utils.py + all)

**Goal:** Add helpers and polish the application.

| Task | Concepts Used |
|------|---------------|
| Create validation helpers | functions, string methods |
| Add error handling throughout | try/except |
| Improve user feedback messages | f-strings |
| Test complete workflow | integration |

**Final Checkpoint:** Complete working application with persistence.

### Placeholder Integration

| Component | Placeholders Used |
|-----------|-------------------|
| Entity types | `{{creature}}`, `{{hero}}`, `{{item}}` |
| Application name | `{{school}} Manager` |
| Messages | `{{CONTEXT_INTRO}}`, `{{exclamation}}` |
| Export files | `{{school}}_entities.csv` |

---

## 4. Project 2: The {{school}} Data Tracker

### Concept

Build a data tracking application that records events/observations, stores them in CSV format, and provides analysis and filtering capabilities.

### Architecture

```
project_2_data_tracker/
├── main.py              # Entry point, main menu loop
├── tracker.py           # Core tracking logic (add, search, filter)
├── data_io.py           # CSV read/write operations
├── analyzer.py          # Statistics and analysis functions
└── config.py            # Settings and constants
```

### Milestones

#### Milestone 1: Data Structure Design (config.py, tracker.py)

**Goal:** Define what data we're tracking and how.

| Task | Concepts Used |
|------|---------------|
| Define record structure (fields) | dicts, lists |
| Create record validation function | functions, conditionals |
| Define constants and settings | variables, module structure |
| Create Tracker class or functions | class or functions |

**Checkpoint:** Can create and validate records in memory.

#### Milestone 2: CSV Operations (data_io.py)

**Goal:** Read and write tracking data.

| Task | Concepts Used |
|------|---------------|
| Implement write_records() | csv.writer, with open |
| Implement read_records() | csv.reader, list building |
| Handle empty/missing file | try/except, defaults |
| Add append mode for new records | file modes |

**Checkpoint:** Can save and load records from CSV.

#### Milestone 3: Main Interface (main.py)

**Goal:** Build the user interface.

| Task | Concepts Used |
|------|---------------|
| Create main menu loop | while loop, input |
| Implement "add record" flow | input, validation |
| Implement "view records" display | loops, formatting |
| Add search/filter interface | string methods, conditionals |

**Checkpoint:** Can add, view, and search records.

#### Milestone 4: Analysis Features (analyzer.py)

**Goal:** Add data analysis capabilities.

| Task | Concepts Used |
|------|---------------|
| Count records by category | dicts for counting |
| Calculate date-based statistics | datetime module |
| Find min/max/average values | loops, math |
| Generate summary report | f-strings, formatting |

**Checkpoint:** Can generate meaningful insights from data.

#### Milestone 5: Polish and Error Handling

**Goal:** Make the application robust.

| Task | Concepts Used |
|------|---------------|
| Add input validation everywhere | try/except, conditionals |
| Handle file errors gracefully | FileNotFoundError |
| Add helpful error messages | f-strings |
| Test edge cases | systematic testing |

**Final Checkpoint:** Complete working data tracker.

### Placeholder Integration

| Component | Placeholders Used |
|-----------|-------------------|
| What's tracked | `{{creature}}` sightings, `{{item}}` inventory |
| Application name | `{{school}} Tracker` |
| Data file | `{{school}}_records.csv` |
| Categories | `{{location}}`, `{{house}}` |

---

## 5. File Structure

```
exercises/
└── module_10_mega_project/
    ├── project_1_entity_manager/
    │   ├── README.md           # Project instructions
    │   ├── main.py             # Starter with TODOs
    │   ├── models.py           # Starter with TODOs
    │   ├── storage.py          # Starter with TODOs
    │   ├── reports.py          # Starter with TODOs
    │   └── utils.py            # Starter with TODOs
    └── project_2_data_tracker/
        ├── README.md           # Project instructions
        ├── main.py             # Starter with TODOs
        ├── tracker.py          # Starter with TODOs
        ├── data_io.py          # Starter with TODOs
        ├── analyzer.py         # Starter with TODOs
        └── config.py           # Starter with TODOs
```

### File Contents

Each starter file contains:
1. Module docstring explaining purpose
2. Imports (pre-filled)
3. Function/class stubs with docstrings
4. `# ✏️ YOUR CODE HERE ✏️` markers
5. `if __name__ == "__main__":` section for testing

---

## 6. Implementation Approach

### How Starter Files Work

**Example: models.py starter**

```python
"""
{{school}} Entity Manager - Models Module

This module defines the entity classes for the management system.
"""


class Entity:
    """
    Base class for all entities in the {{school}}.

    Attributes:
        name (str): The entity's name
        entity_type (str): Type identifier
        created_date (str): When the entity was created
    """

    def __init__(self, name, entity_type):
        """
        Initialize a new Entity.

        Args:
            name: The entity's name
            entity_type: The type of entity
        """
        # ✏️ YOUR CODE HERE ✏️
        # Initialize self.name, self.entity_type
        # Set self.created_date to today's date (use datetime)
        pass

    def __str__(self):
        """Return a string representation of the entity."""
        # ✏️ YOUR CODE HERE ✏️
        pass

    def to_dict(self):
        """
        Convert entity to dictionary for JSON serialization.

        Returns:
            dict: Entity data as dictionary
        """
        # ✏️ YOUR CODE HERE ✏️
        pass


class Character(Entity):
    """
    A character entity with health and level.

    Inherits from Entity and adds:
        health (int): Current health points
        level (int): Experience level
    """

    def __init__(self, name, health=100, level=1):
        """
        Initialize a new Character.

        Args:
            name: Character name
            health: Starting health (default 100)
            level: Starting level (default 1)
        """
        # ✏️ YOUR CODE HERE ✏️
        # Call parent __init__ with entity_type="character"
        # Initialize self.health and self.level
        pass


# Add more entity types as needed...


if __name__ == "__main__":
    # Test your classes here
    # Example:
    # hero = Character("{{hero}}", health=100, level=5)
    # print(hero)
    pass
```

### README Structure

Each project README includes:
1. Project overview and goals
2. Architecture diagram
3. Milestone-by-milestone instructions
4. Hints (but not solutions)
5. Testing suggestions
6. Extension ideas for advanced students

---

## 7. Quality Checklist

### Content Requirements

- [ ] Every file contains at least one `{{placeholder}}`
- [ ] Uses ALL major concepts from curriculum
- [ ] No concepts from outside curriculum (no pip packages, decorators, etc.)
- [ ] Clear milestone progression
- [ ] Each milestone has a testable checkpoint

### Format Requirements

- [ ] All functions/methods use `pass` placeholder
- [ ] Instructions use `# ✏️ YOUR CODE HERE ✏️` marker
- [ ] Each file has `if __name__ == "__main__":` for testing
- [ ] PEP 8 compliant stubs
- [ ] Comprehensive docstrings

### Project Requirements

- [ ] Multi-file architecture (3-5 files per project)
- [ ] Requires file I/O (JSON and/or CSV)
- [ ] Requires OOP (classes with inheritance)
- [ ] Requires error handling
- [ ] Produces working application

### Curriculum Coverage

| Module | Concepts | Where Used |
|--------|----------|------------|
| 0 | print, variables, f-strings, input | All files, user interaction |
| 1 | for loops | Iteration over collections |
| 2 | if/elif/else | Menu logic, validation |
| 3 | lists | Storing collections of entities/records |
| 4 | functions | All modules organized as functions |
| 5 | while loops | Main menu, input validation loops |
| 6 | - | Integration checkpoint (this builds on it) |
| 7 | dictionaries | JSON conversion, data aggregation |
| 8 | json, csv, file I/O | Persistence, exports |
| 9 | classes, inheritance | Entity models |

---

## 8. Implementation Notes

### Key Constraints

1. **No external packages** - Only standard library
2. **Realistic scope** - Completable in 2-4 hours
3. **Incremental progress** - Each milestone produces working code
4. **Testable** - Each file can be run standalone for testing
5. **Theme-agnostic** - Works with any theme via placeholders

### Pedagogical Considerations

**Why multi-file projects?**
- Real software is multi-file
- Teaches import/module organization
- Shows separation of concerns
- Prepares for real development

**Why two projects?**
- Different styles (OOP-heavy vs data-heavy)
- Student choice increases engagement
- Different difficulty levels
- Instructors can assign based on time

**Milestone approach:**
- Prevents "blank page paralysis"
- Ensures incremental progress
- Each checkpoint is motivating
- Easier to debug (know what should work)

### Placeholder Usage

| Placeholder | Project 1 Usage | Project 2 Usage |
|-------------|-----------------|-----------------|
| `{{school}}` | Application name | Application name |
| `{{hero}}` | Example character | N/A |
| `{{creature}}` | Entity type | What's being tracked |
| `{{item}}` | Entity type | What's being tracked |
| `{{location}}` | Entity attribute | Data category |
| `{{exclamation}}` | Success messages | Success messages |

---

## 9. Extension Ideas

For students who finish early or want more challenge:

### Project 1 Extensions
- Add a battle/interaction system between entities
- Implement entity evolution/upgrades
- Add search and filter for entities
- Create entity relationships (groups, teams)

### Project 2 Extensions
- Add date-range filtering for reports
- Implement data visualization (text-based charts)
- Add import from CSV (not just export)
- Create trend analysis over time

---

## 10. Success Criteria

A successful Module 10 implementation will:

1. **Demonstrate integration** - Students use all major concepts together
2. **Build real applications** - Output is a working, usable program
3. **Teach organization** - Students learn multi-file project structure
4. **Show persistence** - Data survives between runs
5. **Prepare for real development** - Skills transfer to actual projects

### Measurable Outcomes

| Objective | How We'll Know |
|-----------|----------------|
| Multi-file skills | Student creates proper imports between files |
| OOP mastery | Classes use inheritance correctly |
| Persistence works | Data loads correctly after restart |
| Error handling | Application doesn't crash on bad input |
| Integration | All concepts work together seamlessly |

---

## 11. Comparison with Module 6

| Aspect | Module 6 (Mid) | Module 10 (Mega) |
|--------|----------------|------------------|
| Position | After module 5 | End of curriculum |
| Concepts available | Basics through functions | Everything |
| File structure | Single file per exercise | Multi-file projects |
| Persistence | None | JSON and CSV |
| OOP | None | Full class hierarchies |
| Project count | 4 hybrid exercises | 2 full projects |
| Scope | Practice integration | Build complete apps |

---

## 12. Transition Notes

### From Module 9 (OOP)

Students arrive knowing:
- Class definition and instantiation
- Inheritance and super()
- Method overriding
- Object interaction
- File I/O (from module 8)

**Bridge to capstone:**
- "Now let's use everything together"
- Classes organize our domain models
- Files persist our objects
- Functions organize our logic

### Course Completion

After Module 10, students can:
- Design and build Python applications
- Use OOP for domain modeling
- Persist data between sessions
- Handle errors gracefully
- Organize multi-file projects

**Next steps (outside curriculum):**
- External packages (pip)
- Web development
- Database integration
- GUI development
- Testing frameworks
