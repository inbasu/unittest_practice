import problems.merge_sorted_arr as merge
import unittest


class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.merge = merge.Solution()

    def test_merge(self):
        tests = [
            [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]],
            [[1], 1, [], 0, [1]],
            [[0], 0, [1], 1, [1]],
        ]

        for test in tests:
            self.merge.merge(nums1=test[0], m=test[1], nums2=test[2], n=test[3])
            self.assertEqual(
                self.merge.nums1,
                test[4],
                msg=f"{test}",
            )


if __name__ == "__main__":
    unittest.main()
