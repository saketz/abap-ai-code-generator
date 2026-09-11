# ABAP AI Code Generator

An intelligent tool for generating ABAP (Advanced Business Application Programming) code using AI language models.

## Features

- 🤖 AI-powered ABAP code generation
- 📝 Natural language to ABAP conversion
- 🔍 Code analysis and suggestions
- 🛠️ Support for common ABAP patterns
- 📚 Code templates and snippets
- ✅ Syntax validation

## Prerequisites

- Python 3.8+
- OpenAI API key (or compatible LLM)
- pip package manager

## Installation

```bash
git clone https://github.com/saketz/abap-ai-code-generator.git
cd abap-ai-code-generator
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4
```

## Quick Start

```python
from abap_generator import ABAPGenerator

generator = ABAPGenerator()

# Generate ABAP code from natural language
code = generator.generate(
    description="Create a simple report that reads from VBAK table"
)
print(code)
```

## Usage Examples

### Example 1: Generate a Basic Report

```python
from abap_generator import ABAPGenerator

generator = ABAPGenerator()
description = "Write a report to fetch all sales orders from VBAK table with filters"
code = generator.generate(description)
print(code)
```

### Example 2: Generate a Function Module

```python
from abap_generator import ABAPGenerator

generator = ABAPGenerator()
description = "Create a function module that calculates total sales amount"
code = generator.generate(description, code_type="function_module")
print(code)
```

## Supported Code Types

- `report` - Standard ABAP reports
- `function_module` - Function modules (FM)
- `class` - OOP classes
- `form` - Subroutines/Forms
- `batch_input` - BDC programs
- `rfc` - Remote Function Calls

## API Reference

### ABAPGenerator

#### `__init__(model='gpt-4', temperature=0.7)`
Initialize the ABAP generator.

**Parameters:**
- `model` (str): LLM model to use
- `temperature` (float): Creativity level (0-1)

#### `generate(description, code_type='report', context=None)`
Generate ABAP code from description.

**Parameters:**
- `description` (str): Natural language description
- `code_type` (str): Type of code to generate
- `context` (dict): Additional context

**Returns:**
- `str`: Generated ABAP code

#### `validate(code)`
Validate ABAP code syntax.

**Parameters:**
- `code` (str): ABAP code to validate

**Returns:**
- `dict`: Validation results

#### `suggest_improvements(code)`
Get AI suggestions for code improvements.

**Parameters:**
- `code` (str): ABAP code

**Returns:**
- `list`: List of suggestions

## Project Structure

```
abap-ai-code-generator/
├── src/
│   ├── abap_generator.py       # Main generator class
│   ├── llm_client.py           # LLM API client
│   ├── validator.py            # ABAP syntax validator
│   ├── templates/              # Code templates
│   │   ├── report.py
│   │   ├── function_module.py
│   │   ├── class.py
│   │   └── form.py
│   └── utils/
│       ├── config.py           # Configuration management
│       └── logger.py           # Logging utilities
├── tests/
│   ├── test_generator.py
│   ├── test_validator.py
│   └── test_templates.py
├── examples/
│   ├── basic_report.py
│   ├── function_module.py
│   └── oop_class.py
├── requirements.txt
├── .env.example
└── README.md
```

## Examples

See the `examples/` directory for complete working examples.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Acknowledgments

- OpenAI for providing powerful language models
- SAP ABAP community for documentation and best practices
