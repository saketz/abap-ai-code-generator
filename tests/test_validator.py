"""Tests for ABAP Validator"""

import unittest
from src.validator import ABAPValidator


class TestABAPValidator(unittest.TestCase):
    """Test cases for ABAPValidator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.validator = ABAPValidator()

    def test_validator_initialization(self):
        """Test that validator initializes correctly."""
        self.assertIsNotNone(self.validator)
        self.assertEqual(self.validator.errors, [])
        self.assertEqual(self.validator.warnings, [])

    def test_basic_code_validation(self):
        """Test validation of basic ABAP code."""
        code = """REPORT z_test_report.
        DATA: lv_var TYPE i.
        START-OF-SELECTION.
          WRITE: / 'Hello World'.
        END-OF-SELECTION.
        """
        result = self.validator.validate(code)
        self.assertIsNotNone(result)
        self.assertIn("valid", result)
        self.assertIn("errors", result)
        self.assertIn("warnings", result)


if __name__ == "__main__":
    unittest.main()
