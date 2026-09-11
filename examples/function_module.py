"""Example: Generate an ABAP Function Module"""

from src.abap_generator import ABAPGenerator


def generate_calculation_function():
    """Generate a function module for calculations."""
    generator = ABAPGenerator()
    
    description = """
    Create a function module named Z_CALCULATE_DISCOUNT that:
    1. Takes order amount and customer type as input
    2. Calculates discount percentage based on customer type
    3. Returns the discount amount and final price
    4. Includes error handling for invalid inputs
    """
    
    code = generator.generate(
        description=description,
        code_type="function_module"
    )
    
    print("Generated ABAP Function Module:")
    print("=" * 50)
    print(code)
    print("=" * 50)
    
    # Get improvement suggestions
    suggestions = generator.suggest_improvements(code)
    print("\nSuggested Improvements:")
    for suggestion in suggestions:
        print(f"  - {suggestion}")


if __name__ == "__main__":
    generate_calculation_function()
