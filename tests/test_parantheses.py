from .logger import *
import problems.parentheses as parentheses
import unittest


class TestParantheses(unittest.TestCase):
    def setUp(self):
        self.paren = parentheses.Solution()

    def test_right(self):
        patterns = (
            "",
            "()",
            "{}",
            "[]",
            "((({[]})))",
            "[sometext]",
            "sometext",
        )
        for pattern in patterns:
            self.assertTrue(self.paren.isValid(pattern))

    def test_bad(self):
        patterns = (
            "]",
            "[",
            "(]",
            "{(})",
            "][",
            "[some(text]",
        )
        for pattern in patterns:
            self.assertFalse(self.paren.isValid(pattern))


if __name__ == "__main__":
    unittest.main()
