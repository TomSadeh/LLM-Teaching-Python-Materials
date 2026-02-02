#!/usr/bin/env python3
"""
Exercise Narrative Structure Audit

Analyzes exercises to identify:
1. Single-task vs multi-task exercises
2. Narrative flow patterns
3. Exercise-level narrative archetypes
4. Story progression structures

This audit helps design exercise-level narrative templates that wrap
around task-level templates.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict


@dataclass
class NarrativeStructure:
    """Analysis of exercise narrative structure"""
    exercise_path: str
    exercise_type: str
    module: str

    # Task structure
    task_count: int
    task_types: List[str]  # ['function', 'class', 'debug', etc.]
    is_multi_task: bool

    # Narrative elements
    has_opening_narrative: bool
    has_closing_narrative: bool
    has_progressive_narrative: bool  # Story evolves between tasks
    narrative_locations: List[str]  # ['module_doc', 'function_1', 'between_tasks', etc.]

    # Story structure
    story_archetype: str  # Will identify patterns
    narrative_complexity: str  # 'none', 'simple', 'moderate', 'rich'

    # Narrative patterns
    has_quest_structure: bool  # "Your mission is..."
    has_world_building: bool  # Describes a world/setting
    has_character_roles: bool  # "You are a..."
    has_progression_phases: bool  # Phase 1, Phase 2, etc.
    has_challenge_escalation: bool  # Difficulty increases with story

    # Context blocks found
    context_blocks: List[str]

    # Metadata
    total_lines: int
    narrative_line_count: int
    code_to_narrative_ratio: float


def load_exercise(path: str) -> str:
    """Load exercise file"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return ""


def identify_task_types(content: str) -> List[str]:
    """Identify types of tasks in the exercise"""
    tasks = []

    # Functions to complete
    if re.search(r'def \w+\([^)]*\):\s*""".*?""".*?pass', content, re.DOTALL):
        tasks.append('complete_function')

    # Classes to implement
    if re.search(r'class \w+.*?:\s*""".*?"""', content, re.DOTALL):
        tasks.append('implement_class')

    # Debug tasks
    if re.search(r'# .*?(?:debug|fix|error)', content, re.IGNORECASE):
        tasks.append('debug')

    # Prediction tasks
    if re.search(r'(?:what will|predict|output)', content, re.IGNORECASE):
        tasks.append('predict')

    # Comparison tasks
    if re.search(r'(?:which is better|compare)', content, re.IGNORECASE):
        tasks.append('compare')

    # Style improvement
    if re.search(r'(?:PEP 8|fix.*?style|improve.*?style)', content, re.IGNORECASE):
        tasks.append('fix_style')

    # Free-form implementation
    if re.search(r'# ✏️', content):
        tasks.append('implement')

    return tasks if tasks else ['unknown']


def detect_narrative_locations(content: str) -> List[str]:
    """Find where narrative appears in the exercise"""
    locations = []
    lines = content.split('\n')

    # Module-level docstring
    if content.strip().startswith('"""') or content.strip().startswith("'''"):
        locations.append('module_docstring')

    # Check for narrative between functions
    in_function = False
    prev_function_end = 0

    for i, line in enumerate(lines):
        # Function definition
        if re.match(r'^\s*def \w+', line):
            # Check if there's narrative before this function
            if i > prev_function_end + 2:  # More than just blank lines
                between_content = '\n'.join(lines[prev_function_end:i])
                if re.search(r'""".*?"""', between_content, re.DOTALL) or \
                   re.search(r'# .*[A-Z].*\.', between_content):
                    locations.append(f'between_functions_line{i}')
            in_function = True

        # Track function ends (rough heuristic)
        if in_function and line and not line[0].isspace() and 'def ' not in line:
            prev_function_end = i
            in_function = False

    # Function docstrings
    func_docs = re.findall(r'def \w+[^:]*:\s*"""', content)
    if func_docs:
        locations.append('function_docstrings')

    # Phase markers
    if re.search(r'(?:Phase|Stage|Step|Part)\s+\d+', content, re.IGNORECASE):
        locations.append('phase_markers')

    # Exercise descriptions
    if re.search(r'Exercise \d+:', content):
        locations.append('exercise_descriptions')

    # Comments with narrative
    narrative_comments = re.findall(r'# [A-Z][^#\n]{20,}', content)
    if narrative_comments:
        locations.append('narrative_comments')

    return list(set(locations))


def identify_story_archetype(content: str, narrative_locations: List[str]) -> str:
    """Identify the narrative archetype/pattern"""

    # Check for common patterns
    content_lower = content.lower()

    # Quest/Mission structure
    if any(word in content_lower for word in ['mission', 'quest', 'task', 'goal', 'objective']):
        return 'quest_mission'

    # World-building
    if any(word in content_lower for word in ['world', 'kingdom', 'land', 'realm', 'empire']):
        return 'world_exploration'

    # Role-based
    if re.search(r'you are (?:a|an) \w+', content_lower):
        return 'role_assignment'

    # Progressive build
    if 'phase_markers' in narrative_locations:
        return 'progressive_build'

    # Tutorial/Guide
    if any(word in content_lower for word in ['example', 'follow', 'similar to', 'like this']):
        return 'tutorial_guide'

    # Challenge/Competition
    if any(word in content_lower for word in ['challenge', 'compete', 'win', 'score']):
        return 'challenge_competition'

    # Mystery/Investigation
    if any(word in content_lower for word in ['find', 'discover', 'investigate', 'solve']):
        return 'mystery_investigation'

    # Minimal/Technical (no story)
    if len(narrative_locations) <= 1:
        return 'technical_only'

    return 'mixed_narrative'


def assess_narrative_complexity(content: str, narrative_locations: List[str]) -> str:
    """Assess how complex/rich the narrative is"""

    # Count narrative indicators
    narrative_score = 0

    # Location diversity
    narrative_score += len(narrative_locations)

    # Story elements
    if re.search(r'(?:once upon|there was|in a|long ago)', content, re.IGNORECASE):
        narrative_score += 2

    # Character names
    if re.search(r'\{\{(?:hero|character|villain|mentor)', content):
        narrative_score += 1

    # World elements
    if re.search(r'\{\{(?:world|kingdom|location|school)', content):
        narrative_score += 1

    # Progressive story
    if re.search(r'(?:phase|chapter|stage|step)\s+\d+', content, re.IGNORECASE):
        narrative_score += 2

    # Dialogue or quotes
    if re.search(r'["""\'\'\'"].*?said', content, re.IGNORECASE):
        narrative_score += 1

    # Classify complexity
    if narrative_score == 0:
        return 'none'
    elif narrative_score <= 2:
        return 'simple'
    elif narrative_score <= 5:
        return 'moderate'
    else:
        return 'rich'


def count_narrative_lines(content: str) -> Tuple[int, int]:
    """Count narrative vs code lines"""
    lines = content.split('\n')
    total_lines = len(lines)
    narrative_lines = 0

    in_docstring = False
    for line in lines:
        stripped = line.strip()

        # Docstrings
        if '"""' in line or "'''" in line:
            in_docstring = not in_docstring
            narrative_lines += 1
            continue

        if in_docstring:
            narrative_lines += 1
            continue

        # Narrative comments (substantial ones)
        if stripped.startswith('#') and len(stripped) > 15:
            narrative_lines += 1

    return total_lines, narrative_lines


def analyze_exercise(exercise_path: str) -> NarrativeStructure:
    """Analyze a single exercise for narrative structure"""

    content = load_exercise(exercise_path)
    if not content:
        return None

    # Extract metadata from path
    parts = exercise_path.replace('\\', '/').split('/')
    module = next((p for p in parts if p.startswith('module_')), 'unknown')
    exercise_type = next((p for p in parts if p in [
        'write_code', 'complete_function', 'decode_error', 'bug_hunt',
        'which_is_better', 'output_prediction', 'code_tracing',
        'blank_page', 'simplify_code', 'fix_style', 'fill_blanks',
        'code_ordering', 'match_output', 'spot_difference'
    ]), 'unknown')

    # Count tasks
    function_count = len(re.findall(r'^\s*def \w+', content, re.MULTILINE))
    class_count = len(re.findall(r'^\s*class \w+', content, re.MULTILINE))
    task_count = max(function_count, class_count, 1)

    # Identify task types
    task_types = identify_task_types(content)

    # Narrative analysis
    narrative_locations = detect_narrative_locations(content)

    # Story patterns
    has_opening = 'module_docstring' in narrative_locations
    has_closing = 'Exercise' in content and content.rindex('Exercise') > len(content) * 0.8
    has_progressive = 'between_functions' in str(narrative_locations) or 'phase_markers' in narrative_locations

    # Identify archetype
    story_archetype = identify_story_archetype(content, narrative_locations)

    # Complexity
    narrative_complexity = assess_narrative_complexity(content, narrative_locations)

    # Narrative patterns
    has_quest = bool(re.search(r'(?:mission|quest|goal|objective)', content, re.IGNORECASE))
    has_world = bool(re.search(r'(?:world|kingdom|realm|empire|land)', content, re.IGNORECASE))
    has_role = bool(re.search(r'you are (?:a|an) \w+', content, re.IGNORECASE))
    has_phases = bool(re.search(r'(?:Phase|Stage|Step|Part)\s+\d+', content, re.IGNORECASE))
    has_escalation = has_phases and task_count > 3

    # Context blocks (from placeholders)
    context_blocks = re.findall(r'\{\{(CONTEXT_\w+)\}\}', content)

    # Line counts
    total_lines, narrative_lines = count_narrative_lines(content)
    ratio = narrative_lines / total_lines if total_lines > 0 else 0

    return NarrativeStructure(
        exercise_path=exercise_path,
        exercise_type=exercise_type,
        module=module,
        task_count=task_count,
        task_types=task_types,
        is_multi_task=task_count > 1,
        has_opening_narrative=has_opening,
        has_closing_narrative=has_closing,
        has_progressive_narrative=has_progressive,
        narrative_locations=narrative_locations,
        story_archetype=story_archetype,
        narrative_complexity=narrative_complexity,
        has_quest_structure=has_quest,
        has_world_building=has_world,
        has_character_roles=has_role,
        has_progression_phases=has_phases,
        has_challenge_escalation=has_escalation,
        context_blocks=context_blocks,
        total_lines=total_lines,
        narrative_line_count=narrative_lines,
        code_to_narrative_ratio=ratio
    )


def analyze_all_exercises(base_path: str = 'exercises') -> List[NarrativeStructure]:
    """Analyze all exercises in the repository"""

    results = []
    base = Path(base_path)

    if not base.exists():
        print(f"Error: {base_path} not found")
        return results

    # Find all Python files
    exercise_files = list(base.glob('**/*.py'))

    print(f"\n{'='*60}")
    print(f"Analyzing {len(exercise_files)} exercises...")
    print(f"{'='*60}\n")

    for i, exercise_file in enumerate(exercise_files, 1):
        print(f"[{i}/{len(exercise_files)}] {exercise_file.name}")

        result = analyze_exercise(str(exercise_file))
        if result:
            results.append(result)

    return results


def generate_statistics(results: List[NarrativeStructure]) -> Dict:
    """Generate comprehensive statistics"""

    total = len(results)

    stats = {
        'total_exercises': total,

        # Task structure
        'single_task': sum(1 for r in results if not r.is_multi_task),
        'multi_task': sum(1 for r in results if r.is_multi_task),
        'avg_tasks_per_exercise': sum(r.task_count for r in results) / total,

        # Narrative presence
        'has_opening': sum(1 for r in results if r.has_opening_narrative),
        'has_closing': sum(1 for r in results if r.has_closing_narrative),
        'has_progressive': sum(1 for r in results if r.has_progressive_narrative),

        # Complexity distribution
        'complexity_none': sum(1 for r in results if r.narrative_complexity == 'none'),
        'complexity_simple': sum(1 for r in results if r.narrative_complexity == 'simple'),
        'complexity_moderate': sum(1 for r in results if r.narrative_complexity == 'moderate'),
        'complexity_rich': sum(1 for r in results if r.narrative_complexity == 'rich'),

        # Archetype distribution
        'archetypes': {},

        # Narrative patterns
        'quest_structure': sum(1 for r in results if r.has_quest_structure),
        'world_building': sum(1 for r in results if r.has_world_building),
        'character_roles': sum(1 for r in results if r.has_character_roles),
        'progression_phases': sum(1 for r in results if r.has_progression_phases),
        'challenge_escalation': sum(1 for r in results if r.has_challenge_escalation),

        # Narrative ratio
        'avg_narrative_ratio': sum(r.code_to_narrative_ratio for r in results) / total,
    }

    # Count archetypes
    for result in results:
        archetype = result.story_archetype
        stats['archetypes'][archetype] = stats['archetypes'].get(archetype, 0) + 1

    return stats


def identify_hybrid_patterns(results: List[NarrativeStructure]) -> List[Dict]:
    """Identify exercises with hybrid narrative patterns"""

    hybrids = []

    for result in results:
        # Multi-task with progressive narrative = hybrid candidate
        if result.is_multi_task and result.has_progressive_narrative:
            hybrids.append({
                'exercise': result.exercise_path,
                'tasks': result.task_count,
                'archetype': result.story_archetype,
                'complexity': result.narrative_complexity,
                'pattern': 'progressive_multi_task'
            })

        # Mixed task types with narrative
        elif len(result.task_types) > 1 and result.narrative_complexity != 'none':
            hybrids.append({
                'exercise': result.exercise_path,
                'tasks': result.task_count,
                'task_types': result.task_types,
                'archetype': result.story_archetype,
                'complexity': result.narrative_complexity,
                'pattern': 'mixed_task_narrative'
            })

    return hybrids


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Audit exercise narrative structures')
    parser.add_argument('--base-path', default='exercises', help='Base path for exercises')
    parser.add_argument('--output', default='narrative_structure_audit.json', help='Output JSON file')
    parser.add_argument('--report-dir', default='docs/audits', help='Directory for reports')

    args = parser.parse_args()

    # Analyze all exercises
    results = analyze_all_exercises(args.base_path)

    if not results:
        print("No exercises analyzed")
        return

    # Generate statistics
    stats = generate_statistics(results)

    # Identify hybrid patterns
    hybrids = identify_hybrid_patterns(results)

    # Create report
    report = {
        'summary': stats,
        'hybrid_exercises': hybrids,
        'all_exercises': [asdict(r) for r in results]
    }

    # Save JSON report
    output_dir = os.path.dirname(args.output)
    if output_dir:  # Only create directory if there is one
        os.makedirs(output_dir, exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"\n{'='*60}")
    print("NARRATIVE STRUCTURE AUDIT SUMMARY")
    print(f"{'='*60}")
    print(f"Total Exercises: {stats['total_exercises']}")
    print(f"\nTask Structure:")
    print(f"  Single-task: {stats['single_task']} ({stats['single_task']/stats['total_exercises']*100:.1f}%)")
    print(f"  Multi-task: {stats['multi_task']} ({stats['multi_task']/stats['total_exercises']*100:.1f}%)")
    print(f"  Avg tasks/exercise: {stats['avg_tasks_per_exercise']:.1f}")

    print(f"\nNarrative Complexity:")
    print(f"  None: {stats['complexity_none']} ({stats['complexity_none']/stats['total_exercises']*100:.1f}%)")
    print(f"  Simple: {stats['complexity_simple']} ({stats['complexity_simple']/stats['total_exercises']*100:.1f}%)")
    print(f"  Moderate: {stats['complexity_moderate']} ({stats['complexity_moderate']/stats['total_exercises']*100:.1f}%)")
    print(f"  Rich: {stats['complexity_rich']} ({stats['complexity_rich']/stats['total_exercises']*100:.1f}%)")

    print(f"\nNarrative Patterns:")
    print(f"  Quest structure: {stats['quest_structure']}")
    print(f"  World building: {stats['world_building']}")
    print(f"  Character roles: {stats['character_roles']}")
    print(f"  Progression phases: {stats['progression_phases']}")
    print(f"  Challenge escalation: {stats['challenge_escalation']}")

    print(f"\nStory Archetypes:")
    for archetype, count in sorted(stats['archetypes'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {archetype}: {count} ({count/stats['total_exercises']*100:.1f}%)")

    print(f"\nHybrid Exercises: {len(hybrids)}")
    if hybrids:
        print("\nTop 5 Hybrid Examples:")
        for hybrid in hybrids[:5]:
            print(f"  - {os.path.basename(hybrid['exercise'])}")
            print(f"    Tasks: {hybrid['tasks']}, Archetype: {hybrid['archetype']}, Pattern: {hybrid['pattern']}")

    print(f"\n{'='*60}")
    print(f"Report written to: {args.output}")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
