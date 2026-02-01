"""
Exercise Narrative Template: Spec Implementation (Theme-Agnostic v2)

UNIVERSAL STRUCTURE - Works with ANY theme via placeholder substitution.

Build to detailed specifications/requirements - professional project approach.
Pattern: Requirements → Feature 1 → Feature 2 → Feature 3 → Testing → Delivery

Compatible themes: Fantasy, Soccer, Sci-fi, Detective, Military, Professional Coding, etc.
"""

TEMPLATE_INFO = {
    'id': 'exercise_narrative_spec_implementation',
    'name': 'Spec Implementation',
    'version': 2,
    'usage_percentage': 0.02,  # Actual from corpus (predicted 18% was for complete_function type)
    'best_for': 'Detailed specification exercises, professional project structure',
    'pattern': 'Requirements → Core Features → Advanced Features → Testing',
    'theme_agnostic': True
}

# =============================================================================
# UNIVERSAL PLACEHOLDERS REQUIRED
# =============================================================================
# Role & Context:
#   - ROLE_TITLE, MENTOR_TITLE, WORKSPACE
# Project & Scope:
#   - PROJECT_TYPE, PROJECT_SCALE, GOAL
# Components & Tasks:
#   - COMPONENT_PLURAL, COMPONENT_SINGULAR, TASK_NOUN
# Progress & Feedback:
#   - SECTION_ICON, SUCCESS_WORD, CELEBRATION
# Narrative Flavor:
#   - OPENING_FLAVOR, CLOSING_FLAVOR
#
# Special for specs:
#   - CLIENT (e.g., client/council/command/manager/lead)
#   - DELIVERABLE (e.g., project/quest/mission/match plan/system)
# =============================================================================

OPENING_TEMPLATE = '''"""
{exercise_title}

{{{{ROLE_TITLE}}}} Assignment: {project_name}

You've been assigned to build a {{{{PROJECT_SCALE}}}} {{{{DELIVERABLE}}}}.

Project Specifications:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Assigned by: {{{{CLIENT}}}}
Scope: {project_scope}
Priority: {priority_level}

Requirements:
{requirement_list}

Success Criteria:
{success_criteria}

{{{{OPENING_FLAVOR}}}}

{{{{SECTION_ICON}}}} Time to start implementation!
"""
'''

FEATURE_SECTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Requirement {num}: {feature_name}
# {separator}

{{{{FEATURE_{num}_SPEC}}}}
"""
Specification Details:

Name: {feature_name}
Priority: {priority}
Complexity: {complexity}

Requirements:
- {req_1}
- {req_2}
- {req_3}

Acceptance Criteria:
- {criteria_1}
- {criteria_2}
"""

# Implementation guidance:
# {implementation_guidance}
'''

TESTING_SECTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Quality Verification
# {separator}

{{{{TESTING_INTRO}}}}
# Time to verify your implementation meets all specifications!
# {testing_guidance}

# Verification Plan:
{test_plan}
'''

DELIVERY_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} {{{{DELIVERABLE_TITLE}}}}
# {separator}

{{{{DELIVERY_CLOSING}}}}
# Status: ✓ COMPLETE
#
# {{{{COMPONENT_PLURAL}}}} Implemented:
# {feature_summary}
#
# Quality Metrics:
# - Completeness: {completeness}%
# - Specification Adherence: {adherence}%
#
# {{{{CLOSING_FLAVOR}}}}
#
# {{{{CELEBRATION}}}}


def main():
    """Verify all specifications."""
    print("{{{{SECTION_ICON}}}} Verification: {exercise_title}")
    print("="*60)

    # Verify features
    {feature_test_calls}

    print("="*60)
    print("✓ All specifications met!")
    print("{{{{CELEBRATION}}}}")


if __name__ == "__main__":
    main()
'''

# =============================================================================
# SPEC STRUCTURE (Universal Logic)
# =============================================================================

def generate_spec_structure(task_count: int) -> list:
    """
    Generate specification implementation phases.

    Universal algorithm - Pattern: Core features → Advanced features → Testing
    Distribution: ~75% features, ~25% testing

    Args:
        task_count: Total number of tasks

    Returns:
        List of (section_type, num, task_num, priority) tuples
    """
    if task_count <= 4:
        # Simple: 3 features, 1 test
        return [
            ('feature', 1, 1, 'core'),
            ('feature', 2, 2, 'core'),
            ('feature', 3, 3, 'core'),
            ('testing', 1, 4, 'all'),
        ]

    elif task_count <= 8:
        # Standard: Features then testing
        test_count = max(1, task_count // 4)
        feature_count = task_count - test_count

        features = []
        for i in range(1, feature_count + 1):
            priority = 'core' if i <= (feature_count // 2) else 'advanced'
            features.append(('feature', i, i, priority))

        tests = [('testing', i, feature_count + i, 'all')
                 for i in range(1, test_count + 1)]

        return features + tests

    else:
        # Large: Multiple priority tiers
        test_count = max(2, task_count // 4)
        feature_count = task_count - test_count

        features = []
        for i in range(1, feature_count + 1):
            if i <= feature_count // 3:
                priority = 'core'
            elif i <= (2 * feature_count) // 3:
                priority = 'standard'
            else:
                priority = 'advanced'

            features.append(('feature', i, i, priority))

        tests = [('testing', i, feature_count + i, 'all')
                 for i in range(1, test_count + 1)]

        return features + tests


def get_priority_markers() -> dict:
    """Get universal priority markers."""
    return {
        'core': '🔴 HIGH',
        'standard': '🟡 MEDIUM',
        'advanced': '🟢 LOW',
    }


def get_complexity_levels() -> list:
    """Get universal complexity levels."""
    return ['Simple', 'Moderate', 'Complex', 'Advanced']


def get_separator(use_icon: bool = True, icon: str = "📋") -> str:
    """Get section separator."""
    if use_icon and icon:
        return f"# {icon * 30}"
    else:
        return "# " + "━" * 60


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
    Generate complete specification exercise structure.

    THEME-AGNOSTIC: Uses universal placeholders filled by theme_vars.

    Args:
        exercise_title: Name of the exercise
        task_count: Number of tasks
        theme_vars: Dictionary from theme mapping JSON
        **kwargs: Additional options

    Returns:
        Dictionary with exercise structure
    """
    sections = generate_spec_structure(task_count)
    priority_markers = get_priority_markers()

    feature_count = sum(1 for s in sections if s[0] == 'feature')
    testing_count = sum(1 for s in sections if s[0] == 'testing')

    icon = theme_vars.get('SECTION_ICON', '📋') if theme_vars else '📋'
    separator = get_separator(use_icon=True, icon=icon)

    structure = {
        'template_id': 'exercise_narrative_spec_implementation',
        'template_version': 2,
        'exercise_title': exercise_title,
        'task_count': task_count,
        'feature_count': feature_count,
        'testing_count': testing_count,
        'theme_agnostic': True,
        'sections': [],
        'opening': {
            'template': OPENING_TEMPLATE,
            'required_placeholders': [
                'ROLE_TITLE',
                'PROJECT_SCALE',
                'DELIVERABLE',
                'CLIENT',
                'OPENING_FLAVOR',
                'SECTION_ICON'
            ]
        },
        'delivery': {
            'template': DELIVERY_TEMPLATE,
            'required_placeholders': [
                'SECTION_ICON',
                'COMPONENT_PLURAL',
                'CLOSING_FLAVOR',
                'CELEBRATION'
            ]
        }
    }

    # Generate feature and testing sections
    for section_type, num, task_num, priority in sections:
        if section_type == 'feature':
            section = {
                'type': 'feature',
                'number': num,
                'task_num': task_num,
                'priority': priority,
                'priority_marker': priority_markers.get(priority, ''),
                'template': FEATURE_SECTION_TEMPLATE,
                'required_placeholders': [
                    'SECTION_ICON',
                    f'FEATURE_{num}_SPEC'
                ]
            }
        else:  # testing
            section = {
                'type': 'testing',
                'number': num,
                'task_num': task_num,
                'priority': 'all',
                'template': TESTING_SECTION_TEMPLATE,
                'required_placeholders': [
                    'SECTION_ICON',
                    'TESTING_INTRO'
                ]
            }

        structure['sections'].append(section)

    return structure


# =============================================================================
# THEME VARIABLE HELPER
# =============================================================================

def get_default_spec_vars() -> dict:
    """
    Get default spec-specific theme variables.

    These supplement the standard theme variables for spec narratives.
    """
    return {
        'CLIENT': 'client',
        'DELIVERABLE': 'project',
        'DELIVERABLE_TITLE': 'Project Complete'
    }


if __name__ == "__main__":
    import json

    print("=" * 70)
    print("Spec Implementation Template (Theme-Agnostic v2)")
    print("=" * 70)

    structure = generate_exercise_structure(
        exercise_title="User Authentication System",
        task_count=10
    )

    print(f"\nExercise: {structure['exercise_title']}")
    print(f"Tasks: {structure['task_count']}")
    print(f"Features: {structure['feature_count']}")
    print(f"Testing: {structure['testing_count']}")
    print(f"\nImplementation plan:")
    for section in structure['sections']:
        if section['type'] == 'feature':
            print(f"  Task {section['task_num']}: Feature {section['number']} - {section['priority_marker']}")
        else:
            print(f"  Task {section['task_num']}: Testing {section['number']}")

    # Test with themes
    try:
        theme_examples = {
            'fantasy_magic.json': ('The Council', 'magical quest'),
            'soccer_academy.json': ('Manager', 'training plan'),
            'professional_coding.json': ('Tech Lead', 'software project')
        }

        print("\n" + "=" * 70)
        print("Same Spec Structure, Different Contexts:")
        print("=" * 70)

        for filename, (client, deliverable) in theme_examples.items():
            with open(f'../../theme_mappings/{filename}', 'r', encoding='utf-8') as f:
                theme_data = json.load(f)
                theme_vars = theme_data['narrative_variables']

            print(f"\n{theme_data['theme_name']}:")
            print(f"  Role: {theme_vars['ROLE_TITLE']}")
            print(f"  Assigned by: {client}")
            print(f"  Deliverable: {deliverable}")
            print(f"  Goal: {theme_vars['GOAL']}")

    except FileNotFoundError:
        pass

    print("\n" + "=" * 70)
    print("Professional structure works for any theme!")
    print("=" * 70)
