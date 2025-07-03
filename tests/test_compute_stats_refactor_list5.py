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

    sample_data = [10.0, 20.0, 30.0, 40.0, 50.0]

    def test_101_calculate_count(self):
        self.assertEqual(calculate_count(self.sample_data), len(self.sample_data))

    def test_102_calculate_sum(self):
        self.assertEqual(calculate_sum(self.sample_data), 150)

    def test_103_calculate_mean(self):
        self.assertEqual(calculate_mean(self.sample_data), 30)

    def test_104_calculate_min(self):
        self.assertEqual(calculate_min(self.sample_data), 10)

    def test_105_calculate_max(self):
        self.assertEqual(calculate_max(self.sample_data), 50)

    def test_106_calculate_harmonic_mean(self):
        self.assertAlmostEqual(calculate_harmonic_mean(self.sample_data), 21.90, places=2)

    def test_107_calculate_variance(self):
        self.assertAlmostEqual(calculate_variance(self.sample_data), 200.00, places=2)

    def test_108_calculate_std_dev(self):
        self.assertAlmostEqual(calculate_std_dev(self.sample_data), 14.14, places=2)

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
