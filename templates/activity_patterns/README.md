# Narrative Template Library

**Purpose:** Ready-to-use narrative templates that work across all genres (fantasy, sci-fi, sports, music, business, etc.)

**Usage:** Copy template, fill in Python concepts, define context blocks for your theme.

---

## Available Templates

| # | Template Name | Purpose | Best For | Complexity |
|---|---------------|---------|----------|------------|
| 1 | [Tutorial Guide](template_1_tutorial_guide.py) | Show example, then replicate | Introducing new concepts | ⭐ Simple |
| 2 | [Incremental Builder](template_2_incremental_builder.py) | Build complex system step-by-step | Multi-part exercises | ⭐⭐ Moderate |
| 3 | [Role Assignment](template_3_role_assignment.py) | Student takes specific role | Contextualized tasks | ⭐ Simple |
| 4 | [Forensic Debugger](template_4_forensic_debugger.py) | Investigate and fix errors | decode_error, bug_hunt | ⭐⭐ Moderate |
| 5 | [Comparison Analyst](template_5_comparison_analyst.py) | Compare approaches, analyze tradeoffs | which_is_better | ⭐⭐⭐ Advanced |
| 6 | [Specification Implementer](template_6_specification_implementer.py) | Build from requirements doc | complete_function, blank_page | ⭐⭐ Moderate |
| 7 | [Prediction Challenger](template_7_prediction_challenger.py) | Predict before running | output_prediction | ⭐ Simple |
| 8 | [Progressive Unlocking](template_8_progressive_unlocking.py) | Gated content students activate | Complex multi-stage exercises | ⭐⭐ Moderate |
| 9 | [World Builder](template_9_world_builder.py) | Create interconnected systems | OOP, data structures | ⭐⭐⭐ Advanced |
| 10 | [Quality Auditor](template_10_quality_auditor.py) | Fix style/quality issues | fix_style | ⭐⭐ Moderate |
| 11 | [Batch Processor](template_11_batch_processor.py) | Operate on multiple items | Lists, loops, comprehensions | ⭐ Simple |
| 12 | [Resource Exchange](template_12_resource_exchange.py) | Trade/convert between types | Type conversion, calculations | ⭐ Simple |
| 13 | [Decision Tree](template_13_decision_tree.py) | Branch through conditional paths | Conditionals, dialog systems | ⭐⭐ Moderate |
| 14 | [Collection Builder](template_14_collection_builder.py) | Accumulate items into collection | Lists, sets, dicts | ⭐ Simple |
| 15 | [Table Tracer](template_15_table_tracer.py) | Track state changes in table | code_tracing | ⭐⭐ Moderate |

---

## Quick Selection Guide

### By Exercise Type

| Exercise Type | Recommended Templates |
|---------------|----------------------|
| `write_code` | 2 (Incremental Builder), 3 (Role Assignment), 9 (World Builder) |
| `complete_function` | 6 (Specification Implementer), 1 (Tutorial Guide) |
| `decode_error` | 4 (Forensic Debugger) |
| `bug_hunt` | 4 (Forensic Debugger) |
| `which_is_better` | 5 (Comparison Analyst) |
| `output_prediction` | 7 (Prediction Challenger) |
| `code_tracing` | 15 (Table Tracer) |
| `blank_page` | 6 (Specification Implementer), 9 (World Builder) |
| `simplify_code` | 10 (Quality Auditor), 5 (Comparison Analyst) |
| `fix_style` | 10 (Quality Auditor) |

### By Module

| Module | Common Patterns | Recommended Templates |
|--------|-----------------|----------------------|
| 0: Basics | Simple hello-world, print practice | 1, 3, 11 |
| 1: Turtle/Loops | Drawing patterns, repetition | 2, 11, 14 |
| 2: Decisions | Branching logic, conditionals | 3, 13, 7 |
| 3: Lists | Collection manipulation | 11, 14, 2 |
| 4: Games | Interactive systems | 9, 13, 3 |
| 5: Functions | Modular code design | 1, 6, 2 |
| 6: Mid Project | Integration projects | 9, 2, 8 |
| 7: Dictionaries | Key-value data | 3, 9, 14 |
| 8: Datetime/Errors | Real-world data handling | 4, 6, 7 |
| 9: OOP | Object systems | 9, 6, 1 |

### By Learning Objective

| Goal | Template |
|------|----------|
| Introduce new concept | 1 (Tutorial Guide) |
| Build confidence gradually | 8 (Progressive Unlocking) |
| Develop debugging skills | 4 (Forensic Debugger) |
| Practice code analysis | 5 (Comparison Analyst) |
| Apply professional standards | 6 (Specification Implementer), 10 (Quality Auditor) |
| Master predictions | 7 (Prediction Challenger), 15 (Table Tracer) |
| Create complex projects | 9 (World Builder), 2 (Incremental Builder) |

---

## How to Use Templates

### Step 1: Choose Template

1. Identify your Python concept (e.g., "dictionary methods")
2. Identify your exercise type (e.g., "complete_function")
3. Look up recommended template in tables above
4. Open the template file from this directory

### Step 2: Copy Template Structure

Copy the template's Python code structure. This includes:
- File docstring with context block placeholders
- Section separators
- Function definitions with ✏️ markers
- Comments with context block placeholders

### Step 3: Add Python Content

Fill in the actual Python code that teaches your concept:
- Replace `pass` with real implementations (for examples)
- Keep `pass` in student-editable sections
- Ensure technical accuracy

### Step 4: Define Context Blocks

For EACH theme you want to support, define values for all context blocks used in the template.

Add to `theme_variables.json`:
```json
{
  "your-theme-name": {
    "hero": "Character Name",
    "CONTEXT_INTRO": "Your intro narrative...",
    "CONTEXT_STUDENT_TASK": "Your task description...",
    // etc. for all blocks in template
  }
}
```

### Step 5: Test Across Themes

```bash
python scripts/convert_exercises.py --theme theme1
python scripts/convert_exercises.py --theme theme2
```

Verify narrative coherence in each theme.

---

## Template Conventions

All templates follow these conventions:

### Context Block Naming
- `{{CONTEXT_*}}`: Full sentences/paragraphs of narrative content
- `{{ENTITY_*}}`: Entity names (hero, item, school, etc.)
- `{{*_TITLE}}`: Section headings
- `{{*_DESCRIPTION}}`: Technical descriptions (stay consistent across themes)

### Section Structure
```python
# ============================================================
# {{SECTION_TITLE}}
# ============================================================
# {{CONTEXT_SECTION_NARRATIVE}}
#
# {{CONTEXT_SECTION_GUIDANCE}}
```

### Student Markers
- `# ✏️ YOUR CODE HERE ✏️` - General code writing
- `# ✏️ COMPLETE THIS FUNCTION ✏️` - Function completion
- `# ✏️ FIX THE CODE ✏️` - Debugging tasks
- `# ✏️ YOUR ANALYSIS ✏️` - Written analysis
- `# ✏️ YOUR PREDICTION ✏️` - Output prediction

### Docstrings
Technical docstrings (Args, Returns, Examples) should remain CONSISTENT across themes. Only narrative context changes.

---

## Context Block Best Practices

### Do:
✅ Write context blocks in second person ("You are...", "Your task...")
✅ Make blocks self-contained (readable without seeing code)
✅ Keep technical descriptions theme-neutral
✅ Provide clear success criteria
✅ Match tone to theme (formal fantasy, casual sports, etc.)

### Don't:
❌ Include Python code in context blocks
❌ Reference specific line numbers (code may change)
❌ Make blocks dependent on other blocks (each should work alone)
❌ Use theme-specific terms in block names (use CONTEXT_INTRO not CONTEXT_FANTASY_INTRO)
❌ Mix narrative and technical content in same block

### Example of Good Context Block:

**Fantasy:**
```
CONTEXT_INTRO: "Welcome to your first day at {{school}}! The Sorting Ceremony will determine which house becomes your new family."
```

**Sci-fi:**
```
CONTEXT_INTRO: "Welcome aboard {{school}}, Cadet. Division assignment protocols will determine which department you serve in."
```

**Sports:**
```
CONTEXT_INTRO: "Welcome to {{school}}, rookie! Position tryouts will determine which role you play on the team."
```

All three serve the same STRUCTURAL purpose (introduce categorization concept), but with appropriate narrative flavor.

---

## Template Combinations

Templates can be combined for complex exercises:

### Example: Tutorial Guide + Incremental Builder
```python
# Part 1: Show complete example (Template 1)
def example_complete_system():
    pass

# Part 2: Build piece by piece (Template 2)
def exercise_a_foundation():
    pass

def exercise_b_expansion():
    pass
```

### Example: Role Assignment + World Builder
```python
# Opening: Assign role (Template 3)
"""
{{CONTEXT_ROLE_INTRO}}
"""

# Main content: Build interconnected entities (Template 9)
def create_entity_1():
    pass

def entities_interact():
    pass
```

---

## Migration Checklist

When converting an existing exercise to use templates:

- [ ] Identify which template(s) match the exercise structure
- [ ] Copy template structure
- [ ] Preserve existing Python code logic
- [ ] Replace hardcoded narrative with context block placeholders
- [ ] Define context blocks for at least 2 themes
- [ ] Test generation with both themes
- [ ] Verify technical content is identical across themes
- [ ] Verify narrative is coherent in each theme
- [ ] Remove any remaining hardcoded references
- [ ] Update exercise documentation

---

## Getting Help

**Template doesn't match my exercise?**
- Check Template Combinations section
- Consider creating variant of closest template
- Consult `docs/NARRATIVE_TEMPLATE_SYSTEM_V2.md` for pattern analysis

**Context blocks too verbose?**
- Shorter blocks are fine! Blocks can be 1-2 sentences
- Some blocks can be identical across themes if truly universal
- Focus detail where themes diverge most

**Technical content changing between themes?**
- ❌ This means you have theme-specific Python code (problem!)
- Should only be narrative/context that changes
- Revisit exercise design to be more generic

---

## Contributing New Templates

To add a new template pattern:

1. Create `template_N_name.py` in this directory
2. Follow naming conventions (context blocks, markers, structure)
3. Add entry to this README in all tables
4. Document which modules/exercise types benefit
5. Provide example with 2+ themes showing it works

---

**Template Library Status:** ✅ 15 templates documented
**Next:** Create individual template files for templates 1-15
