# Audit Plan: Missing Critical Content

Identify pedagogical gaps by comparing against reference curricula.

---

## Overview

**Goal:** Document what's missing from our curriculum compared to standard Python teaching resources.

**Scope:** All 10 modules + analysis of 3 reference curricula
**Method:** Compare, document gaps, categorize by priority
**Output:** Gap analysis reports, no implementation recommendations

**Current State:** 145 exercises across 10 modules, heavily weighted toward `write_code` type

---

## Audit Categories

### 1. Exercise Type Distribution

**Purpose:** Identify which pedagogically valuable exercise types are missing or underrepresented.

**Method:**
1. List all exercise types from reference curricula
2. Count current distribution across modules
3. Identify types with 0 exercises
4. Identify types with <3 exercises
5. Note which modules lack type diversity

**Documentation Format:**
```
Type: [exercise_type]
Current Count: X exercises across Y modules
Reference Frequency: [Common/Occasional/Rare] in curricula
Modules Present: [list]
Modules Absent: [list]
Priority: [To be determined after analysis]
```

**Output:** Exercise type gap matrix

---

### 2. Topic Coverage

**Purpose:** Document Python concepts present in references but absent from our curriculum.

**Method:**
1. Extract topic lists from each reference curriculum
2. Map topics to our modules
3. Identify unmapped topics
4. Note topics mentioned in 2+ references

**Documentation Format:**
```
Topic: [e.g., "File I/O", "Exception Handling", "Tuples"]
References Mentioning: [Think Python Ch X, Python for Everybody Ch Y, etc.]
Our Coverage: [None/Minimal/Partial/Complete]
Notes: [Context about how references teach this]
```

**Output:** Topic coverage report

---

### 3. Difficulty Progression

**Purpose:** Check if modules have appropriate difficulty curves.

**Method:**
1. Map difficulty ratings (1-3) per exercise
2. Check for gaps (e.g., jump from 1→3)
3. Verify each module has range of difficulties
4. Note modules with only one difficulty level

**Documentation Format:**
```
Module: module_X_topic
Difficulty 1: X exercises
Difficulty 2: Y exercises
Difficulty 3: Z exercises
Issues: [e.g., "No difficulty 2", "Jump from 1 to 3"]
```

**Output:** Difficulty distribution report

---

## Audit Process

### Phase 1: Data Collection (Week 1)
- [ ] Review reference curricula gap analyses
- [ ] Count exercises by type per module
- [ ] Extract topic lists from each reference
- [ ] Map topics to current modules

### Phase 2: Gap Analysis (Week 2)
- [ ] Identify exercise types with 0 count
- [ ] Identify topics present in references but not ours
- [ ] Check difficulty progression in each module
- [ ] Document type distribution patterns

### Phase 3: Categorization (Week 3)
- [ ] Group findings by category
- [ ] Note frequency in references (universal vs. occasional)
- [ ] Identify patterns across modules
- [ ] Cross-reference with pedagogy research

### Phase 4: Documentation (Week 4)
- [ ] Create gap analysis reports
- [ ] Generate statistics and matrices
- [ ] Summarize findings
- [ ] No recommendations - just facts

---

## Output Documents

All findings will be documented in `docs/audits/missing_content/`:

1. **exercise_type_matrix.md** - Count of each type per module
2. **topic_coverage_report.md** - Topics from references vs. ours
3. **difficulty_analysis.md** - Progression check per module
4. **summary_findings.md** - High-level overview

---

## Success Criteria

Audit is complete when:
- [ ] All exercise types counted and categorized
- [ ] All reference topics extracted and mapped
- [ ] Difficulty progression analyzed for each module
- [ ] Findings documented in structured format
- [ ] No recommendations or solutions proposed
