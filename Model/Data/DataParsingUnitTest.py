import unittest
from Model.Data import DataParsing


class MyTestCase(unittest.TestCase):
    def test_enPoissant(self):
        prev = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['p', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', 'P', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        curr = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['p', 'P', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        curr[3][1] = "p"
        prev[3][1] = "p"
        self.assertEqual(False, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        curr[3][1] = "N"
        prev[3][1] = "N'"
        self.assertEqual(False, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        prev = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', 'p'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', 'P', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        curr = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', 'P', 'p'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        curr[3][6] = "p"
        prev[3][6] = "p"
        self.assertEqual(False, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        curr[3][6] = "N"
        prev[3][6] = "N"
        self.assertEqual(False, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        prev = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'p', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        curr = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'p', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        curr[4][2] = "P"
        prev[4][2] = "P"
        self.assertEqual(False, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        curr[4][2] = "n"
        prev[4][2] = "n"
        self.assertEqual(False, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))
        prev = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'p', '.', '.', '.', '.', '.'],
                ['.', '.', 'p', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        curr = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'p', '.', '.', '.', '.', '.'],
                ['.', '.', 'p', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, DataParsing.checkIfEnPoissantAllowedStr(curr, prev))


if __name__ == '__main__':
    unittest.main()
