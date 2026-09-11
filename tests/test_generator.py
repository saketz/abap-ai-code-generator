"""Tests for ABAP Generator"""

import unittest
from src.abap_generator import ABAPGenerator
from src.utils.config import Config


class TestABAPGenerator(unittest.TestCase):
    """Test cases for ABAPGenerator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.config = Config()
        self.generator = ABAPGenerator(self.config)

    def test_generator_initialization(self):
        """Test that generator initializes correctly."""
        self.assertIsNotNone(self.generator)
        self.assertIsNotNone(self.generator.llm_client)
        self.assertIsNotNone(self.generator.validator)

    def test_supported_types(self):
        """Test that all supported code types are defined."""
        supported_types = self.generator.list_supported_types()
        self.assertIn("report", supported_types)
        self.assertIn("function_module", supported_types)
        self.assertIn("class", supported_types)
        self.assertIn("form", supported_types)
        self.assertIn("batch_input", supported_types)
        self.assertIn("rfc", supported_types)

    def test_invalid_code_type(self):
        """Test that invalid code type raises error."""
        with self.assertRaises(ValueError):
            self.generator.generate(
                "Create a simple report",
                code_type="invalid_type"
            )


if __name__ == "__main__":
    unittest.main()
