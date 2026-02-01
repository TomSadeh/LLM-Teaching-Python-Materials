"""
Exercise Narrative Template: Challenge Quest (Theme-Agnostic v2)

UNIVERSAL STRUCTURE - Works with ANY theme via placeholder substitution.

Progressive difficulty with level-based structure and achievement tracking.
Pattern: Challenge Intro → Level 1 → Level 2 → Level 3 → Victory

Compatible themes: Fantasy, Soccer, Sci-fi, Detective, Military, Professional Coding, etc.
"""

TEMPLATE_INFO = {
    'id': 'exercise_narrative_challenge_quest',
    'name': 'Challenge Quest',
    'version': 2,
    'usage_percentage': 0.37,  # Most common! Actual from corpus
    'best_for': 'Progressive difficulty exercises with clear achievement levels',
    'pattern': 'Challenge Intro → Level 1 → Level 2 → Level 3 → Victory',
    'theme_agnostic': True
}

# =============================================================================
# UNIVERSAL PLACEHOLDERS REQUIRED
# =============================================================================
# Role & Context:
#   - ROLE_TITLE, WORKSPACE
# Project & Scope:
#   - PROJECT_TYPE, GOAL
# Components & Tasks:
#   - COMPONENT_PLURAL, TASK_NOUN
# Progress & Feedback:
#   - SECTION_ICON, SUCCESS_WORD, CELEBRATION, PROGRESS_UNIT
# Narrative Flavor:
#   - OPENING_FLAVOR, CLOSING_FLAVOR
# =============================================================================

OPENING_TEMPLATE = '''"""
{exercise_title}

{{{{ROLE_TITLE}}}} Challenge: {challenge_name}

Welcome to the Challenge Arena! You'll face {task_count} {{{{COMPONENT_PLURAL}}}}
organized into progressive difficulty levels.

Your objective: {challenge_goal}

Difficulty Levels:
{{{{SECTION_ICON}}}} Level 1: {level_1_desc} (Foundational)
{{{{SECTION_ICON}}}}{{{{SECTION_ICON}}}} Level 2: {level_2_desc} (Intermediate)
{{{{SECTION_ICON}}}}{{{{SECTION_ICON}}}}{{{{SECTION_ICON}}}} Level 3: {level_3_desc} (Advanced)

Achievement System:
- Each level tests your growing skills
- Progress unlocks new capabilities
- Complete all levels to reach {{{{GOAL}}}}

{{{{OPENING_FLAVOR}}}}

Are you ready? The challenge begins!
"""
'''

LEVEL_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Level {num}: {level_name} {level_stars}
# {separator}

{{{{LEVEL_{num}_INTRO}}}}
# Challenge Level: {difficulty}
# Tasks in this level: {task_count}
# Achievement: {achievement_name}
#
# {level_description}
#
# Strategy: {level_strategy}
'''

VICTORY_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Challenge Complete!
# {separator}

{{{{VICTORY_CLOSING}}}}
# {{{{SUCCESS_WORD}}}}! All levels cleared!
#
# Final Results:
# - Levels completed: {levels_completed}
# - {{{{COMPONENT_PLURAL}}}} mastered: {task_count}
# - Achievement rank: {achievement_rank}
#
# {{{{CLOSING_FLAVOR}}}}
#
# {{{{CELEBRATION}}}}


def main():
    """Run challenge levels."""
    print("{{{{SECTION_ICON}}}} Challenge: {exercise_title}")
    print("="*60)

    current_level = 1
    {level_test_calls}

    print("="*60)
    print(f"Challenge Cleared! Achievement: {{achievement}}")
    print("{{{{CELEBRATION}}}}")


if __name__ == "__main__":
    main()
'''

# =============================================================================
# LEVEL STRUCTURE (Universal Logic)
# =============================================================================

def calculate_levels(task_count: int) -> list:
    """
    Divide tasks into progressive difficulty levels.

    Universal algorithm - works regardless of theme.

    Args:
        task_count: Total number of tasks

    Returns:
        List of (level_num, start_task, end_task, difficulty, achievement_points)
    """
    if task_count <= 3:
        return [(1, 1, task_count, 'Foundational', 100)]

    elif task_count <= 6:
        # 2 levels
        mid = task_count // 2
        return [
            (1, 1, mid, 'Foundational', 100),
            (2, mid + 1, task_count, 'Intermediate', 200),
        ]

    elif task_count <= 9:
        # 3 levels
        third = task_count // 3
        return [
            (1, 1, third, 'Foundational', 100),
            (2, third + 1, third * 2, 'Intermediate', 200),
            (3, third * 2 + 1, task_count, 'Advanced', 300),
        ]

    else:
        # 4 levels for large exercises
        quarter = task_count // 4
        return [
            (1, 1, quarter, 'Foundational', 100),
            (2, quarter + 1, quarter * 2, 'Intermediate', 200),
            (3, quarter * 2 + 1, quarter * 3, 'Advanced', 300),
            (4, quarter * 3 + 1, task_count, 'Expert', 500),
        ]


def get_level_stars(level_num: int) -> str:
    """Get star indicator for level (universal)."""
    stars = {
        1: '⭐',
        2: '⭐⭐',
        3: '⭐⭐⭐',
        4: '⭐⭐⭐⭐',
    }
    return stars.get(level_num, '⭐' * level_num)


def get_achievement_rank(completion_ratio: float) -> str:
    """
    Get achievement rank based on completion.

    Universal achievement system.
    """
    if completion_ratio >= 1.0:
        return 'Legendary'
    elif completion_ratio >= 0.8:
        return 'Master'
    elif completion_ratio >= 0.6:
        return 'Advanced'
    elif completion_ratio >= 0.3:
        return 'Skilled'
    else:
        return 'Apprentice'


def get_separator(use_icon: bool = True, icon: str = "💻") -> str:
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
    Generate complete challenge exercise structure.

    THEME-AGNOSTIC: Uses universal placeholders filled by theme_vars.

    Args:
        exercise_title: Name of the exercise
        task_count: Number of tasks
        theme_vars: Dictionary from theme mapping JSON
        **kwargs: Additional options

    Returns:
        Dictionary with exercise structure
    """
    levels = calculate_levels(task_count)
    icon = theme_vars.get('SECTION_ICON', '💻') if theme_vars else '💻'
    separator = get_separator(use_icon=True, icon=icon)

    structure = {
        'template_id': 'exercise_narrative_challenge_quest',
        'template_version': 2,
        'exercise_title': exercise_title,
        'task_count': task_count,
        'level_count': len(levels),
        'theme_agnostic': True,
        'levels': [],
        'opening': {
            'template': OPENING_TEMPLATE,
            'required_placeholders': [
                'ROLE_TITLE',
                'COMPONENT_PLURAL',
                'SECTION_ICON',
                'GOAL',
                'OPENING_FLAVOR'
            ]
        },
        'victory': {
            'template': VICTORY_TEMPLATE,
            'required_placeholders': [
                'SECTION_ICON',
                'SUCCESS_WORD',
                'COMPONENT_PLURAL',
                'CLOSING_FLAVOR',
                'CELEBRATION'
            ]
        }
    }

    # Generate levels with universal structure
    for level_num, start_task, end_task, difficulty, points in levels:
        level_task_count = end_task - start_task + 1

        level = {
            'level_num': level_num,
            'name': f"Level {level_num}",
            'difficulty': difficulty,
            'task_range': (start_task, end_task),
            'task_count': level_task_count,
            'points': points,
            'stars': get_level_stars(level_num),
            'template': LEVEL_TEMPLATE,
            'required_placeholders': [
                'SECTION_ICON',
                f'LEVEL_{level_num}_INTRO'
            ]
        }

        structure['levels'].append(level)

    return structure


if __name__ == "__main__":
    import json

    print("=" * 70)
    print("Challenge Quest Template (Theme-Agnostic v2)")
    print("=" * 70)

    structure = generate_exercise_structure(
        exercise_title="Data Structure Challenge",
        task_count=12
    )

    print(f"\nExercise: {structure['exercise_title']}")
    print(f"Tasks: {structure['task_count']}")
    print(f"Levels: {structure['level_count']}")
    print(f"\nLevel breakdown:")
    for level in structure['levels']:
        print(f"  Level {level['level_num']} {level['stars']}: "
              f"Tasks {level['task_range'][0]}-{level['task_range'][1]} "
              f"({level['task_count']} tasks) - {level['difficulty']} - {level['points']} pts")

    # Test with multiple themes
    try:
        themes_to_test = [
            '../../theme_mappings/fantasy_magic.json',
            '../../theme_mappings/soccer_academy.json',
            '../../theme_mappings/professional_coding.json'
        ]

        print("\n" + "=" * 70)
        print("Same Structure, Different Themes:")
        print("=" * 70)

        for theme_path in themes_to_test:
            with open(theme_path, 'r', encoding='utf-8') as f:
                theme_data = json.load(f)
                theme_vars = theme_data['narrative_variables']

            print(f"\n{theme_data['theme_name']}:")
            print(f"  Role: {theme_vars['ROLE_TITLE']}")
            print(f"  Goal: {theme_vars['GOAL']}")
            print(f"  Icon: {theme_vars['SECTION_ICON']}")
            print(f"  Celebration: {theme_vars['CELEBRATION']}")

    except FileNotFoundError:
        pass

    print("\n" + "=" * 70)
