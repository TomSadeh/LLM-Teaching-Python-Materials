"""
TEMPLATE 12: RESOURCE EXCHANGE
Purpose: Trade/convert/exchange between entity types or resource types
Complexity: ⭐ Simple
Best for: Type conversion, currency exchange, trading systems, resource management
"""

"""
{{CONTEXT_EXCHANGE_INTRO}}

{{CONTEXT_EXCHANGE_PURPOSE}}
"""

# ============================================================
# EXCHANGE RATES
# ============================================================
# {{CONTEXT_EXCHANGE_RATES_NARRATIVE}}

EXCHANGE_RATES = {
    "{{RESOURCE_1}}_to_{{RESOURCE_2}}": "{{RATE_1_TO_2}}",
    "{{RESOURCE_2}}_to_{{RESOURCE_3}}": "{{RATE_2_TO_3}}",
    "{{RESOURCE_1}}_to_{{RESOURCE_3}}": "{{RATE_1_TO_3}}",
}

# ============================================================
# {{EXCHANGE_1_TITLE}}
# ============================================================
# {{CONTEXT_EXCHANGE_1_NARRATIVE}}


def exchange_resource_1_to_2(amount):
    """
    {{EXCHANGE_1_DESCRIPTION}}

    Args:
        amount (int/float): {{EXCHANGE_1_AMOUNT_PARAM}}

    Returns:
        int/float: {{EXCHANGE_1_RETURN}}

    Example:
        {{EXCHANGE_1_EXAMPLE}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Calculate exchange based on rate
    # Return converted amount
    pass


# ============================================================
# {{EXCHANGE_2_TITLE}}
# ============================================================
# {{CONTEXT_EXCHANGE_2_NARRATIVE}}


def exchange_resource_2_to_3(amount):
    """
    {{EXCHANGE_2_DESCRIPTION}}

    Args:
        amount (int/float): {{EXCHANGE_2_AMOUNT_PARAM}}

    Returns:
        int/float: {{EXCHANGE_2_RETURN}}

    Example:
        {{EXCHANGE_2_EXAMPLE}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{EXCHANGE_3_TITLE}}
# ============================================================
# {{CONTEXT_EXCHANGE_3_NARRATIVE}}


def exchange_resource_1_to_3(amount):
    """
    {{EXCHANGE_3_DESCRIPTION}}

    Args:
        amount (int/float): {{EXCHANGE_3_AMOUNT_PARAM}}

    Returns:
        int/float: {{EXCHANGE_3_RETURN}}

    Example:
        {{EXCHANGE_3_EXAMPLE}}
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{TRADE_TITLE}}
# ============================================================
# {{CONTEXT_TRADE_NARRATIVE}}


def complete_trade(resource_type, amount, target_resource):
    """
    {{TRADE_DESCRIPTION}}

    Args:
        resource_type (str): {{TRADE_RESOURCE_PARAM}}
        amount (int/float): {{TRADE_AMOUNT_PARAM}}
        target_resource (str): {{TRADE_TARGET_PARAM}}

    Returns:
        int/float: {{TRADE_RETURN}}

    {{CONTEXT_TRADE_VALIDATION}}
    """
    # ✏️ YOUR CODE HERE ✏️
    # Determine which exchange function to call
    # Validate inputs
    # Perform exchange
    # Return result
    pass


# ============================================================
# EXCHANGE DEMONSTRATION
# ============================================================


def demonstrate_exchanges():
    """Show all possible exchanges with examples."""
    print("=" * 60)
    print("{{CONTEXT_DEMO_START}}")
    print("=" * 60)
    print()

    # Exchange 1
    print("{{EXCHANGE_1_DEMO_LABEL}}")
    print("-" * 60)
    original = "{{DEMO_AMOUNT_1}}"
    result = exchange_resource_1_to_2(float(original))
    if result:
        print(f"{{CONTEXT_EXCHANGE_DISPLAY_1}}")
        print(f"{original} {{RESOURCE_1}} → {result} {{RESOURCE_2}}")
    print()

    # Exchange 2
    print("{{EXCHANGE_2_DEMO_LABEL}}")
    print("-" * 60)
    original = "{{DEMO_AMOUNT_2}}"
    result = exchange_resource_2_to_3(float(original))
    if result:
        print(f"{{CONTEXT_EXCHANGE_DISPLAY_2}}")
        print(f"{original} {{RESOURCE_2}} → {result} {{RESOURCE_3}}")
    print()

    # Exchange 3
    print("{{EXCHANGE_3_DEMO_LABEL}}")
    print("-" * 60)
    original = "{{DEMO_AMOUNT_3}}"
    result = exchange_resource_1_to_3(float(original))
    if result:
        print(f"{{CONTEXT_EXCHANGE_DISPLAY_3}}")
        print(f"{original} {{RESOURCE_1}} → {result} {{RESOURCE_3}}")
    print()

    # Complete trade example
    print("{{TRADE_DEMO_LABEL}}")
    print("-" * 60)
    trade_result = complete_trade("{{RESOURCE_1}}", float("{{DEMO_AMOUNT_4}}"), "{{RESOURCE_3}}")
    if trade_result:
        print(f"{{CONTEXT_TRADE_DISPLAY}}")
        print(f"{{DEMO_AMOUNT_4}} {{RESOURCE_1}} → {trade_result} {{RESOURCE_3}}")
    print()

    print("=" * 60)
    print("{{CONTEXT_DEMO_COMPLETE}}")
    print("=" * 60)


def main():
    """Run exchange demonstrations."""
    print("{{CONTEXT_EXCHANGE_WELCOME}}")
    print()

    # Show exchange rates
    print("{{CONTEXT_RATES_DISPLAY_TITLE}}")
    print("-" * 60)
    print(f"1 {{RESOURCE_1}} = {EXCHANGE_RATES['{{RESOURCE_1}}_to_{{RESOURCE_2}}']} {{RESOURCE_2}}")
    print(f"1 {{RESOURCE_2}} = {EXCHANGE_RATES['{{RESOURCE_2}}_to_{{RESOURCE_3}}']} {{RESOURCE_3}}")
    print(f"1 {{RESOURCE_1}} = {EXCHANGE_RATES['{{RESOURCE_1}}_to_{{RESOURCE_3}}']} {{RESOURCE_3}}")
    print()

    # Run demonstrations
    demonstrate_exchanges()


if __name__ == "__main__":
    main()


# ============================================================
# CONTEXT BLOCKS REFERENCE
# ============================================================
# {{CONTEXT_EXCHANGE_INTRO}}           - Why exchange/trading matters
# {{CONTEXT_EXCHANGE_PURPOSE}}         - What system accomplishes
# {{CONTEXT_EXCHANGE_RATES_NARRATIVE}} - Explanation of rates
#
# Resources (1-3):
# {{RESOURCE_N}}                       - Name of resource type
# {{RATE_X_TO_Y}}                      - Exchange rate value
#
# For each exchange (1-3):
# {{EXCHANGE_N_TITLE}}                 - Exchange heading
# {{CONTEXT_EXCHANGE_N_NARRATIVE}}     - Story behind exchange
# {{EXCHANGE_N_DESCRIPTION}}           - Technical description
# {{EXCHANGE_N_AMOUNT_PARAM}}          - Amount parameter description
# {{EXCHANGE_N_RETURN}}                - Return value description
# {{EXCHANGE_N_EXAMPLE}}               - Usage example
# {{EXCHANGE_N_DEMO_LABEL}}            - Label for demo output
# {{CONTEXT_EXCHANGE_DISPLAY_N}}       - Display message
#
# Trading:
# {{TRADE_TITLE}}                      - Complete trade function heading
# {{CONTEXT_TRADE_NARRATIVE}}          - Story behind trading
# {{TRADE_DESCRIPTION}}                - Technical description
# {{TRADE_RESOURCE_PARAM}}             - Resource type parameter
# {{TRADE_AMOUNT_PARAM}}               - Amount parameter
# {{TRADE_TARGET_PARAM}}               - Target resource parameter
# {{TRADE_RETURN}}                     - Return value
# {{CONTEXT_TRADE_VALIDATION}}         - Validation rules
# {{TRADE_DEMO_LABEL}}                 - Label for trade demo
# {{CONTEXT_TRADE_DISPLAY}}            - Trade display message
#
# Demonstration:
# {{CONTEXT_DEMO_START}}               - Demo opening message
# {{DEMO_AMOUNT_N}}                    - Example amounts for demos (1-4)
# {{CONTEXT_DEMO_COMPLETE}}            - Demo closing message
# {{CONTEXT_EXCHANGE_WELCOME}}         - Welcome message
# {{CONTEXT_RATES_DISPLAY_TITLE}}      - Title for rates display
#
# Note: Can have more resource types and exchange pairs. Adjust as needed.
