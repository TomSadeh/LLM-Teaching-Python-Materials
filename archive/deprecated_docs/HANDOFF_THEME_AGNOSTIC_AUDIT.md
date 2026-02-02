# Handoff: Theme-Agnostic Exercise System Audit

## The Situation

**Good news:** A comprehensive three-layer system is already designed in [docs/NARRATIVE_SYSTEM.md](NARRATIVE_SYSTEM.md).

**The problem:** The exercises haven't been converted to use it, and `theme_variables.json` doesn't contain the context blocks yet.

## The Existing Three-Layer System

From NARRATIVE_SYSTEM.md:

### Layer 1: Entity Names (IMPLEMENTED)
```python
name = "{{hero}}"  # Harry / Captain Nova / Ronaldo / Alice
```
Simple string replacements. We have ~23 of these in `theme_variables.json`.

### Layer 2: Narrative Context Blocks (DESIGNED, NOT IMPLEMENTED)
```python
# {{CONTEXT_INTRO}}
# Fantasy: "Welcome to {{school}}! Before you can cast your own spells..."
# Sci-Fi:  "Welcome aboard {{school}}, Cadet! All crew must complete training..."
# Sports:  "Welcome to {{school}}, rookie! Before you hit the field..."
```
Full sentences/paragraphs that swap by genre. **These are documented but NOT in theme_variables.json yet.**

### Layer 3: Framework Concepts (DESIGNED, NOT IMPLEMENTED)
```python
# {{INSTITUTION_TYPE}}, {{CATEGORY_SYSTEM}}, {{ABILITY_TYPE}}
```
Structural elements that define universe rules.

## The 15 Universal Narrative Templates

Already documented in NARRATIVE_SYSTEM.md:

1. **Tutorial Guide** - Show example, then replicate
2. **Incremental Builder** - Build complex system piece by piece
3. **Role Assignment** - Student takes specific role
4. **Forensic Debugger** - Debug broken code (for bug_hunt, decode_error)
5. **Comparison Analyst** - Compare approaches (for which_is_better)
6. **Specification Implementer** - Build from spec (for complete_function, blank_page)
7. **Prediction Challenger** - Predict output (for output_prediction)
8. **Progressive Unlocking** - Gated content students unlock
9. **World Builder** - Create interconnected systems (for OOP)
10. **Quality Auditor** - Fix style issues (for fix_style, simplify_code)
11. **Batch Processor** - Same operation on multiple items
12. **Resource Exchange** - Trading/conversion
13. **Decision Tree** - Branching paths
14. **Collection Builder** - Accumulate items
15. **Table Tracer** - Track state changes (for code_tracing)

## What's Actually Missing

### 1. Context Blocks in theme_variables.json

The document defines ~50+ context block placeholders like:
- `{{CONTEXT_INTRO}}`
- `{{CONTEXT_STUDENT_TASK}}`
- `{{CONTEXT_INVESTIGATION_INTRO}}`
- `{{CONTEXT_WORLD_VISION}}`
- etc.

**None of these exist in theme_variables.json yet.** They need to be added for each theme.

### 2. Exercises Using the Templates

Current exercises use only Layer 1 (noun placeholders). They need to be rewritten to use the full template structure with context blocks.

### 3. Hybrid Exercise Format

Multi-part exercises that flow through different types (decode_error → bug_hunt → write_code) while maintaining a cohesive narrative via context blocks.

## The Goal

**ONE exercise file works perfectly with ANY theme:**

| Theme | Same Exercise Renders As |
|-------|--------------------------|
| Fantasy | "Cast the spell to unlock the door" |
| Sci-Fi | "Enter the access code to unlock the airlock" |
| Soccer | "Call the play to start the match" |
| Plain Coding | "Write the function to validate the input" |
| Detective | "Crack the code to open the safe" |

**The Python code is IDENTICAL. Only the context blocks change.**

## Audit Tasks

### Phase 1: Audit theme_variables.json

- [ ] List all Layer 1 placeholders currently in theme_variables.json
- [ ] Compare against context blocks defined in NARRATIVE_SYSTEM.md
- [ ] Identify which context blocks are missing
- [ ] Decide: Add to theme_variables.json OR to theme_mappings/*.json?

### Phase 2: Pick 3 Pilot Exercises to Convert

From NARRATIVE_SYSTEM.md suggested pilots:
- [ ] Module 7, Exercise 1 → Template 2 (Incremental Builder)
- [ ] Module 9, Exercise 8 → Template 9 (World Builder)
- [ ] Module 7, decode_error → Template 4 (Forensic Debugger)

For each:
- [ ] Rewrite using template structure with context block placeholders
- [ ] Add context block values for 3 themes (fantasy, sci-fi, plain coding)
- [ ] Test that exercise renders correctly in all 3 themes

### Phase 3: Create Hybrid Exercise Template

- [ ] Define hybrid exercise structure (multi-part, one narrative)
- [ ] Ensure each part uses appropriate narrative template
- [ ] Context blocks flow across parts (same story, different exercise types)
- [ ] Create one pilot hybrid for Module 2

### Phase 4: Full Conversion

Once pilots validated:
- [ ] Convert all 145 exercises to template system
- [ ] Populate context blocks for all themes
- [ ] Validate with automated script

## Example: Theme-Agnostic Hybrid Exercise

### The Exercise File (ONE file, works with ALL themes)

```python
"""
{{CONTEXT_HYBRID_INTRO}}
{{CONTEXT_HYBRID_OVERVIEW}}
"""

# ============================================================
# PART A: {{PART_A_TITLE}}
# ============================================================
# {{CONTEXT_PART_A_NARRATIVE}}
#
# ERROR MESSAGE:
# TypeError: 'NoneType' object is not subscriptable
#
# {{CONTEXT_PART_A_TASK}}

def part_a_broken():
    """Broken code to analyze."""
    access = None
    return access["granted"]  # 🐛 BUG

# ✏️ What's wrong? Write your explanation:
# ________________________________________________

# ============================================================
# PART B: {{PART_B_TITLE}}
# ============================================================
# {{CONTEXT_PART_B_NARRATIVE}}

def part_b_buggy(password):
    if password = "{{password}}":  # 🐛 BUG: = vs ==
        return True
    return False

def part_b_fixed(password):
    # ✏️ FIX THE BUG ✏️
    pass

# ============================================================
# PART C: {{PART_C_TITLE}}
# ============================================================
# {{CONTEXT_PART_C_NARRATIVE}}

def part_c_complete(password, has_key, is_member):
    """
    {{PART_C_SPEC}}

    Returns True if access granted, False otherwise.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass

def main():
    print("{{CONTEXT_HYBRID_START}}")
    # Run all parts
    print("{{CONTEXT_HYBRID_COMPLETE}}")

main()
```

### Context Blocks by Theme (in theme_variables.json)

**Fantasy (dumblecode):**
```json
{
  "CONTEXT_HYBRID_INTRO": "The entrance to {{school}} has been sabotaged!",
  "PART_A_TITLE": "The Frozen Gate",
  "CONTEXT_PART_A_NARRATIVE": "{{mentor}} shows you the broken spell...",
  "PART_B_TITLE": "Emergency Repairs",
  "PART_C_TITLE": "Grand Reopening",
  "PART_C_SPEC": "Grant access if: password matches OR (has_key AND is_member)"
}
```

**Sci-Fi (cepheus):**
```json
{
  "CONTEXT_HYBRID_INTRO": "The airlock on {{school}} is malfunctioning!",
  "PART_A_TITLE": "System Crash Analysis",
  "CONTEXT_PART_A_NARRATIVE": "The Chief Engineer shows you the error log...",
  "PART_B_TITLE": "Debug Protocol",
  "PART_C_TITLE": "Security Restoration",
  "PART_C_SPEC": "Grant access if: code matches OR (has_keycard AND is_crew)"
}
```

**Plain Coding (pymentor):**
```json
{
  "CONTEXT_HYBRID_INTRO": "This authentication module has bugs.",
  "PART_A_TITLE": "Understanding the Error",
  "CONTEXT_PART_A_NARRATIVE": "Read the error message and identify the problem.",
  "PART_B_TITLE": "Fix the Bug",
  "PART_C_TITLE": "Complete Implementation",
  "PART_C_SPEC": "Grant access if: password matches OR (has_key AND is_member)"
}
```

**THE PYTHON CODE IS IDENTICAL. Only context blocks change.**

## Key Principle

> **The theme is the flavor, not the meal.**
>
> Students learn `if/elif/else` regardless of whether they're "casting spells" or "running security checks". The narrative makes it engaging, but the LEARNING is theme-independent.

## Key Files

| File | Purpose | Status |
|------|---------|--------|
| [docs/NARRATIVE_SYSTEM.md](NARRATIVE_SYSTEM.md) | **THE DESIGN DOC** - Three-layer system, 15 templates | Complete |
| [TEMPLATE.md](../TEMPLATE.md) | Layer 1 placeholder list | Has nouns only |
| [theme_variables.json](../theme_variables.json) | Placeholder values by theme | Has nouns only, needs context blocks |
| [theme_mappings/*.json](../theme_mappings/) | Extended theme variables | Partial, may have some context blocks |
| [templates/activity_patterns/](../templates/activity_patterns/) | 15 template structures | Reference only, not used by exercises |
| [raw_exercises/](../raw_exercises/) | 145 exercises | Need conversion to use templates |

## Success Criteria

1. **Any exercise** can be rendered in **any theme** with zero code changes
2. **Hybrid exercises** flow naturally across parts in any theme
3. **New themes** can be added with just a JSON file (no exercise changes)
4. **Plain coding theme** works perfectly (no forced narrative)
5. **Validation script** can verify theme-agnosticism automatically

## Immediate Next Steps

### Step 1: Audit theme_variables.json
Check what context blocks (Layer 2) already exist vs what NARRATIVE_SYSTEM.md defines.

### Step 2: Pick ONE Pilot Exercise
Convert a single exercise to the full template system:
- Use template structure from `templates/activity_patterns/`
- Add context blocks to `theme_variables.json` for 3 themes
- Verify it renders correctly in all 3 themes

### Step 3: Create ONE Pilot Hybrid
Create a multi-part exercise (3 parts) using the hybrid format:
- decode_error → bug_hunt → write_code
- One cohesive narrative via context blocks
- Test with 3 themes

### Step 4: Document and Scale
Once pilots work:
- Document the conversion process
- Create remaining exercises using the system

---

## Reference: Context Block Categories (from NARRATIVE_SYSTEM.md)

The document defines these context block categories:

**Introduction & Framing:** `{{CONTEXT_INTRO}}`, `{{CONTEXT_PROJECT_INTRO}}`, `{{CONTEXT_ROLE_INTRO}}`, etc.

**Learning Objectives:** `{{CONTEXT_LEARNING_OBJECTIVE}}`, `{{CONTEXT_PREDICTION_PURPOSE}}`, etc.

**Narrative Context:** `{{CONTEXT_EXAMPLE_NARRATIVE}}`, `{{CONTEXT_PHASE_N}}`, `{{CONTEXT_CASE_N_NARRATIVE}}`, etc.

**Tasks & Instructions:** `{{CONTEXT_STUDENT_TASK}}`, `{{CONTEXT_ROLE_RESPONSIBILITIES}}`, etc.

**Guidance & Support:** `{{CONTEXT_SUCCESS_CRITERIA}}`, `{{CONTEXT_IMPLEMENTATION_GUIDANCE}}`, etc.

**Results & Completion:** `{{CONTEXT_INTEGRATION}}`, `{{CONTEXT_FINAL_ASSEMBLY}}`, `{{CONTEXT_ROLE_COMPLETE}}`, etc.

See NARRATIVE_SYSTEM.md "Context Block Library" section for complete list.

---

*This document serves as a handoff for completing the theme-agnostic exercise system. The design exists - we need to implement it.*
