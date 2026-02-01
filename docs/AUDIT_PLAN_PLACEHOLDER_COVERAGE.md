# Audit Plan: Theme Placeholder Coverage

Systematic assessment of placeholder usage across all exercises.

---

## Overview

**Goal:** Document which exercises have placeholders, which don't, and how they're used.

**Current State:**
- Total exercises: 145
- Exercises with placeholders: 90 (62%)
- Exercises without placeholders: 55 (38%)

**Critical Rule:** CLAUDE.md mandates "Every exercise must contain at least one placeholder"

---

## Audit Categories

### 1. Zero-Placeholder Identification

**Purpose:** Find all exercises violating the placeholder requirement.

**Method:**
```bash
find raw_exercises -name "*.py" -exec sh -c '
  if ! grep -q "{{" "$1"; then
    echo "$1"
  fi
' _ {} \;
```

**Documentation Format:**
```
File: raw_exercises/module_X/type/exercise_N_name.py
Module: module_X_topic
Type: exercise_type
Has Placeholders: NO
```

**Output:** List of 55 exercises without placeholders

---

### 2. Placeholder Appropriateness

**Purpose:** Assess how existing placeholders are used.

**Method:**
1. For each exercise with placeholders, extract all `{{variables}}`
2. Read exercise context
3. Note usage pattern (string literal, comment, variable name, etc.)
4. Check for common anti-patterns

**Anti-Patterns to Document:**
- Character names used as numeric values
- Items/creatures used as actions
- Mixed fantasy/real-world context
- Placeholder as variable name (not value)

**Documentation Format:**
```
File: raw_exercises/module_X/type/exercise_N.py
Placeholders Used: [list all {{vars}}]
Usage Pattern: [string/comment/other]
Issues Observed: [list any problems]
Notes: [context if needed]
```

**Output:** Appropriateness report for 90 exercises

---

### 3. Placeholder Distribution Statistics

**Purpose:** Understand usage patterns across the curriculum.

**Method:**
```bash
# Count each placeholder variable across all files
for var in hero heroine friend mentor villain school house spell1 spell2 spell3 spell4 creature pet location place item transport group exclamation greeting password; do
  count=$(grep -roh "{{$var}}" raw_exercises | wc -l)
  files=$(grep -rl "{{$var}}" raw_exercises | wc -l)
  echo "$var: $count uses in $files exercises"
done | sort -t: -k2 -rn
```

**Documentation Format:**
```
Placeholder: {{variable}}
Total Uses: X
Exercises: Y
Modules: [list which modules]
Frequency: [High/Medium/Low]
```

**Output:** Usage statistics table

---

### 4. Module-Level Analysis

**Purpose:** See placeholder patterns by module.

**Method:**
1. Group exercises by module
2. Count placeholder presence per module
3. Calculate percentage with placeholders
4. Note most/least used placeholders per module

**Documentation Format:**
```
Module: module_X_topic
Total Exercises: N
With Placeholders: X (Y%)
Without Placeholders: Z
Most Used: [top 3 placeholders]
Least Used: [bottom 3 placeholders]
```

**Output:** Per-module placeholder report

---

## Audit Execution

### Week 1: Zero-Placeholder Scan
**Days 1-2:** Run automated scan
**Days 3-5:** Manual verification and categorization

**Deliverable:** Complete list of exercises without placeholders

---

### Week 2: Appropriateness Review
**Days 1-3:** Read and document each exercise with placeholders
**Days 4-5:** Categorize issues and patterns

**Deliverable:** Appropriateness findings document

---

### Week 3: Statistical Analysis
**Days 1-2:** Generate placeholder usage counts
**Days 3-4:** Create distribution tables and charts
**Day 5:** Module-level aggregation

**Deliverable:** Statistics and distribution report

---

### Week 4: Documentation
**Days 1-3:** Compile all findings
**Days 4-5:** Create summary and observations

**Deliverable:** Final audit report

---

## Documentation Structure

Create in `docs/audits/placeholder_coverage/`:

1. **zero_placeholders.md** - List of 55 exercises
2. **appropriateness_findings.md** - Issues in existing usage
3. **usage_statistics.md** - Counts and distributions
4. **module_analysis.md** - Per-module breakdowns
5. **summary.md** - High-level findings

---

## Success Criteria

Audit is complete when:
- [ ] All 145 exercises scanned for placeholder presence
- [ ] Zero-placeholder list documented (55 exercises)
- [ ] Appropriateness reviewed for all 90 with placeholders
- [ ] Usage statistics generated for all placeholder variables
- [ ] Module-level analysis complete
- [ ] Findings documented without recommendations

---

## Tools

### Placeholder Detector Script
```bash
#!/bin/bash
# placeholder_audit.sh

echo "=== Exercises Without Placeholders ==="
find raw_exercises -name "*.py" -exec sh -c '
  if ! grep -q "{{" "$1"; then
    echo "$1"
  fi
' _ {} \;
```

### Placeholder Counter Script
```bash
#!/bin/bash
# count_placeholders.sh

find raw_exercises -name "*.py" -exec sh -c '
  count=$(grep -o "{{[^}]*}}" "$1" | sort -u | wc -l)
  if [ $count -gt 0 ]; then
    echo "$1: $count"
  fi
' _ {} \;
```

### Usage Extractor Script
```bash
#!/bin/bash
# extract_usage.sh

find raw_exercises -name "*.py" -exec grep -Ho "{{[^}]*}}" {} \; | \
  sed 's/.*{{/{{/' | \
  sort | uniq -c | sort -rn
```
