"""
Initializes the py_stats_toolkit package.

This __init__.py file is used to expose the main statistical calculation functions
from the 'calculations' submodule directly under the 'py_stats_toolkit' namespace.
This allows users to import functions like 'from py_stats_toolkit import calculate_mean'
instead of 'from py_stats_toolkit.calculations import calculate_mean'.

It also defines __all__ to explicitly control which names are exported when
'from py_stats_toolkit import *' is used.
"""

from .calculations import (
    calculate_count,
    calculate_sum,
    calculate_mean,
    calculate_min,
    calculate_max,
    calculate_harmonic_mean,
    calculate_variance,
    calculate_std_dev
)

# Define __all__ to explicitly control what 'from py_stats_toolkit import *' imports
__all__ = [
    'calculate_count',
    'calculate_sum',
    'calculate_mean',
    'calculate_min',
    'calculate_max',
    'calculate_harmonic_mean',
    'calculate_variance',
    'calculate_std_dev'
]

# Package-level setup below
# None
