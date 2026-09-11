"""Main ABAP Code Generator Class"""

from typing import Optional, Dict, List
from src.llm_client import LLMClient
from src.validator import ABAPValidator
from src.utils.config import Config
from src.utils.logger import Logger
from src.templates import report_template, function_module_template, class_template


class ABAPGenerator:
    """Main class for generating ABAP code using AI."""

    # Supported code types
    SUPPORTED_TYPES = {
        "report": "ABAP Report Program",
        "function_module": "ABAP Function Module",
        "class": "ABAP OOP Class",
        "form": "ABAP Subroutine/Form",
        "batch_input": "ABAP BDC Program",
        "rfc": "ABAP RFC-enabled Function Module",
    }

    def __init__(self, config: Optional[Config] = None):
        """Initialize the ABAP Generator."""
        self.config = config or Config()
        self.llm_client = LLMClient(self.config)
        self.validator = ABAPValidator()
        self.logger = Logger.get_logger(__name__, self.config.log_level)
        self.logger.info("ABAP Generator initialized")

    def generate(
        self,
        description: str,
        code_type: str = "report",
        context: Optional[Dict] = None,
        validate: bool = True,
    ) -> str:
        """Generate ABAP code from a natural language description."""
        if code_type not in self.SUPPORTED_TYPES:
            raise ValueError(
                f"Unsupported code type: {code_type}. "
                f"Supported types: {list(self.SUPPORTED_TYPES.keys())}"
            )

        self.logger.info(f"Generating {code_type} from description: {description}")

        # Build prompt
        prompt = self._build_prompt(description, code_type, context)

        # Generate code
        generated_code = self.llm_client.generate(prompt)
        self.logger.info("Code generation completed")

        # Validate if requested
        if validate:
            validation_result = self.validator.validate(generated_code)
            if validation_result["warnings"]:
                self.logger.warning(
                    f"Validation warnings: {validation_result['warnings']}"
                )
            if not validation_result["valid"]:
                self.logger.error(
                    f"Validation errors: {validation_result['errors']}"
                )

        return generated_code

    def analyze(self, code: str) -> Dict:
        """Analyze ABAP code and provide insights."""
        self.logger.info("Analyzing ABAP code")
        
        analysis_prompt = f"""
        Please analyze the following ABAP code and provide:
        1. Code quality assessment
        2. Potential performance issues
        3. Security concerns
        4. Best practice violations
        5. Suggested improvements
        
        Code:
        {code}
        """
        
        analysis_result = self.llm_client.analyze(code, analysis_prompt)
        return {"analysis": analysis_result}

    def suggest_improvements(self, code: str) -> List[str]:
        """Get AI suggestions for code improvements."""
        self.logger.info("Generating improvement suggestions")
        
        prompt = f"""
        Review the following ABAP code and provide specific, actionable improvement suggestions:
        
        {code}
        
        Format your response as a numbered list.
        """
        
        suggestions_text = self.llm_client.analyze(code, prompt)
        suggestions = [
            s.strip() for s in suggestions_text.split("\n") if s.strip()
        ]
        return suggestions

    def validate_code(self, code: str) -> Dict:
        """Validate ABAP code syntax and conventions."""
        self.logger.info("Validating ABAP code")
        return self.validator.validate(code)

    def _build_prompt(self, description: str, code_type: str, context: Optional[Dict]) -> str:
        """Build the prompt for the LLM."""
        code_type_desc = self.SUPPORTED_TYPES[code_type]
        
        prompt = f"""
        Generate ABAP code for the following request:
        
        Description: {description}
        Code Type: {code_type_desc}
        
        Requirements:
        1. Write clean, well-documented ABAP code
        2. Follow ABAP naming conventions
        3. Include meaningful comments
        4. Include error handling where appropriate
        5. Use modern ABAP syntax (avoid deprecated statements)
        
        Context: {context or 'None'}
        
        Please provide only the ABAP code without additional explanation.
        """
        
        return prompt

    def list_supported_types(self) -> Dict:
        """List all supported code types."""
        return self.SUPPORTED_TYPES
