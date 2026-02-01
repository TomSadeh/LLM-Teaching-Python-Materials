# Audit Plan: Theme Placeholder Coverage

Systematic audit of all exercises to ensure proper theme variable usage.

---

## Overview

**Goal:** Ensure every exercise contains at least one theme placeholder and uses them appropriately.

**Current State:**
- Total exercises: 145
- Exercises with placeholders: 90 (62%)
- Exercises without placeholders: 55 (38%)

**Critical Issue:** CLAUDE.md mandates "Every exercise must contain at least one placeholder" but 38% violate this rule.

---

## Audit Criteria

### Rule 1: Minimum Coverage ⚠️ BLOCKING
Every exercise MUST have at least one `{{placeholder}}`.

**Why:** Dynamic theming is core to engagement. Exercises without placeholders break the theme immersion.

### Rule 2: Appropriate Selection
Placeholders should match the exercise context.

**Good:**
```python
# Print a greeting to {{hero}}
print(f"Welcome, {{hero}}!")
```

**Bad:**
```python
# Calculate area of rectangle
width = {{hero}}  # Wrong - hero is a name, not a number
```

### Rule 3: Consistency Within Exercise
If an exercise introduces a character/item, keep using it.

**Good:**
```python
# Exercise 1: Create variable for {{hero}}
hero_name = "{{hero}}"

# Exercise 2: Print {{hero}}'s greeting
print(f"{hero_name} says: {{greeting}}")
```

**Bad:**
```python
# Exercise 1: Create variable for {{hero}}
hero_name = "{{hero}}"

# Exercise 2: Print villain's greeting  ← Lost consistency
print(f"{villain_name} says: {{greeting}}")
```

### Rule 4: Simplicity Over Quantity
Use 1-3 placeholders per exercise, not all 30+.

**Good:**
```python
# {{hero}} learns {{spell1}}
```

**Bad:**
```python
# {{hero}} meets {{heroine}} at {{school}} in {{house}}
# with {{friend}} and {{mentor}} to fight {{villain}} using
# {{spell1}}, {{spell2}}, {{spell3}}, and {{spell4}}
```

---

## Phase 1: Identify Zero-Placeholder Exercises

**Priority:** CRITICAL - These break the theme system.

### Audit Process

```bash
# Find all exercises without placeholders
find raw_exercises -name "*.py" -type f -exec sh -c '
  if ! grep -q "{{" "$1"; then
    echo "$1"
  fi
' _ {} \;
```

### Documentation Format

For each exercise without placeholders:

```
File: raw_exercises/module_X/type/exercise_N_name.py
Topic: [e.g., "variables", "loops", "functions"]
Current Content: [Brief description]
Suggested Placeholders: [{{placeholder1}}, {{placeholder2}}]
Rationale: [Why these placeholders fit]
Priority: [CRITICAL/HIGH/MEDIUM]
```

### Expected Output

Create `PLACEHOLDER_AUDIT_ZERO.md` with all 55 exercises that need placeholders added.

---

## Phase 2: Audit Placeholder Appropriateness

**Priority:** HIGH - Incorrect placeholders break immersion.

### Common Anti-Patterns

#### 2.1 Using Character Names for Numbers

**Wrong:**
```python
age = {{hero}}  # hero is "Harry Potter", not a number
```

**Right:**
```python
hero_name = "{{hero}}"
```

#### 2.2 Using Items for Actions

**Wrong:**
```python
spell_power = {{creature}}  # creature is "hippogriff", not a power level
```

**Right:**
```python
creature_name = "{{creature}}"
```

#### 2.3 Mixed Theme Context

**Wrong:**
```python
# Welcome to {{school}}
# Please enter your email address  ← Breaks fantasy theme
```

**Right:**
```python
# Welcome to {{school}}
# Please state your {{house}} affiliation
```

### Audit Process

For each exercise WITH placeholders, check:
- [ ] Are placeholders used as strings (not numbers)?
- [ ] Do placeholders fit the context (fantasy names in fantasy scenarios)?
- [ ] Are placeholders consistent throughout the exercise?

### Documentation Format

```
File: raw_exercises/module_X/type/exercise_N_name.py
Current Usage: [List placeholders used]
Issue: [Describe problem]
Suggested Fix: [Corrected usage]
Priority: [HIGH/MEDIUM/LOW]
```

---

## Phase 3: Improve Placeholder Flow and Logic

**Priority:** MEDIUM - Enhance engagement and narrative coherence.

### What is "Flow"?

Good flow means placeholders create a mini-narrative that:
1. Makes logical sense
2. Follows a clear progression
3. Relates to the programming concept

### Examples

#### Poor Flow (disconnected)
```python
# Exercise 1: Print {{hero}}
print("{{hero}}")

# Exercise 2: Print {{villain}}  ← No connection
print("{{villain}}")

# Exercise 3: Print {{creature}}  ← Random
print("{{creature}}")
```

#### Good Flow (narrative progression)
```python
# Exercise 1: {{hero}} arrives at {{school}}
print("{{hero}} arrives at {{school}}")

# Exercise 2: {{hero}} meets {{friend}}
print("{{hero}} meets {{friend}}")

# Exercise 3: {{hero}} learns {{spell1}}
print("{{hero}} learns {{spell1}}")
```

### Audit Criteria

For each module's exercises (as a set):
- [ ] Do placeholders tell a mini-story?
- [ ] Does the story follow the module's theme?
- [ ] Are transitions between exercises logical?

### Example Flows by Module

#### module_0_basics: First Day at School
- Ex 1: Arrival → `{{hero}}`, `{{school}}`
- Ex 2: Meeting friends → `{{friend}}`, `{{greeting}}`
- Ex 3: Getting supplies → `{{item}}`, `{{place}}`

#### module_1_turtle_loops: Drawing Class
- Ex 1: First shape → `{{spell1}}` creates shape
- Ex 2: Colored patterns → Use `{{house}}` colors
- Ex 3: Complex design → `{{creature}}` drawing

#### module_2_decisions: Choices and Consequences
- Ex 1: House sorting → `{{house}}` selection
- Ex 2: Facing challenge → `{{villain}}` encounter
- Ex 3: Using abilities → `{{spell1}}` vs `{{spell2}}`

#### module_4_games: Adventures and Battles
- Ex 1: Quest setup → `{{hero}}`, `{{location}}`
- Ex 2: Combat system → `{{spell1}}`, `{{spell2}}`
- Ex 3: Victory/defeat → `{{exclamation}}`

### Documentation Format

```
Module: module_X_topic
Current Flow: [Describe existing placeholder narrative]
Issues:
  - [Issue 1: e.g., "No coherent story"]
  - [Issue 2: e.g., "Placeholders seem random"]
Suggested Flow: [Describe improved narrative]
Changes Required:
  - [File 1: Change X to Y]
  - [File 2: Change A to B]
Priority: [HIGH/MEDIUM/LOW]
```

---

## Phase 4: Placeholder Distribution Analysis

**Priority:** LOW - Statistical overview for future planning.

### Metrics to Track

For each placeholder variable:
- Total usage count across all exercises
- Usage by module
- Usage by exercise type

### Questions to Answer

1. Are some placeholders overused? (e.g., `{{hero}}` in 80% of exercises)
2. Are some placeholders underused? (e.g., `{{transport}}` in 1 exercise)
3. Do certain modules lack variety?
4. Do certain exercise types need specific placeholder patterns?

### Output Format

Create `PLACEHOLDER_STATS.md`:

```markdown
# Placeholder Usage Statistics

## Overall Distribution

| Placeholder | Total Uses | % of Exercises | Most Used In |
|-------------|-----------|----------------|--------------|
| {{hero}} | 65 | 45% | basics, games |
| {{spell1}} | 42 | 29% | turtle, decisions |
| ... | ... | ... | ... |

## By Module

### module_0_basics (23 exercises)
- {{hero}}: 18 (78%)
- {{school}}: 12 (52%)
- ...

## Recommendations
- Increase diversity in module_0 (too hero-heavy)
- Underutilized: {{transport}}, {{password}}, {{pet}}
- Consider module-specific placeholder sets
```

---

## Audit Execution Plan

### Week 1: Zero-Placeholder Audit (Phase 1)
**Day 1-2: Run automated scan**
```bash
find raw_exercises -name "*.py" -type f -exec sh -c '
  if ! grep -q "{{" "$1"; then
    echo "$1" >> zero_placeholders.txt
  fi
' _ {} \;
```

**Day 3-5: Manual review of each file**
- Read exercise content
- Identify natural placeholder opportunities
- Document in `PLACEHOLDER_AUDIT_ZERO.md`

**Deliverable:** List of 55 exercises needing placeholders

---

### Week 2: Appropriateness Audit (Phase 2)
**Day 1-3: Review all 90 exercises with placeholders**
- Check for anti-patterns
- Verify placeholder types match usage
- Document issues in `PLACEHOLDER_AUDIT_ISSUES.md`

**Day 4-5: Prioritize fixes**
- Rate each issue (HIGH/MEDIUM/LOW)
- Create fix recommendations
- Estimate effort

**Deliverable:** Issues list with priorities

---

### Week 3: Flow Analysis (Phase 3)
**Day 1-2: Module-by-module narrative review**
- Map placeholder usage across exercises
- Identify disconnects or random selections
- Sketch ideal narrative flow

**Day 3-5: Document improvements**
- Create flow diagrams per module
- Write specific change recommendations
- Note which exercises need reordering

**Deliverable:** `PLACEHOLDER_FLOW_IMPROVEMENTS.md`

---

### Week 4: Distribution Analysis (Phase 4)
**Day 1-2: Generate statistics**
```bash
# Count each placeholder across all files
for var in hero heroine friend mentor villain school house spell1 spell2 spell3 spell4 creature pet location place item transport group exclamation greeting password; do
  count=$(grep -r "{{$var}}" raw_exercises | wc -l)
  echo "$var: $count"
done
```

**Day 3-4: Analysis and recommendations**
- Identify overused/underused placeholders
- Check module-specific patterns
- Write recommendations

**Deliverable:** `PLACEHOLDER_STATS.md`

---

## Tools and Scripts

### Placeholder Detection Script

```bash
#!/bin/bash
# placeholder_audit.sh

echo "=== Zero Placeholder Exercises ==="
find raw_exercises -name "*.py" -exec sh -c '
  if ! grep -q "{{" "$1"; then
    echo "$1"
  fi
' _ {} \;

echo ""
echo "=== Placeholder Count by Exercise ==="
find raw_exercises -name "*.py" -exec sh -c '
  count=$(grep -o "{{[^}]*}}" "$1" | sort -u | wc -l)
  if [ $count -gt 0 ]; then
    echo "$1: $count unique placeholders"
  fi
' _ {} \;
```

### Placeholder Extractor

```bash
#!/bin/bash
# extract_placeholders.sh

find raw_exercises -name "*.py" -exec grep -o "{{[^}]*}}" {} \; | sort | uniq -c | sort -rn
```

---

## Success Criteria

### Phase 1 Complete When:
- [ ] All 55 zero-placeholder exercises documented
- [ ] Placeholder suggestions provided for each
- [ ] Priority ratings assigned

### Phase 2 Complete When:
- [ ] All 90 existing exercises reviewed
- [ ] Anti-patterns identified and documented
- [ ] Fix recommendations written

### Phase 3 Complete When:
- [ ] Each module has narrative flow documented
- [ ] Placeholder improvements suggested
- [ ] Implementation priority set

### Phase 4 Complete When:
- [ ] Statistical analysis complete
- [ ] Usage patterns identified
- [ ] Recommendations for future exercises written

---

## Output Documents

All audit results will be documented in:

1. `PLACEHOLDER_AUDIT_ZERO.md` - Exercises missing placeholders
2. `PLACEHOLDER_AUDIT_ISSUES.md` - Inappropriate placeholder usage
3. `PLACEHOLDER_FLOW_IMPROVEMENTS.md` - Narrative flow enhancements
4. `PLACEHOLDER_STATS.md` - Usage statistics and analysis

These will be created in `docs/audits/` directory.
