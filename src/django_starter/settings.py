"""
Django settings for Django_Starter project.
Import all settings from the modular settings files.
"""

from .settings.base import *

try:
    from .settings.development import *
except ImportError:
    pass
