"""
Main init file for the sssdevops package
"""

from .sssdevops import *
from .listtools import *


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
