"""Configuration management for ABAP AI Code Generator"""

import os
from dotenv import load_dotenv
from typing import Optional


class Config:
    """Configuration class for managing application settings."""

    def __init__(self):
        """Initialize configuration from environment variables."""
        load_dotenv()
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4")
        self.openai_temperature = float(os.getenv("OPENAI_TEMPERATURE", 0.7))
        
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.debug_mode = os.getenv("DEBUG_MODE", "false").lower() == "true"
        self.max_retries = int(os.getenv("MAX_RETRIES", 3))

    def validate(self) -> bool:
        """Validate that all required configuration is set."""
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        return True

    def get_openai_config(self) -> dict:
        """Get OpenAI configuration dictionary."""
        return {
            "api_key": self.openai_api_key,
            "model": self.openai_model,
            "temperature": self.openai_temperature,
        }
