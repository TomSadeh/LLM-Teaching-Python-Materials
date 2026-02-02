"""
TEMPLATE 9: WORLD BUILDER
Purpose: Create interconnected systems where objects/entities interact
Complexity: ⭐⭐⭐ Advanced
Best for: OOP exercises, complex data structures, system design
"""

"""
{{CONTEXT_WORLD_INTRO}}

{{CONTEXT_WORLD_VISION}}
"""

# ============================================================
# {{ENTITY_TYPE_1}} - {{ENTITY_TYPE_1_DESCRIPTION}}
# ============================================================
# {{CONTEXT_ENTITY_1_NARRATIVE}}


def create_entity_1(name, attribute1, attribute2):
    """
    {{ENTITY_1_CREATION_DESCRIPTION}}

    Args:
        name (str): {{ENTITY_1_NAME_PARAM}}
        attribute1 (type): {{ENTITY_1_ATTR1_PARAM}}
        attribute2 (type): {{ENTITY_1_ATTR2_PARAM}}

    Returns:
        dict: {{ENTITY_1_RETURN_DESCRIPTION}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Create a dictionary representing this entity type
    # Include all required attributes
    pass


# ============================================================
# {{ENTITY_TYPE_2}} - {{ENTITY_TYPE_2_DESCRIPTION}}
# ============================================================
# {{CONTEXT_ENTITY_2_NARRATIVE}}


def create_entity_2(name, attribute1, attribute2):
    """
    {{ENTITY_2_CREATION_DESCRIPTION}}

    Args:
        name (str): {{ENTITY_2_NAME_PARAM}}
        attribute1 (type): {{ENTITY_2_ATTR1_PARAM}}
        attribute2 (type): {{ENTITY_2_ATTR2_PARAM}}

    Returns:
        dict: {{ENTITY_2_RETURN_DESCRIPTION}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{ENTITY_TYPE_3}} - {{ENTITY_TYPE_3_DESCRIPTION}}
# ============================================================
# {{CONTEXT_ENTITY_3_NARRATIVE}}


def create_entity_3(name, attribute1):
    """
    {{ENTITY_3_CREATION_DESCRIPTION}}

    Args:
        name (str): {{ENTITY_3_NAME_PARAM}}
        attribute1 (type): {{ENTITY_3_ATTR1_PARAM}}

    Returns:
        dict: {{ENTITY_3_RETURN_DESCRIPTION}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{INTERACTION_TITLE_1_2}}
# ============================================================
# {{CONTEXT_INTERACTION_1_2_NARRATIVE}}


def entities_interact_1_2(entity1, entity2):
    """
    {{INTERACTION_1_2_DESCRIPTION}}

    Args:
        entity1 (dict): {{ENTITY_TYPE_1}}
        entity2 (dict): {{ENTITY_TYPE_2}}

    Returns:
        str: {{INTERACTION_1_2_RESULT}}

    {{CONTEXT_INTERACTION_1_2_RULES}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Determine interaction outcome based on entity attributes
    # Return description of what happens
    pass


# ============================================================
# {{INTERACTION_TITLE_2_3}}
# ============================================================
# {{CONTEXT_INTERACTION_2_3_NARRATIVE}}


def entities_interact_2_3(entity2, entity3):
    """
    {{INTERACTION_2_3_DESCRIPTION}}

    Args:
        entity2 (dict): {{ENTITY_TYPE_2}}
        entity3 (dict): {{ENTITY_TYPE_3}}

    Returns:
        str: {{INTERACTION_2_3_RESULT}}

    {{CONTEXT_INTERACTION_2_3_RULES}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{SYSTEM_TITLE}}
# ============================================================
# {{CONTEXT_SYSTEM_NARRATIVE}}


def create_ecosystem():
    """
    {{SYSTEM_CREATION_DESCRIPTION}}

    Creates multiple entities and demonstrates their interactions.
    This is where your world comes alive!
    """
    # ✏️ YOUR CODE HERE ✏️
    # 1. Create instances of each entity type
    # 2. Display entity details
    # 3. Show interactions between entities
    # 4. Print results

    pass


# ============================================================
# WORLD SIMULATION
# ============================================================


def display_entity(entity, entity_type):
    """
    Display an entity's details in formatted output.

    Args:
        entity (dict): The entity to display
        entity_type (str): Type label (for display purposes)
    """
    print(f"\n{{CONTEXT_ENTITY_DISPLAY_HEADER}} {entity_type}")
    print("-" * 40)
    for key, value in entity.items():
        print(f"  {key}: {value}")


def main():
    """Run complete world simulation."""
    print("=" * 60)
    print("{{CONTEXT_WORLD_BUILDING_START}}")
    print("=" * 60)

    # Example entities (for testing)
    print("\n{{CONTEXT_EXAMPLE_CREATION}}")

    # Create example of Entity Type 1
    entity1_example = create_entity_1(
        "{{ENTITY_1_EXAMPLE_NAME}}",
        "{{ENTITY_1_EXAMPLE_ATTR1}}",
        10
    )
    if entity1_example:
        display_entity(entity1_example, "{{ENTITY_TYPE_1}}")

    # Create example of Entity Type 2
    entity2_example = create_entity_2(
        "{{ENTITY_2_EXAMPLE_NAME}}",
        "{{ENTITY_2_EXAMPLE_ATTR1}}",
        True
    )
    if entity2_example:
        display_entity(entity2_example, "{{ENTITY_TYPE_2}}")

    # Create example of Entity Type 3
    entity3_example = create_entity_3(
        "{{ENTITY_3_EXAMPLE_NAME}}",
        "{{ENTITY_3_EXAMPLE_ATTR1}}"
    )
    if entity3_example:
        display_entity(entity3_example, "{{ENTITY_TYPE_3}}")

    # Show interactions
    if entity1_example and entity2_example:
        print("\n{{CONTEXT_INTERACTION_DEMO_1_2}}")
        print("-" * 40)
        result = entities_interact_1_2(entity1_example, entity2_example)
        if result:
            print(result)

    if entity2_example and entity3_example:
        print("\n{{CONTEXT_INTERACTION_DEMO_2_3}}")
        print("-" * 40)
        result = entities_interact_2_3(entity2_example, entity3_example)
        if result:
            print(result)

    # Full ecosystem
    print("\n" + "=" * 60)
    print("{{CONTEXT_ECOSYSTEM_CREATION}}")
    print("=" * 60)
    create_ecosystem()

    print("\n" + "=" * 60)
    print("{{CONTEXT_WORLD_BUILDING_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_WORLD_INTRO}}              - The world being created
# {{CONTEXT_WORLD_VISION}}             - What the complete system will do
#
# For each entity type (1-3):
# {{ENTITY_TYPE_N}}                    - Name of entity type
# {{ENTITY_TYPE_N_DESCRIPTION}}        - Brief description
# {{CONTEXT_ENTITY_N_NARRATIVE}}       - Story behind this entity type
# {{ENTITY_N_CREATION_DESCRIPTION}}    - Technical: what creation function does
# {{ENTITY_N_NAME_PARAM}}              - Description of name parameter
# {{ENTITY_N_ATTR1_PARAM}}             - Description of attribute 1
# {{ENTITY_N_ATTR2_PARAM}}             - Description of attribute 2 (if applicable)
# {{ENTITY_N_RETURN_DESCRIPTION}}      - What creation function returns
# {{ENTITY_N_EXAMPLE_NAME}}            - Example name for testing
# {{ENTITY_N_EXAMPLE_ATTR1}}           - Example attribute value
#
# For each interaction (1-2, 2-3):
# {{INTERACTION_TITLE_X_Y}}            - Interaction heading
# {{CONTEXT_INTERACTION_X_Y_NARRATIVE}} - Story behind interaction
# {{INTERACTION_X_Y_DESCRIPTION}}      - Technical description
# {{INTERACTION_X_Y_RESULT}}           - What function returns
# {{CONTEXT_INTERACTION_X_Y_RULES}}    - Rules governing interaction
# {{CONTEXT_INTERACTION_DEMO_X_Y}}     - Label for demo output
#
# System/World:
# {{SYSTEM_TITLE}}                     - Ecosystem/system heading
# {{CONTEXT_SYSTEM_NARRATIVE}}         - How system works as whole
# {{SYSTEM_CREATION_DESCRIPTION}}      - What ecosystem function does
# {{CONTEXT_ENTITY_DISPLAY_HEADER}}    - Label for entity display
# {{CONTEXT_EXAMPLE_CREATION}}         - Label for example section
# {{CONTEXT_ECOSYSTEM_CREATION}}       - Label for ecosystem section
# {{CONTEXT_WORLD_BUILDING_START}}     - Opening message
# {{CONTEXT_WORLD_BUILDING_COMPLETE}}  - Closing message
#
# Note: Can have more or fewer entity types and interactions. Adjust as needed.
