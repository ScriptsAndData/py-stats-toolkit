import unittest
from compute_stats_refactor.compute_stats_refactor import *

class TestComputeStats(unittest.TestCase):
    """
    Test suite for the statistical computation functions.
    """

    """Testing blank list []"""
    sample_data = []

    def test_201_count(self):
        self.assertEqual(count(self.sample_data), 0)

    def test_202_summation(self):
        self.assertEqual(summation(self.sample_data), 0)

    def test_203_average(self):
        with self.assertRaises(ValueError) as cm:
            average(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate average of an empty list")

    def test_204_minimum(self):
        with self.assertRaises(ValueError) as cm:
            minimum(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot find minimum value of an empty list")

    def test_205_maximum(self):
        with self.assertRaises(ValueError) as cm:
            maximum(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot find maximum value of an empty list")

    def test_206_harmonic_mean(self):
        with self.assertRaises(ValueError) as cm:
            harmonic_mean(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate harmonic mean of an empty list")

    def test_207_variance(self):
        with self.assertRaises(ValueError) as cm:
            variance(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate variance of an empty list")

    def test_208_standard_dev(self):
        with self.assertRaises(ValueError) as cm:
            standard_dev(self.sample_data)
        self.assertEqual(str(cm.exception), "Cannot calculate standard deviation of an empty list")

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
