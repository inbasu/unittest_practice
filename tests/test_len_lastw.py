import problems.len_lastw as len_lastw
from random import randint
import unittest


class TestlengthOfLastWord(unittest.TestCase):
    def setUp(self):
        self.len_last = len_lastw.Solution()
        self.frases = ("hello world!", "hello world  ", "hello world")

    def test_zero(self):
        self.assertFalse(self.len_last.lengthOfLastWord(""), True)
        self.assertFalse(self.len_last.lengthOfLastWord(" "), True)

    def test_test_len_last_good(self):
        for frase in self.frases:
            self.assertEqual(
                self.len_last.lengthOfLastWord(frase),
                5,
                msg=f"{frase},",
            )

    def test_len_last_bad(self):
        for frase in self.frases:
            self.assertNotEqual(
                self.len_last.lengthOfLastWord(frase),
                randint(6, 15),
                msg=f"{frase}",
            )


if __name__ == "__main__":
    unittest.main()
