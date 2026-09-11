"""Example: Generate an ABAP OOP Class"""

from src.abap_generator import ABAPGenerator


def generate_logger_class():
    """Generate an OOP class for logging."""
    generator = ABAPGenerator()
    
    description = """
    Create an ABAP OOP class named ZCL_LOGGER that:
    1. Has methods for different log levels (DEBUG, INFO, WARNING, ERROR)
    2. Writes logs to a table or file
    3. Has a private attribute for log level threshold
    4. Implements singleton pattern for single instance
    5. Has timestamps for all log entries
    """
    
    code = generator.generate(
        description=description,
        code_type="class"
    )
    
    print("Generated ABAP OOP Class:")
    print("=" * 50)
    print(code)
    print("=" * 50)
    
    # Analyze the code
    analysis = generator.analyze(code)
    print("\nCode Analysis:")
    print(analysis['analysis'])


if __name__ == "__main__":
    generate_logger_class()
