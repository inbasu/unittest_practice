import pali_num
from random import randint
import unittest


class TestPalindrom(unittest.TestCase):
    def setUp(self):
        self.pali = pali_num.Solution()

    def test_zero(self):
        self.assertEqual(self.pali.isPalindrome(0), True)

    def test_negative_nums(self):
        nums = (-1, -121, -113)
        for num in nums:
            self.assertFalse(self.pali.isPalindrome(num))

    def test_palinom_nums(self):
        nums = (123321, 1, 11, 121)
        for num in nums:
            self.assertTrue(self.pali.isPalindrome(num))

    def test_non_palinom_nums(self):
        nums = (13, 12345321, 10)
        for num in nums:
            self.assertFalse(self.pali.isPalindrome(num))

    def test_randome(self):

        test = 10
        for _ in range(test):
            num = randint(-999_999, 999_999)
            self.assertEqual(self.pali.isPalindrome(num), self.is_poli(num))

    def is_poli(self, num: int) -> True:
        num = str(num)
        return num[::-1] == num


if __name__ == "__main__":
    unittest.main()
