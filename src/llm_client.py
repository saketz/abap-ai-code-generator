"""OpenAI LLM Client for ABAP Code Generation"""

import openai
from typing import Optional
from src.utils.config import Config
from src.utils.logger import Logger


class LLMClient:
    """Client for interacting with OpenAI language models."""

    def __init__(self, config: Optional[Config] = None):
        """Initialize the LLM client."""
        self.config = config or Config()
        self.config.validate()
        self.logger = Logger.get_logger(__name__)
        
        # Configure OpenAI
        openai.api_key = self.config.openai_api_key

    def generate(self, prompt: str, max_tokens: int = 2000) -> str:
        """Generate text using OpenAI API."""
        try:
            self.logger.info(f"Generating with model: {self.config.openai_model}")
            
            response = openai.ChatCompletion.create(
                model=self.config.openai_model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert ABAP programmer. Generate clean, well-documented ABAP code.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=self.config.openai_temperature,
                max_tokens=max_tokens,
            )
            
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Error generating code: {str(e)}")
            raise

    def analyze(self, code: str, prompt: str) -> str:
        """Analyze code with a specific prompt."""
        try:
            response = openai.ChatCompletion.create(
                model=self.config.openai_model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert ABAP code analyst.",
                    },
                    {
                        "role": "user",
                        "content": f"Code:\n{code}\n\nRequest: {prompt}",
                    },
                ],
                temperature=0.5,
                max_tokens=1500,
            )
            
            return response.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Error analyzing code: {str(e)}")
            raise
