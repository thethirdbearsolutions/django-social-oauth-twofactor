"""Top-level package for Django Social OAuth Two Factor."""

__author__ = """Ethan Jucovy"""
__email__ = 'hello@thirdbearsolutions.com'
__version__ = '0.1.0'

from .core import settings
from .utils import enforce_2fa_setup
