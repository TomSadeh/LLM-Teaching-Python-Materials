"""
Exercise Narrative Template: World Builder (Theme-Agnostic v2)

UNIVERSAL STRUCTURE - Works with ANY theme via placeholder substitution.

Build a system piece by piece - ideal for OOP exercises with entities.
Pattern: World Intro → Entities → Interactions → Systems → Complete World

Compatible themes: Fantasy, Soccer, Sci-fi, Detective, Military, Professional Coding, etc.
"""

TEMPLATE_INFO = {
    'id': 'exercise_narrative_world_builder',
    'name': 'World Builder',
    'version': 2,
    'usage_percentage': 0.08,
    'best_for': 'OOP exercises, entity systems, simulations, complex builders',
    'pattern': 'Setup → Entities (40%) → Interactions (40%) → Systems (20%)',
    'theme_agnostic': True
}

# =============================================================================
# UNIVERSAL PLACEHOLDERS REQUIRED
# =============================================================================
# Role & Context:
#   - ROLE_TITLE, WORKSPACE
# Project & Scope:
#   - PROJECT_TYPE, PROJECT_SCALE
# Components & Tasks:
#   - COMPONENT_PLURAL, COMPONENT_SINGULAR
# Progress & Feedback:
#   - SECTION_ICON, SUCCESS_WORD, CELEBRATION
# Narrative Flavor:
#   - OPENING_FLAVOR, CLOSING_FLAVOR
#
# Special for builder:
#   - ENTITY_NOUN (e.g., entity/player/module/agent/unit/component)
#   - SYSTEM_NOUN (e.g., system/mechanism/framework/infrastructure)
# =============================================================================

OPENING_TEMPLATE = '''"""
{exercise_title}

{{{{ROLE_TITLE}}}} Builder: {project_name}

Welcome, System Builder! You'll construct a {{{{PROJECT_SCALE}}}} {{{{PROJECT_TYPE}}}}
by building {task_count} interconnected {{{{COMPONENT_PLURAL}}}}.

Building Phases:
{{{{SECTION_ICON}}}} Phase 1: {entity_noun_plural} (Foundation)
{{{{SECTION_ICON}}}} Phase 2: Interactions (Connections)
{{{{SECTION_ICON}}}} Phase 3: Systems (Integration)

Your {{{{PROJECT_TYPE}}}} will feature:
- {feature_1}
- {feature_2}
- {feature_3}

{{{{OPENING_FLAVOR}}}}

Let's start building!
"""
'''

ENTITY_SECTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Phase 1: Building {entity_type_plural}
# {separator}

{{{{ENTITY_SECTION_INTRO}}}}
# Every {{{{PROJECT_TYPE}}}} needs foundational {entity_description}.
# These {entity_noun_plural} are the building blocks of your system.
#
# Build them carefully - everything else depends on these foundations.
#
# {entity_guidance}
'''

INTERACTION_SECTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Phase 2: Creating Interactions
# {separator}

{{{{INTERACTION_SECTION_INTRO}}}}
# Now that {entity_noun_plural} exist, make them work together!
# Define how they communicate, cooperate, and interact.
#
# {interaction_description}
#
# Design principle: {interaction_principle}
'''

SYSTEMS_SECTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Phase 3: Integrating Systems
# {separator}

{{{{SYSTEMS_SECTION_INTRO}}}}
# {{{{SUCCESS_WORD}}}}! The components are ready.
# Now create the {{{{SYSTEM_NOUN}}}}s that bring everything together.
#
# Complex behavior emerges from simple interactions.
# These {{{{SYSTEM_NOUN}}}}s orchestrate all the parts.
#
# {systems_guidance}
'''

COMPLETION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Build Complete!
# {separator}

{{{{WORLD_CLOSING}}}}
# {{{{SUCCESS_WORD}}}}! Your {{{{PROJECT_TYPE}}}} is fully operational.
#
# System Components:
# - {component_summary_1}
# - {component_summary_2}
# - {component_summary_3}
#
# Skills Mastered:
# - {skill_1}
# - {skill_2}
# - {skill_3}
#
# {{{{CLOSING_FLAVOR}}}}
#
# {{{{CELEBRATION}}}}


def main():
    """Test the complete system."""
    print("{{{{SECTION_ICON}}}} System Test: {exercise_title}")
    print("="*60)

    # Initialize {entity_noun_plural}
    print("\\nPhase 1: Creating {entity_noun_plural}...")
    {entity_creation_calls}

    # Test interactions
    print("\\nPhase 2: Testing interactions...")
    {interaction_calls}

    # Run systems
    print("\\nPhase 3: Running systems...")
    {system_calls}

    print("="*60)
    print("{{{{CELEBRATION}}}}")


if __name__ == "__main__":
    main()
'''

# =============================================================================
# BUILDER STRUCTURE (Universal Logic)
# =============================================================================

def generate_world_structure(task_count: int) -> list:
    """
    Generate system building phases.

    Universal algorithm - Pattern: Entities → Interactions → Systems
    Distribution: ~40% entities, ~40% interactions, ~20% systems

    Args:
        task_count: Total number of tasks

    Returns:
        List of (phase_name, start_task, end_task) tuples
    """
    if task_count <= 6:
        # Simple system: equal thirds
        third = task_count // 3
        return [
            ('entities', 1, third),
            ('interactions', third + 1, third * 2),
            ('systems', third * 2 + 1, task_count),
        ]

    elif task_count <= 12:
        # Standard system: 40% entities, 40% interactions, 20% systems
        entity_end = max(2, int(task_count * 0.4))
        interaction_end = min(task_count - 1, int(task_count * 0.8))

        return [
            ('entities', 1, entity_end),
            ('interactions', entity_end + 1, interaction_end),
            ('systems', interaction_end + 1, task_count),
        ]

    else:
        # Complex system: Add foundation phase
        # 30% foundation, 30% entities, 25% interactions, 15% systems
        foundation_end = max(2, int(task_count * 0.3))
        entity_end = int(task_count * 0.6)
        interaction_end = int(task_count * 0.85)

        return [
            ('foundation', 1, foundation_end),
            ('entities', foundation_end + 1, entity_end),
            ('interactions', entity_end + 1, interaction_end),
            ('systems', interaction_end + 1, task_count),
        ]


def get_phase_icons() -> dict:
    """Get universal phase icons (fallback if theme doesn't provide)."""
    return {
        'foundation': '🏗️',
        'entities': '🔨',
        'interactions': '🔗',
        'systems': '⚙️',
    }


def get_separator(use_icon: bool = True, icon: str = "🌍") -> str:
    """Get section separator."""
    if use_icon and icon:
        return f"# {icon * 30}"
    else:
        return "# " + "═" * 60


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
    Generate complete builder exercise structure.

    THEME-AGNOSTIC: Uses universal placeholders filled by theme_vars.

    Args:
        exercise_title: Name of the exercise
        task_count: Number of tasks
        theme_vars: Dictionary from theme mapping JSON
        **kwargs: Additional options

    Returns:
        Dictionary with exercise structure
    """
    phases = generate_world_structure(task_count)
    phase_icons = get_phase_icons()

    icon = theme_vars.get('SECTION_ICON', '🌍') if theme_vars else '🌍'
    separator = get_separator(use_icon=True, icon=icon)

    structure = {
        'template_id': 'exercise_narrative_world_builder',
        'template_version': 2,
        'exercise_title': exercise_title,
        'task_count': task_count,
        'phase_count': len(phases),
        'theme_agnostic': True,
        'phases': [],
        'opening': {
            'template': OPENING_TEMPLATE,
            'required_placeholders': [
                'ROLE_TITLE',
                'PROJECT_SCALE',
                'PROJECT_TYPE',
                'COMPONENT_PLURAL',
                'SECTION_ICON',
                'OPENING_FLAVOR'
            ]
        },
        'completion': {
            'template': COMPLETION_TEMPLATE,
            'required_placeholders': [
                'SECTION_ICON',
                'SUCCESS_WORD',
                'PROJECT_TYPE',
                'CLOSING_FLAVOR',
                'CELEBRATION'
            ]
        }
    }

    # Generate phases
    for phase_name, start_task, end_task in phases:
        phase_task_count = end_task - start_task + 1

        if phase_name == 'entities' or phase_name == 'foundation':
            template = ENTITY_SECTION_TEMPLATE
            placeholder_key = 'ENTITY_SECTION_INTRO'
        elif phase_name == 'interactions':
            template = INTERACTION_SECTION_TEMPLATE
            placeholder_key = 'INTERACTION_SECTION_INTRO'
        else:  # systems
            template = SYSTEMS_SECTION_TEMPLATE
            placeholder_key = 'SYSTEMS_SECTION_INTRO'

        phase = {
            'name': phase_name.title(),
            'phase_type': phase_name,
            'task_range': (start_task, end_task),
            'task_count': phase_task_count,
            'icon': phase_icons.get(phase_name, '🔨'),
            'template': template,
            'required_placeholders': [
                'SECTION_ICON',
                'PROJECT_TYPE',
                placeholder_key
            ]
        }

        structure['phases'].append(phase)

    return structure


# =============================================================================
# THEME VARIABLE HELPER
# =============================================================================

def get_default_builder_vars() -> dict:
    """
    Get default builder-specific theme variables.

    These supplement the standard theme variables for builder narratives.
    """
    return {
        'ENTITY_NOUN': 'entity',
        'ENTITY_NOUN_PLURAL': 'entities',
        'SYSTEM_NOUN': 'system'
    }


if __name__ == "__main__":
    import json

    print("=" * 70)
    print("World Builder Template (Theme-Agnostic v2)")
    print("=" * 70)

    structure = generate_exercise_structure(
        exercise_title="Build a Game Engine",
        task_count=15
    )

    print(f"\nExercise: {structure['exercise_title']}")
    print(f"Tasks: {structure['task_count']}")
    print(f"Phases: {structure['phase_count']}")
    print(f"\nBuild phases:")
    for phase in structure['phases']:
        print(f"  {phase['icon']} {phase['name']}: "
              f"Tasks {phase['task_range'][0]}-{phase['task_range'][1]} "
              f"({phase['task_count']} tasks)")

    # Test with themes
    try:
        theme_examples = {
            'fantasy_magic.json': ('magical creatures', 'enchantment systems'),
            'soccer_academy.json': ('team players', 'tactical systems'),
            'professional_coding.json': ('software modules', 'integration systems')
        }

        print("\n" + "=" * 70)
        print("Same Builder Structure, Different Contexts:")
        print("=" * 70)

        for filename, (entities, systems) in theme_examples.items():
            with open(f'../../theme_mappings/{filename}', 'r', encoding='utf-8') as f:
                theme_data = json.load(f)
                theme_vars = theme_data['narrative_variables']

            print(f"\n{theme_data['theme_name']}:")
            print(f"  Builder: {theme_vars['ROLE_TITLE']}")
            print(f"  Building: {theme_vars['PROJECT_TYPE']}")
            print(f"  Phase 1: Create {entities}")
            print(f"  Phase 2: Define interactions")
            print(f"  Phase 3: Build {systems}")

    except FileNotFoundError:
        pass

    print("\n" + "=" * 70)
    print("Perfect for OOP exercises - same structure, any theme!")
    print("=" * 70)
