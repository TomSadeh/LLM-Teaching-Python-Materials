# Audit Plan: Missing Critical Content

Based on reference materials analysis and curriculum gap identification.

---

## Overview

**Goal:** Identify and prioritize missing topics, concepts, and exercise types that are present in standard Python curricula but absent from our materials.

**Scope:** All 10 modules + references analysis
**Timeline:** Phase 1 (Critical) → Phase 2 (Important) → Phase 3 (Nice-to-have)
**Current State:** 145 exercises across 10 modules, heavily weighted toward `write_code` type

---

## Phase 1: Critical Missing Exercise Types

These types are pedagogically essential and completely missing.

### 1.1 Code Tracing (0 exist, need 6-8)

**Why Critical:** Students can't debug without understanding execution flow.

**References Support:**
- Think Python: Emphasizes execution model understanding
- Research: Tracing exercises reduce "magic variable" misconceptions

**Needed Exercises:**

| Module | Exercise | Difficulty | Description |
|--------|----------|------------|-------------|
| module_1_turtle_loops | `trace_turtle_position.py` | 1 | Track (x,y) through forward/turn calls |
| module_2_decisions | `trace_if_else_flow.py` | 2 | Follow variables through branching |
| module_3_lists | `trace_list_mutations.py` | 2 | Track list changes in loops |
| module_4_games | `trace_game_state.py` | 2 | Track score/lives through game loop |
| module_7_dictionaries | `trace_dict_updates.py` | 2 | Follow dictionary modifications |
| module_9_oop | `trace_object_state.py` | 3 | Track object attributes through methods |

**Success Criteria:**
- [ ] Each exercise has 3-4 checkpoints asking "What are the values now?"
- [ ] Mix of print statements and variable inspection
- [ ] Progressive complexity within each module

---

### 1.2 Match Output (0 exist, need 4-6)

**Why Critical:** Fast pattern recognition, builds code reading fluency.

**References Support:**
- All three textbooks use "predict output" exercises early
- Research: Low cognitive load, high practice volume

**Needed Exercises:**

| Module | Exercise | Difficulty | Description |
|--------|----------|------------|-------------|
| module_0_basics | `match_print_statements.py` | 1 | Match code to printed output |
| module_1_turtle_loops | `match_turtle_paths.py` | 1 | Match code to drawn shapes |
| module_3_lists | `match_list_operations.py` | 2 | Match list methods to results |
| module_5_functions | `match_return_values.py` | 2 | Match function calls to returns |
| module_7_dictionaries | `match_dict_lookups.py` | 2 | Match key access to values |

**Success Criteria:**
- [ ] Multiple choice format (4 options)
- [ ] Include one "trick" option (common mistake)
- [ ] 5-8 questions per exercise
- [ ] Can be completed in <5 minutes

---

### 1.3 Fill Blanks (0 exist, need 4-6)

**Why Critical:** Syntax reinforcement, reduces "blank page anxiety."

**References Support:**
- Automate Boring Stuff: Heavy scaffolding early
- Research: Parsons problems (reordering/completion) effective for novices

**Needed Exercises:**

| Module | Exercise | Difficulty | Description |
|--------|----------|------------|-------------|
| module_0_basics | `fill_string_formatting.py` | 1 | Complete f-strings and format() |
| module_1_turtle_loops | `fill_loop_syntax.py` | 1 | Complete for loop structures |
| module_2_decisions | `fill_condition_syntax.py` | 2 | Complete if/elif/else |
| module_5_functions | `fill_function_syntax.py` | 2 | Complete def, parameters, return |
| module_7_dictionaries | `fill_dict_syntax.py` | 2 | Complete dict creation/access |
| module_9_oop | `fill_class_syntax.py` | 3 | Complete class definition |

**Success Criteria:**
- [ ] Blanks clearly marked with `___`
- [ ] Focus on one syntax element per exercise
- [ ] Hints available for each blank
- [ ] Gradual removal of scaffolding

---

## Phase 2: Important Missing Topics

These topics appear in all reference curricula but are absent from ours.

### 2.1 Tuples (0 exercises, need module or integration)

**References:**
- Think Python: Ch 12 (after lists/dicts)
- Python for Everybody: Ch 10 (with sorting)
- Automate: Implicitly with multiple assignment

**Options:**
1. Add to module_3_lists as "immutable sequences"
2. Add to module_7_dictionaries as "dict items"
3. Create lightweight integration exercises in existing modules

**Recommended:** Option 3 - Add tuple exercises to:
- module_3_lists: `write_code_tuple_packing.py`
- module_7_dictionaries: `write_code_items_iteration.py`
- module_5_functions: `write_code_multiple_returns.py`

---

### 2.2 File I/O (0 exercises)

**References:**
- Think Python: Ch 14 (before OOP)
- Python for Everybody: Ch 7 (early, with persistence)
- Automate: Ch 11-12 (with paths)

**Gap:** No file operations in any module

**Options:**
1. Add to module_8_modules as "file handling"
2. Create module_10_files
3. Add to module_6_final_project only

**Recommended:** Option 1 + Option 3:
- module_8_modules: Add 3 file exercises (read, write, append)
- module_6_final_project: Projects requiring file persistence

**Needed Exercises:**
- `write_code_read_file.py` - Read and process lines
- `write_code_write_file.py` - Save user data
- `add_error_handling_file_errors.py` - Handle missing files

---

### 2.3 String Methods (limited coverage)

**References:**
- All textbooks dedicate a chapter to string manipulation
- Our coverage: Implicit in module_0, not explicit

**Gap:** No dedicated string exercises beyond basics

**Needed Exercises:**
- module_0_basics: `write_code_string_methods.py`
- module_3_lists: `write_code_split_join.py`
- module_7_dictionaries: `write_code_character_count.py`

---

### 2.4 Exception Handling (0 exercises)

**References:**
- Python for Everybody: Ch 3 (early with try/except)
- Think Python: Ch 14 (with files)
- Automate: Debugging chapter

**Gap:** No try/except exercises

**Recommended Addition:**
- module_4_games: `add_error_handling_game_input.py`
- module_5_functions: `add_error_handling_validation.py`
- module_8_modules: `add_error_handling_file_io.py`

---

### 2.5 List Comprehensions (0 exercises)

**References:**
- All textbooks mention as "Pythonic" pattern
- Usually after loops + lists

**Gap:** No comprehension exercises

**Needed Exercises:**
- module_3_lists: `simplify_code_to_comprehension.py`
- module_7_dictionaries: `write_code_dict_comprehension.py`

---

## Phase 3: Advanced/Optional Topics

Topics that differentiate curricula but aren't universal.

### 3.1 Regex (mentioned in 2/3 textbooks)

**Status:** Not critical for beginner curriculum
**Recommendation:** Skip unless module_8 expanded

---

### 3.2 Recursion (Think Python emphasis)

**Status:** Advanced topic, not essential
**Recommendation:** Add 1 optional exercise to module_5_functions

---

### 3.3 Data Structures (sets, deque, defaultdict)

**Status:** Collections module partially covered
**Recommendation:** Add to module_8_modules if expanded

---

## Missing Exercise Type Summary

| Type | Priority | Exists | Needed | Target Modules |
|------|----------|--------|--------|----------------|
| code_tracing | HIGH | 0 | 6-8 | turtle, decisions, lists, games, dicts, oop |
| match_output | HIGH | 0 | 4-6 | basics, turtle, lists, functions, dicts |
| fill_blanks | HIGH | 0 | 4-6 | basics, turtle, decisions, functions, dicts, oop |
| bug_hunt | MEDIUM | 1 | 4-6 | turtle, decisions, lists, games |
| complete_function | MEDIUM | 5 | 3-5 | lists, functions, dicts |
| decode_error | MEDIUM | 4 | 2-3 | functions, dicts |
| code_ordering | MEDIUM | 1 | 2-3 | basics, functions |
| fix_style | MEDIUM | 2 | 3-4 | basics, functions, oop |
| simplify_code | MEDIUM | 3 | 3-4 | lists, functions, dicts |
| which_is_better | LOW | 4 | 2-3 | functions, dicts, oop |
| spot_difference | LOW | 3 | 2-3 | lists, functions |
| add_error_handling | LOW | 3 | 2-3 | games, functions, modules |
| blank_page | LOW | 3 | 2-3 | functions, final, oop |

---

## Audit Process

### Step 1: Topic Coverage Audit
- [ ] Review all references gap analyses
- [ ] List missing topics by priority
- [ ] Map topics to existing modules
- [ ] Identify topics requiring new modules

### Step 2: Exercise Type Distribution Audit
- [ ] Count current distribution by type
- [ ] Compare to pedagogical best practices
- [ ] Identify types completely missing
- [ ] Identify types under-represented

### Step 3: Difficulty Progression Audit
- [ ] Check each module has 1→2→3 progression
- [ ] Verify no jumps (1→3)
- [ ] Ensure variety at each level

### Step 4: Prioritization
- [ ] Rate each gap as HIGH/MEDIUM/LOW
- [ ] Estimate effort (Easy/Medium/Hard)
- [ ] Create implementation roadmap

### Step 5: Documentation
- [ ] Update EXERCISE_ADDITION_PLAN.md
- [ ] Update CATALOG.md with planned additions
- [ ] Create templates for new types if needed

---

## Success Metrics

**Completion Criteria:**
- [ ] All HIGH priority types have ≥4 exercises
- [ ] All modules have ≥3 exercise types
- [ ] File I/O covered (min 3 exercises)
- [ ] Exception handling covered (min 3 exercises)
- [ ] Tuples integrated into existing modules

**Quality Criteria:**
- [ ] Each exercise has theme placeholders
- [ ] Difficulty ratings accurate
- [ ] Clear learning objectives
- [ ] Hints system implemented

---

## Next Steps

1. Review this audit plan with stakeholders
2. Prioritize Phase 1 types for immediate creation
3. Schedule Phase 2 topic integration
4. Create new exercise templates if needed
5. Update tracking documents as exercises added
