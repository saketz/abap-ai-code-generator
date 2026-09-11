"""Example: Generate a Basic ABAP Report"""

from src.abap_generator import ABAPGenerator


def generate_sales_report():
    """Generate a report that reads from VBAK table."""
    generator = ABAPGenerator()
    
    description = """
    Create a simple report that:
    1. Reads sales orders from VBAK table
    2. Filters for orders created in the last 30 days
    3. Displays order number, customer, and order date
    4. Shows total number of orders found
    """
    
    code = generator.generate(
        description=description,
        code_type="report"
    )
    
    print("Generated ABAP Report:")
    print("=" * 50)
    print(code)
    print("=" * 50)
    
    # Validate the generated code
    validation = generator.validate_code(code)
    print(f"\nValidation Result: {validation['valid']}")
    if validation['warnings']:
        print(f"Warnings: {validation['warnings']}")


if __name__ == "__main__":
    generate_sales_report()
