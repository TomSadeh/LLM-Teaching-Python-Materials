# Handoff: Hybrid Exercise Template System

**Status:** Design needed
**Priority:** High - Blocks module recreation
**Complexity:** High - Most complex template challenge in the system

---

## The Challenge

Hybrid exercises combine 2-4 exercise types into a single file with a **narrative arc**. This is NOT just about sequencing exercise types in a "proper coding workflow" - the **narrative is equally important** as the exercise combination.

Current state: We have task-level templates (15) and exercise-level templates (6), but no system for designing hybrid exercises that weave narrative and exercise types together meaningfully.

---

## What Needs to Be Designed

### 1. Narrative Arc Templates

Hybrid exercises need story structures independent of exercise types. These are the **dramatic shapes** of the learning experience.

**Potential Narrative Arcs:**

| Arc Name | Shape | Emotional Journey |
|----------|-------|-------------------|
| **The Build** | Foundation → Walls → Roof → Decoration | Pride in creation |
| **The Mystery** | Discovery → Investigation → Revelation → Resolution | Curiosity → Satisfaction |
| **The Journey** | Departure → Trials → Transformation → Return | Growth and mastery |
| **The Rescue** | Crisis → Assessment → Action → Success | Urgency → Relief |
| **The Competition** | Challenge → Struggle → Breakthrough → Victory | Tension → Triumph |
| **The Apprenticeship** | Observe → Assist → Solo → Master | Guided to independent |
| **The Repair** | Broken system → Diagnosis → Fix → Improvement | Frustration → Accomplishment |
| **The Evolution** | Version 1 → Feedback → Version 2 → Polish | Iteration mindset |

**Key insight:** The narrative arc is about *how the student feels* through the exercise, not just what they do.

### 2. Exercise Type Sequences

Separately from narrative, we need valid **exercise type combinations** that work pedagogically.

**Valid Sequences (examples):**

| Sequence ID | Types | Learning Flow |
|-------------|-------|---------------|
| `understand-extend-debug` | output_prediction → write_code → bug_hunt | Read → Build → Fix |
| `trace-write-compare` | code_tracing → write_code → which_is_better | Analyze → Create → Evaluate |
| `spec-implement-test` | complete_function → write_code → decode_error | Contract → Code → Verify |
| `example-practice-create` | fill_blanks → write_code → blank_page | Scaffold → Guided → Independent |
| `diagnose-fix-improve` | decode_error → bug_hunt → simplify_code | Find → Fix → Refactor |
| `design-build-compare` | output_prediction → write_code → which_is_better | Plan → Execute → Reflect |

**Constraints by module:** Not all sequences work in all modules (e.g., `complete_function` requires functions from module 5+).

### 3. The Combination Matrix

A hybrid template = **Narrative Arc × Exercise Type Sequence × Theme**

```
┌─────────────────────────────────────────────────────────────┐
│                    HYBRID TEMPLATE                          │
│                                                             │
│  Narrative Arc: "The Build"                                 │
│  Exercise Sequence: understand-extend-debug                 │
│  Theme: {{theme_variables}}                                 │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ PART 1: "Lay the Foundation"                        │   │
│  │ Narrative: You discover an existing {{item}} system │   │
│  │ Exercise Type: output_prediction                    │   │
│  │ Task: Understand what's already built               │   │
│  └─────────────────────────────────────────────────────┘   │
│                         ↓                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ PART 2: "Raise the Walls"                           │   │
│  │ Narrative: Time to add your own features            │   │
│  │ Exercise Type: write_code                           │   │
│  │ Task: Extend the system                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                         ↓                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ PART 3: "Inspect and Repair"                        │   │
│  │ Narrative: {{mentor}} found issues in another copy  │   │
│  │ Exercise Type: bug_hunt                             │   │
│  │ Task: Find and fix the problems                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  CLOSING: "{{hero}}'s {{item}} system is complete!"         │
└─────────────────────────────────────────────────────────────┘
```

---

## Design Questions to Resolve

### Narrative Questions

1. **How many narrative arc templates do we need?**
   - Too few: Exercises feel repetitive
   - Too many: Maintenance burden, inconsistent quality

2. **How does narrative map to exercise parts?**
   - 1:1 (one narrative beat per exercise type)?
   - Or more flexible (narrative can span multiple parts)?

3. **How themed should narratives be?**
   - Generic arcs with {{placeholders}}?
   - Or theme-specific arc variants?

4. **What's the emotional design goal?**
   - Should every hybrid feel like an accomplishment?
   - Should some be deliberately challenging/frustrating then resolved?

### Exercise Combination Questions

1. **How many valid sequences exist?**
   - Need to enumerate all pedagogically sound combinations
   - Some types don't work together (e.g., two output_predictions in a row)

2. **Should sequences be fixed or flexible?**
   - Fixed: Easier to template, more consistent
   - Flexible: More creative freedom, harder to maintain

3. **How long should each part be?**
   - Should parts be roughly equal?
   - Or should some be longer (build phase) vs shorter (debug phase)?

4. **Module constraints:**
   - Which sequences are valid at each curriculum point?
   - Need a matrix of sequence × module compatibility

### Integration Questions

1. **How do students know they're in a hybrid vs isolated exercise?**
   - Visual markers? Duration estimate? Part numbers?

2. **Can students skip parts or do them out of order?**
   - Or is the sequence enforced?

3. **How does grading/completion work?**
   - Per-part? Overall? Partial credit?

4. **How do hybrids appear in the exercise list?**
   - Single entry with parts? Or multiple linked entries?

---

## Proposed Deliverables

### Phase 1: Foundation (This Handoff)
- [x] Define the challenge
- [x] Identify key design decisions
- [ ] Get stakeholder input on questions above

### Phase 2: Narrative Arc Library
- [ ] Design 6-8 narrative arc templates
- [ ] Define emotional journey for each
- [ ] Create part-by-part narrative beat structure
- [ ] Add theme placeholders

### Phase 3: Exercise Sequence Catalog
- [ ] Enumerate all valid 2-type sequences
- [ ] Enumerate all valid 3-type sequences
- [ ] Enumerate all valid 4-type sequences
- [ ] Map sequences to module availability

### Phase 4: Combination System
- [ ] Design the combination matrix format
- [ ] Create tooling to generate hybrid from arc + sequence + theme
- [ ] Define part duration guidelines
- [ ] Create validation rules

### Phase 5: Template Files
- [ ] Create narrative arc template files
- [ ] Create example hybrids for each arc
- [ ] Document the combination process
- [ ] Test with multiple themes

---

## File Structure Proposal

```
templates/
├── activity_patterns/            # Task-level narrative patterns
├── structure_patterns/           # Multi-task organization patterns
├── exercise_types/               # Exercise type templates
├── hybrid_templates/             # NEW: Hybrid-specific templates
│   ├── README.md                 # This becomes the guide
│   ├── narrative_arcs/           # Story structure templates
│   │   ├── arc_the_build.md
│   │   ├── arc_the_mystery.md
│   │   ├── arc_the_journey.md
│   │   └── ...
│   ├── exercise_sequences/       # Valid type combinations
│   │   ├── seq_understand_extend_debug.md
│   │   ├── seq_spec_implement_test.md
│   │   └── ...
│   └── examples/                 # Complete hybrid examples
│       ├── hybrid_example_build_inventory.py
│       ├── hybrid_example_mystery_debug.py
│       └── ...
```

---

## Module Structure Update

Per conversation, the module structure should be:

| Order | Module | Purpose |
|:-----:|--------|---------|
| 0 | module_0_basics | Fundamentals |
| 1 | module_1_turtle_loops | Visual loops |
| 2 | module_2_decisions | Conditionals |
| 3 | module_3_lists | Collections |
| 4 | module_4_games | While loops |
| 5 | module_5_functions | Abstraction |
| 6 | **module_6_mid_project** | Mid-curriculum integration |
| 7 | module_7_dictionaries | Key-value data |
| 8 | module_8_modules | Standard library |
| 9 | module_9_oop | Object-oriented |
| 10 | **module_10_mega_project** | Full curriculum integration |

**mid_project:** Integration of modules 0-5 (basics through functions)
**mega_project:** Integration of everything (modules 0-9)

---

## Why This Is Hard

1. **Combinatorial explosion:** 8 arcs × 20 sequences × 5 themes = 800 possible hybrids
2. **Quality vs quantity:** Need enough variety without creating maintenance nightmare
3. **Coherence:** Arc + sequence + theme must feel unified, not bolted together
4. **Curriculum constraints:** Different modules allow different combinations
5. **Narrative craft:** Good story structure requires careful writing, not just templates

---

## Recommendation

Before creating the hybrid template system, we should:

1. **Create 3-5 hand-crafted hybrid examples** across different modules
2. **Identify what made them good** (extract patterns)
3. **Then** generalize into templates

Starting with templates risks creating soulless exercises. Starting with great examples and extracting patterns gives us templates that actually work.

---

## Open Questions for Stakeholder

1. How important is variety? (Can we reuse narrative arcs across modules?)
2. Should hybrids have a consistent "feel" or surprise students?
3. What's the time budget for hybrid design? (This is significant work)
4. Are there existing exercises we love that could inform the arc/sequence design?

---

**Next Action:** Review this handoff, make decisions on open questions, then proceed to Phase 2.
