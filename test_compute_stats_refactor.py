import unittest
from compute_stats_refactor import *

class TestComputeStats(unittest.TestCase):

    def test_01_read_ints(self):
        self.assertEqual(len(read_ints()), 1000)

    def test_02_count(self):
        self.assertEqual(count(), 1000)

    def test_03_summation(self):
        self.assertEqual(summation(), 499498)

    def test_04_average(self):
        self.assertEqual(average(), 499.498)

    def test_05_minimum(self):
        self.assertEqual(minimum(), 1)

    def test_06_maximum(self):
        self.assertEqual(maximum(), 997)

    def test_07_harmonic_mean(self):
        self.assertAlmostEqual(harmonic_mean(), 129.728, places=3)

    def test_08_variance(self):
        self.assertAlmostEqual(variance(),81476.49, places=2)

    def test_09_standard_dev(self):
        self.assertAlmostEqual(standard_dev(),285.44, places=2)

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
