# import sys
# !{sys.executable} -m pip install chess
# !{sys.executable} -m pip install pgn-parser
# !{sys.executable} -m pip install --upgrade pip
# !{sys.executable} -m pip install tensorflow

import chess
import pgn_parser
from pgn_parser import parser, pgn
import numpy as np
import chess.pgn
import math
import re
from random import random
from datetime import datetime
from platform import python_version
import time
import copy

def getBoardNP(board):
    strBoard = str(board)
    strBoard = re.split('\s|\n',strBoard)
    #Parse board string into (2,6,8,8) dimensional matrix (color, pieceType, row, column)
    npBoard = np.array(strBoard).reshape((8,8))
    return npBoard


# Check if the current position allows for an enpoissant
def checkIfEnPoissantAllowed(currPos, prevPos):
    currWhitePawns = currPos[0][0]
    currBlackPawns = currPos[1][0]
    prevWhitePawns = prevPos[0][0]
    prevBlackPawns = prevPos[1][0]

    if (checkIfEnPoissantHelper(currWhitePawns, prevWhitePawns, currBlackPawns, True)):
        return True
    if (checkIfEnPoissantHelper(currBlackPawns, prevBlackPawns, currWhitePawns, False)):
        return True
    return False


def checkIfEnPoissantHelper(myPawns, myPrevPawns, oppPawns, isWhite):
    startRow = 1
    advancedRow = 3
    if isWhite:
        startRow = 6
        advancedRow = 4
    for i in range(0, 8):
        if (myPawns[advancedRow][i] and myPrevPawns[startRow][i]):
            if (i > 0 and oppPawns[advancedRow][i - 1]) or (i < 7 and oppPawns[advancedRow][i + 1]):
                return True
    return False


# Check if the previous move was a capture
def checkIfCaptureMove(currBoard, prevBoard):
    for i in range(0, 8):
        for j in range(0, 8):
            isPrevBlack = False
            isPrevWhite = False
            isCurrBlack = False
            isCurrWhite = False
            for k in range(0, 6):
                if (currBoard[0][k][i][j] == 1):
                    isCurrWhite = True
                elif (currBoard[1][k][i][j] == 1):
                    isCurrBlack = True
                if (prevBoard[0][k][i][j] == 1):
                    isPrevWhite = True
                elif (prevBoard[1][k][i][j] == 1):
                    isPrevBlack = True
                if ((isCurrBlack and isPrevWhite) or (isCurrWhite and isPrevBlack)):
                    return True
    return False


def checkIfEnPoissantAllowedStrHelper(currPos, prevPos, startIndex, endIndex, piece, capturingPiece):
    for i in range(0, 8):
        if prevPos[startIndex][i] == piece and prevPos[endIndex][i] == '.' and currPos[startIndex][i] == '.' and \
                currPos[endIndex][i] == piece:
            if i > 0 and currPos[endIndex][i - 1] == capturingPiece:
                return True
            if i < 7 and currPos[endIndex][i + 1] == capturingPiece:
                return True
    return False


def checkIfEnPoissantAllowedStr(boardNp, prevBoardNP):
    if checkIfEnPoissantAllowedStrHelper(boardNp, prevBoardNP, 6, 4, 'P', 'p') or checkIfEnPoissantAllowedStrHelper(
            boardNp, prevBoardNP, 1, 3, 'p', 'P'):
        return True
    return False


def checkIfCaptureMoveStr(currPos, prevPos):
    for i in range(0, 8):
        for j in range(0, 8):
            currVal = currPos[i][j]
            prevVal = prevPos[i][j]
            if currVal != '.' and prevVal != '.' and (
                    (currVal.isupper() and prevVal.islower()) or (currVal.islower() and prevVal.isupper())):
                return True
    return False


def getBoardInit():
    return np.zeros((2, 6, 8, 8))


def convertBoolToNum(flag):
    if flag == True:
        return 1
    return 0


def convertBoardToMatrix(board):
    npBoard = getBoardNP(board)
    # Initialize an empty board
    newBoard = getBoardInit()
    for i in range(0, 8):
        for j in range(0, 8):
            b = npBoard[i][j]
            if b == '.':
                continue
            if b.isupper():
                color = 0
            else:
                color = 1
            piece = 0
            lower = b.lower()
            if lower == 'p':
                piece = 0
            elif lower == 'r':
                piece = 1
            elif lower == 'n':
                piece = 2
            elif lower == 'b':
                piece = 3
            elif lower == 'q':
                piece = 4
            elif lower == 'k':
                piece = 5
            newBoard[color][piece][i][j] = 1
    return newBoard


interval = 1000
skipFirst = 0

skipInitialMoves = 10
from inspect import getmembers, isfunction

with open("CCRL-4040.[1239176].pgn") as pgn:
    boardStates = []
    boardStatesStr = []
    boardStateBools = []
    winStates = np.array([])
    gameCount = -1
    lastIndex = 0
    sumTime = 0
    while True:
        first_game = chess.pgn.read_game(pgn)
        gameCount = gameCount + 1
        if int(gameCount % interval) == 0:
            print("reached " + str(gameCount))
        if gameCount < skipFirst:
            continue;
        if int(gameCount % interval) == 0 and gameCount > skipFirst:
            print(gameCount)
            np.savez("resultStr/results" + str(gameCount) + ".npz", results=winStates)
            np.savez("boardStr/boardStates" + str(gameCount) + ".npz", states=boardStatesStr)
            np.savez("boardStateBools/boardStatesBools" + str(gameCount) + ".npz", states=boardStateBools)
            winStates = []
            boardStatesStr = []
            boardStateBools = []
        if first_game == None:
            if int(gameCount % interval) != 0:
                np.savez("boardStr/boardStates" + str(gameCount) + ".npz", states=boardStatesStr)
                np.savez("resultStr/results" + str(gameCount) + ".npz", results=winStates)
                np.savez("boardStateBools/boardStatesBools" + str(gameCount) + ".npz", states=boardStateBools)
                winStates = []
                boardStatesStr = []
                boardStateBools = []
            break
        board = first_game.board()
        result = first_game.headers["Result"]
        # Skip draws
        if (result == '1/2-1/2'):
            continue
        # print(result)
        whiteMove = True
        bQCastle = True
        bKCastle = True
        wQCastle = True
        wKCastle = True
        mvCount = 0
        for move in first_game.mainline_moves():
            mvCount = mvCount + 1
            strMove = str(move)
            # Check if castling is enabled for white/black
            if whiteMove:
                if strMove.startswith('e1') or strMove.startswith("O-O") or strMove.startswith("0-0"):
                    wQCastle = False
                    wKCastle = False
            else:
                if strMove.startswith('e8') or strMove.startswith("O-O") or strMove.startswith("0-0"):
                    bQCastle = False
                    bKCastle = False

            if "a1" in strMove:
                wQCastle = False
            elif "h1" in strMove:
                wKCastle = False
            elif "a8" in strMove:
                bQCastle = False
            elif "h8" in strMove:
                bKCastle = False
            prevBoard = copy.deepcopy(board)
            board.push(move)
            if whiteMove == True:
                whiteMove = False
            else:
                whiteMove = True
            # skip opening moves of the game and
            if random() > 0.15 or mvCount <= skipInitialMoves or strMove == "1-0" or strMove == "0-1" or strMove == "1/2-1/2":
                continue
            now = time.time()
            currBoardNP = getBoardNP(board)
            prevBoardNP = getBoardNP(prevBoard)
            enPoissEnabled = checkIfEnPoissantAllowedStr(currBoardNP, prevBoardNP)
            isCaptureMove = checkIfCaptureMoveStr(currBoardNP, prevBoardNP)
            # Skip enpoissant moves and capture moves
            if enPoissEnabled or isCaptureMove:
                continue

            if result == "0-1":
                winStates = np.append(winStates, 0)
            elif result == "1-0":
                winStates = np.append(winStates, 1)
            else:
                winStates = np.append(winStates, 0.5)
            boardStatesStr.append(currBoardNP)
            boardStateBools.append([convertBoolToNum(wKCastle), convertBoolToNum(wQCastle), convertBoolToNum(bKCastle),
                                    convertBoolToNum(bQCastle), convertBoolToNum(whiteMove)])






