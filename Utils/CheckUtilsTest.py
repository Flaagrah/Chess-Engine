import unittest
import CheckUtils

class MyTestCase(unittest.TestCase):
    def test_whiteKingCheck(self):
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', 'r', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', 'r', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', 'b', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', 'R', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', 'q', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', 'n', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'n', '.', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'b', '.', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', 'R', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'b', '.', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', 'R', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', 'b', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', 'r', '.', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', 'b', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'k', '.', '.', '.'],
                    ['.', '.', 'r', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, True))
        self.assertEqual(True, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', 'p', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'p', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'p', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, True))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', 'p', 'p', 'p', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, True))

        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'k', '.', '.', '.', '.'],
                    ['.', '.', 'P', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'k', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'P', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'k', '.', '.', '.', '.'],
                    ['.', '.', '.', 'P', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', 'P', 'P', 'P', '.', '.', '.'],
                    ['.', '.', '.', 'k', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'b', '.', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', 'R', 'b', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', 'b', '.', '.', '.'],
                    ['.', 'r', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'K', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', 'R', 'B', 'k', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, False))
        position = [['.', '.', '.', 'Q', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', 'R', '.', 'r', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', 'k', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, CheckUtils.isKingChecked(position, False))

if __name__ == '__main__':
    unittest.main()
