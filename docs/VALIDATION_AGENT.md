# Haiku Validation Agent

**Script:** `scripts/validate_conversions.py`
**Purpose:** Validate and refine template matches from conversion script
**Status:** ✅ Implemented (Rule-based, ready for API integration)

---

## Overview

The Haiku Validation Agent reviews conversion reports and provides validation for template matches. It's designed to catch edge cases, suggest alternatives, and flag exercises needing human review.

### Current Implementation

**Version 1.0 (Rule-based)**
- Uses confidence thresholds for validation
- Classifies exercises into: Approved, Needs Review, Alternative Suggested
- Generates comprehensive validation reports
- **Ready for Claude API integration**

### Future Enhancement

**Version 2.0 (API-powered)**
- Will use Claude Haiku API for intelligent validation
- Reviews exercise code and context
- Suggests specific alternative templates
- Provides detailed reasoning

---

## Usage

### Validate Medium Confidence Exercises

```bash
python scripts/validate_conversions.py \
  --report-dir conversion_reports_full \
  --focus medium \
  --output validation_report_medium.json
```

### Validate Low Confidence Exercises

```bash
python scripts/validate_conversions.py \
  --report-dir conversion_reports_full \
  --focus low \
  --output validation_report_low.json
```

###Validate All Exercises

```bash
python scripts/validate_conversions.py \
  --report-dir conversion_reports_full \
  --output validation_report_all.json
```

### Validate Single Exercise

```bash
python scripts/validate_conversions.py \
  --report conversion_reports_full/exercise_1_report.json \
  --output validation_single.json
```

---

## Validation Logic

### Rule-Based (Current)

| Confidence | Validation Status | Reasoning |
|------------|-------------------|-----------|
| ≥90% | **Approved** | High confidence, no concerns |
| 70-89% | **Needs Review** | Medium confidence, manual review recommended |
| <70% | **Alternative Suggested** | Low confidence, template may be incorrect |

### API-Powered (Future)

Will analyze:
1. Exercise code structure
2. Template fit assessment
3. Pattern indicators in code
4. Context alignment
5. Pedagogical appropriateness

---

## Validation Results

### Medium Confidence Exercises (70-84%)

**Tested:** 14 exercises
**Results:**
- Approved: 0
- Needs Review: 14 (100%)
- Alternative Suggested: 0

**Common Patterns:**
- Most are `template_2_incremental_builder` at 70% confidence
- Function count heuristic triggered (conservative fallback)
- All flagged for manual review

**Recommendation:** These likely correct but need human verification of template match.

### Low Confidence Exercises (<70%)

**Tested:** 35 exercises
**Results:**
- Approved: 0
- Needs Review: 0
- Alternative Suggested: 35 (100%)

**Common Patterns:**
- Most are `template_3_role_assignment` at 60% confidence
- write_code fallback triggered
- All flagged for alternative templates

**Recommendation:** These need better pattern detection or new templates.

---

## Output Format

### JSON Report Structure

```json
{
  "summary": {
    "total_validated": 49,
    "approved": 0,
    "needs_review": 14,
    "alternative_suggested": 35,
    "approval_rate": 0.0
  },
  "approved_exercises": [...],
  "needs_review_exercises": [
    {
      "exercise": "raw_exercises/.../exercise.py",
      "template": "template_2_incremental_builder",
      "confidence": 0.70,
      "concerns": [
        "Confidence below 90%",
        "Pattern match may need verification"
      ],
      "suggestions": [
        "Review exercise manually",
        "Check context blocks are appropriate"
      ]
    }
  ],
  "alternative_suggested_exercises": [
    {
      "exercise": "raw_exercises/.../exercise.py",
      "original_template": "template_3_role_assignment",
      "original_confidence": 0.60,
      "recommended_template": "template_2_incremental_builder",
      "confidence_adjustment": 0.75,
      "reasoning": "Low confidence suggests uncertain match",
      "concerns": [
        "Confidence below 70%",
        "May not match intended template pattern"
      ]
    }
  ]
}
```

---

## Validation Categories

### Approved ✅

**Criteria:**
- Confidence ≥90%
- Template match is clear and appropriate
- No concerns identified

**Action:** Ready for conversion

### Needs Review ⚠️

**Criteria:**
- Confidence 70-89%
- Template match is likely correct but uncertain
- Manual verification recommended

**Action:** Human review to confirm template

**Common Reasons:**
- Pattern-based match (not exact)
- Multiple patterns could apply
- Heuristic fallback used

### Alternative Suggested 🔄

**Criteria:**
- Confidence <70%
- Template match is uncertain or likely wrong
- Alternative template suggested

**Action:** Manual template selection or pattern improvement

**Common Reasons:**
- No clear pattern detected
- Exercise type unknown
- write_code fallback (too generic)

---

## Integration with Workflow

### Current Workflow

1. **Run conversion script** → Generate reports
2. **Run validation agent** → Classify exercises
3. **Manual review** → Verify medium/low confidence
4. **Update patterns** → Improve detection
5. **Re-run conversion** → Better matches

### Recommended Process

```bash
# Step 1: Convert all exercises
python scripts/convert_to_templates.py --all --dry-run --report-dir conversion_reports_full

# Step 2: Validate medium confidence
python scripts/validate_conversions.py --report-dir conversion_reports_full --focus medium --output validation_medium.json

# Step 3: Validate low confidence
python scripts/validate_conversions.py --report-dir conversion_reports_full --focus low --output validation_low.json

# Step 4: Review validation reports
# - Check validation_medium.json for manual review items
# - Check validation_low.json for pattern improvement opportunities

# Step 5: Update conversion script patterns
# - Add new patterns based on manual review
# - Improve existing pattern detection

# Step 6: Re-run conversion
python scripts/convert_to_templates.py --all --dry-run --report-dir conversion_reports_v3
```

---

## Future API Integration

### Prompt Structure (Ready)

The script includes `create_validation_prompt()` function that generates structured prompts for Claude Haiku:

**Prompt includes:**
- Exercise code (first 100 lines)
- Current template match and confidence
- Template descriptions and indicators
- List of available templates
- Structured validation criteria

**Expected Response:**
```json
{
  "validation_status": "APPROVED|NEEDS_REVIEW|ALTERNATIVE_SUGGESTED",
  "recommended_template": "template_name or null",
  "confidence_adjustment": 0.95 or null,
  "reasoning": "Brief explanation",
  "concerns": ["concern 1", "concern 2"],
  "suggestions": ["suggestion 1", "suggestion 2"]
}
```

### API Integration Steps

1. Add Claude SDK dependency
2. Configure API key
3. Replace `validate_with_haiku()` function
4. Add retry logic and rate limiting
5. Test on pilot exercises
6. Roll out to full corpus

---

## Performance Metrics

### Current Results (Rule-Based)

**Medium Confidence (14 exercises):**
- Processing time: <1 second
- All correctly flagged for review
- No false approvals

**Low Confidence (35 exercises):**
- Processing time: <1 second
- All correctly flagged for alternatives
- Conservative recommendations

**Assessment:** Rule-based validation working as designed - erring on side of caution.

### Expected with API Integration

**Estimated Performance:**
- Processing time: ~2-3 seconds per exercise
- Higher accuracy in alternative suggestions
- Better reasoning and explanations
- Context-aware recommendations

**Cost Estimate (Haiku):**
- ~500 tokens per exercise (input)
- ~100 tokens per response (output)
- 145 exercises × 600 tokens = ~87,000 tokens
- **Cost: ~$0.02 for full corpus validation**

---

## Insights from Validation

### Medium Confidence Issues

**Root Cause:** Function count heuristic
- 70% confidence triggers when exercise has 5+ functions
- Template: `template_2_incremental_builder`
- Issue: Too generic, doesn't differentiate exercise types

**Solution:** Add more specific patterns
- Turtle graphics detection
- Game creation patterns
- Function-specific indicators

### Low Confidence Issues

**Root Cause:** write_code fallback
- 60% confidence triggers for write_code exercises without patterns
- Template: `template_3_role_assignment`
- Issue: Catch-all for unclassified write_code

**Solution:** Improve write_code detection
- Detect turtle graphics → template_5_scenario_specialist
- Detect games → template_9_world_builder or template_13_decision_tree
- Detect calculators → template_6_specification_implementer

---

## Recommendations

### Priority 1: Add Exercise Type Mappings

Add exact matches for:
- `code_ordering` → `template_11_code_arranger` (needs creation)
- `fill_blanks` → `template_2_incremental_builder`
- `match_output` → `template_7_prediction_challenger`
- `spot_difference` → `template_5_comparison_analyst`

### Priority 2: Improve write_code Detection

Add sub-patterns:
- `has_turtle_graphics` → detect turtle imports/calls
- `has_game_logic` → detect game-specific patterns
- `has_calculator_logic` → detect math operations
- `has_creative_freedom` → detect open-ended prompts

### Priority 3: Refine Confidence Scoring

Adjust thresholds:
- Multiple patterns: +10% confidence (currently +5%)
- Module-specific matches: +10% confidence
- Exact type matches: Keep at 100%

### Priority 4: API Integration

When ready to integrate:
1. Test on pilot exercises first (3 exercises)
2. Compare API results to rule-based results
3. Validate accuracy improvement
4. Roll out gradually (module by module)

---

## Command Reference

### Basic Commands

```bash
# Validate medium confidence
python scripts/validate_conversions.py --report-dir conversion_reports_full --focus medium --output validation_medium.json

# Validate low confidence
python scripts/validate_conversions.py --report-dir conversion_reports_full --focus low --output validation_low.json

# Validate high confidence (quality check)
python scripts/validate_conversions.py --report-dir conversion_reports_full --focus high --output validation_high.json

# Validate all
python scripts/validate_conversions.py --report-dir conversion_reports_full --output validation_all.json
```

### Advanced Options

```bash
# Single report file
python scripts/validate_conversions.py --report path/to/report.json --output validation.json

# Custom exercise base path
python scripts/validate_conversions.py --report-dir reports --exercise-base-path /path/to/exercises --output validation.json
```

---

## Success Criteria

### Phase 2 Goals (All Met ✅)

- [x] Validation agent implemented
- [x] Works with conversion reports
- [x] Classifies exercises correctly
- [x] Generates JSON reports
- [x] Tested on medium/low confidence
- [x] No crashes or errors

### Phase 3 Goals (Next)

- [ ] Integrate Claude Haiku API
- [ ] Test API validation vs rule-based
- [ ] Measure accuracy improvement
- [ ] Document API integration process

---

## Files

**Script:**
- `scripts/validate_conversions.py` (515 lines)

**Reports Generated:**
- `validation_report_medium.json` (14 exercises)
- `validation_report_low.json` (35 exercises)

**Documentation:**
- `docs/VALIDATION_AGENT.md` (this file)

---

## Status

**Phase 2: ✅ COMPLETE**

Validation agent implemented and tested:
- Rule-based validation working
- Medium confidence: 14 exercises reviewed
- Low confidence: 35 exercises reviewed
- All flagged appropriately
- Reports generated successfully

**Next Steps:**
- Add exercise type mappings (Priority 1)
- Improve write_code detection (Priority 2)
- Consider API integration (Priority 4)

---

**Document Updated:** 2026-02-01
**Status:** ✅ Phase 2 Complete
**Next Phase:** Pattern Improvements (Phase 3)
