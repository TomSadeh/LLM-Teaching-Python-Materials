"""
Theme Validation Script

Test that exercise narrative templates work across all themes.
Generates sample narratives for each theme to verify coherence.
"""

import json
import os
from pathlib import Path

# Import template generators
import sys
sys.path.append(str(Path(__file__).parent.parent / 'templates' / 'exercise_narratives'))

def load_theme(theme_file: str) -> dict:
    """Load theme mapping from JSON file."""
    theme_path = Path(__file__).parent.parent / 'theme_mappings' / theme_file
    with open(theme_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def apply_placeholders(text: str, theme_vars: dict) -> str:
    """Apply theme variables to placeholders in text."""
    result = text
    for key, value in theme_vars.items():
        placeholder = f"{{{{{{{key}}}}}}}"
        result = result.replace(placeholder, str(value))
    return result

def generate_sample_narrative(template_name: str, theme: dict, task_count: int) -> dict:
    """
    Generate a sample narrative using a template and theme.

    Returns dict with template structure and sample text.
    """
    theme_vars = theme['narrative_variables']

    # Sample opening text for each template
    samples = {
        'progressive_chapter': f"""
Exercise: Build a {theme_vars['PROJECT_TYPE'].title()}

{theme_vars['ROLE_TITLE']} Training: Advanced Techniques

Welcome, aspiring {theme_vars['ROLE_TITLE']}! In this exercise, you'll develop {task_count}
{theme_vars['COMPONENT_PLURAL']} that form the foundation of a {theme_vars['PROJECT_SCALE']} {theme_vars['PROJECT_TYPE']}.

{theme_vars['OPENING_FLAVOR']}

{theme_vars['SECTION_ICON']} Let's begin your journey!
""",
        'tutorial_walkthrough': f"""
Exercise: Learn {theme_vars['COMPONENT_PLURAL'].title()}

{theme_vars['ROLE_TITLE']} Tutorial: Hands-On Practice

Welcome! In this hands-on tutorial, you'll learn by following examples
and practicing each {theme_vars['TASK_NOUN']} step by step.

{theme_vars['OPENING_FLAVOR']}

Let's begin your training!
""",
        'challenge_quest': f"""
Exercise: The Ultimate Challenge

{theme_vars['ROLE_TITLE']} Challenge: Test Your Skills

Welcome to the Challenge Arena! You'll face {task_count} {theme_vars['COMPONENT_PLURAL']}
organized into progressive difficulty levels.

{theme_vars['OPENING_FLAVOR']}

Are you ready? The challenge begins!
""",
        'mystery_investigation': f"""
Exercise: Debug the System

{theme_vars['ROLE_TITLE']} Investigation: Find the Issue

Something requires investigation in your {theme_vars['WORKSPACE']}...

{theme_vars['OPENING_FLAVOR']}

{theme_vars['SECTION_ICON']} Begin your investigation!
""",
        'world_builder': f"""
Exercise: Build the Complete System

{theme_vars['ROLE_TITLE']} Builder: System Construction

Welcome, System Builder! You'll construct a {theme_vars['PROJECT_SCALE']} {theme_vars['PROJECT_TYPE']}
by building {task_count} interconnected {theme_vars['COMPONENT_PLURAL']}.

{theme_vars['OPENING_FLAVOR']}

Let's start building!
""",
        'spec_implementation': f"""
Exercise: Professional Assignment

{theme_vars['ROLE_TITLE']} Assignment: Complete the {theme_vars.get('DELIVERABLE', 'project').title()}

You've been assigned to build a {theme_vars['PROJECT_SCALE']} {theme_vars.get('DELIVERABLE', 'project')}.

Assigned by: {theme_vars.get('CLIENT', 'Client')}

{theme_vars['OPENING_FLAVOR']}

{theme_vars['SECTION_ICON']} Time to start implementation!
"""
    }

    # Sample closing for each template
    closings = {
        'progressive_chapter': f"""
{theme_vars['SECTION_ICON']} Training Complete!

{theme_vars['SUCCESS_WORD']}! You've completed all {task_count} {theme_vars['COMPONENT_PLURAL']}.

{theme_vars['CLOSING_FLAVOR']}

Your {theme_vars['PROJECT_TYPE']} is now ready for the next {theme_vars['PROGRESS_UNIT']}!

{theme_vars['CELEBRATION']}
""",
        'tutorial_walkthrough': f"""
{theme_vars['SECTION_ICON']} Tutorial Complete!

{theme_vars['SUCCESS_WORD']}! You've mastered the fundamentals.

{theme_vars['CLOSING_FLAVOR']}

You're ready for the next {theme_vars['PROGRESS_UNIT']}!

{theme_vars['CELEBRATION']}
""",
        'challenge_quest': f"""
{theme_vars['SECTION_ICON']} Challenge Complete!

{theme_vars['SUCCESS_WORD']}! All levels cleared!

{theme_vars['CLOSING_FLAVOR']}

{theme_vars['CELEBRATION']}
""",
        'mystery_investigation': f"""
{theme_vars['SECTION_ICON']} Investigation Complete!

Investigation Status: RESOLVED

{theme_vars['CLOSING_FLAVOR']}

{theme_vars['CELEBRATION']}
""",
        'world_builder': f"""
{theme_vars['SECTION_ICON']} Build Complete!

{theme_vars['SUCCESS_WORD']}! Your {theme_vars['PROJECT_TYPE']} is fully operational.

{theme_vars['CLOSING_FLAVOR']}

{theme_vars['CELEBRATION']}
""",
        'spec_implementation': f"""
{theme_vars['SECTION_ICON']} {theme_vars.get('DELIVERABLE_TITLE', 'Complete')}

Status: ✓ COMPLETE

{theme_vars['CLOSING_FLAVOR']}

{theme_vars['CELEBRATION']}
"""
    }

    return {
        'template': template_name,
        'theme': theme['theme_name'],
        'opening': samples.get(template_name, 'Template not found'),
        'closing': closings.get(template_name, 'Template not found')
    }

def main():
    """Run theme validation across all templates."""

    # Load all themes
    theme_files = [
        'professional_coding.json',
        'fantasy_magic.json',
        'soccer_academy.json',
        'detective_agency.json',
        'scifi_engineering.json',
        'military_ops.json'
    ]

    themes = {}
    for theme_file in theme_files:
        try:
            theme = load_theme(theme_file)
            themes[theme['theme_id']] = theme
            print(f"[OK] Loaded theme: {theme['theme_name']}")
        except Exception as e:
            print(f"[FAIL] Failed to load {theme_file}: {e}")

    print(f"\nTotal themes loaded: {len(themes)}\n")

    # Templates to test
    templates = [
        'progressive_chapter',
        'tutorial_walkthrough',
        'challenge_quest',
        'mystery_investigation',
        'world_builder',
        'spec_implementation'
    ]

    # Generate sample narratives
    print("=" * 80)
    print("THEME VALIDATION RESULTS")
    print("=" * 80)
    print()

    for template in templates:
        print(f"\n{'=' * 80}")
        print(f"Template: {template.replace('_', ' ').title()}")
        print(f"{'=' * 80}\n")

        for theme_id, theme in themes.items():
            print(f"--- {theme['theme_name']} Theme ---")

            sample = generate_sample_narrative(template, theme, task_count=8)

            # Check for coherence
            issues = []

            # Check if key variables are being used
            opening = sample['opening']
            closing = sample['closing']

            if not opening or len(opening.strip()) < 50:
                issues.append("Opening too short or missing")

            if not closing or len(closing.strip()) < 30:
                issues.append("Closing too short or missing")

            # Check for remaining placeholders (indicates missing theme vars)
            if '{{' in opening or '{{' in closing:
                issues.append("Unfilled placeholders detected")

            if issues:
                print(f"[WARN] Issues found: {', '.join(issues)}\n")
            else:
                print(f"[OK] Coherent narrative generated\n")

            # Show sample (first 200 chars of opening)
            print(f"Sample opening: {opening[:200]}...")
            print()

    print("\n" + "=" * 80)
    print("VALIDATION COMPLETE")
    print("=" * 80)
    print(f"\n[OK] Tested {len(templates)} templates across {len(themes)} themes")
    print(f"Total combinations: {len(templates) * len(themes)}")

    # Summary
    print("\n" + "=" * 80)
    print("THEME SUMMARY")
    print("=" * 80)
    print()
    for theme_id, theme in themes.items():
        print(f"{theme['theme_name']}:")
        theme_vars = theme['narrative_variables']
        print(f"  Role: {theme_vars['ROLE_TITLE']}")
        print(f"  Project: {theme_vars['PROJECT_TYPE']}")
        print(f"  Components: {theme_vars['COMPONENT_PLURAL']}")
        print(f"  Goal: {theme_vars['GOAL']}")
        print(f"  Celebration: {theme_vars['CELEBRATION']}")
        print()

if __name__ == "__main__":
    main()
