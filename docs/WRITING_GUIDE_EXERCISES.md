# Writing Guide: Exercises

Guidelines for creating theme-agnostic Python exercises.

**Before writing:** Load [REFERENCES.md](REFERENCES.md) for pedagogical context on the topic.

---

## Core Rules

### 1. Theme-Agnostic Content

Every exercise must work with **any** theme. Use placeholders, never hardcode theme-specific text.

- **Placeholders**: See [TEMPLATE.md](../TEMPLATE.md) for all available variables
- **Layer 1** (`{{hero}}`, `{{school}}`): Entity names
- **Layer 2** (`{{CONTEXT_INTRO}}`): Full narrative sentences
- **Layer 3** (`{{PRACTITIONER_SINGULAR}}`): Framework concepts

### 2. Teach Proper Python

- Follow PEP 8
- Use meaningful variable names
- Explain trade-offs when multiple approaches exist
- Never oversimplify to the point of teaching bad habits

### 3. Progressive Complexity

Each exercise within a module introduces one new element.

---

## File Structure

**Location**: `exercises/{module}/{type}/exercise_N_name.py`

**Naming**: Lowercase, underscores, numbered sequentially.

---

## Required Elements

| Element | Description |
|---------|-------------|
| Placeholder | At least one `{{placeholder}}` per file |
| Student marker | `# ✏️ YOUR CODE HERE ✏️` at edit locations |
| Pass placeholder | All student functions contain `pass` |
| Main function | `main()` calls all exercises |

---

## Templates and Patterns

| Need | Document |
|------|----------|
| Exercise type templates | [templates/exercise_types/](../templates/exercise_types/) |
| Type-to-module mapping | [templates/EXERCISE_TYPE_MODULE_MAPPING.md](../templates/EXERCISE_TYPE_MODULE_MAPPING.md) |
| Narrative archetypes | [NARRATIVE_ARCHETYPES.md](NARRATIVE_ARCHETYPES.md) |
| Archetype quick templates | [templates/ARCHETYPE_QUICK_REFERENCE.md](../templates/ARCHETYPE_QUICK_REFERENCE.md) |
| Activity patterns | [templates/activity_patterns/](../templates/activity_patterns/) |
| Structure patterns | [templates/structure_patterns/](../templates/structure_patterns/) |
| Full examples | [FULL_EXERCISE_EXAMPLES.md](FULL_EXERCISE_EXAMPLES.md) |

---

## Checklist

- [ ] At least one `{{placeholder}}` per file
- [ ] Uses `pass` in all student functions
- [ ] Uses `✏️` marker at edit locations
- [ ] `main()` calls all exercises
- [ ] Follows PEP 8
