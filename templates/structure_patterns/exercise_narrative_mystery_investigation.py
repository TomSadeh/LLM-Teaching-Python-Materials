"""
Exercise Narrative Template: Mystery Investigation (Theme-Agnostic v2)

UNIVERSAL STRUCTURE - Works with ANY theme via placeholder substitution.

Debug/discover pattern with evidence gathering and problem-solving.
Pattern: Mystery Setup → Evidence 1 → Evidence 2 → Evidence 3 → Solution

Compatible themes: Fantasy, Soccer, Sci-fi, Detective, Military, Professional Coding, etc.
"""

TEMPLATE_INFO = {
    'id': 'exercise_narrative_mystery_investigation',
    'name': 'Mystery Investigation',
    'version': 2,
    'usage_percentage': 0.08,
    'best_for': 'Debug exercises, error decoding, code analysis, problem-solving',
    'pattern': 'Mystery Setup → Evidence → Evidence → Evidence → Solution',
    'theme_agnostic': True
}

# =============================================================================
# UNIVERSAL PLACEHOLDERS REQUIRED
# =============================================================================
# Role & Context:
#   - ROLE_TITLE, WORKSPACE
# Project & Scope:
#   - PROJECT_TYPE
# Components & Tasks:
#   - COMPONENT_PLURAL, TASK_NOUN
# Progress & Feedback:
#   - SECTION_ICON, SUCCESS_WORD, CELEBRATION
# Narrative Flavor:
#   - OPENING_FLAVOR, CLOSING_FLAVOR
#
# Special for investigation:
#   - EVIDENCE_NOUN (e.g., clue/data point/trace/lead/diagnostic)
#   - SOLVE_VERB (e.g., solve/fix/decode/resolve/complete)
# =============================================================================

OPENING_TEMPLATE = '''"""
{exercise_title}

{{{{ROLE_TITLE}}}} Investigation: {mystery_name}

Something requires investigation in your {{{{WORKSPACE}}}}...

The Challenge:
{mystery_description}

Your mission: {investigation_goal}

Investigation Tools:
- {tool_1}
- {tool_2}
- {tool_3}

{{{{OPENING_FLAVOR}}}}

{{{{SECTION_ICON}}}} Begin your investigation!
"""
'''

EVIDENCE_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Evidence {num}: {evidence_name}
# {separator}

{{{{EVIDENCE_{num}_INTRO}}}}
# Investigation Note: {investigation_note}
# What this reveals: {evidence_reveals}

# Evidence:
{code_or_data}

# Your task: {analysis_task}
'''

SOLUTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Solution: Putting It Together
# {separator}

{{{{SOLUTION_INTRO}}}}
# {{{{SUCCESS_WORD}}}}! You've gathered all the evidence.
# Now apply your findings to {{{{SOLVE_VERB}}}} the challenge.
#
# {solution_guidance}

# Final task: {final_task_description}
'''

CLOSING_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Investigation Complete!
# {separator}

{{{{INVESTIGATION_CLOSING}}}}
# Investigation Status: RESOLVED
#
# Key Discoveries:
# - {discovery_1}
# - {discovery_2}
# - {discovery_3}
#
# Skills Developed:
# - {skill_1}
# - {skill_2}
#
# {{{{CLOSING_FLAVOR}}}}
#
# {{{{CELEBRATION}}}}


def main():
    """Run investigation."""
    print("{{{{SECTION_ICON}}}} Investigation: {exercise_title}")
    print("="*60)
    print("Analyzing evidence...")

    {evidence_test_calls}

    print("="*60)
    print("{{{{CELEBRATION}}}}")


if __name__ == "__main__":
    main()
'''

# =============================================================================
# INVESTIGATION STRUCTURE (Universal Logic)
# =============================================================================

def generate_investigation_structure(task_count: int) -> list:
    """
    Generate evidence gathering sequence.

    Universal algorithm - Pattern: Each task is evidence, last 1-2 are solution.

    Args:
        task_count: Total number of tasks

    Returns:
        List of (section_type, num, task_num) tuples
    """
    if task_count <= 3:
        # Simple: 2 evidence pieces, 1 solution
        return [
            ('evidence', 1, 1),
            ('evidence', 2, 2),
            ('solution', 1, 3),
        ]

    elif task_count <= 6:
        # Standard: Most are evidence, last is solution
        solution_count = 1
        evidence_count = task_count - solution_count

        structure = [('evidence', i, i) for i in range(1, evidence_count + 1)]
        structure.append(('solution', 1, task_count))
        return structure

    else:
        # Large: Multiple evidence pieces, 1-2 solution tasks
        solution_count = min(2, task_count // 4)
        evidence_count = task_count - solution_count

        structure = [('evidence', i, i) for i in range(1, evidence_count + 1)]
        for i in range(1, solution_count + 1):
            structure.append(('solution', i, evidence_count + i))

        return structure


def get_evidence_types() -> list:
    """
    Get universal evidence type names.

    These are theme-agnostic investigation steps.
    """
    return [
        "Initial Assessment",
        "Pattern Analysis",
        "Root Cause",
        "Supporting Data",
        "Validation Check",
        "Edge Case",
        "Final Verification"
    ]


def get_separator(use_icon: bool = True, icon: str = "🔍") -> str:
    """Get section separator."""
    if use_icon and icon:
        return f"# {icon * 30}"
    else:
        return "# " + "─" * 60


# =============================================================================
# FULL EXERCISE GENERATOR (Theme-Agnostic)
# =============================================================================

def generate_exercise_structure(
    exercise_title: str,
    task_count: int,
    theme_vars: dict = None,
    **kwargs
) -> dict:
    """
    Generate complete investigation exercise structure.

    THEME-AGNOSTIC: Uses universal placeholders filled by theme_vars.

    Args:
        exercise_title: Name of the exercise
        task_count: Number of tasks
        theme_vars: Dictionary from theme mapping JSON
        **kwargs: Additional options

    Returns:
        Dictionary with exercise structure
    """
    sections = generate_investigation_structure(task_count)
    evidence_types = get_evidence_types()

    evidence_count = sum(1 for s in sections if s[0] == 'evidence')
    solution_count = sum(1 for s in sections if s[0] == 'solution')

    icon = theme_vars.get('SECTION_ICON', '🔍') if theme_vars else '🔍'
    separator = get_separator(use_icon=True, icon=icon)

    structure = {
        'template_id': 'exercise_narrative_mystery_investigation',
        'template_version': 2,
        'exercise_title': exercise_title,
        'task_count': task_count,
        'evidence_count': evidence_count,
        'solution_count': solution_count,
        'theme_agnostic': True,
        'sections': [],
        'opening': {
            'template': OPENING_TEMPLATE,
            'required_placeholders': [
                'ROLE_TITLE',
                'WORKSPACE',
                'SECTION_ICON',
                'OPENING_FLAVOR'
            ]
        },
        'closing': {
            'template': CLOSING_TEMPLATE,
            'required_placeholders': [
                'SECTION_ICON',
                'CLOSING_FLAVOR',
                'CELEBRATION'
            ]
        }
    }

    # Generate evidence/solution sections
    for section_type, num, task_num in sections:
        if section_type == 'evidence':
            evidence_name = evidence_types[(num - 1) % len(evidence_types)]
            section = {
                'type': 'evidence',
                'number': num,
                'task_num': task_num,
                'name': evidence_name,
                'template': EVIDENCE_TEMPLATE,
                'required_placeholders': [
                    'SECTION_ICON',
                    f'EVIDENCE_{num}_INTRO'
                ]
            }
        else:
            section = {
                'type': 'solution',
                'number': num,
                'task_num': task_num,
                'name': f'Solution {num}' if solution_count > 1 else 'Solution',
                'template': SOLUTION_TEMPLATE,
                'required_placeholders': [
                    'SECTION_ICON',
                    'SUCCESS_WORD',
                    'SOLUTION_INTRO',
                    'SOLVE_VERB'
                ]
            }

        structure['sections'].append(section)

    return structure


# =============================================================================
# THEME VARIABLE HELPER
# =============================================================================

def get_default_investigation_vars() -> dict:
    """
    Get default investigation-specific theme variables.

    These supplement the standard theme variables for investigation narratives.
    """
    return {
        'EVIDENCE_NOUN': 'evidence',
        'SOLVE_VERB': 'resolve'
    }


if __name__ == "__main__":
    import json

    print("=" * 70)
    print("Mystery Investigation Template (Theme-Agnostic v2)")
    print("=" * 70)

    structure = generate_exercise_structure(
        exercise_title="Debug the Authentication System",
        task_count=7
    )

    print(f"\nExercise: {structure['exercise_title']}")
    print(f"Tasks: {structure['task_count']}")
    print(f"Evidence pieces: {structure['evidence_count']}")
    print(f"Solution steps: {structure['solution_count']}")
    print(f"\nInvestigation flow:")
    for section in structure['sections']:
        if section['type'] == 'evidence':
            print(f"  Task {section['task_num']}: Evidence {section['number']} - {section['name']}")
        else:
            print(f"  Task {section['task_num']}: {section['name']}")

    # Test with themes
    try:
        themes_config = {
            'fantasy_magic.json': ('EVIDENCE_NOUN', 'clue', 'SOLVE_VERB', 'solve'),
            'professional_coding.json': ('EVIDENCE_NOUN', 'diagnostic', 'SOLVE_VERB', 'fix'),
        }

        print("\n" + "=" * 70)
        print("Investigation adapted to different themes:")
        print("=" * 70)

        for filename, extras in themes_config.items():
            with open(f'../../theme_mappings/{filename}', 'r', encoding='utf-8') as f:
                theme_data = json.load(f)
                theme_vars = theme_data['narrative_variables']

            print(f"\n{theme_data['theme_name']}:")
            print(f"  Investigator: {theme_vars['ROLE_TITLE']}")
            print(f"  Location: {theme_vars['WORKSPACE']}")
            print(f"  Gathering: {extras[1]} (instead of generic 'evidence')")
            print(f"  Action: {extras[3]} the mystery")

    except FileNotFoundError:
        pass

    print("\n" + "=" * 70)
    print("Note: Themes can customize EVIDENCE_NOUN and SOLVE_VERB")
    print("for investigation-specific flavor!")
    print("=" * 70)
