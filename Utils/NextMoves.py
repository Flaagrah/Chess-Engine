# import CheckUtils
# from copy import deepcopy
# import chess
# import re
# import numpy as np
# import time
#
# def addMoveIfLegal(position, row, col, newRow, newCol, upperCase, nonCaptureMoves, captureMoves):
#     if CheckUtils.isInRange(newRow) == False or CheckUtils.isInRange(newCol) == False:
#         return False
#
#     copy = deepcopy(position)
#     c = copy[newRow][newCol]
#     isSameCase = ((c.isupper() and upperCase == True) or (c.islower() and upperCase == False)) and c != '.'
#
#     if c != '.' and isSameCase:
#         return False
#     copy[newRow][newCol] = copy[row][col]
#     copy[row][col] = '.'
#     if CheckUtils.isKingChecked(copy, upperCase):
#         return False
#
#     # def checkForPromotion(mvList):
#     #     if (upperCase and newRow==0) or (upperCase == False and newRow==7):
#     #         copy1 = deepcopy(newPos)
#     #         copy2 = deepcopy(newPos)
#     #         copy3 = deepcopy(newPos)
#     #         copy4 = deepcopy(newPos)
#     #         newC1 = 'q'
#     #         newC2 = 'b'
#     #         newC3 = 'r'
#     #         newC4 = 'n'
#     #         if upperCase:
#     #             newC1 = 'Q'
#     #             newC2 = 'B'
#     #             newC3 = 'R'
#     #             newC4 = 'N'
#     #         if upperCase:
#     #             copy1[newRow][newCol] = newC1
#     #             copy2[newRow][newCol] = newC2
#     #             copy3[newRow][newCol] = newC3
#     #             copy4[newRow][newCol] = newC4
#     #         mvList.append(copy1)
#     #         mvList.append(copy2)
#     #         mvList.append(copy3)
#     #         mvList.append(copy4)
#
#     if c == '.':
#         nonCaptureMoves.append(copy)
#         return True
#     else:
#         captureMoves.append(copy)
#         return False
#
# def possibleLinearMoves(position, upperCase, row, col, rowInc, colInc, nonCaptureMoves, captureMoves):
#     currRow = row
#     currCol = col
#     while True:
#         currRow = currRow + rowInc
#         currCol = currCol + colInc
#         cont = addMoveIfLegal(position, row, col, currRow, currCol, upperCase, nonCaptureMoves, captureMoves)
#         if cont == False:
#             break
#
# def getRookMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
#     possibleLinearMoves(position, upperCase, row, col, 1, 0, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, -1, 0, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, 0, 1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, 0, -1, nonCaptureMoves, captureMoves)
#
# def getBishopMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
#     possibleLinearMoves(position, upperCase, row, col, 1, 1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, -1, -1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, -1, 1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, 1, -1, nonCaptureMoves, captureMoves)
#
# def getQueenMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
#     possibleLinearMoves(position, upperCase, row, col, 1, 1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, -1, -1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, -1, 1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, 1, -1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, 1, 0, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, -1, 0, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, 0, 1, nonCaptureMoves, captureMoves)
#     possibleLinearMoves(position, upperCase, row, col, 0, -1, nonCaptureMoves, captureMoves)
#
# def getKnightMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
#     addMoveIfLegal(position, row, col, row+1, col+2, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row+1, col-2, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row-1, col+2, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row-1, col-2, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row+2, col+1, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row+2, col-1, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row-2, col+1, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row-2, col-1, upperCase, nonCaptureMoves, captureMoves)
#
# def getKingMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
#     addMoveIfLegal(position, row, col, row+1, col+1, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row+1, col-1, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row+1, col, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row-1, col+1, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row-1, col-1, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row-1, col, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row, col+1, upperCase, nonCaptureMoves, captureMoves)
#     addMoveIfLegal(position, row, col, row, col-1, upperCase, nonCaptureMoves, captureMoves)
#
#
# def getPawnMoveHelper(prevPosition, position, upperCase, row, col, rowInc, nonCaptureMoves, captureMoves):
#     nextRow = row+rowInc
#     if CheckUtils.isInRange(nextRow) == False:
#         return
#
#     if position[nextRow][col] == '.':
#         addMoveIfLegal(position, row, col, nextRow, col, upperCase, nonCaptureMoves, captureMoves)
#     plus = col+1
#     minus = col-1
#     if CheckUtils.isInRange(plus) and position[nextRow][plus] != '.' and \
#             ((upperCase == True and position[nextRow][plus].islower()) or \
#              (upperCase == False and position[nextRow][plus].isupper())):
#         addMoveIfLegal(position, row, col, nextRow, plus, upperCase, nonCaptureMoves, captureMoves)
#     if CheckUtils.isInRange(minus) and position[nextRow][minus] != '.' and \
#             ((upperCase == True and position[nextRow][minus].islower()) or \
#              (upperCase == False and position[nextRow][minus].isupper())):
#         addMoveIfLegal(position, row, col, nextRow, minus, upperCase, nonCaptureMoves, captureMoves)
#
#     piece = 'P'
#     thisPiece = 'p'
#     if upperCase:
#         piece = 'p'
#         thisPiece = 'P'
#     if CheckUtils.isInRange(col+1):
#         print(row, rowInc, col)
#         if prevPosition[row + rowInc*2][col+1] == piece and prevPosition[row][col+1] == '.' and \
#             position[row + rowInc*2][col+1] == '.' and position[row][col+1] == piece:
#             newPos = deepcopy(position)
#             newPos[row][col] = '.'
#             newPos[nextRow][col+1] = thisPiece
#             newPos[row][col+1] = '.'
#             captureMoves.append(newPos)
#     if CheckUtils.isInRange(col - 1):
#         if prevPosition[row + rowInc*2][col - 1] == piece and prevPosition[row][col - 1] == '.' and \
#                 position[row + rowInc*2][col - 1] == '.' and position[row][col - 1] == piece:
#             newPos = deepcopy(position)
#             newPos[row][col] = '.'
#             newPos[nextRow][col - 1] = thisPiece
#             newPos[row][col - 1] = '.'
#             captureMoves.append(newPos)
#
#
# def getPawnMoves(prevPosition, position, upperCase, row, col, nonCaptureMoves, captureMoves):
#     if upperCase:
#         getPawnMoveHelper(prevPosition, position, upperCase, row, col, -1, nonCaptureMoves, captureMoves)
#     else:
#         getPawnMoveHelper(prevPosition, position, upperCase, row, col, 1, nonCaptureMoves, captureMoves)

#def getAllMoves(prevPosition, position, whiteMove):
    # nonCaptureMoves = []
    # captureMoves = []
    # print(whiteMove)
    # for i in range(0, 8):
    #     for j in range(0,8):
    #         if position[i][j] == '.':
    #             continue
    #         if (whiteMove and position[i][j].islower()) or (whiteMove == False and position[i][j].isupper()):
    #             continue
    #         elif position[i][j].lower() == 'p':
    #             getPawnMoves(prevPosition, position, whiteMove, i, j, nonCaptureMoves, captureMoves)
    #         elif position[i][j].lower() == 'k':
    #             getKingMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
    #         elif position[i][j].lower() == 'q':
    #             getQueenMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
    #         elif position[i][j].lower() == 'r':
    #             getRookMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
    #         elif position[i][j].lower() == 'n':
    #             getKnightMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
    #         elif position[i][j].lower() == 'b':
    #             getBishopMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
    #
    # return nonCaptureMoves, captureMoves
# t = time.time()
# board = chess.Board()
# for move in list(board.legal_moves):
#     c = deepcopy(board)
#     c.push(move)
#     print(str(c))
#     strBoard = re.split('\s|\n', str(c))
#     # Parse board string into (2,6,8,8) dimensional matrix (color, pieceType, row, column)
#     npBoard = np.array(strBoard).reshape((8, 8))
# print(time.time() - t)

#IS WHITE TURN 0 OR 1?????
def convertFenToBoard(fen):
    index = fen.index(' ')
    board = fen[0:index]
    rest = fen[fen.index(' ')+1:]
    whiteTurn = 0
    whiteKC = 0
    whiteQC = 0
    blackKC = 0
    blackQC = 0
    if 'w' in rest:
        whiteTurn = 1
    if 'K' in rest:
        whiteKC = 1
    if 'Q' in rest:
        whiteQC = 1
    if 'k' in rest:
        blackKC = 1
    if 'q' in rest:
        blackQC = 1

    matrix = np.zeros(shape=(2, 6, 8, 8))
    currRow = 0
    currCol = 0
    for c in board:
        if c=='/':
            currRow = currRow + 1
            currCol = 0
            continue
        elif c>='1' and c<='8':
            currCol = currCol + int(str(c))
            continue

        lower = c.lower()
        piece = 0
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

        colour = 0
        if c.islower():
            colour = 1
        matrix[colour][piece][currRow][currCol]=1
        currCol = currCol+1
    matrix = np.reshape(matrix, (768)).tolist()
    matrix.append(whiteKC)
    matrix.append(whiteQC)
    matrix.append(blackKC)
    matrix.append(blackQC)
    matrix.append(whiteTurn)
    return matrix

def getAllNextPositions(board, includeCaptures):
    positions = []
    for move in list(board.legal_moves):
        c = board.copy()
        c.push(move)
        if includeCaptures == False and (isCaptureMove(c, board) or c.has_legal_en_passant()):
            continue
        positions.append(c)
    return positions

import ModelGenerator as mg
import tensorflow as tf
import numpy as np
import chess

model = mg.genModel()
model.load_weights('../Model/totalModel50SGD')
model =tf.lite.TFLiteConverter.from_keras_model(model).convert()
with open('model.tflite', 'wb') as f:
  f.write(model)

model = tf.lite.Interpreter(model_path="model.tflite")
model.allocate_tensors()

input_details = model.get_input_details()
output_details = model.get_output_details()
def compare(b1, b2):
    w = '1-0'
    b = '0-1'
    whiteLeft = [1.0, 0.0]
    whiteRight = [0.0, 1.0]
    if b1.is_checkmate() and b2.is_checkmate():
        if b1.result() == b2.result():
            if b1.result() == w:
                if b1.fullmove_number < b2.fullmove_number:
                    return whiteLeft
                else:
                    return whiteRight
            else:
                if b1.fullmove_number < b2.fullmove_number:
                    return whiteRight
                else:
                    return whiteLeft
        elif b1.result()==w:
            return whiteLeft
        else:
            return whiteRight
    elif b1.is_checkmate():
        if b1.result() == w:
            return whiteLeft
        else:
            return whiteRight
    elif b2.is_checkmate():
        if b2.result() == b:
            return whiteLeft
        else:
            return whiteRight


    isB1Stale = b1.is_stalemate()
    isB2Stale = b2.is_stalemate()

    if (isB1Stale == True and isB2Stale == True):
        return [0.5, 0.5]
    elif (isB1Stale == True):
        b1 = chess.Board()
    elif (isB2Stale == True):
        b2 = chess.Board()

    m1 = convertFenToBoard(b1.fen())
    m2 = convertFenToBoard(b2.fen())
    #t = time.time()
    model.set_tensor(input_details[0]['index'], np.asarray([m1],dtype=np.float32))
    model.set_tensor(input_details[1]['index'], np.asarray([m2], dtype=np.float32))
    model.invoke()
    pred = model.get_tensor(output_details[0]['index'])
    #print(time.time() - t)
    print("-----")
    print(b1)
    print("--")
    print(b2)
    print(pred[0])
    print("-----")
    return pred[0]

import timeit
import time
import multiprocessing as mp


def isBetter(b1, b2, isWhiteMove):
    if b1 == None:
        return False
    vals = compare(b1, b2)
    if (isWhiteMove and vals[0] > vals[1]) or (isWhiteMove == False and vals[1] > vals[0]):
        return True
    return False

def isCaptureMove(currPos, prevPos):
    curr = currPos.fen()
    prev = prevPos.fen()
    curr = curr[0:curr.index(' ')]
    prev = prev[0:prev.index(' ')]
    def numPieces(b):
        num = 0
        for i in b:
            if i in ['p','r','n','b','q','k','P','R','N','B','Q','K']:
                num = num + 1
        return num
    if numPieces(curr) < numPieces(prev):
        return True
    return False

def getNextWhiteMove(board, alpha, depth, maxDepth):
    if board.is_checkmate() or board.is_stalemate():
        return board
    nextPositions = getAllNextPositions(board, depth<=maxDepth)
    currPos = None
    nextMove = True

    i = -1
    index = -1

    for pos in nextPositions:
        index = index + 1
        compareTo = pos
        if depth < maxDepth or isCaptureMove(pos, board) or pos.has_legal_en_passant():
            compareTo = getNextBlackMove(pos, currPos, depth + 1, maxDepth)
        compareTo = compareTo
        if currPos == None or isBetter(compareTo, currPos, True):
            currPos = compareTo
            i = index
        if alpha != None and isBetter(compareTo, alpha, True):
            return alpha

    if len(nextPositions)==0 or i == -1:
        return board
    if (depth == 0):
        return nextPositions[i]
    return currPos


def getNextBlackMove(board, alpha, depth, maxDepth):
    if board.is_checkmate() or board.is_stalemate():
        return board
    nextPositions = getAllNextPositions(board, depth<=maxDepth)
    currPos = None
    nextMove = True

    i = -1
    index = -1

    for pos in nextPositions:
        index = index + 1
        compareTo = pos
        if depth<maxDepth or isCaptureMove(pos, board) or pos.has_legal_en_passant():
            compareTo = getNextWhiteMove(pos, currPos, depth+1, maxDepth)
        compareTo = compareTo
        if currPos == None or isBetter(compareTo, currPos, False):
            currPos = compareTo
            i = index
        if alpha != None and isBetter(compareTo, alpha, False):
            return alpha

    if len(nextPositions) == 0 or i == -1:
        return board
    if (depth == 0):
        return nextPositions[i]
    return currPos

def getNextMove(board, isWhiteMove, maxDepth):
    if isWhiteMove:
        return getNextWhiteMove(board, None, 0, maxDepth)
    else:
        return getNextBlackMove(board, None, 0, maxDepth)

# board = chess.Board()
# board2 = chess.Board()
# board2.set_fen('8/4k3/8/8/KQR5/8/8/8 w')
# print(str(board2))
# compare(board, board2, True)
