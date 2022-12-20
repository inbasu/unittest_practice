import problems.remove_duplicates as remove_duplicates
from random import randint
import unittest


class TestRemoveDiplicates(unittest.TestCase):
    def setUp(self):
        self.remove_duplicates = remove_duplicates.Solution()

    def test_random(self):
        for l in range(1, 100):
            test_list = sorted([randint(1, 10) for _ in range(l)])
            self.remove_duplicates.nums = []
            idx = self.remove_duplicates.removeDuplicates(test_list)
            self.assertEqual(
                self.remove_duplicates.nums[:idx], self.greed(test_list), msg=test_list
            )

    def greed(self, lst) -> list:
        return sorted((list(set(lst))))


if __name__ == "__main__":
    unittest.main()
