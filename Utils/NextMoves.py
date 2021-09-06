import CheckUtils
from copy import deepcopy

def addMoveIfLegal(position, row, col, newRow, newCol, upperCase, nonCaptureMoves, captureMoves):
    if CheckUtils.isInRange(newRow) == False or CheckUtils.isInRange(newCol) == False:
        return False

    copy = deepcopy(position)
    c = copy[newRow][newCol]
    isSameCase = ((c.isupper() and upperCase == True) or (c.islower() and upperCase == False)) and c != '.'

    if c != '.' and isSameCase:
        return False
    copy[newRow][newCol] = copy[row][col]
    copy[row][col] = '.'
    if CheckUtils.isKingChecked(copy, upperCase):
        return False

    if c == '.':
        nonCaptureMoves.append(copy)
        return True
    else:
        captureMoves.append(copy)
        return False

def possibleLinearMoves(position, upperCase, row, col, rowInc, colInc, nonCaptureMoves, captureMoves):
    currRow = row
    currCol = col
    while True:
        currRow = currRow + rowInc
        currCol = currCol + colInc
        cont = addMoveIfLegal(position, row, col, currRow, currCol, upperCase, nonCaptureMoves, captureMoves)
        if cont == False:
            break

def getRookMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
    possibleLinearMoves(position, upperCase, row, col, 1, 0, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, -1, 0, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, 0, 1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, 0, -1, nonCaptureMoves, captureMoves)

def getBishopMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
    possibleLinearMoves(position, upperCase, row, col, 1, 1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, -1, -1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, -1, 1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, 1, -1, nonCaptureMoves, captureMoves)

def getQueenMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
    possibleLinearMoves(position, upperCase, row, col, 1, 1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, -1, -1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, -1, 1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, 1, -1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, 1, 0, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, -1, 0, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, 0, 1, nonCaptureMoves, captureMoves)
    possibleLinearMoves(position, upperCase, row, col, 0, -1, nonCaptureMoves, captureMoves)

def getKnightMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
    addMoveIfLegal(position, row, col, row+1, col+2, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row+1, col-2, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row-1, col+2, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row-1, col-2, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row+2, col+1, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row+2, col-1, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row-2, col+1, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row-2, col-1, upperCase, nonCaptureMoves, captureMoves)

def getKingMoves(position, upperCase, row, col, nonCaptureMoves, captureMoves):
    addMoveIfLegal(position, row, col, row+1, col+1, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row+1, col-1, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row+1, col, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row-1, col+1, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row-1, col-1, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row-1, col, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row, col+1, upperCase, nonCaptureMoves, captureMoves)
    addMoveIfLegal(position, row, col, row, col-1, upperCase, nonCaptureMoves, captureMoves)


def getPawnMoveHelper(prevPosition, position, upperCase, row, col, rowInc, nonCaptureMoves, captureMoves):
    nextRow = row+rowInc
    if CheckUtils.isInRange(nextRow) == False:
        return

    if position[nextRow][col] == '.':
        addMoveIfLegal(position, row, col, nextRow, col, upperCase, nonCaptureMoves, captureMoves)
    plus = col+1
    minus = col-1
    if CheckUtils.isInRange(plus) and position[nextRow][plus] != '.' and \
            ((upperCase == True and position[nextRow][plus].islower()) or
             (upperCase == False and position[nextRow][plus].isupper())):
        addMoveIfLegal(position, row, col, nextRow, plus, upperCase, nonCaptureMoves, captureMoves)
    if CheckUtils.isInRange(minus) and position[nextRow][minus] != '.' and \
            ((upperCase == True and position[nextRow][minus].islower()) or \
             (upperCase == False and position[nextRow][minus].isupper())):
        addMoveIfLegal(position, row, col, nextRow, minus, upperCase, nonCaptureMoves, captureMoves)

    piece = 'P'
    thisPiece = 'p'
    if upperCase:
        piece = 'p'
        thisPiece = 'P'
    if CheckUtils.isInRange(col+1):
        if prevPosition[row + rowInc*2][col+1] == piece and prevPosition[row][col+1] == '.' and \
            position[row + rowInc*2][col+1] == '.' and position[row][col+1] == piece:
            newPos = deepcopy(position)
            newPos[row][col] = '.'
            newPos[nextRow][col+1] = thisPiece
            newPos[row][col+1] = '.'
            captureMoves.append(newPos)
    if CheckUtils.isInRange(col - 1):
        if prevPosition[row + rowInc*2][col - 1] == piece and prevPosition[row][col - 1] == '.' and \
                position[row + rowInc*2][col - 1] == '.' and position[row][col - 1] == piece:
            newPos = deepcopy(position)
            newPos[row][col] = '.'
            newPos[nextRow][col - 1] = thisPiece
            newPos[row][col - 1] = '.'
            captureMoves.append(newPos)


def getPawnMoves(prevPosition, position, upperCase, row, col, nonCaptureMoves, captureMoves):
    if upperCase:
        getPawnMoveHelper(prevPosition, position, upperCase, row, col, -1, nonCaptureMoves, captureMoves)
    else:
        getPawnMoveHelper(prevPosition, position, upperCase, row, col, 1, nonCaptureMoves, captureMoves)

def getAllMoves(prevPosition, position, whiteMove):
    nonCaptureMoves = []
    captureMoves = []

    for i in range(0, 8):
        for j in range(0,8):
            if position[i][j] == '.':
                continue
            elif position[i][j].lower == 'p':
                getPawnMoves(prevPosition, position, whiteMove, i, j, nonCaptureMoves, captureMoves)
            elif position[i][j].lower == 'k':
                getKingMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
            elif position[i][j].lower == 'p':
                getQueenMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
            elif position[i][j].lower == 'p':
                getRookMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
            elif position[i][j].lower == 'p':
                getKnightMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)
            elif position[i][j].lower == 'p':
                getBishopMoves(position, whiteMove, i, j, nonCaptureMoves, captureMoves)

    return nonCaptureMoves, captureMoves
