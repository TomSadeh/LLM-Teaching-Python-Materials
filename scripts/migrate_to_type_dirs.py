#!/usr/bin/env python3
"""
Migration script: Move existing exercises into write_code/ subdirectories.

This script restructures the raw_exercises folder from:
    raw_exercises/module_X/exercise_1_topic.py

To:
    raw_exercises/module_X/write_code/exercise_1_topic.py

Usage:
    python scripts/migrate_to_type_dirs.py          # Dry run (preview)
    python scripts/migrate_to_type_dirs.py --run    # Actually move files
"""

import os
import shutil
import argparse
from pathlib import Path


def get_project_root():
    """Get the project root directory."""
    script_dir = Path(__file__).parent
    return script_dir.parent


def find_modules(raw_exercises_dir: Path) -> list[Path]:
    """Find all module directories."""
    modules = []
    for item in sorted(raw_exercises_dir.iterdir()):
        if item.is_dir() and item.name.startswith("module_"):
            modules.append(item)
    return modules


def find_exercises_to_migrate(module_dir: Path) -> list[Path]:
    """Find exercise files that need to be migrated (not already in subdirs)."""
    exercises = []
    for item in module_dir.iterdir():
        if item.is_file() and item.name.startswith("exercise_") and item.suffix == ".py":
            exercises.append(item)
    return sorted(exercises)


def migrate_module(module_dir: Path, dry_run: bool = True) -> dict:
    """
    Migrate a single module's exercises to write_code/ subdirectory.

    Returns dict with migration stats.
    """
    stats = {
        "module": module_dir.name,
        "exercises_found": 0,
        "exercises_moved": 0,
        "write_code_created": False,
        "errors": []
    }

    exercises = find_exercises_to_migrate(module_dir)
    stats["exercises_found"] = len(exercises)

    if not exercises:
        return stats

    write_code_dir = module_dir / "write_code"

    # Create write_code directory if needed
    if not write_code_dir.exists():
        if dry_run:
            print(f"  [DRY RUN] Would create: {write_code_dir}")
        else:
            write_code_dir.mkdir(parents=True)
            print(f"  Created: {write_code_dir}")
        stats["write_code_created"] = True

    # Move each exercise
    for exercise in exercises:
        dest = write_code_dir / exercise.name

        if dest.exists():
            stats["errors"].append(f"Destination already exists: {dest}")
            continue

        if dry_run:
            print(f"  [DRY RUN] Would move: {exercise.name}")
        else:
            shutil.move(str(exercise), str(dest))
            print(f"  Moved: {exercise.name}")

        stats["exercises_moved"] += 1

    return stats


def print_summary(all_stats: list[dict]):
    """Print migration summary."""
    print("\n" + "=" * 60)
    print("MIGRATION SUMMARY")
    print("=" * 60)

    total_found = sum(s["exercises_found"] for s in all_stats)
    total_moved = sum(s["exercises_moved"] for s in all_stats)
    dirs_created = sum(1 for s in all_stats if s["write_code_created"])
    total_errors = sum(len(s["errors"]) for s in all_stats)

    print(f"\nModules processed:     {len(all_stats)}")
    print(f"write_code/ created:   {dirs_created}")
    print(f"Exercises found:       {total_found}")
    print(f"Exercises moved:       {total_moved}")

    if total_errors > 0:
        print(f"\nErrors: {total_errors}")
        for stats in all_stats:
            for error in stats["errors"]:
                print(f"  - {error}")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Migrate exercises to write_code/ subdirectories"
    )
    parser.add_argument(
        "--run",
        action="store_true",
        help="Actually perform the migration (default is dry run)"
    )
    args = parser.parse_args()

    dry_run = not args.run

    project_root = get_project_root()
    raw_exercises_dir = project_root / "raw_exercises"

    if not raw_exercises_dir.exists():
        print(f"Error: raw_exercises directory not found at {raw_exercises_dir}")
        return 1

    print("=" * 60)
    if dry_run:
        print("MIGRATION DRY RUN (use --run to actually move files)")
    else:
        print("MIGRATION IN PROGRESS")
    print("=" * 60)
    print(f"\nSource: {raw_exercises_dir}\n")

    modules = find_modules(raw_exercises_dir)

    if not modules:
        print("No module directories found.")
        return 0

    all_stats = []

    for module in modules:
        print(f"\n{module.name}/")
        stats = migrate_module(module, dry_run=dry_run)
        all_stats.append(stats)

        if stats["exercises_found"] == 0:
            print("  (no exercises to migrate)")

    print_summary(all_stats)

    if dry_run and any(s["exercises_found"] > 0 for s in all_stats):
        print("To perform the migration, run:")
        print("  python scripts/migrate_to_type_dirs.py --run")
        print()

    return 0


if __name__ == "__main__":
    exit(main())
