from math import sqrt
import problems.reverse_num as reverse
from random import randint
import unittest


class TestReverse(unittest.TestCase):
    def setUp(self):
        self.reverse = reverse.Solution()

    def test_zero(self):
        self.assertEqual(self.reverse.reverse(0), 0, msg=f"{0}")

    def test_num(self):
        nums = (
            1,
            123456789,
            100000,
            randint(999_999_999, 999_999_999),
        )
        for num in nums:
            self.assertEqual(
                self.reverse.reverse(num),
                int(str(num)[::-1]),
                msg=f"{num}",
            )

    def test_negative_num(self):
        nums = (
            -1,
            -123456789,
            -100000,
            -randint(999_999_999, 999_999_999),
        )
        for num in nums:
            self.assertEqual(
                self.reverse.reverse(num),
                int(str(num * -1)[::-1]) * -1,
                msg=f"{num}",
            )

    def test_num(self):
        nums = (
            2147483648,
            -2147483648,
        )
        for num in nums:
            self.assertEqual(
                self.reverse.reverse(num),
                0,
                msg=f"{num}",
            )


if __name__ == "__main__":
    unittest.main()
