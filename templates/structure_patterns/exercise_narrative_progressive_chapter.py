"""
Exercise Narrative Template: Progressive Chapter (Theme-Agnostic v2)

UNIVERSAL STRUCTURE - Works with ANY theme via placeholder substitution.

This template divides tasks into progressive sections with increasing difficulty.
Theme creators provide a theme mapping JSON to customize all {{PLACEHOLDER}} variables.

Compatible themes: Fantasy, Soccer, Sci-fi, Detective, Military, Professional Coding, etc.
"""

# Template metadata
TEMPLATE_INFO = {
    'id': 'exercise_narrative_progressive_chapter',
    'name': 'Progressive Chapter',
    'version': 2,  # Theme-agnostic version
    'usage_percentage': 0.21,  # Actual usage from corpus
    'best_for': 'Multi-task exercises with clear progression',
    'min_tasks': 6,
    'sections': '2-5',
    'theme_agnostic': True
}

# =============================================================================
# UNIVERSAL PLACEHOLDERS REQUIRED
# =============================================================================
# This template requires these variables from theme mapping:
#
# Role & Context:
#   - ROLE_TITLE (e.g., Wizard/Coach/Developer/Detective/Commander)
#   - WORKSPACE (e.g., realm/pitch/codebase/precinct/base)
#
# Project & Scope:
#   - PROJECT_TYPE (e.g., kingdom/squad/system/case/operation)
#   - PROJECT_SCALE (e.g., grand/competitive/production/complex/tactical)
#
# Components & Tasks:
#   - COMPONENT_PLURAL (e.g., spells/drills/features/clues/objectives)
#   - TASK_NOUN (e.g., incantation/play/function/lead/order)
#
# Progress & Feedback:
#   - SECTION_ICON (e.g., ✨/⚽/💻/🔍/🎯)
#   - SUCCESS_WORD (e.g., Excellent/Great/Success/Solved/Completed)
#   - CELEBRATION (e.g., Well done!/Goal!/Deployed!/Case closed!/Mission complete!)
#   - PROGRESS_UNIT (e.g., level/session/version/evidence/phase)
#
# Narrative Flavor:
#   - OPENING_FLAVOR (theme-specific hook)
#   - CLOSING_FLAVOR (theme-specific conclusion)
#
# =============================================================================

# =============================================================================
# EXERCISE OPENING (Universal)
# =============================================================================

OPENING_TEMPLATE = '''"""
{exercise_title}

{{{{ROLE_TITLE}}}} Training: {exercise_topic}

Welcome, aspiring {{{{ROLE_TITLE}}}}! In this exercise, you'll develop {task_count}
{{{{COMPONENT_PLURAL}}}} that form the foundation of a {{{{PROJECT_SCALE}}}} {{{{PROJECT_TYPE}}}}.

This progressive training will teach you:
- {learning_objective_1}
- {learning_objective_2}
- {learning_objective_3}

{{{{OPENING_FLAVOR}}}}

{{{{SECTION_ICON}}}} Let's begin your journey!
"""
'''

# =============================================================================
# SECTION TEMPLATES (Universal)
# =============================================================================

SECTION_HEADER_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Section {section_num}: {section_name}
# {separator}

{{{{SECTION_{section_num}_INTRO}}}}
# {section_intro_text}
'''

SECTION_TRANSITION_TEMPLATE = '''
{{{{SECTION_{section_num}_TRANSITION}}}}
# {{{{SUCCESS_WORD}}}}! Now let's continue.
# {transition_text}
'''

# =============================================================================
# CLOSING TEMPLATE (Universal)
# =============================================================================

CLOSING_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Training Complete!
# {separator}

{{{{EXERCISE_CLOSING}}}}
# {{{{SUCCESS_WORD}}}}! You've completed all {task_count} {{{{COMPONENT_PLURAL}}}}.
#
# You now have mastery of:
# - {skill_learned_1}
# - {skill_learned_2}
# - {skill_learned_3}
#
# {{{{CLOSING_FLAVOR}}}}
#
# Your {{{{PROJECT_TYPE}}}} is ready for the next {{{{PROGRESS_UNIT}}}}!


def main():
    """Run all exercises to test your implementation."""
    print("Testing {exercise_title}...")
    print("="*60)

    {main_function_calls}

    print("="*60)
    print("{{{{CELEBRATION}}}}")


if __name__ == "__main__":
    main()
'''

# =============================================================================
# SECTION CALCULATION (Universal Logic)
# =============================================================================

def calculate_sections(task_count: int) -> list:
    """
    Calculate how to divide tasks into progressive sections.

    Universal algorithm - works regardless of theme.

    Args:
        task_count: Total number of tasks in exercise

    Returns:
        List of (start_task, end_task) tuples for each section
    """
    if task_count <= 5:
        # Single section - no breaks needed
        return [(1, task_count)]

    elif task_count <= 9:
        # 2-3 sections based on size
        if task_count <= 6:
            mid = task_count // 2
            return [(1, mid), (mid + 1, task_count)]
        else:
            third = task_count // 3
            return [
                (1, third),
                (third + 1, third * 2),
                (third * 2 + 1, task_count)
            ]

    elif task_count <= 15:
        # 3 sections - most common
        third = task_count // 3
        return [
            (1, third),
            (third + 1, third * 2),
            (third * 2 + 1, task_count)
        ]

    elif task_count <= 20:
        # 4 sections for larger exercises
        quarter = task_count // 4
        return [
            (1, quarter),
            (quarter + 1, quarter * 2),
            (quarter * 2 + 1, quarter * 3),
            (quarter * 3 + 1, task_count)
        ]

    else:
        # 5 sections for very large exercises
        fifth = task_count // 5
        return [
            (1, fifth),
            (fifth + 1, fifth * 2),
            (fifth * 2 + 1, fifth * 3),
            (fifth * 3 + 1, fifth * 4),
            (fifth * 4 + 1, task_count)
        ]


def get_section_names(section_count: int) -> list:
    """
    Get universal section names based on count.

    These are theme-agnostic structural names.

    Args:
        section_count: Number of sections (2-5)

    Returns:
        List of section name strings
    """
    section_sets = {
        2: ["Foundation", "Completion"],
        3: ["Foundation", "Building", "Enhancement"],
        4: ["Foundation", "Building", "Enhancement", "Mastery"],
        5: ["Foundation", "Building", "Enhancement", "Advanced", "Mastery"]
    }

    return section_sets.get(section_count, [f"Part {i+1}" for i in range(section_count)])


# =============================================================================
# VISUAL SEPARATORS (Universal)
# =============================================================================

def get_separator(use_icon: bool = True, icon: str = "💻") -> str:
    """
    Get section separator - can use theme icon or plain.

    Args:
        use_icon: Whether to use theme icon
        icon: Icon from theme (SECTION_ICON placeholder value)

    Returns:
        Separator string
    """
    if use_icon and icon:
        return f"# {icon * 30}"
    else:
        return "# " + "=" * 60


# =============================================================================
# NARRATIVE GENERATORS (Universal)
# =============================================================================

def generate_section_intro(section_num: int, section_name: str, task_range: tuple) -> str:
    """
    Generate universal introduction for a section.

    Args:
        section_num: Section number (1-5)
        section_name: Name of section (Foundation, Building, etc.)
        task_range: (start_task, end_task) tuple

    Returns:
        Intro text with universal phrasing
    """
    task_count = task_range[1] - task_range[0] + 1

    intros = {
        1: f"We begin with the {section_name.lower()} - {task_count} essential {{{{TASK_NOUN}}}}s to establish our base.",
        2: f"With the foundation set, we move to {section_name.lower()} - {task_count} more {{{{TASK_NOUN}}}}s to expand.",
        3: f"Now for {section_name.lower()} - {task_count} {{{{TASK_NOUN}}}}s that add power and capability.",
        4: f"Nearly complete! The {section_name.lower()} phase requires {task_count} {{{{TASK_NOUN}}}}s.",
        5: f"Final section: {section_name.lower()} - {task_count} {{{{TASK_NOUN}}}}s to reach full mastery."
    }

    return intros.get(section_num, f"Section {section_num}: {section_name} - {task_count} {{{{TASK_NOUN}}}}s.")


def generate_transition(section_num: int, section_name: str) -> str:
    """
    Generate universal transition between sections.

    Args:
        section_num: Section number being transitioned TO
        section_name: Name of upcoming section

    Returns:
        Transition text
    """
    transitions = {
        2: f"{{{{SUCCESS_WORD}}}}! The foundation is solid. Now let's move to {section_name.lower()}.",
        3: f"Great progress! With those completed, we can begin {section_name.lower()}.",
        4: f"Impressive work! You're ready for {section_name.lower()}.",
        5: f"Almost there! Time for the final push: {section_name.lower()}."
    }

    return transitions.get(section_num, f"Let's continue to {section_name.lower()}.")


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
    Generate complete exercise structure with Progressive Chapter narrative.

    THEME-AGNOSTIC: Uses universal placeholders filled by theme_vars.

    Args:
        exercise_title: Name of the exercise
        task_count: Number of tasks
        theme_vars: Dictionary from theme mapping JSON (optional for structure only)
        **kwargs: Additional customization options

    Returns:
        Dictionary with exercise structure and universal placeholders
    """

    # Calculate sections (universal algorithm)
    sections = calculate_sections(task_count)
    section_count = len(sections)
    section_names = get_section_names(section_count)

    # Get icon for separator (if theme_vars provided)
    icon = theme_vars.get('SECTION_ICON', '💻') if theme_vars else '💻'
    separator = get_separator(use_icon=True, icon=icon)

    # Build structure
    structure = {
        'template_id': 'exercise_narrative_progressive_chapter',
        'template_version': 2,
        'exercise_title': exercise_title,
        'task_count': task_count,
        'section_count': section_count,
        'theme_agnostic': True,
        'sections': [],
        'opening': {
            'template': OPENING_TEMPLATE,
            'required_placeholders': [
                'ROLE_TITLE',
                'COMPONENT_PLURAL',
                'PROJECT_SCALE',
                'PROJECT_TYPE',
                'OPENING_FLAVOR',
                'SECTION_ICON'
            ],
            'content_placeholders': [
                'exercise_title',
                'exercise_topic',
                'task_count',
                'learning_objective_1',
                'learning_objective_2',
                'learning_objective_3'
            ]
        },
        'closing': {
            'template': CLOSING_TEMPLATE,
            'required_placeholders': [
                'SECTION_ICON',
                'SUCCESS_WORD',
                'COMPONENT_PLURAL',
                'CLOSING_FLAVOR',
                'PROJECT_TYPE',
                'PROGRESS_UNIT',
                'CELEBRATION'
            ],
            'content_placeholders': [
                'separator',
                'task_count',
                'skill_learned_1',
                'skill_learned_2',
                'skill_learned_3',
                'exercise_title',
                'main_function_calls'
            ]
        }
    }

    # Generate sections with universal narrative
    for i, (start_task, end_task) in enumerate(sections):
        section_num = i + 1
        section_name = section_names[i]

        section = {
            'section_num': section_num,
            'name': section_name,
            'task_range': (start_task, end_task),
            'task_count': end_task - start_task + 1,
            'intro_text': generate_section_intro(section_num, section_name, (start_task, end_task)),
            'transition_text': generate_transition(section_num, section_name) if section_num > 1 else None,
            'template': SECTION_TRANSITION_TEMPLATE if section_num > 1 else SECTION_HEADER_TEMPLATE,
            'required_placeholders': [
                'SECTION_ICON',
                'SUCCESS_WORD',
                'TASK_NOUN',
                f'SECTION_{section_num}_INTRO',
                f'SECTION_{section_num}_TRANSITION' if section_num > 1 else None
            ],
            'content_placeholders': [
                'separator',
                'section_num',
                'section_name',
                'section_intro_text',
                'transition_text' if section_num > 1 else None
            ]
        }

        structure['sections'].append(section)

    return structure


# =============================================================================
# THEME APPLICATION HELPER
# =============================================================================

def apply_theme(structure: dict, theme_vars: dict) -> dict:
    """
    Apply theme variables to exercise structure.

    This is for DEMONSTRATION - actual theme application happens in Maya Chat app.

    Args:
        structure: Exercise structure from generate_exercise_structure()
        theme_vars: Variables from theme mapping JSON

    Returns:
        Structure with placeholders filled
    """
    import json

    # Create a copy
    themed = json.loads(json.dumps(structure))

    # Add theme info
    themed['theme_applied'] = True
    themed['theme_variables'] = theme_vars

    return themed


# =============================================================================
# USAGE EXAMPLE
# =============================================================================

if __name__ == "__main__":
    import json

    # Example 1: Generate universal structure
    print("=" * 70)
    print("EXAMPLE 1: Universal Structure (no theme)")
    print("=" * 70)

    structure = generate_exercise_structure(
        exercise_title="RPG Battle System",
        task_count=21
    )

    print(f"\nExercise: {structure['exercise_title']}")
    print(f"Tasks: {structure['task_count']}")
    print(f"Sections: {structure['section_count']}")
    print(f"Theme-agnostic: {structure['theme_agnostic']}")
    print("\nSection breakdown:")
    for section in structure['sections']:
        print(f"  {section['section_num']}. {section['name']}: "
              f"Tasks {section['task_range'][0]}-{section['task_range'][1]} "
              f"({section['task_count']} tasks)")

    # Example 2: Apply different themes to same structure
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Same Structure, Three Different Themes")
    print("=" * 70)

    # Load theme mappings (if they exist)
    try:
        with open('../../theme_mappings/fantasy_magic.json', 'r', encoding='utf-8') as f:
            fantasy_theme = json.load(f)['narrative_variables']

        with open('../../theme_mappings/soccer_academy.json', 'r', encoding='utf-8') as f:
            soccer_theme = json.load(f)['narrative_variables']

        with open('../../theme_mappings/professional_coding.json', 'r', encoding='utf-8') as f:
            coding_theme = json.load(f)['narrative_variables']

        for theme_name, theme_vars in [
            ('Fantasy Magic', fantasy_theme),
            ('Soccer Academy', soccer_theme),
            ('Professional Coding', coding_theme)
        ]:
            print(f"\n{theme_name} Theme:")
            print(f"  Role: {theme_vars['ROLE_TITLE']}")
            print(f"  Project: {theme_vars['PROJECT_TYPE']}")
            print(f"  Components: {theme_vars['COMPONENT_PLURAL']}")
            print(f"  Celebration: {theme_vars['CELEBRATION']}")

    except FileNotFoundError:
        print("\nTheme mapping files not found. Run from correct directory.")
        print("Expected: theme_mappings/*.json")

    print("\n" + "=" * 70)
    print("Structure is universal - themes customize the narrative!")
    print("=" * 70)
