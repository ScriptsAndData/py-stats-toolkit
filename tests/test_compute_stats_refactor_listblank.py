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
    Test suite for the statistical computation functions.
    """

    """Testing blank list []"""
    sample_data = []

    def test_201_calculate_count(self):
        self.assertEqual(calculate_count(self.sample_data), 0)

    def test_202_calculate_sum(self):
        self.assertEqual(calculate_sum(self.sample_data), 0)

    def test_203_calculate_mean(self):
        with self.assertRaises(ValueError) as cm:
            calculate_mean(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate average of an empty list")

    def test_204_calculate_min(self):
        with self.assertRaises(ValueError) as cm:
            calculate_min(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot find minimum value of an empty list")

    def test_205_calculate_max(self):
        with self.assertRaises(ValueError) as cm:
            calculate_max(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot find maximum value of an empty list")

    def test_206_calculate_harmonic_mean(self):
        with self.assertRaises(ValueError) as cm:
            calculate_harmonic_mean(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate harmonic mean of an empty list")

    def test_207_calculate_variance(self):
        with self.assertRaises(ValueError) as cm:
            calculate_variance(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate variance of an empty list")

    def test_208_calculate_std_dev(self):
        with self.assertRaises(ValueError) as cm:
            calculate_std_dev(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate standard deviation of an empty list")

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
