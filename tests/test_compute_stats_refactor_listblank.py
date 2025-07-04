"""
This module contains unit tests specifically designed to verify the behavior
of the statistical calculation functions from 'py_stats_toolkit' when
provided with **empty input lists**.

It uses the unittest framework to assert expected return values (e.g., for
count and sum) or, critically, to confirm that appropriate ValueError
exceptions are raised for functions that cannot operate on empty data.
"""

import unittest
from py_stats_toolkit import (
    calculate_count,
    calculate_sum,
    calculate_mean,
    calculate_min,
    calculate_max,
    calculate_harmonic_mean,
    calculate_variance,
    calculate_std_dev
)

class TestComputeStatsEmptyList(unittest.TestCase):
    """
    Test suite for the statistical computation functions, focusing on edge cases
    with empty input lists.

    Each test method verifies that functions handle an empty list as input,
    either by returning an expected default value (like 0) or by raising
    the appropriate ValueError exception with a specific error message.
    """

    # Define an empty dataset to specifically test edge cases and error handling.
    sample_data = []

    def test_201_calculate_count(self):
        """
        Verifies that 'calculate_count' correctly returns 0 when provided
        with an empty list.
        """
        self.assertEqual(calculate_count(self.sample_data), 0)

    def test_202_calculate_sum(self):
        """
        Ensures 'calculate_sum' accurately returns 0 when provided with
        an empty list.
        """
        self.assertEqual(calculate_sum(self.sample_data), 0)

    def test_203_calculate_mean(self):
        """
        Tests that 'calculate_mean' raises a ValueError when provided with
        an empty list, and verifies the exact error message.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_mean(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate average of an empty list")

    def test_204_calculate_min(self):
        """
        Tests that 'calculate_min' raises a ValueError when provided with
        an empty list, and verifies the exact error message.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_min(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot find minimum value of an empty list")

    def test_205_calculate_max(self):
        """
        Tests that 'calculate_max' raises a ValueError when provided with
        an empty list, and verifies the exact error message.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_max(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot find maximum value of an empty list")

    def test_206_calculate_harmonic_mean(self):
        """
        Tests that 'calculate_harmonic_mean' raises a ValueError when provided
        with an empty list, and verifies the exact error message.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_harmonic_mean(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate harmonic mean of an empty list")

    def test_207_calculate_variance(self):
        """
        Tests that 'calculate_variance' raises a ValueError when provided with
        an empty list, and verifies the exact error message.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_variance(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate variance of an empty list")

    def test_208_calculate_std_dev(self):
        """
        Tests that 'calculate_std_dev' raises a ValueError when provided with
        an empty list, and verifies the exact error message.
        """
        with self.assertRaises(ValueError) as cm:
            calculate_std_dev(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate standard deviation of an empty list")

# This block allows the tests to be run directly from the command line,
# e.g., by executing 'python your_test_file.py'.
if __name__ == '__main__':
    # unittest.main() is the standard entry point for running all tests
    # discovered in this module.
    #
    # argv=['ignored', '-v']:
    #   - 'ignored': This is a dummy argument for sys.argv[0]. unittest.main
    #                expects the first argument to be the script name.
    #   - '-v': This flag enables verbose output, causing unittest to print
    #           the name of each test method as it runs, which is useful
    #           for detailed feedback during development or demos.
    #
    # exit=False:
    #   - This prevents unittest.main from calling sys.exit(), which
    #     would terminate the script after tests are run. It's often
    #     useful when running tests from an IDE, a larger script, or
    #     in environments where you want to continue execution after tests.
    unittest.main(argv=['ignored', '-v'], exit=False)
    