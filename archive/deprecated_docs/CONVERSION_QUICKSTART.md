# Conversion System Quick Start

**Last Updated:** 2026-02-01
**Status:** ✅ Production Ready

---

## Overview

The conversion system transforms 145 existing Python exercises from hardcoded Harry Potter themes to a universal template system that works with any genre (fantasy, sci-fi, sports, music, business, etc.).

**Current Status:**
- ✅ Script production-ready
- ✅ 100% accuracy on pilot exercises
- ✅ All critical bugs fixed
- 🔄 Full corpus analysis in progress

---

## Quick Commands

### Single Exercise Analysis

```bash
python scripts/convert_to_templates.py \
  --input "exercises/module_7_dictionaries/complete_function/exercise_1.py" \
  --dry-run
```

**Output:** Console report showing:
- Template match (with confidence %)
- Hardcoded references found
- Context blocks created
- Manual review recommendation

### Module Batch Analysis

```bash
python scripts/convert_to_templates.py \
  --module 7 \
  --dry-run \
  --report-dir conversion_reports
```

**Output:**
- Console summary of all exercises in module
- JSON report per exercise in `conversion_reports/`
- Master summary: `conversion_reports/module_7_summary.json`

### Full Corpus Analysis

```bash
python scripts/convert_to_templates.py \
  --all \
  --dry-run \
  --report-dir conversion_reports_full
```

**Output:**
- Analysis of all 145 exercises
- Comprehensive statistics report
- Template distribution analysis
- Hardcoded reference inventory

---

## What the Script Does

### 1. Exercise Analysis
- Identifies module and exercise type
- Counts functions, classes, code complexity
- Extracts metadata from file structure

### 2. Template Matching
Matches exercise to one of 15 universal templates:

| Template | Best For | Confidence |
|----------|----------|------------|
| template_1_blank_canvas | Write from scratch | 100% (exact match) |
| template_2_incremental_builder | Build step-by-step | 85-95% (pattern) |
| template_3_puzzle_solver | Follow flowchart | 85-95% (pattern) |
| template_4_forensic_debugger | Decode errors | 100% (exact match) |
| template_5_scenario_specialist | World-building code | 85-95% (pattern) |
| template_6_specification_implementer | Build to spec | 85-95% (pattern) |
| template_7_apprentice | Fix broken code | 100% (exact match) |
| template_8_code_connoisseur | Compare solutions | 100% (exact match) |
| template_9_world_builder | OOP interactions | 85-95% (pattern) |
| template_10_simplifier | Refactor for clarity | 100% (exact match) |
| template_11_style_guide | Apply PEP 8 | 100% (exact match) |
| template_12_oracle | Predict output | 100% (exact match) |
| template_13_investigator | Trace execution | 100% (exact match) |
| template_14_strategist | Plan then code | 85-95% (pattern) |
| template_15_role_switcher | Multiple scenarios | 85-95% (pattern) |

### 3. Hardcoded Reference Detection

Finds theme-specific references:

**Categories Detected:**
- **houses** - Gryffindor, Slytherin, Hufflepuff, Ravenclaw
- **characters** - Harry, Hermione, Ron, Dumbledore, etc.
- **locations** - Hogwarts, Hogsmeade, Diagon Alley
- **objects** - wand, broomstick, potion, spell
- **events** - Quidditch, Triwizard Tournament

**Suggested Replacements:**
```python
"Gryffindor" → {{house_1}}
"Harry" → {{hero}}
"Hogwarts" → {{school}}
"wand" → {{tool}}
```

### 4. Narrative Extraction

Identifies narrative text to convert to context blocks:

**Locations Searched:**
- Module docstrings
- Function docstrings (non-technical only)
- Exercise description comments
- Multi-line comments with narrative

**Context Block Types:**
- `CONTEXT_NARRATIVE` - Story setup
- `CONTEXT_SCENARIO` - Situation description
- `CONTEXT_PHASE_N` - Build phases
- `CONTEXT_CASE_N` - Debug scenarios
- `CONTEXT_FUNCTION_DESCRIPTION` - What function should do

### 5. Pattern Detection

Detects exercise patterns for better template matching:

**General Patterns:**
- `has_docstring_specs` - Detailed specs in docstrings
- `has_multiple_functions` - 3+ functions
- `has_batch_operations` - List/dict operations
- `has_role_description` - User role defined
- `has_collection_building` - Building data structures

**OOP Patterns (Module 9):**
- `has_multiple_classes` - 2+ class definitions
- `has_oop_context` - OOP keywords (adventure, game, world)
- `has_entity_system` - create_X functions + classes

---

## Understanding the Output

### Console Report Example

```
=== EXERCISE ANALYSIS ===

File: exercises/module_7_dictionaries/complete_function/exercise_1_complete_dict_functions.py
Module: module_7_dictionaries
Exercise Type: complete_function

Template Match: template_6_specification_implementer
Confidence: 95%
Reasoning: Pattern match: has_docstring_specs (+2 more)

Context Blocks Created: 1
  - CONTEXT_NARRATIVE

Hardcoded References: 12 found
  Line 103: "Gryffindor" (houses) -> {{house_1}}
  Line 103: "Hufflepuff" (houses) -> {{house_2}}
  Line 200: "Harry" (characters) -> {{hero}}
  Line 200: "Luna" (characters) -> {{character}}
  ... (8 more)

⚠️  Manual Review Recommended
Reason: >10 hardcoded references require careful review
```

### JSON Report Structure

```json
{
  "exercise_path": "exercises/module_7/.../exercise_1.py",
  "template_matched": "template_6_specification_implementer",
  "confidence": 0.95,
  "context_blocks_created": ["CONTEXT_NARRATIVE"],
  "hardcoded_references_found": [
    {
      "line_num": 103,
      "text": "Gryffindor",
      "category": "houses",
      "suggested_replacement": "{{house_1}}",
      "confidence": 0.9
    }
  ],
  "manual_review_needed": true,
  "notes": "Pattern match: has_docstring_specs (+2 more)",
  "warnings": ["Manual review recommended due to complexity"]
}
```

---

## Confidence Levels

**100% - Exact Match**
- Exercise type directly maps to template
- decode_error → forensic_debugger
- bug_hunt → apprentice
- which_is_better → code_connoisseur
- No ambiguity, perfect match

**90-95% - Strong Pattern Match**
- Multiple patterns detected
- OOP patterns in module 9
- Clear indicators align with template
- High confidence, minimal review needed

**85-89% - Good Pattern Match**
- Single clear pattern detected
- Function count suggests template
- Module context supports match
- Likely correct, light review recommended

**70-84% - Uncertain Match**
- Weak patterns or conflicting signals
- Heuristic fallback used
- Manual review strongly recommended
- May need template adjustment

---

## Flags and Warnings

### Manual Review Needed

Script sets `manual_review_needed: true` when:
- Confidence < 85%
- Hardcoded references > 10
- No clear pattern match
- Multiple templates seem viable

### Common Warnings

**"Manual review recommended due to low confidence or complexity"**
- Template match uncertain
- Human judgment needed
- Check if better template exists

**"Many hardcoded references - careful replacement needed"**
- 10+ theme references found
- May require context-aware replacement
- Don't blindly replace all

**"No narrative found - may not need context blocks"**
- Exercise has no story elements
- Purely technical exercise
- Context blocks may not apply

---

## Production Usage

### Phase 1: Dry Run Analysis (Current)

```bash
# Analyze without modifying files
python scripts/convert_to_templates.py --module 7 --dry-run
```

**Purpose:** Understand what needs conversion

### Phase 2: Validation (Next Step)

```bash
# Use Haiku agents to validate reports
# (Not yet implemented)
```

**Purpose:** Verify template matches and context blocks

### Phase 3: Actual Conversion

```bash
# Rewrite files with templates
python scripts/convert_to_templates.py --module 7 --output-dir exercises_converted
```

**Purpose:** Generate converted exercise files

### Phase 4: Testing

```bash
# Generate exercises with different themes
# Test narrative coherence
# Verify all hardcoded refs replaced
```

**Purpose:** Ensure quality across themes

---

## Troubleshooting

### Issue: "No patterns detected, using heuristic"

**Meaning:** Script couldn't find clear indicators for template match
**Solution:** Check if exercise has unique characteristics to add to pattern detection

### Issue: "Wrong template match"

**Meaning:** Exercise characteristics don't align with template
**Solution:**
1. Check if new pattern detection rule needed
2. Consider if exercise is edge case
3. May need manual template override

### Issue: "Missing hardcoded references"

**Meaning:** Script didn't detect all theme references
**Solution:**
1. Check if reference uses unusual format
2. Add pattern to `HARDCODED_PATTERNS` in script
3. May need manual review

### Issue: "Too many context blocks"

**Meaning:** Script extracted too much narrative
**Solution:**
1. Check if technical docstrings being extracted
2. Adjust `suggest_context_block()` filtering
3. May need manual consolidation

---

## Performance

**Tested on 3 pilot exercises:**
- ✅ 100% template accuracy
- ✅ 100% hardcoded reference detection
- ✅ 0 crashes
- ✅ Clean context block naming
- ✅ 95-100% confidence scores

**Expected for full corpus (145 exercises):**
- Runtime: ~5-10 minutes
- Template matches: 95%+ correct
- Hardcoded refs: 80-100 per corpus
- Manual review needed: ~20-30 exercises

---

## Next Steps

1. **Monitor full corpus analysis** (currently running)
2. **Review statistics** from comprehensive report
3. **Create Haiku validation agent** (~2 hours)
4. **Define context blocks for themes** (~12-16 hours)
5. **Run actual conversion** (non-dry-run)
6. **Test across themes**

---

## Documentation

- **CONVERSION_SCRIPT_FINAL.md** - Complete technical documentation
- **PILOT_CONVERSION_RESULTS.md** - Detailed pilot test analysis
- **CONVERSION_PLAN.md** - Original conversion strategy
- **templates/activity_patterns/** - All 15 task-level narrative patterns

---

**Status:** ✅ Ready for production use
**Recommendation:** Proceed with validation and theme definition
