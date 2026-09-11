"""ABAP AI Code Generator Package"""

__version__ = "0.1.0"
__author__ = "ABAP AI Generator Team"
__license__ = "MIT"

from .abap_generator import ABAPGenerator
from .utils.config import Config

__all__ = ["ABAPGenerator", "Config"]
