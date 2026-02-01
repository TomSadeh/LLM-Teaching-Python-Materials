#!/usr/bin/env python3
"""
Haiku Validation Agent for Exercise Conversion

This script uses Claude Haiku to validate and refine template matches from the
conversion script. It reviews JSON reports and provides recommendations for:
- Template match validation
- Alternative template suggestions
- Context block quality assessment
- Confidence score verification

Usage:
    python scripts/validate_conversions.py --report conversion_reports_full/all_exercises_report.json
    python scripts/validate_conversions.py --report-dir conversion_reports_full
    python scripts/validate_conversions.py --focus medium  # Only medium confidence
    python scripts/validate_conversions.py --focus low     # Only low confidence
"""

import json
import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result from Haiku validation"""
    exercise_path: str
    original_template: str
    original_confidence: float
    validation_status: str  # 'approved', 'needs_review', 'alternative_suggested'
    recommended_template: Optional[str]
    confidence_adjustment: Optional[float]
    reasoning: str
    concerns: List[str]
    suggestions: List[str]


# Template descriptions for Haiku to understand each template
TEMPLATE_DESCRIPTIONS = {
    'template_1_tutorial_guide': {
        'name': 'Tutorial Guide',
        'best_for': 'Exercises with example functions that students study then implement similar ones',
        'indicators': ['has example function', 'follow the pattern', 'similar to example'],
    },
    'template_2_incremental_builder': {
        'name': 'Incremental Builder',
        'best_for': 'Multi-phase exercises building complexity step-by-step',
        'indicators': ['phase 1', 'phase 2', 'step 1', 'step 2', 'build incrementally'],
    },
    'template_3_role_assignment': {
        'name': 'Role Assignment',
        'best_for': 'Exercises where student has a specific job/role',
        'indicators': ['you are a', 'your job', 'as a', 'your role'],
    },
    'template_4_forensic_debugger': {
        'name': 'Forensic Debugger',
        'best_for': 'Debug exercises (decode_error, bug_hunt)',
        'indicators': ['error message', 'debug', 'fix the bug', 'what went wrong'],
    },
    'template_5_comparison_analyst': {
        'name': 'Comparison Analyst',
        'best_for': 'Compare solutions or approaches (which_is_better)',
        'indicators': ['which is better', 'compare', 'analyze approaches'],
    },
    'template_6_specification_implementer': {
        'name': 'Specification Implementer',
        'best_for': 'Build to detailed specifications with Args/Returns',
        'indicators': ['Args:', 'Returns:', 'specification', 'requirements'],
    },
    'template_7_prediction_challenger': {
        'name': 'Prediction Challenger',
        'best_for': 'Predict output exercises',
        'indicators': ['what will print', 'predict output', 'what happens'],
    },
    'template_8_progressive_unlocking': {
        'name': 'Progressive Unlocking',
        'best_for': 'Exercises with progressive stages that unlock',
        'indicators': ['stage_1', 'stage_2', 'unlock', 'progress'],
    },
    'template_9_world_builder': {
        'name': 'World Builder',
        'best_for': 'OOP exercises with entities and interactions',
        'indicators': ['class', 'entity', 'create_', 'interact', 'adventure', 'game'],
    },
    'template_10_quality_auditor': {
        'name': 'Quality Auditor',
        'best_for': 'Fix style, simplify code, improve quality',
        'indicators': ['PEP 8', 'fix style', 'simplify', 'improve'],
    },
    'template_11_batch_processor': {
        'name': 'Batch Processor',
        'best_for': 'Process collections, lists, batches',
        'indicators': ['for item in', 'process batch', 'collection'],
    },
    'template_12_resource_exchange': {
        'name': 'Resource Exchange',
        'best_for': 'Trading, exchange rates, conversions',
        'indicators': ['exchange', 'trade', 'convert', 'rate'],
    },
    'template_13_decision_tree': {
        'name': 'Decision Tree',
        'best_for': 'Branching logic, decision making',
        'indicators': ['if/elif', 'decision', 'choose', 'branch'],
    },
    'template_14_collection_builder': {
        'name': 'Collection Builder',
        'best_for': 'Build data structures, collections',
        'indicators': ['build dict', 'build list', 'create collection'],
    },
    'template_15_table_tracer': {
        'name': 'Table Tracer',
        'best_for': 'Code tracing with variable tables',
        'indicators': ['trace', 'variable table', 'step through'],
    },
}


def load_report(report_path: str) -> Dict:
    """Load a JSON report file"""
    with open(report_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_exercise_code(exercise_path: str) -> str:
    """Load the actual exercise Python file"""
    try:
        with open(exercise_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Could not load file: {e}]"


def create_validation_prompt(report: Dict, exercise_code: str) -> str:
    """
    Create a prompt for Haiku to validate the template match.

    This is a structured prompt that asks Haiku to:
    1. Review the exercise code and current template match
    2. Assess if the match is appropriate
    3. Suggest alternatives if needed
    4. Provide reasoning
    """

    template_name = report['template_matched']
    confidence = report['confidence']
    reasoning = report['notes']

    # Get template description
    template_desc = TEMPLATE_DESCRIPTIONS.get(template_name, {
        'name': template_name,
        'best_for': 'Unknown',
        'indicators': []
    })

    prompt = f"""You are reviewing an automated template match for a Python teaching exercise.

## Exercise Information
**File:** {report['exercise_path']}
**Matched Template:** {template_name} ({template_desc['name']})
**Confidence:** {confidence * 100:.0f}%
**Reasoning:** {reasoning}

## Template Description
**Best For:** {template_desc['best_for']}
**Typical Indicators:** {', '.join(template_desc['indicators'])}

## Exercise Code (First 100 lines)
```python
{chr(10).join(exercise_code.split(chr(10))[:100])}
```

## Available Templates
{format_template_list()}

## Your Task
Review this template match and provide:

1. **Validation Status** (choose one):
   - APPROVED: Match is correct and appropriate
   - NEEDS_REVIEW: Match is uncertain, human review recommended
   - ALTERNATIVE_SUGGESTED: Different template would be better

2. **Recommended Template** (if suggesting alternative):
   - Template name (e.g., template_2_incremental_builder)
   - Why it's better than current match

3. **Confidence Adjustment** (if applicable):
   - New confidence score (0.0-1.0)
   - Reasoning for adjustment

4. **Concerns** (if any):
   - List specific issues with current match

5. **Suggestions** (always provide):
   - Improvement recommendations
   - Context block suggestions
   - Any other relevant advice

## Response Format (JSON)
Respond with ONLY a JSON object in this exact format:
{{
  "validation_status": "APPROVED|NEEDS_REVIEW|ALTERNATIVE_SUGGESTED",
  "recommended_template": "template_name or null",
  "confidence_adjustment": 0.95 or null,
  "reasoning": "Brief explanation of your decision",
  "concerns": ["concern 1", "concern 2"],
  "suggestions": ["suggestion 1", "suggestion 2"]
}}

Be concise but specific. Focus on pedagogical appropriateness."""

    return prompt


def format_template_list() -> str:
    """Format available templates for the prompt"""
    lines = []
    for template_id, info in TEMPLATE_DESCRIPTIONS.items():
        lines.append(f"- {template_id}: {info['best_for']}")
    return '\n'.join(lines)


def validate_with_haiku(report: Dict, exercise_code: str) -> ValidationResult:
    """
    Validate a single exercise using Claude Haiku.

    Note: This is a placeholder that would integrate with Claude API.
    For now, it returns mock validation based on confidence thresholds.
    """

    # TODO: Integrate with Claude API (Haiku)
    # For now, use rule-based validation

    confidence = report['confidence']
    template = report['template_matched']
    exercise_path = report['exercise_path']

    # Rule-based validation for demonstration
    if confidence >= 0.9:
        return ValidationResult(
            exercise_path=exercise_path,
            original_template=template,
            original_confidence=confidence,
            validation_status='approved',
            recommended_template=None,
            confidence_adjustment=None,
            reasoning='High confidence match, no concerns',
            concerns=[],
            suggestions=['Consider manual spot-check for quality assurance']
        )
    elif confidence >= 0.7:
        return ValidationResult(
            exercise_path=exercise_path,
            original_template=template,
            original_confidence=confidence,
            validation_status='needs_review',
            recommended_template=None,
            confidence_adjustment=None,
            reasoning='Medium confidence - manual review recommended',
            concerns=['Confidence below 90%', 'Pattern match may need verification'],
            suggestions=['Review exercise manually', 'Check context blocks are appropriate']
        )
    else:
        # Low confidence - suggest review
        return ValidationResult(
            exercise_path=exercise_path,
            original_template=template,
            original_confidence=confidence,
            validation_status='alternative_suggested',
            recommended_template='template_2_incremental_builder',  # Conservative fallback
            confidence_adjustment=0.75,
            reasoning='Low confidence suggests uncertain match',
            concerns=['Confidence below 70%', 'May not match intended template pattern'],
            suggestions=[
                'Manual template selection recommended',
                'Review exercise structure carefully',
                'Consider if exercise fits any exact-match patterns'
            ]
        )


def validate_report(report: Dict, exercise_base_path: str = '.') -> ValidationResult:
    """Validate a single conversion report"""

    # Load the actual exercise code
    exercise_path = os.path.join(exercise_base_path, report['exercise_path'])
    exercise_code = load_exercise_code(exercise_path)

    # Create validation prompt (for future API integration)
    prompt = create_validation_prompt(report, exercise_code)

    # Validate with Haiku (currently rule-based)
    result = validate_with_haiku(report, exercise_code)

    return result


def validate_batch(reports: List[Dict],
                   focus: Optional[str] = None,
                   exercise_base_path: str = '.') -> List[ValidationResult]:
    """
    Validate multiple conversion reports.

    Args:
        reports: List of conversion reports to validate
        focus: Filter by confidence level ('high', 'medium', 'low')
        exercise_base_path: Base path for exercise files

    Returns:
        List of validation results
    """

    results = []

    # Filter by focus if specified
    if focus:
        if focus == 'high':
            reports = [r for r in reports if r['confidence'] >= 0.85]
        elif focus == 'medium':
            reports = [r for r in reports if 0.70 <= r['confidence'] < 0.85]
        elif focus == 'low':
            reports = [r for r in reports if r['confidence'] < 0.70]

    total = len(reports)
    print(f"\n{'='*60}")
    print(f"Validating {total} exercise conversions...")
    print(f"{'='*60}\n")

    for i, report in enumerate(reports, 1):
        exercise_path = report['exercise_path']
        print(f"[{i}/{total}] Validating: {os.path.basename(exercise_path)}")

        result = validate_report(report, exercise_base_path)
        results.append(result)

        # Print summary
        status_icon = {
            'approved': '[OK]',
            'needs_review': '[REVIEW]',
            'alternative_suggested': '[ALT]'
        }.get(result.validation_status, '[?]')

        print(f"  {status_icon} {result.validation_status.upper()}")
        print(f"  Original: {result.original_template} ({result.original_confidence:.0%})")
        if result.recommended_template:
            print(f"  Recommended: {result.recommended_template}")
        print(f"  Reasoning: {result.reasoning}")
        if result.concerns:
            print(f"  Concerns: {', '.join(result.concerns[:2])}")
        print()

    return results


def generate_validation_report(results: List[ValidationResult], output_path: str):
    """Generate comprehensive validation report"""

    # Calculate statistics
    total = len(results)
    approved = sum(1 for r in results if r.validation_status == 'approved')
    needs_review = sum(1 for r in results if r.validation_status == 'needs_review')
    alternatives = sum(1 for r in results if r.validation_status == 'alternative_suggested')

    # Group by status
    approved_exercises = [r for r in results if r.validation_status == 'approved']
    review_exercises = [r for r in results if r.validation_status == 'needs_review']
    alternative_exercises = [r for r in results if r.validation_status == 'alternative_suggested']

    report = {
        'summary': {
            'total_validated': total,
            'approved': approved,
            'needs_review': needs_review,
            'alternative_suggested': alternatives,
            'approval_rate': approved / total if total > 0 else 0,
        },
        'approved_exercises': [
            {
                'exercise': r.exercise_path,
                'template': r.original_template,
                'confidence': r.original_confidence,
                'reasoning': r.reasoning
            }
            for r in approved_exercises
        ],
        'needs_review_exercises': [
            {
                'exercise': r.exercise_path,
                'template': r.original_template,
                'confidence': r.original_confidence,
                'concerns': r.concerns,
                'suggestions': r.suggestions
            }
            for r in review_exercises
        ],
        'alternative_suggested_exercises': [
            {
                'exercise': r.exercise_path,
                'original_template': r.original_template,
                'original_confidence': r.original_confidence,
                'recommended_template': r.recommended_template,
                'confidence_adjustment': r.confidence_adjustment,
                'reasoning': r.reasoning,
                'concerns': r.concerns
            }
            for r in alternative_exercises
        ]
    }

    # Write JSON report
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"VALIDATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total Validated: {total}")
    print(f"[OK] Approved: {approved} ({approved/total*100:.1f}%)")
    print(f"[REVIEW] Needs Review: {needs_review} ({needs_review/total*100:.1f}%)")
    print(f"[ALT] Alternative Suggested: {alternatives} ({alternatives/total*100:.1f}%)")
    print(f"\nReport written to: {output_path}")
    print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Validate exercise conversion template matches using Claude Haiku'
    )
    parser.add_argument(
        '--report',
        help='Path to single JSON report file'
    )
    parser.add_argument(
        '--report-dir',
        help='Directory containing conversion reports'
    )
    parser.add_argument(
        '--focus',
        choices=['high', 'medium', 'low'],
        help='Focus on specific confidence level'
    )
    parser.add_argument(
        '--output',
        default='validation_report.json',
        help='Output path for validation report'
    )
    parser.add_argument(
        '--exercise-base-path',
        default='.',
        help='Base path for exercise files'
    )

    args = parser.parse_args()

    # Load reports
    reports = []

    if args.report:
        # Single report file
        data = load_report(args.report)
        if isinstance(data, list):
            reports = data
        else:
            reports = [data]
    elif args.report_dir:
        # Directory of reports
        report_path = Path(args.report_dir)
        if report_path.exists():
            # Look for master report first
            master_report = report_path / 'all_exercises_report.json'
            if master_report.exists():
                reports = load_report(str(master_report))
            else:
                # Load individual reports
                for report_file in report_path.glob('*.json'):
                    try:
                        data = load_report(str(report_file))
                        if isinstance(data, list):
                            reports.extend(data)
                        else:
                            reports.append(data)
                    except Exception as e:
                        print(f"Warning: Could not load {report_file}: {e}")
    else:
        print("Error: Must specify --report or --report-dir")
        sys.exit(1)

    if not reports:
        print("Error: No reports found to validate")
        sys.exit(1)

    # Validate
    results = validate_batch(reports, args.focus, args.exercise_base_path)

    # Generate report
    generate_validation_report(results, args.output)


if __name__ == '__main__':
    main()
