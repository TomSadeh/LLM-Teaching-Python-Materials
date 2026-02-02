"""
TEMPLATE 2: INCREMENTAL BUILDER
Purpose: Build complex system one feature at a time across multiple sub-exercises
Complexity: ⭐⭐ Moderate
Best for: Multi-part exercises, building projects step-by-step
"""

# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_INCREMENTAL_NARRATIVE}}

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# ✏️ YOUR CODE HERE ✏️

def exercise_a():
    """
    {{PHASE_1_DESCRIPTION}}

    This is the foundation. All later phases build on this.
    """
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# ✏️ YOUR CODE HERE ✏️

def exercise_b():
    """
    {{PHASE_2_DESCRIPTION}}

    Builds on Phase 1 by adding [new feature].
    """
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# ✏️ YOUR CODE HERE ✏️

def exercise_c():
    """
    {{PHASE_3_DESCRIPTION}}

    Enhances Phases 1-2 with [additional capability].
    """
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# ✏️ YOUR CODE HERE ✏️

def exercise_d():
    """
    {{PHASE_4_DESCRIPTION}}

    Adds [advanced feature] to the growing system.
    """
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}
#
# ✏️ YOUR CODE HERE ✏️

def exercise_e():
    """
    {{PHASE_5_DESCRIPTION}}

    Final integration: brings all phases together.
    """
    pass


# ============================================================
# {{CONTEXT_INTEGRATION}}
# ============================================================
# {{CONTEXT_FINAL_ASSEMBLY}}

def main():
    """Run all phases in sequence."""
    print("{{CONTEXT_ASSEMBLY_START}}")
    print("=" * 60)

    print("\n{{PHASE_1_LABEL}}")
    print("-" * 60)
    exercise_a()

    print("\n{{PHASE_2_LABEL}}")
    print("-" * 60)
    exercise_b()

    print("\n{{PHASE_3_LABEL}}")
    print("-" * 60)
    exercise_c()

    print("\n{{PHASE_4_LABEL}}")
    print("-" * 60)
    exercise_d()

    print("\n{{PHASE_5_LABEL}}")
    print("-" * 60)
    exercise_e()

    print("\n" + "=" * 60)
    print("{{CONTEXT_ASSEMBLY_COMPLETE}}")


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_PROJECT_INTRO}}          - Overall project framing
# {{CONTEXT_INCREMENTAL_NARRATIVE}}  - Why building piece by piece
#
# For each phase (1-5):
# {{PHASE_N_TITLE}}                  - Phase heading
# {{CONTEXT_PHASE_N}}                - What this phase accomplishes (narrative)
# {{PHASE_N_DESCRIPTION}}            - What this phase does (technical)
# {{PHASE_N_LABEL}}                  - Label for output section
#
# Integration:
# {{CONTEXT_INTEGRATION}}            - How pieces fit together
# {{CONTEXT_FINAL_ASSEMBLY}}         - The completed system description
# {{CONTEXT_ASSEMBLY_START}}         - Message when starting full assembly
# {{CONTEXT_ASSEMBLY_COMPLETE}}      - Message when assembly complete
#
# Note: Can have fewer or more than 5 phases. Adjust as needed.
