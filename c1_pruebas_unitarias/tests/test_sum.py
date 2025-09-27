import unittest

from sum import sum_numbers


class TestSumNumbers(unittest.TestCase):
    def test_sum_positive(self):
        self.assertEqual(sum_numbers(1, 2), 3)

    def test_sum_zero(self):
        self.assertEqual(sum_numbers(0, 0), 0)

    def test_sum_negative_and_positive(self):
        self.assertEqual(sum_numbers(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
