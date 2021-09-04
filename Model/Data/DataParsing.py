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
    numPrev = 0
    numCurr = 0
    for i in range(0, 8):
        for j in range(0, 8):
            currVal = currPos[i][j]
            prevVal = prevPos[i][j]
            if (currVal != '.'):
                numCurr = numCurr + 1
            if (prevVal != '.'):
                numPrev = numPrev + 1

            if currVal != '.' and prevVal != '.' and (
                    (currVal.isupper() and prevVal.islower()) or (currVal.islower() and prevVal.isupper())):
                return True
    if numPrev != numCurr:
        return True
    return False


def getBoardInit():
    return np.zeros((2, 6, 8, 8))


def convertBoolToNum(flag):
    if flag == True:
        return 1
    return 0

interval = 1000
skipFirst = 0

skipInitialMoves = 10
from inspect import getmembers, isfunction

def process(num, randomNum, strBuff):
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
            print("---")
            gameCount = gameCount + 1
            if (gameCount == num):
                break
            if int(gameCount % interval) == 0:
                print("reached " + str(gameCount))
            if gameCount < skipFirst:
                continue
            if int(gameCount % interval) == 0 and gameCount > skipFirst:
                print(gameCount)
                np.savez("resultStr/results" + strBuff + str(gameCount) + ".npz", results=winStates)
                np.savez("boardStr/boardStates" + strBuff + str(gameCount) + ".npz", states=boardStatesStr)
                np.savez("boardStateBools/boardStatesBools" + strBuff + str(gameCount) + ".npz", states=boardStateBools)
                winStates = []
                boardStatesStr = []
                boardStateBools = []
            if first_game == None:
                if int(gameCount % interval) != 0:
                    np.savez("boardStr/boardStates" + strBuff + str(gameCount) + ".npz", states=boardStatesStr)
                    np.savez("resultStr/results" + strBuff + str(gameCount) + ".npz", results=winStates)
                    np.savez("boardStateBools/boardStatesBools" + strBuff + str(gameCount) + ".npz", states=boardStateBools)
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
                if random() > randomNum or (mvCount <= skipInitialMoves and randomNum<1.0) or strMove == "1-0" or strMove == "0-1" or strMove == "1/2-1/2":
                    continue
                now = time.time()
                currBoardNP = getBoardNP(board)
                prevBoardNP = getBoardNP(prevBoard)
                enPoissEnabled = checkIfEnPoissantAllowedStr(currBoardNP, prevBoardNP)
                isCaptureMove = checkIfCaptureMoveStr(currBoardNP, prevBoardNP)
                # Skip enpoissant moves and capture moves
                if (enPoissEnabled or isCaptureMove) and randomNum<1.0:
                    continue

                if result == "0-1":
                    winStates = np.append(winStates, 0)
                elif result == "1-0":
                    winStates = np.append(winStates, 1)
                else:
                    winStates = np.append(winStates, 0.5)

                boardStatesStr.append(currBoardNP)
                print(whiteMove)
                boardStateBools.append([convertBoolToNum(wKCastle), convertBoolToNum(wQCastle), convertBoolToNum(bKCastle),
                                        convertBoolToNum(bQCastle), convertBoolToNum(whiteMove)])



if __name__ == '__main__':
    process(-1, 0.15, "")




