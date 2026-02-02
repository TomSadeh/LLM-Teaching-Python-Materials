"""
TEMPLATE 11: BATCH PROCESSOR
Purpose: Perform similar operation on multiple items
Complexity: ⭐ Simple
Best for: Lists, loops, comprehensions, applying functions to collections
"""

"""
{{CONTEXT_BATCH_INTRO}}

{{CONTEXT_BATCH_PURPOSE}}
"""

# ============================================================
# THE COLLECTION
# ============================================================
# {{CONTEXT_COLLECTION_NARRATIVE}}

# The items to process
BATCH_ITEMS = [
    "{{BATCH_ITEM_1}}",
    "{{BATCH_ITEM_2}}",
    "{{BATCH_ITEM_3}}",
    "{{BATCH_ITEM_4}}",
    "{{BATCH_ITEM_5}}"
]

# ============================================================
# {{OPERATION_1_TITLE}}
# ============================================================
# {{CONTEXT_OPERATION_1_NARRATIVE}}


def process_operation_1(items):
    """
    {{OPERATION_1_DESCRIPTION}}

    Args:
        items (list): {{OPERATION_1_INPUT}}

    Returns:
        list: {{OPERATION_1_OUTPUT}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Process each item in the collection
    # Apply operation 1 to each
    # Return results
    pass


# ============================================================
# {{OPERATION_2_TITLE}}
# ============================================================
# {{CONTEXT_OPERATION_2_NARRATIVE}}


def process_operation_2(items):
    """
    {{OPERATION_2_DESCRIPTION}}

    Args:
        items (list): {{OPERATION_2_INPUT}}

    Returns:
        list: {{OPERATION_2_OUTPUT}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{OPERATION_3_TITLE}}
# ============================================================
# {{CONTEXT_OPERATION_3_NARRATIVE}}


def process_operation_3(items):
    """
    {{OPERATION_3_DESCRIPTION}}

    Args:
        items (list): {{OPERATION_3_INPUT}}

    Returns:
        type: {{OPERATION_3_OUTPUT}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# BATCH PROCESSING EXECUTION
# ============================================================


def main():
    """Run all batch operations."""
    print("=" * 60)
    print("{{CONTEXT_BATCH_START}}")
    print("=" * 60)
    print()

    # Show original collection
    print("{{CONTEXT_ORIGINAL_COLLECTION}}")
    print("-" * 60)
    for i, item in enumerate(BATCH_ITEMS, 1):
        print(f"{i}. {item}")
    print()

    # Operation 1
    print("{{OPERATION_1_LABEL}}")
    print("-" * 60)
    result1 = process_operation_1(BATCH_ITEMS)
    if result1:
        for i, item in enumerate(result1, 1):
            print(f"{i}. {item}")
    print()

    # Operation 2
    print("{{OPERATION_2_LABEL}}")
    print("-" * 60)
    result2 = process_operation_2(BATCH_ITEMS)
    if result2:
        for i, item in enumerate(result2, 1):
            print(f"{i}. {item}")
    print()

    # Operation 3
    print("{{OPERATION_3_LABEL}}")
    print("-" * 60)
    result3 = process_operation_3(BATCH_ITEMS)
    if result3:
        print(result3)
    print()

    print("=" * 60)
    print("{{CONTEXT_BATCH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_BATCH_INTRO}}              - Why batch processing matters
# {{CONTEXT_BATCH_PURPOSE}}            - What we're accomplishing
# {{CONTEXT_COLLECTION_NARRATIVE}}     - Story behind the collection
#
# The items (1-5):
# {{BATCH_ITEM_N}}                     - Individual item values
#
# For each operation (1-3):
# {{OPERATION_N_TITLE}}                - Operation heading
# {{CONTEXT_OPERATION_N_NARRATIVE}}    - Story behind operation
# {{OPERATION_N_DESCRIPTION}}          - Technical description
# {{OPERATION_N_INPUT}}                - Input parameter description
# {{OPERATION_N_OUTPUT}}               - Return value description
# {{OPERATION_N_LABEL}}                - Label for output section
#
# Execution:
# {{CONTEXT_BATCH_START}}              - Opening message
# {{CONTEXT_ORIGINAL_COLLECTION}}      - Label for original items
# {{CONTEXT_BATCH_COMPLETE}}           - Closing message
#
# Note: Can have more items or operations. Adjust as needed.
