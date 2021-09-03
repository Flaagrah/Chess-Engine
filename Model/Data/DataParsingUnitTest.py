import unittest
from Model.Data import DataParsing
import numpy as np

def checkIfInit(board):
    init = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

    numDiff = 0
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] != init[i][j]:
                numDiff = numDiff + 1
                if numDiff>2:
                    return -1
    return numDiff

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

    def test_capture(self):
        prev = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', 'p', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'b', '.', 'R', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        curr = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', 'p', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'R', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, DataParsing.checkIfCaptureMoveStr(curr, prev))
        prev = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', 'p', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'b', '.', 'R', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        curr = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', 'p', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'b', 'R', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(False, DataParsing.checkIfCaptureMoveStr(curr, prev))
        prev = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', 'p', 'P', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        curr = [['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', 'p', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(True, DataParsing.checkIfCaptureMoveStr(curr, prev))

    def test_process(self):
        strBuff = "Test"
        #DataParsing.process(1001, 1.0, strBuff)
        results = np.load("resultStr/results" + strBuff + str(1000) + ".npz")["results"]
        boardStates = np.load("boardStr/boardStates" + strBuff + str(1000) + ".npz")["states"]
        boardStateBools = np.load("boardStateBools/boardStatesBools" + strBuff + str(1000) + ".npz")["states"]
        whiteQ = 1
        blackQ = 1
        whiteK = 1
        blackK = 1
        whiteTurn = 1

        for i in range(1, 5000):
            currBoard = boardStates[i]
            currBools = boardStateBools[i]
            checkNum = checkIfInit(currBoard)
            #print(currBoard)
            # print(currBools)
            #print(checkNum)
            if checkNum != -1:
                whiteQ = 1
                blackQ = 1
                whiteK = 1
                blackK = 1
                if (checkNum == 2):
                    whiteTurn = 0
                elif checkNum == 0:
                    whiteTurn = 1

            if (currBoard[0][4]!='k'):
                blackQ = 0
                blackK = 0

            if (currBoard[7][4]!='K'):
                whiteQ = 0
                whiteK = 0

            if (currBoard[0][0]!='r'):
                blackQ = 0

            if (currBoard[0][7]!='r'):
                blackK = 0

            if (currBoard[7][0]!='R'):
                whiteQ = 0

            if (currBoard[7][7]!='R'):
                whiteK = 0

            self.assertEqual(whiteK, currBools[0])
            self.assertEqual(whiteQ, currBools[1])
            self.assertEqual(blackK, currBools[2])
            self.assertEqual(blackQ, currBools[3])
            self.assertEqual(whiteTurn, currBools[4])
            if whiteTurn == 1:
                whiteTurn = 0
            else:
                whiteTurn = 1

if __name__ == '__main__':
    unittest.main()
