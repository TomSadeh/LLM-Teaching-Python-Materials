#!/usr/bin/env python3
"""
Convert existing exercises to use universal narrative templates.

This script analyzes existing exercises and converts them to use the
universal narrative template system with context blocks.

Usage:
    python scripts/convert_to_templates.py --input path/to/exercise.py
    python scripts/convert_to_templates.py --module 7
    python scripts/convert_to_templates.py --all --dry-run
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict


# ============================================================
# TEMPLATE MATCHING CONFIGURATION
# ============================================================

# Exact matches based on exercise type
EXACT_TEMPLATE_MATCHES = {
    'decode_error': 'template_4_forensic_debugger',
    'bug_hunt': 'template_4_forensic_debugger',
    'which_is_better': 'template_5_comparison_analyst',
    'output_prediction': 'template_7_prediction_challenger',
    'code_tracing': 'template_15_table_tracer',
    'fix_style': 'template_10_quality_auditor',
    'simplify_code': 'template_10_quality_auditor',
}

# Pattern-based template selection
# Higher priority patterns should be checked first (order matters for some)
PATTERN_TEMPLATES = {
    'has_entity_system': 'template_9_world_builder',  # High priority for OOP
    'has_multiple_classes': 'template_9_world_builder',  # High priority for OOP
    'has_oop_context': 'template_9_world_builder',  # Module 9 + OOP keywords
    'has_entity_interactions': 'template_9_world_builder',
    'has_progressive_sections': 'template_8_progressive_unlocking',
    'has_example_function': 'template_1_tutorial_guide',
    'has_multiple_phases': 'template_2_incremental_builder',
    'has_role_description': 'template_3_role_assignment',
    'has_docstring_specs': 'template_6_specification_implementer',
    'has_batch_operations': 'template_11_batch_processor',
    'has_exchange_rates': 'template_12_resource_exchange',
    'has_decision_branches': 'template_13_decision_tree',
    'has_collection_building': 'template_14_collection_builder',
}

# Hardcoded theme references to detect
HARDCODED_REFERENCES = {
    'harry_potter': {
        'houses': ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'],
        'characters': ['Harry', 'Hermione', 'Ron', 'Dumbledore', 'Snape',
                      'Voldemort', 'Luna', 'Neville', 'Draco'],
        'locations': ['Hogwarts', 'Diagon Alley', 'Hogsmeade'],
        'items': ['Invisibility Cloak', 'Elder Wand'],
        'spells': ['Expelliarmus', 'Lumos', 'Wingardium Leviosa', 'Patronus'],
    }
}

# Context block naming patterns
CONTEXT_BLOCK_PATTERNS = {
    'intro': ['CONTEXT_INTRO', 'CONTEXT_PROJECT_INTRO', 'CONTEXT_ROLE_INTRO'],
    'objective': ['CONTEXT_LEARNING_OBJECTIVE', 'CONTEXT_PREDICTION_PURPOSE'],
    'task': ['CONTEXT_STUDENT_TASK', 'CONTEXT_ROLE_RESPONSIBILITIES'],
    'guidance': ['CONTEXT_GUIDANCE', 'CONTEXT_IMPLEMENTATION_GUIDANCE'],
    'result': ['CONTEXT_RESULT', 'CONTEXT_COMPLETE', 'CONTEXT_SUCCESS'],
}


# ============================================================
# DATA STRUCTURES
# ============================================================

@dataclass
class ExerciseAnalysis:
    """Analysis results for an exercise."""
    exercise_path: str
    exercise_type: str
    module: str
    patterns: List[str]
    has_sections: bool
    has_examples: bool
    function_count: int
    narrative_locations: List[Dict]
    placeholders_found: List[str]


@dataclass
class TemplateMatch:
    """Template matching result."""
    template_name: str
    template_path: str
    confidence: float
    reasoning: str


@dataclass
class NarrativeExtraction:
    """Extracted narrative text."""
    location: str
    line_num: int
    text: str
    suggested_block: str
    context: str


@dataclass
class HardcodedReference:
    """Detected hardcoded reference."""
    line_num: int
    text: str
    category: str  # house, character, location, etc.
    suggested_replacement: str
    confidence: float


@dataclass
class ConversionReport:
    """Complete conversion report."""
    exercise_path: str
    template_matched: str
    confidence: float
    context_blocks_created: List[str]
    hardcoded_references_found: List[Dict]
    manual_review_needed: bool
    notes: str
    warnings: List[str]
    exercise_narrative_template: str = None  # NEW: Exercise-level template
    exercise_sections: List[Dict] = None  # NEW: Section breakdown


# ============================================================
# EXERCISE NARRATIVE TEMPLATE DETECTION
# ============================================================

def detect_exercise_narrative_template(
    exercise_path: str,
    task_count: int,
    exercise_type: str,
    module: str,
    analysis: 'ExerciseAnalysis'
) -> Tuple[str, float, str]:
    """
    Detect appropriate exercise narrative template.

    Returns:
        (template_name, confidence, reasoning)
    """
    content = open(exercise_path, 'r', encoding='utf-8').read()
    content_lower = content.lower()

    # Priority 1: Mystery Investigation (debug/decode focus)
    if exercise_type in ['decode_error', 'bug_hunt']:
        return ('exercise_narrative_mystery_investigation', 1.0,
                'Debug/decode exercises fit Mystery Investigation pattern')

    # Priority 2: World Builder (OOP with entities)
    if module == 'module_9_oop' and task_count >= 6:
        if any(p in analysis.patterns for p in ['has_multiple_classes', 'has_oop_context', 'has_entity_system']):
            return ('exercise_narrative_world_builder', 0.95,
                    'OOP exercise with entity system')

    # Priority 3: Spec Implementation (detailed Args/Returns)
    if exercise_type == 'complete_function':
        # Check for detailed specifications
        if re.search(r'Args:.*?Returns:', content, re.DOTALL | re.IGNORECASE):
            spec_count = len(re.findall(r'(?:Args|Returns|Raises):', content, re.IGNORECASE))
            if spec_count >= task_count // 2:  # Most functions have specs
                return ('exercise_narrative_spec_implementation', 0.90,
                        'Complete_function with detailed specifications')

    # Priority 4: Tutorial Walkthrough (has examples)
    if analysis.has_examples or 'has_example_function' in analysis.patterns:
        return ('exercise_narrative_tutorial_walkthrough', 0.85,
                'Exercise contains example code for students to follow')

    # Priority 5: Challenge Quest (game-like or competitive)
    competitive_keywords = ['score', 'points', 'level', 'challenge', 'win', 'compete']
    if any(keyword in content_lower for keyword in competitive_keywords):
        return ('exercise_narrative_challenge_quest', 0.80,
                'Game-like or competitive elements detected')

    # Default: Progressive Chapter (most common, works for multi-task)
    if task_count >= 6:
        return ('exercise_narrative_progressive_chapter', 0.75,
                f'Multi-task exercise ({task_count} tasks) benefits from chapter structure')

    # Very small exercises: Tutorial or Single Chapter
    if task_count <= 5:
        return ('exercise_narrative_tutorial_walkthrough', 0.70,
                'Small exercise suitable for tutorial format')

    # Fallback
    return ('exercise_narrative_progressive_chapter', 0.60,
            'Default progressive structure')


# ============================================================
# EXERCISE ANALYSIS
# ============================================================

def analyze_exercise(exercise_path: str) -> ExerciseAnalysis:
    """
    Analyze existing exercise structure.

    Args:
        exercise_path: Path to exercise file

    Returns:
        ExerciseAnalysis object with detected patterns
    """
    with open(exercise_path, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    # Detect exercise type from path
    path_parts = Path(exercise_path).parts
    exercise_type = 'unknown'
    module = 'unknown'

    for part in path_parts:
        if part.startswith('module_'):
            module = part
        elif part in ['write_code', 'complete_function', 'decode_error',
                     'bug_hunt', 'which_is_better', 'output_prediction',
                     'code_tracing', 'blank_page', 'simplify_code', 'fix_style',
                     'bonus', 'match_output']:
            exercise_type = part

    # Detect patterns
    patterns = []

    # Check for section separators
    has_sections = bool(re.search(r'#\s*=+', content))

    # Check for example functions
    has_examples = bool(re.search(r'def\s+example_\w+\(', content))
    if has_examples:
        patterns.append('has_example_function')

    # Check for multiple phases (exercise_a, exercise_b, etc.)
    phase_pattern = r'def\s+exercise_[a-z]\('
    if len(re.findall(phase_pattern, content)) >= 3:
        patterns.append('has_multiple_phases')

    # Check for role descriptions
    role_keywords = ['You are', 'Your job', 'Your role', 'Your task']
    if any(keyword in content for keyword in role_keywords):
        patterns.append('has_role_description')

    # Check for docstring specifications
    if re.search(r'Args:\s*\n', content) and re.search(r'Returns:\s*\n', content):
        patterns.append('has_docstring_specs')

    # Check for progressive sections (stage_1, stage_2, etc.)
    if re.search(r'def\s+stage_\d+\(', content):
        patterns.append('has_progressive_sections')

    # Check for OOP patterns (classes, entity creation)
    class_count = len(re.findall(r'^\s*class\s+\w+', content, re.MULTILINE))
    if class_count >= 2:
        patterns.append('has_multiple_classes')

    # Check for entity interactions
    if re.search(r'def\s+create_\w+\(', content) and 'interact' in content.lower():
        patterns.append('has_entity_interactions')

    # Check for OOP-specific keywords in module 9
    if module == 'module_9_oop':
        oop_keywords = ['adventure', 'game', 'world', 'character', 'entity', 'player']
        if any(keyword in exercise_path.lower() or keyword in content.lower()
               for keyword in oop_keywords):
            patterns.append('has_oop_context')

    # Check for entity creation pattern (create_X functions + class definitions)
    create_funcs = len(re.findall(r'def\s+create_\w+\(', content))
    if create_funcs >= 2 and (class_count >= 1 or 'entity' in content.lower()):
        patterns.append('has_entity_system')

    # Check for batch operations
    batch_keywords = ['for.*in.*items', 'process.*batch', 'for.*in.*collection']
    if any(re.search(pattern, content) for pattern in batch_keywords):
        patterns.append('has_batch_operations')

    # Check for exchange/trading
    if 'exchange' in content.lower() or 'trade' in content.lower():
        patterns.append('has_exchange_rates')

    # Check for decision branches
    if_count = len(re.findall(r'\bif\b', content))
    elif_count = len(re.findall(r'\belif\b', content))
    if if_count + elif_count >= 5:
        patterns.append('has_decision_branches')

    # Check for collection building
    collection_keywords = ['append', 'add.*collection', 'build.*collection']
    if any(re.search(pattern, content) for pattern in collection_keywords):
        patterns.append('has_collection_building')

    # Count functions
    function_count = len(re.findall(r'^\s*def\s+\w+\(', content, re.MULTILINE))

    # Find narrative locations
    narrative_locations = find_narrative_locations(content, lines)

    # Find existing placeholders
    placeholders_found = re.findall(r'\{\{(\w+)\}\}', content)

    return ExerciseAnalysis(
        exercise_path=exercise_path,
        exercise_type=exercise_type,
        module=module,
        patterns=patterns,
        has_sections=has_sections,
        has_examples=has_examples,
        function_count=function_count,
        narrative_locations=narrative_locations,
        placeholders_found=list(set(placeholders_found))
    )


def find_narrative_locations(content: str, lines: List[str]) -> List[Dict]:
    """
    Find locations of narrative text in exercise.

    Args:
        content: Full file content
        lines: List of lines

    Returns:
        List of dictionaries with narrative location info
    """
    locations = []

    # File-level docstring
    file_docstring_match = re.match(r'^"""\s*\n(.*?)\n"""', content, re.DOTALL)
    if file_docstring_match:
        text = file_docstring_match.group(1).strip()
        locations.append({
            'type': 'file_docstring',
            'line_start': 1,
            'line_end': content[:file_docstring_match.end()].count('\n'),
            'text': text
        })

    # Function docstrings
    for match in re.finditer(r'def\s+(\w+)\([^)]*\):\s*\n\s*"""(.*?)"""',
                            content, re.DOTALL):
        func_name = match.group(1)
        docstring = match.group(2).strip()
        line_num = content[:match.start()].count('\n') + 1

        # Only include if it's narrative (not just technical Args/Returns)
        if not (('Args:' in docstring or 'Returns:' in docstring) and
                len(docstring.split('\n')) <= 5):
            locations.append({
                'type': 'function_docstring',
                'function': func_name,
                'line_start': line_num,
                'text': docstring
            })

    # Multi-line comments
    for match in re.finditer(r'#\s*(.+)\n((?:#\s*.+\n)+)', content):
        first_line = match.group(1).strip()
        full_text = match.group(0).strip()
        line_num = content[:match.start()].count('\n') + 1

        # Skip section separators
        if '=====' in full_text or '-----' in full_text:
            continue

        locations.append({
            'type': 'multi_line_comment',
            'line_start': line_num,
            'text': full_text
        })

    return locations


# ============================================================
# TEMPLATE MATCHING
# ============================================================

def match_template(analysis: ExerciseAnalysis) -> TemplateMatch:
    """
    Select best template based on analysis.

    Args:
        analysis: Exercise analysis results

    Returns:
        TemplateMatch with selected template and confidence
    """
    # First check exact matches by exercise type
    if analysis.exercise_type in EXACT_TEMPLATE_MATCHES:
        template_name = EXACT_TEMPLATE_MATCHES[analysis.exercise_type]
        return TemplateMatch(
            template_name=template_name,
            template_path=f'templates/narrative_templates/{template_name}.py',
            confidence=1.0,
            reasoning=f'Exact match for exercise type: {analysis.exercise_type}'
        )

    # Then check pattern matches (ordered by priority)
    matched_patterns = [p for p in analysis.patterns if p in PATTERN_TEMPLATES]

    if matched_patterns:
        # Use pattern priority based on order in PATTERN_TEMPLATES
        pattern_priority = list(PATTERN_TEMPLATES.keys())
        # Sort matched patterns by their priority (earlier = higher priority)
        matched_patterns.sort(key=lambda p: pattern_priority.index(p))

        pattern = matched_patterns[0]
        template_name = PATTERN_TEMPLATES[pattern]

        # Boost confidence for multiple matching patterns
        confidence = 0.85
        if len(matched_patterns) > 1:
            confidence = min(0.95, 0.85 + (len(matched_patterns) - 1) * 0.05)

        # Extra boost for OOP patterns in module 9
        if analysis.module == 'module_9_oop' and 'world_builder' in template_name:
            confidence = min(0.95, confidence + 0.05)

        return TemplateMatch(
            template_name=template_name,
            template_path=f'templates/narrative_templates/{template_name}.py',
            confidence=confidence,
            reasoning=f'Pattern match: {pattern}' +
                     (f' (+{len(matched_patterns)-1} more)' if len(matched_patterns) > 1 else '')
        )

    # Heuristic fallbacks
    # Special case: module_9 + complete_function + many functions = world builder
    if (analysis.module == 'module_9_oop' and
        analysis.exercise_type == 'complete_function' and
        analysis.function_count >= 10):
        return TemplateMatch(
            template_name='template_9_world_builder',
            template_path='templates/narrative_templates/template_9_world_builder.py',
            confidence=0.75,
            reasoning=f'Module 9 OOP with many functions ({analysis.function_count}), likely entity system'
        )

    if analysis.function_count >= 5:
        return TemplateMatch(
            template_name='template_2_incremental_builder',
            template_path='templates/narrative_templates/template_2_incremental_builder.py',
            confidence=0.7,
            reasoning=f'Many functions ({analysis.function_count}), likely incremental'
        )

    if analysis.exercise_type == 'complete_function':
        return TemplateMatch(
            template_name='template_6_specification_implementer',
            template_path='templates/narrative_templates/template_6_specification_implementer.py',
            confidence=0.75,
            reasoning='complete_function type usually needs specs'
        )

    if analysis.exercise_type == 'write_code':
        return TemplateMatch(
            template_name='template_3_role_assignment',
            template_path='templates/narrative_templates/template_3_role_assignment.py',
            confidence=0.6,
            reasoning='write_code with role assignment works well'
        )

    # Default fallback
    return TemplateMatch(
        template_name='template_1_tutorial_guide',
        template_path='templates/narrative_templates/template_1_tutorial_guide.py',
        confidence=0.5,
        reasoning='Default fallback - simple tutorial structure'
    )


# ============================================================
# NARRATIVE EXTRACTION
# ============================================================

def extract_narrative(exercise_path: str,
                     analysis: ExerciseAnalysis) -> List[NarrativeExtraction]:
    """
    Extract narrative text and suggest context blocks.

    Args:
        exercise_path: Path to exercise
        analysis: Exercise analysis

    Returns:
        List of NarrativeExtraction objects
    """
    extractions = []

    with open(exercise_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for location in analysis.narrative_locations:
        text = location['text']
        line_num = location.get('line_start', 0)
        loc_type = location['type']

        # Determine suggested context block based on content
        suggested_block = suggest_context_block(text, loc_type, line_num)

        # Skip if function suggests skipping (None for technical docstrings)
        if suggested_block is None:
            continue

        extractions.append(NarrativeExtraction(
            location=loc_type,
            line_num=line_num,
            text=text,
            suggested_block=suggested_block,
            context=f'{loc_type} at line {line_num}'
        ))

    return extractions


def suggest_context_block(text: str, location_type: str, line_num: int) -> str:
    """
    Suggest appropriate context block name for narrative text.

    Args:
        text: The narrative text
        location_type: Where it was found (file_docstring, etc.)
        line_num: Line number

    Returns:
        Suggested context block name
    """
    text_lower = text.lower()

    # File-level docstring patterns
    if location_type == 'file_docstring':
        if any(word in text_lower for word in ['welcome', 'at {{school}}', 'you are']):
            return 'CONTEXT_INTRO'
        if 'you\'ll learn' in text_lower or 'this teaches' in text_lower:
            return 'CONTEXT_LEARNING_OBJECTIVE'
        if 'scenario' in text_lower or 'situation' in text_lower:
            return 'CONTEXT_SCENARIO'
        return 'CONTEXT_INTRO'

    # Function docstring patterns
    if location_type == 'function_docstring':
        # Check for narrative content (not just technical specs)
        if 'example' in text_lower and ('story' in text_lower or 'scenario' in text_lower):
            return 'CONTEXT_EXAMPLE_NARRATIVE'
        if any(word in text_lower for word in ['your task', 'your job', 'you must']):
            return 'CONTEXT_STUDENT_TASK'
        if 'complete this' in text_lower or 'implement' in text_lower:
            return 'CONTEXT_STUDENT_TASK'
        # Skip function docstrings that are purely technical
        if 'args:' in text_lower and 'returns:' in text_lower:
            return None  # Signal to skip this
        return 'CONTEXT_FUNCTION_DESCRIPTION'

    # Comment patterns
    if location_type == 'multi_line_comment':
        if 'step' in text_lower or 'phase' in text_lower:
            return 'CONTEXT_PHASE_N'
        if 'error' in text_lower or 'bug' in text_lower or 'case' in text_lower:
            return 'CONTEXT_CASE_N'
        if 'hint' in text_lower or 'tip' in text_lower:
            return 'CONTEXT_GUIDANCE'
        return 'CONTEXT_NARRATIVE'

    return 'CONTEXT_PLACEHOLDER'


# ============================================================
# HARDCODED REFERENCE DETECTION
# ============================================================

def detect_hardcoded_references(exercise_path: str) -> List[HardcodedReference]:
    """
    Detect hardcoded theme-specific content.

    Args:
        exercise_path: Path to exercise

    Returns:
        List of HardcodedReference objects
    """
    references = []

    with open(exercise_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Build flat list of all hardcoded terms
    hardcoded_terms = {}
    for theme, categories in HARDCODED_REFERENCES.items():
        for category, terms in categories.items():
            for term in terms:
                hardcoded_terms[term] = category

    # Search each line
    for line_num, line in enumerate(lines, 1):
        # Skip comments (but not docstrings, which might have hardcoded refs in examples)
        if line.strip().startswith('#'):
            continue

        for term, category in hardcoded_terms.items():
            # Word boundary search
            pattern = r'\b' + re.escape(term) + r'\b'
            if re.search(pattern, line):
                suggested = suggest_placeholder_replacement(term, category)
                references.append(HardcodedReference(
                    line_num=line_num,
                    text=term,
                    category=category,
                    suggested_replacement=suggested,
                    confidence=0.9
                ))

    return references


def suggest_placeholder_replacement(term: str, category: str) -> str:
    """
    Suggest placeholder replacement for hardcoded reference.

    Args:
        term: The hardcoded term
        category: Category (house, character, etc.)

    Returns:
        Suggested placeholder
    """
    if category == 'houses':
        house_order = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
        if term in house_order:
            idx = house_order.index(term) + 1
            return f'{{{{house_{idx}}}}}'
        return '{{house_1}}'

    if category == 'characters':
        # Try to map to existing placeholders
        main_chars = ['Harry', 'Hermione', 'Ron']
        if term in main_chars:
            char_map = {'Harry': '{{hero}}', 'Hermione': '{{heroine}}',
                       'Ron': '{{friend_1}}'}
            return char_map.get(term, '{{hero}}')
        return '{{character}}'

    if category == 'locations':
        if 'school' in term.lower():
            return '{{school}}'
        return '{{location}}'

    if category == 'items':
        return '{{item}}'

    if category == 'spells':
        return '{{spell1}}'

    return '{{placeholder}}'


# ============================================================
# CONTEXT BLOCK CREATION
# ============================================================

def create_context_blocks(narrative_extractions: List[NarrativeExtraction]) -> Dict[str, Dict]:
    """
    Generate context block definitions from extracted narratives.

    Args:
        narrative_extractions: List of extracted narratives

    Returns:
        Dictionary of context block definitions
    """
    context_blocks = {}
    block_counter = {}  # Track multiples (CONTEXT_PHASE_1, CONTEXT_PHASE_2, etc.)

    for extraction in narrative_extractions:
        suggested = extraction.suggested_block

        # Handle numbered blocks (PHASE_N, TASK_N, CASE_N, etc.)
        # Only match _N at the end of the string to avoid false matches like CONTEXT_NARRATIVE
        if suggested.endswith('_N'):
            base = suggested[:-2]  # Remove last 2 characters (_N)
            if base not in block_counter:
                block_counter[base] = 1
            num = block_counter[base]
            block_name = f'{base}_{num}'
            block_counter[base] += 1
        else:
            block_name = suggested

        # Avoid duplicate keys - use more descriptive suffixes
        if block_name in context_blocks:
            # For function descriptions, use function name if available
            if 'function' in extraction.location:
                func_info = extraction.context.split('function_docstring')[0]
                block_name = f'{block_name}_{extraction.line_num}'
            else:
                # Otherwise append line number
                block_name = f'{block_name}_LINE{extraction.line_num}'

        context_blocks[block_name] = {
            'original_text': extraction.text,
            'location': extraction.location,
            'line_num': extraction.line_num,
            'context': extraction.context
        }

    return context_blocks


# ============================================================
# MAIN CONVERSION FUNCTION
# ============================================================

def convert_exercise(exercise_path: str, output_path: str = None,
                    dry_run: bool = False) -> ConversionReport:
    """
    Convert exercise to use template system.

    Args:
        exercise_path: Path to original exercise
        output_path: Path for converted exercise (optional)
        dry_run: If True, don't write files, just report

    Returns:
        ConversionReport with conversion details
    """
    print(f"\n{'='*60}")
    print(f"Converting: {exercise_path}")
    print(f"{'='*60}")

    # Step 1: Analyze
    print("Step 1: Analyzing exercise...")
    analysis = analyze_exercise(exercise_path)
    print(f"  Exercise type: {analysis.exercise_type}")
    print(f"  Module: {analysis.module}")
    print(f"  Patterns detected: {', '.join(analysis.patterns) if analysis.patterns else 'none'}")
    print(f"  Functions: {analysis.function_count}")
    print(f"  Existing placeholders: {len(analysis.placeholders_found)}")

    # Step 2: Match template
    print("\nStep 2: Matching template...")
    template_match = match_template(analysis)
    print(f"  Template: {template_match.template_name}")
    print(f"  Confidence: {template_match.confidence:.0%}")
    print(f"  Reasoning: {template_match.reasoning}")

    # Step 3: Extract narrative
    print("\nStep 3: Extracting narrative...")
    narrative_extractions = extract_narrative(exercise_path, analysis)
    print(f"  Narrative locations found: {len(narrative_extractions)}")

    # Step 4: Detect hardcoded references
    print("\nStep 4: Detecting hardcoded references...")
    hardcoded_refs = detect_hardcoded_references(exercise_path)
    print(f"  Hardcoded references found: {len(hardcoded_refs)}")
    for ref in hardcoded_refs[:5]:  # Show first 5
        print(f"    Line {ref.line_num}: '{ref.text}' -> {ref.suggested_replacement}")
    if len(hardcoded_refs) > 5:
        print(f"    ... and {len(hardcoded_refs) - 5} more")

    # Step 5: Create context blocks
    print("\nStep 5: Creating context blocks...")
    context_blocks = create_context_blocks(narrative_extractions)
    print(f"  Context blocks created: {len(context_blocks)}")
    for block_name in list(context_blocks.keys())[:5]:
        print(f"    {block_name}")
    if len(context_blocks) > 5:
        print(f"    ... and {len(context_blocks) - 5} more")

    # Detect exercise narrative template
    exercise_narrative, narrative_confidence, narrative_reasoning = detect_exercise_narrative_template(
        exercise_path,
        analysis.function_count,
        analysis.exercise_type,
        analysis.module,
        analysis
    )

    print(f"\nStep 6: Detecting exercise narrative template...")
    print(f"  Exercise Narrative: {exercise_narrative}")
    print(f"  Confidence: {narrative_confidence * 100:.0f}%")
    print(f"  Reasoning: {narrative_reasoning}")

    # Determine if manual review needed
    manual_review = (
        template_match.confidence < 0.7 or
        len(hardcoded_refs) > 10 or
        analysis.exercise_type == 'unknown'
    )

    # Build report
    report = ConversionReport(
        exercise_path=exercise_path,
        template_matched=template_match.template_name,
        confidence=template_match.confidence,
        context_blocks_created=list(context_blocks.keys()),
        hardcoded_references_found=[asdict(ref) for ref in hardcoded_refs],
        manual_review_needed=manual_review,
        notes=template_match.reasoning,
        warnings=[],
        exercise_narrative_template=exercise_narrative,
        exercise_sections=[]  # Will be populated in future enhancement
    )

    if manual_review:
        report.warnings.append('Manual review recommended due to low confidence or complexity')

    print(f"\n{'='*60}")
    print(f"Conversion {'simulation' if dry_run else 'complete'}")
    print(f"Manual review needed: {'Yes' if manual_review else 'No'}")
    print(f"{'='*60}")

    return report


# ============================================================
# CLI INTERFACE
# ============================================================

def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description='Convert exercises to use narrative templates'
    )

    parser.add_argument(
        '--input',
        help='Path to single exercise file to convert'
    )

    parser.add_argument(
        '--module',
        type=int,
        help='Module number to convert (e.g., 7 for module_7)'
    )

    parser.add_argument(
        '--all',
        action='store_true',
        help='Convert all exercises'
    )

    parser.add_argument(
        '--output',
        help='Output path for converted exercise'
    )

    parser.add_argument(
        '--output-dir',
        default='raw_exercises_converted',
        help='Output directory for batch conversions'
    )

    parser.add_argument(
        '--report-dir',
        default='conversion_reports',
        help='Directory for conversion reports'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Analyze and report only, do not write files'
    )

    args = parser.parse_args()

    # Validate arguments
    if not (args.input or args.module or args.all):
        parser.error('Must specify --input, --module, or --all')

    # Create report directory
    os.makedirs(args.report_dir, exist_ok=True)

    # Single file conversion
    if args.input:
        report = convert_exercise(args.input, args.output, args.dry_run)

        # Write report
        report_path = Path(args.report_dir) / f'{Path(args.input).stem}_report.json'
        with open(report_path, 'w') as f:
            json.dump(asdict(report), f, indent=2)
        print(f"\nReport written to: {report_path}")

    # Module conversion
    elif args.module:
        raw_exercises = Path('raw_exercises')
        module_pattern = f'module_{args.module}_*'

        module_dirs = list(raw_exercises.glob(module_pattern))
        if not module_dirs:
            print(f"Error: No module found matching {module_pattern}")
            return

        print(f"\nConverting Module {args.module}...")
        print(f"Found: {module_dirs[0]}")

        # Find all Python files in module
        exercise_files = list(module_dirs[0].rglob('*.py'))
        print(f"Found {len(exercise_files)} exercise files")

        reports = []
        for ex_file in exercise_files:
            report = convert_exercise(str(ex_file), dry_run=args.dry_run)
            reports.append(report)

        # Write summary report
        summary_path = Path(args.report_dir) / f'module_{args.module}_summary.json'
        with open(summary_path, 'w') as f:
            json.dump([asdict(r) for r in reports], f, indent=2)
        print(f"\nSummary report written to: {summary_path}")

    # All exercises conversion
    elif args.all:
        print("\nConverting all exercises...")
        print("This may take several minutes...")

        raw_exercises = Path('raw_exercises')
        exercise_files = list(raw_exercises.rglob('*.py'))

        # Filter out __init__.py and other non-exercise files
        exercise_files = [f for f in exercise_files if not f.name.startswith('__')]

        print(f"Found {len(exercise_files)} exercise files")

        reports = []
        for i, ex_file in enumerate(exercise_files, 1):
            print(f"\n[{i}/{len(exercise_files)}]")
            report = convert_exercise(str(ex_file), dry_run=args.dry_run)
            reports.append(report)

        # Write master report
        master_path = Path(args.report_dir) / 'all_exercises_report.json'
        with open(master_path, 'w') as f:
            json.dump([asdict(r) for r in reports], f, indent=2)

        # Print summary statistics
        print("\n" + "="*60)
        print("CONVERSION SUMMARY")
        print("="*60)
        print(f"Total exercises: {len(reports)}")
        print(f"High confidence (>0.85): {sum(1 for r in reports if r.confidence > 0.85)}")
        print(f"Medium confidence (0.7-0.85): {sum(1 for r in reports if 0.7 <= r.confidence <= 0.85)}")
        print(f"Low confidence (<0.7): {sum(1 for r in reports if r.confidence < 0.7)}")
        print(f"Manual review needed: {sum(1 for r in reports if r.manual_review_needed)}")
        print(f"Total hardcoded refs: {sum(len(r.hardcoded_references_found) for r in reports)}")
        print(f"\nMaster report written to: {master_path}")


if __name__ == '__main__':
    main()
