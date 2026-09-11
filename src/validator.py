"""ABAP Code Validator"""

import re
from typing import Dict, List
from src.utils.logger import Logger


class ABAPValidator:
    """Validator for ABAP code syntax and patterns."""

    def __init__(self):
        """Initialize the validator."""
        self.logger = Logger.get_logger(__name__)
        self.errors = []
        self.warnings = []

    def validate(self, code: str) -> Dict:
        """Validate ABAP code."""
        self.errors = []
        self.warnings = []
        
        self._check_syntax(code)
        self._check_naming_conventions(code)
        self._check_best_practices(code)
        
        return {
            "valid": len(self.errors) == 0,
            "errors": self.errors,
            "warnings": self.warnings,
        }

    def _check_syntax(self, code: str) -> None:
        """Check basic ABAP syntax."""
        lines = code.split("\n")
        
        # Check for matching REPORT/PROGRAM declarations
        if not re.search(r"^REPORT|^PROGRAM", code, re.MULTILINE):
            self.warnings.append("No REPORT or PROGRAM statement found")
        
        # Check for END-OF-SELECTION if START-OF-SELECTION is present
        if "START-OF-SELECTION" in code and "END-OF-SELECTION" not in code:
            self.warnings.append(
                "START-OF-SELECTION found but no END-OF-SELECTION"
            )

    def _check_naming_conventions(self, code: str) -> None:
        """Check ABAP naming conventions."""
        # Find variable declarations
        var_pattern = r"DATA\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+TYPE"
        variables = re.findall(var_pattern, code)
        
        for var in variables:
            # ABAP convention: lowercase with underscores or camelCase
            if not re.match(r"^[a-z][a-z0-9_]*$|^[a-z][a-zA-Z0-9]*$", var):
                self.warnings.append(
                    f"Variable '{var}' does not follow naming conventions"
                )

    def _check_best_practices(self, code: str) -> None:
        """Check ABAP best practices."""
        # Check for deprecated WRITE statements (suggest WRITE TO)
        if re.search(r"^WRITE\s+['\"].*['\"]\.", code, re.MULTILINE):
            self.warnings.append(
                "Consider using modern ALV for output instead of WRITE"
            )
        
        # Check for SELECT without WHERE (performance issue)
        select_pattern = r"SELECT\s+\*\s+FROM\s+\w+\s*\.(?!\s*WHERE)"
        if re.search(select_pattern, code, re.IGNORECASE):
            self.warnings.append(
                "SELECT * without WHERE clause may have performance issues"
            )
