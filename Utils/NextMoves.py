
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

import Utils.ModelGenerator as mg
import tensorflow as tf
import numpy as np
import chess

model = mg.genModel()
model.load_weights('Model/totalModel50SGD')
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
    # print("-----")
    # print(b1)
    # print("--")
    # print(b2)
    # print(pred[0])
    # print("-----")
    return pred[0]

import timeit
import time
import multiprocessing as mp
import chess

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
    nextPositions = getAllNextPositions(board, True)
    currPos = None
    nextMove = True

    i = -1
    index = -1

    for pos in nextPositions:
        index = index + 1
        compareTo = pos
        if depth < maxDepth or pos.has_legal_en_passant():
            compareTo = getNextBlackMove(pos, currPos, depth + 1, maxDepth)
        change = False
        if currPos == None or (compareTo.fen() != currPos.fen() and isBetter(compareTo, currPos, True)):
            currPos = compareTo
            i = index
            change = True
        if alpha != None and change and isBetter(currPos, alpha, True):
            return alpha

    if len(nextPositions)==0 or i == -1:
        return board
    if (depth == 0):
        return nextPositions[i]
    return currPos


def getNextBlackMove(board, alpha, depth, maxDepth):
    if board.is_checkmate() or board.is_stalemate():
        return board
    nextPositions = getAllNextPositions(board, True)
    currPos = None
    nextMove = True

    i = -1
    index = -1

    for pos in nextPositions:
        index = index + 1
        compareTo = pos
        if depth<maxDepth or pos.has_legal_en_passant():
            compareTo = getNextWhiteMove(pos, currPos, depth+1, maxDepth)

        change = False
        if currPos == None or (compareTo.fen() != currPos.fen() and isBetter(compareTo, currPos, False)):
            currPos = compareTo
            i = index
            change = True
        if alpha != None and change and isBetter(currPos, alpha, False):
            return alpha

    if len(nextPositions) == 0 or i == -1:
        return board
    if (depth == 0):
        return nextPositions[i]
    return currPos

def getNextMove(board, maxDepth, isWhiteMove=None):
    if isWhiteMove==None:
        isWhiteMove = (board.turn==chess.WHITE)
    print(isWhiteMove)
    if isWhiteMove:
        return getNextWhiteMove(board, None, 0, maxDepth)
    else:
        return getNextBlackMove(board, None, 0, maxDepth)


