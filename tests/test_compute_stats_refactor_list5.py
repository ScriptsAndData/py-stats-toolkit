import unittest
from compute_stats_refactor.compute_stats_refactor import *

class TestComputeStats(unittest.TestCase):
    """
    Test suite for the statistical computation functions.
    """

    sample_data = [10.0, 20.0, 30.0, 40.0, 50.0]

    def test_101_count(self):
        self.assertEqual(count(self.sample_data), len(self.sample_data))

    def test_102_summation(self):
        self.assertEqual(summation(self.sample_data), 150)

    def test_103_average(self):
        self.assertEqual(average(self.sample_data), 30)

    def test_104_minimum(self):
        self.assertEqual(minimum(self.sample_data), 10)

    def test_105_maximum(self):
        self.assertEqual(maximum(self.sample_data), 50)

    def test_106_harmonic_mean(self):
        self.assertAlmostEqual(harmonic_mean(self.sample_data), 21.90, places=2)

    def test_107_variance(self):
        self.assertAlmostEqual(variance(self.sample_data), 200.00, places=2)

    def test_108_standard_dev(self):
        self.assertAlmostEqual(standard_dev(self.sample_data), 14.14, places=2)

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
