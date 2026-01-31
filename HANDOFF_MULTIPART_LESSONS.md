# Multi-Part Lessons Integration Guide

This document explains how to integrate the multi-part lesson structure into Maya Chat.

## Overview

Lessons are now split into focused **parts**, each covering a single teaching phase. This reduces context size and allows students to take natural breaks between concepts.

**Before**: One large lesson per module (~150 lines, 15-20 minutes)
**After**: 5-6 small parts per module (~50 lines each, 3-8 minutes each)

---

## JSON Structure

### Identifying Part-Based Lessons

In `lessons.json`, part-based lessons have two additional fields:

```json
{
  "source_id": "lesson_module_0_basics_part_1",
  "title": "Python Basics - Part 1: Hello World with print()",
  "title_he": "יסודות פייתון - חלק 1: שלום עולם עם print()",
  "module": "module_0_basics",
  "part": 1,
  "total_parts": 5,
  "order_index": 0,
  "difficulty": 1,
  "duration": "3-5 minutes",
  "content_md": "...",
  "content_md_he": "..."
}
```

| Field | Type | Description |
|-------|------|-------------|
| `part` | `int \| null` | Part number (1, 2, 3...). `null` for legacy full lessons |
| `total_parts` | `int \| null` | Total parts in this module. `null` for legacy lessons |

### Filtering Logic

```python
# Get all part-based lessons for a module
def get_module_parts(lessons: list, module: str) -> list:
    return sorted(
        [l for l in lessons if l["module"] == module and l.get("part") is not None],
        key=lambda x: x["part"]
    )

# Check if a lesson is part-based
def is_multipart(lesson: dict) -> bool:
    return lesson.get("part") is not None

# Get the legacy full lesson (if exists)
def get_full_lesson(lessons: list, module: str) -> dict | None:
    for l in lessons:
        if l["module"] == module and l.get("part") is None:
            return l
    return None
```

---

## Ordering

Lessons are sorted by:
1. `order_index` (module order: 0, 1, 2...)
2. `part` (part order within module: 1, 2, 3...)

The `source_id` follows the pattern:
- Full lesson: `lesson_module_0_basics`
- Part lesson: `lesson_module_0_basics_part_1`

---

## Module Part Counts

| Module | Parts | Duration |
|--------|-------|----------|
| module_0_basics | 5 | 3-7 min each |
| module_1_turtle_loops | 5 | 4-6 min each |
| module_2_decisions | 5 | 5-6 min each |
| module_3_lists | 5 | 5-6 min each |
| module_4_games | 5 | 5-6 min each |
| module_5_functions | 5 | 6-8 min each |
| module_7_dictionaries | 5 | 5-6 min each |
| module_8_modules | 6 | 5-6 min each |
| module_9_oop | 5 | 6-8 min each |
| free_practice | 1 (no parts) | Open-ended |

---

## UI Integration Patterns

### Pattern 1: Progressive Disclosure

Show parts as expandable sections within a module:

```
📘 Python Basics
   ├── Part 1: Hello World with print() ✓
   ├── Part 2: Variables ✓
   ├── Part 3: Math Operations (current)
   ├── Part 4: Getting User Input
   └── Part 5: Putting It All Together
```

### Pattern 2: Sequential Navigation

Load one part at a time with next/previous navigation:

```
[← Part 2: Variables]  Part 3 of 5: Math Operations  [Part 4: Input →]
```

### Pattern 3: Smart Context Loading

Only load the current part's `content_md` into the LLM context:

```python
def get_lesson_context(lessons: list, module: str, current_part: int) -> str:
    parts = get_module_parts(lessons, module)
    for part in parts:
        if part["part"] == current_part:
            return part["content_md"]  # or content_md_he for Hebrew
    return ""
```

---

## Content Structure Within Parts

### Part 1 Contains

- Prerequisites (what student should know)
- Learning Objective (single, focused goal)
- Key Concepts (table of terms)
- Lesson Content (teaching material)
- Practice Exercises (exercise references)
- Checkpoint (comprehension question)
- If Student Struggles (troubleshooting)
- Real-World Connection (motivation)
- Notes for LLM Teacher (teaching tips)

### Parts 2+ Contain

- Learning Objective
- Key Concepts
- Lesson Content (includes "Building on Part N-1" section)
- Practice Exercises
- Checkpoint
- If Student Struggles

---

## Backward Compatibility

The original full lesson files are **preserved** alongside the parts:

```
lessons.json contains:
├── lesson_module_0_basics          (full lesson, part=null)
├── lesson_module_0_basics_part_1   (part=1)
├── lesson_module_0_basics_part_2   (part=2)
├── lesson_module_0_basics_part_3   (part=3)
├── lesson_module_0_basics_part_4   (part=4)
└── lesson_module_0_basics_part_5   (part=5)
```

You can choose to:
1. **Use only parts** - Filter where `part is not None`
2. **Use only full lessons** - Filter where `part is None`
3. **Offer a choice** - Let users pick "Quick lessons" vs "Full lessons"

---

## Sync Service Updates

Update `remote_sync_service.sync_lessons()` to handle the new fields:

```python
class Lesson:
    source_id: str
    title: str
    title_he: str
    module: str
    part: int | None          # NEW
    total_parts: int | None   # NEW
    order_index: int
    difficulty: int
    duration: str
    content_md: str
    content_md_he: str
```

### Database Migration (if storing locally)

```sql
ALTER TABLE lessons ADD COLUMN part INTEGER;
ALTER TABLE lessons ADD COLUMN total_parts INTEGER;
```

---

## Progress Tracking

Consider tracking progress per-part for finer granularity:

```python
# Old: Single completion per module
progress = {"module_0_basics": "completed"}

# New: Per-part progress
progress = {
    "lesson_module_0_basics_part_1": "completed",
    "lesson_module_0_basics_part_2": "completed",
    "lesson_module_0_basics_part_3": "in_progress",
    "lesson_module_0_basics_part_4": "not_started",
    "lesson_module_0_basics_part_5": "not_started",
}

# Calculate module completion percentage
def get_module_progress(progress: dict, module: str) -> float:
    parts = [k for k in progress if module in k and "_part_" in k]
    if not parts:
        return 0.0
    completed = sum(1 for p in parts if progress[p] == "completed")
    return completed / len(parts)
```

---

## Example: Loading a Lesson Session

```python
async def start_lesson_session(module: str, part: int = 1):
    lessons = await fetch_lessons_json()

    # Get all parts for this module
    module_parts = get_module_parts(lessons, module)

    if not module_parts:
        # Fallback to full lesson
        full_lesson = get_full_lesson(lessons, module)
        return full_lesson["content_md"]

    # Get the requested part
    current_part = next(
        (p for p in module_parts if p["part"] == part),
        module_parts[0]
    )

    # Build context for LLM
    context = f"""
    Module: {current_part['module']}
    Part {current_part['part']} of {current_part['total_parts']}: {current_part['title']}
    Duration: {current_part['duration']}

    {current_part['content_md']}
    """

    return context
```

---

## Questions?

If you need clarification on integration, the key files are:
- `lessons.json` - The generated output with all lessons
- `scripts/build_lessons_json.py` - How the JSON is built
- `en/lessons/lesson_*_part_*.md` - The source markdown files
