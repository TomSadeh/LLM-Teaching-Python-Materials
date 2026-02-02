"""
Exercise Narrative Template: Tutorial Walkthrough (Theme-Agnostic v2)

UNIVERSAL STRUCTURE - Works with ANY theme via placeholder substitution.

Follow-along structure where students see examples then try similar tasks.
Pattern: Setup → Example → Try It → Example → Try It → Practice

Compatible themes: Fantasy, Soccer, Sci-fi, Detective, Military, Professional Coding, etc.
"""

TEMPLATE_INFO = {
    'id': 'exercise_narrative_tutorial_walkthrough',
    'name': 'Tutorial Walkthrough',
    'version': 2,
    'usage_percentage': 0.25,  # Actual from corpus
    'best_for': 'Example-driven learning with practice tasks',
    'pattern': 'Setup → Example 1 → Try It 1 → Example 2 → Try It 2 → Practice',
    'theme_agnostic': True
}

# =============================================================================
# UNIVERSAL PLACEHOLDERS REQUIRED
# =============================================================================
# Role & Context:
#   - ROLE_TITLE, MENTOR_TITLE
# Project & Scope:
#   - PROJECT_TYPE, COMPONENT_PLURAL
# Components & Tasks:
#   - TASK_NOUN, TASK_VERB
# Progress & Feedback:
#   - SECTION_ICON, SUCCESS_WORD, CELEBRATION, PROGRESS_UNIT
# Narrative Flavor:
#   - OPENING_FLAVOR, CLOSING_FLAVOR
# =============================================================================

OPENING_TEMPLATE = '''"""
{exercise_title}

{{{{ROLE_TITLE}}}} Tutorial: {concept_name}

Welcome! In this hands-on tutorial, you'll learn {concept} by following examples
and practicing each {{{{TASK_NOUN}}}} step by step.

Learning Path:
{{{{SECTION_ICON}}}} Step 1: See an example demonstration
{{{{SECTION_ICON}}}} Step 2: Try it yourself with guidance
{{{{SECTION_ICON}}}} Step 3: Practice independently

This tutorial teaches:
- {learning_objective_1}
- {learning_objective_2}
- {learning_objective_3}

{{{{OPENING_FLAVOR}}}}

Let's begin your training!
"""
'''

EXAMPLE_SECTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Example {num}: {example_name}
# {separator}

{{{{EXAMPLE_{num}_INTRO}}}}
# Here's a demonstration of {example_demonstrates}.
# Pay attention to {key_technique}.

def example_{num}_{function_name}():
    """
    {{{{CONTEXT_EXAMPLE_DESCRIPTION}}}}
    Example: {example_description}

    This demonstrates: {concept_demonstrated}
    """
    {example_code}

# Study this example carefully before the next step!
'''

TRY_IT_SECTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Try It {num}: Your Turn!
# {separator}

{{{{TRY_IT_{num}_INTRO}}}}
# Now apply what you learned! Create a similar {{{{TASK_NOUN}}}}.
# {guidance_hint}

def {function_name}():
    """
    {{{{CONTEXT_FUNCTION_DESCRIPTION}}}}
    {task_description}

    Follow the pattern from example {num}.
    """
    pass  # ✏️ Your code here
'''

PRACTICE_SECTION_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Independent Practice
# {separator}

{{{{PRACTICE_INTRO}}}}
# {{{{SUCCESS_WORD}}}}! You've learned the fundamentals.
# Now practice these {{{{COMPONENT_PLURAL}}}} on your own.
#
# These tasks combine everything from the examples.
# {practice_guidance}
'''

CLOSING_TEMPLATE = '''
# {separator}
# {{{{SECTION_ICON}}}} Tutorial Complete!
# {separator}

{{{{TUTORIAL_CLOSING}}}}
# {{{{SUCCESS_WORD}}}}! You've completed the tutorial.
#
# You've mastered:
# - {skill_learned_1}
# - {skill_learned_2}
# - {skill_learned_3}
#
# {{{{CLOSING_FLAVOR}}}}
#
# You're ready for the next {{{{PROGRESS_UNIT}}}}!


def main():
    """Run all exercises."""
    print("{{{{SECTION_ICON}}}} Tutorial: {exercise_title}")
    print("="*60)

    print("\\nExamples:")
    {example_calls}

    print("\\nYour Turn:")
    {try_it_calls}

    print("\\nPractice:")
    {practice_calls}

    print("="*60)
    print("{{{{CELEBRATION}}}}")


if __name__ == "__main__":
    main()
'''

# =============================================================================
# STRUCTURE GENERATOR (Universal Logic)
# =============================================================================

def generate_tutorial_structure(task_count: int) -> list:
    """
    Generate tutorial structure with examples and try-its.

    Universal algorithm - pattern: Example → Try It → Example → Try It → Practice

    Args:
        task_count: Total number of tasks

    Returns:
        List of (section_type, num, task_num) tuples
    """
    if task_count <= 4:
        # Simple: 2 examples, 2 try-its
        return [
            ('example', 1, 1),
            ('try_it', 1, 2),
            ('example', 2, 3),
            ('try_it', 2, 4),
        ]

    elif task_count <= 8:
        # Standard: 3 example/try-it pairs, practice
        sections = []
        pairs = min(3, task_count // 2)
        current_task = 1

        for i in range(1, pairs + 1):
            sections.append(('example', i, current_task))
            current_task += 1
            if current_task <= task_count:
                sections.append(('try_it', i, current_task))
                current_task += 1

        # Remaining tasks are practice
        while current_task <= task_count:
            sections.append(('practice', 0, current_task))
            current_task += 1

        return sections

    else:
        # Large: 4 example/try-it pairs, practice
        sections = []
        pairs = min(4, task_count // 2)
        current_task = 1

        for i in range(1, pairs + 1):
            sections.append(('example', i, current_task))
            current_task += 1
            if current_task <= task_count:
                sections.append(('try_it', i, current_task))
                current_task += 1

        # Remaining are practice
        while current_task <= task_count:
            sections.append(('practice', 0, current_task))
            current_task += 1

        return sections


def get_separator(use_icon: bool = True, icon: str = "💻") -> str:
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
    Generate complete tutorial exercise structure.

    THEME-AGNOSTIC: Uses universal placeholders filled by theme_vars.

    Args:
        exercise_title: Name of the exercise
        task_count: Number of tasks
        theme_vars: Dictionary from theme mapping JSON
        **kwargs: Additional options

    Returns:
        Dictionary with exercise structure
    """
    sections = generate_tutorial_structure(task_count)

    # Count section types
    example_count = sum(1 for s in sections if s[0] == 'example')
    try_it_count = sum(1 for s in sections if s[0] == 'try_it')
    practice_count = sum(1 for s in sections if s[0] == 'practice')

    icon = theme_vars.get('SECTION_ICON', '💻') if theme_vars else '💻'
    separator = get_separator(use_icon=True, icon=icon)

    structure = {
        'template_id': 'exercise_narrative_tutorial_walkthrough',
        'template_version': 2,
        'exercise_title': exercise_title,
        'task_count': task_count,
        'example_count': example_count,
        'try_it_count': try_it_count,
        'practice_count': practice_count,
        'theme_agnostic': True,
        'sections': sections,
        'opening': {
            'template': OPENING_TEMPLATE,
            'required_placeholders': [
                'ROLE_TITLE',
                'SECTION_ICON',
                'TASK_NOUN',
                'OPENING_FLAVOR'
            ]
        },
        'closing': {
            'template': CLOSING_TEMPLATE,
            'required_placeholders': [
                'SECTION_ICON',
                'SUCCESS_WORD',
                'CLOSING_FLAVOR',
                'PROGRESS_UNIT',
                'CELEBRATION'
            ]
        }
    }

    return structure


if __name__ == "__main__":
    import json

    print("=" * 70)
    print("Tutorial Walkthrough Template (Theme-Agnostic v2)")
    print("=" * 70)

    structure = generate_exercise_structure(
        exercise_title="String Methods Tutorial",
        task_count=8
    )

    print(f"\nExercise: {structure['exercise_title']}")
    print(f"Tasks: {structure['task_count']}")
    print(f"Examples: {structure['example_count']}")
    print(f"Try-Its: {structure['try_it_count']}")
    print(f"Practice: {structure['practice_count']}")
    print(f"\nStructure:")
    for section_type, num, task in structure['sections']:
        if section_type == 'example':
            print(f"  Task {task}: Example {num} (demonstration)")
        elif section_type == 'try_it':
            print(f"  Task {task}: Try It {num} (guided practice)")
        else:
            print(f"  Task {task}: Practice (independent)")

    # Test with theme
    try:
        with open('../../theme_mappings/professional_coding.json', 'r', encoding='utf-8') as f:
            theme = json.load(f)['narrative_variables']

        print(f"\n\nApplied Theme: Professional Coding")
        print(f"  Role: {theme['ROLE_TITLE']}")
        print(f"  Icon: {theme['SECTION_ICON']}")
        print(f"  Celebration: {theme['CELEBRATION']}")
    except FileNotFoundError:
        pass

    print("\n" + "=" * 70)
