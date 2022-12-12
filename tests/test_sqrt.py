from math import sqrt
import sqrt as rsqrt
from random import randint
import unittest


class TestSqrt(unittest.TestCase):
    def setUp(self):
        self.sqrt = rsqrt.Solution()

    def test_zero(self):
        self.assertEqual(self.sqrt.mySqrt(0), 0)

    def test_right_sqrt(self):
        nums = (1, 4, 8, 65)
        for num in nums:
            self.assertEqual(self.sqrt.mySqrt(num), int(sqrt(num)))

    def test_bad_sqrt(self):
        nums = (1, 4, 8, 65)
        for num in nums:
            self.assertNotEqual(self.sqrt.mySqrt(num), int(sqrt(num) + 1))

    def test_randome(self):
        test = 10
        for _ in range(test):
            num = randint(0, 999_999)
            self.assertEqual(self.sqrt.mySqrt(num), int(sqrt(num)))

    def test_negative_sqrt(self):
        # Exception test
        with self.assertRaises(Exception) as context:
            self.sqrt.mySqrt(-1)
        self.assertTrue("Negative number" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
