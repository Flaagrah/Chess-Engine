import unittest
import Utils.NextMoves
import chess
import time
import timeit
import numpy as np
class MyTestCase(unittest.TestCase):
    def test_board(self):
        board = chess.Board()
        m1 = chess.Move.from_uci('e2e4')
        m2 = chess.Move.from_uci('e7e5')
        m3 = chess.Move.from_uci('d1f3')
        m4 = chess.Move.from_uci('a7a6')
        m5 = chess.Move.from_uci('f1c4')
        m6 = chess.Move.from_uci('a6a5')
        m7 = chess.Move.from_uci('f3f7')
        board.push(m1)
        board.push(m2)
        board.push(m3)
        board.push(m4)
        board.push(m5)
        board.push(m6)
        self.assertEqual(1.0, Utils.NextMoves.convertFenToBoard(board.fen())[-1])
        board.push(m7)
        result = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0,
         0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0,
         1.0, 1.0, 0.0]

        self.assertEqual(result, Utils.NextMoves.convertFenToBoard(board.fen()))

    def test_board_castle(self):
        boardObj = chess.Board()
        boardObj.set_fen('rnbq1rk1/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 w KQkq')
        board = Utils.NextMoves.convertFenToBoard(boardObj.fen())
        self.assertEqual(0, board[-2])
        self.assertEqual(0, board[-3])
        self.assertEqual(0, board[-4])
        self.assertEqual(0, board[-5])

        boardObj.set_fen('rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 b kq')
        board = Utils.NextMoves.convertFenToBoard(boardObj.fen())
        self.assertEqual(1, board[-2])
        self.assertEqual(1, board[-3])
        self.assertEqual(0, board[-4])
        self.assertEqual(0, board[-5])

        boardObj.set_fen('rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQKR2 b Qkq')
        board = Utils.NextMoves.convertFenToBoard(boardObj.fen())
        self.assertEqual(1, board[-2])
        self.assertEqual(1, board[-3])
        self.assertEqual(1, board[-4])
        self.assertEqual(0, board[-5])

        boardObj.set_fen('rnbqkr2/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQKR2 w Qq')
        board = Utils.NextMoves.convertFenToBoard(boardObj.fen())
        self.assertEqual(1, board[-2])
        self.assertEqual(0, board[-3])
        self.assertEqual(1, board[-4])
        self.assertEqual(0, board[-5])

        boardObj.set_fen('rnbqkr2/pppp1ppp/5n2/2b1p3/2B1P3/P4N2/RPPP1PPP/1NBQKR2 b q')
        board = Utils.NextMoves.convertFenToBoard(boardObj.fen())
        self.assertEqual(1, board[-2])
        self.assertEqual(0, board[-3])
        self.assertEqual(0, board[-4])
        self.assertEqual(0, board[-5])

        boardObj.set_fen('1nbqkr2/rppp1ppp/p4n2/2b1p3/2B1P3/P4N2/RPPP1PPP/1NBQKR2 w q')
        board = Utils.NextMoves.convertFenToBoard(boardObj.fen())
        self.assertEqual(0, board[-2])
        self.assertEqual(0, board[-3])
        self.assertEqual(0, board[-4])
        self.assertEqual(0, board[-5])

    def test_getAllNextPositions(self):
        board = chess.Board()
        t = time.time()
        positions = Utils.NextMoves.getAllNextPositions(board, True)
        self.assertEqual(20, len(positions))
        board = positions[0]
        positions = Utils.NextMoves.getAllNextPositions(board, True)
        self.assertEqual(20, len(positions))

        board = chess.Board()
        m1 = chess.Move.from_uci('e2e4')
        board.push(m1)
        m2 = chess.Move.from_uci('d7d5')
        board.push(m2)
        positions = Utils.NextMoves.getAllNextPositions(board, True)
        positionsWC = Utils.NextMoves.getAllNextPositions(board, False)
        self.assertEqual(1, len(positions)-len(positionsWC))

    def test_compare(self):
        board1 = chess.Board()
        board2 = chess.Board()
        board1.set_fen('4k3/8/8/KQ6/8/8/8/8 w')
        board2.set_fen('4K3/8/8/kq6/8/8/8/8 w')
        result = Utils.NextMoves.compare(board1, board2)
        self.assertGreater(result[0], result[1])
        result = Utils.NextMoves.compare(board2, board1)
        self.assertGreater(result[1], result[0])

        board1.set_fen('4k3/4Q3/4K3/8/8/8/8/8 b')
        board2.set_fen('4k3/8/8/KQ6/8/8/8/8 b')
        result = Utils.NextMoves.compare(board1, board2)
        self.assertEqual(result[0], 1.0)
        result = Utils.NextMoves.compare(board2, board1)
        self.assertEqual(result[0], 0.0)

        board1.set_fen('k7/2Q5/4K3/8/8/8/8/8 b')
        board2.set_fen('K7/2q5/4k3/8/8/8/8/8 w')
        result = Utils.NextMoves.compare(board1, board2)
        self.assertEqual(result[0], 0.5)
        board1.set_fen('k7/2Q5/4K3/8/8/8/8/8 b')
        board2.set_fen('k7/3Q4/4K3/8/8/8/8/8 b')
        result = Utils.NextMoves.compare(board1, board2)
        self.assertLess(result[0], result[1])

    def test_capture_move(self):
        board = chess.Board()
        board2 = chess.Board()
        m1 = chess.Move.from_uci('e2e4')
        board2.push(m1)
        self.assertEqual(False, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('rnbqk2r/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 b kq')
        board2.set_fen('rnbq1rk1/pppp1ppp/5n2/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQ1RK1 w')
        self.assertEqual(False, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/pk6/8/RK6/8/8 w')
        board2.set_fen('8/8/8/Rk6/8/1K6/8/8 w')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/qk6/8/RK6/8/8 w')
        board2.set_fen('8/8/8/Rk6/8/1K6/8/8 w')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/rk6/8/RK6/8/8 w')
        board2.set_fen('8/8/8/Rk6/8/1K6/8/8 w')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/nk6/8/RK6/8/8 w')
        board2.set_fen('8/8/8/Rk6/8/1K6/8/8 w')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/bk6/8/RK6/8/8 w')
        board2.set_fen('8/8/8/Rk6/8/1K6/8/8 w')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/PK6/8/rk6/8/8 b')
        board2.set_fen('8/8/8/rK6/8/1k6/8/8 b')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/QK6/8/rk6/8/8 b')
        board2.set_fen('8/8/8/rK6/8/1k6/8/8 b')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/RK6/8/rk6/8/8 b')
        board2.set_fen('8/8/8/rK6/8/1k6/8/8 b')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/NK6/8/rk6/8/8 b')
        board2.set_fen('8/8/8/rK6/8/1k6/8/8 b')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))

        board.set_fen('8/8/8/BK6/8/rk6/8/8 b')
        board2.set_fen('8/8/8/rK6/8/1k6/8/8 b')
        self.assertEqual(True, Utils.NextMoves.isCaptureMove(board2, board))


    def test_get_next_move(self):
        board = chess.Board()
        board.set_fen('k7/8/1K6/1R6/8/8/8/8 w')
        nextPosition = Utils.NextMoves.getNextMove(board, 2)
        nextPosition2 = Utils.NextMoves.getNextMove(nextPosition, 2)
        nextPosition3 = Utils.NextMoves.getNextMove(nextPosition2, 2)
        print(str(nextPosition3))
        self.assertEqual(True, nextPosition3.is_checkmate())

        board.set_fen('K7/8/1k6/1r6/8/8/8/8 b')
        nextPosition = Utils.NextMoves.getNextMove(board, 2)
        nextPosition2 = Utils.NextMoves.getNextMove(nextPosition, 2)
        nextPosition3 = Utils.NextMoves.getNextMove(nextPosition2, 2)
        print(str(nextPosition3))
        self.assertEqual(True, nextPosition3.is_checkmate())

        t = time.time()
        board = chess.Board("2r2rk1/pp1n1pp1/1q3b1p/2pp2PP/2P5/Q4N2/PP1B1P2/1K1R3R b - - 0 20 ")
        print(board)
        nextPosition = Utils.NextMoves.getNextMove(board, 3)
        print(nextPosition)
        print(time.time()-t)


if __name__ == '__main__':
    unittest.main()
