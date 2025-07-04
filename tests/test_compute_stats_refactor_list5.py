"""
This module contains unit tests for the statistical calculation functions
provided by the 'py_stats_toolkit' package.

It leverages Python's built-in 'unittest' framework to verify the correctness
and robustness of statistical functions such as count, sum, mean, min, max,
harmonic mean, variance, and standard deviation against predefined datasets
and expected outputs.
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

class TestComputeStats(unittest.TestCase):
    """
    Test suite for the statistical computation functions within py_stats_toolkit.

    This class defines a series of unit tests, each designed to verify the
    correct behavior of a specific statistical function. A consistent
    sample dataset is used across most tests for clear and predictable
    assertions.
    """

    # Define a consistent dataset to be used across multiple test methods.
    # Using floats to ensure compatibility with functions that might return floats.
    sample_data = [10.0, 20.0, 30.0, 40.0, 50.0]

    def test_101_calculate_count(self):
        """
        Verifies that 'calculate_count' correctly returns the number of elements
        in a list, comparing it to the standard 'len()' function.
        """
        self.assertEqual(calculate_count(self.sample_data), len(self.sample_data))

    def test_102_calculate_sum(self):
        """
        Ensures 'calculate_sum' accurately computes the total sum of all elements
        in the sample data.
        """
        self.assertEqual(calculate_sum(self.sample_data), 150)

    def test_103_calculate_mean(self):
        """
        Checks if 'calculate_mean' correctly calculates the arithmetic average
        for the given sample dataset.
        """
        self.assertEqual(calculate_mean(self.sample_data), 30)

    def test_104_calculate_min(self):
        """
        Tests 'calculate_min' to confirm it correctly identifies the minimum
        value within the sample data list.
        """
        self.assertEqual(calculate_min(self.sample_data), 10)

    def test_105_calculate_max(self):
        """
        Verifies 'calculate_max' accurately finds the maximum value within
        the sample data list.
        """
        self.assertEqual(calculate_max(self.sample_data), 50)

    def test_106_calculate_harmonic_mean(self):
        """
        Asserts that 'calculate_harmonic_mean' computes the harmonic mean
        with a specified precision, ensuring accuracy for this complex calculation.
        """
        # Using assertAlmostEqual for floating-point comparisons due to precision
        self.assertAlmostEqual(calculate_harmonic_mean(self.sample_data), 21.90, places=2)

    def test_107_calculate_variance(self):
        """
        Confirms 'calculate_variance' correctly calculates the variance
        of the sample data, asserting with a tolerance for floating-point results.
        """
        self.assertAlmostEqual(calculate_variance(self.sample_data), 200.00, places=2)

    def test_108_calculate_std_dev(self):
        """
        Checks 'calculate_std_dev' for accurate computation of the standard
        deviation from the sample data, using assertAlmostEqual for precision.
        """
        self.assertAlmostEqual(calculate_std_dev(self.sample_data), 14.14, places=2)

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
    