import numpy as np

def checkHelper(row, col, rowInc, colInc, position, checkForPiece, kingCaseUpper):
    currRow = row
    currCol = col
    while True:
        currRow = currRow + rowInc
        currCol = currCol + colInc
        if currRow < 0 or currRow > 7 or currCol < 0 or currCol > 7:
            return False

        c = position[currRow][currCol]
        if c == '.':
            continue
        elif (c.isupper() and kingCaseUpper == True) or (c.islower() and kingCaseUpper == False):
            break
        elif c.lower() == checkForPiece.lower():
            return True
        else:
            return False
    return False

def rookChecks(position, kingCaseUpper, row, col):
    check1 = checkHelper(row, col, 1, 0, position, 'r', kingCaseUpper)
    check2 = checkHelper(row, col, -1, 0, position, 'r', kingCaseUpper)
    check3 = checkHelper(row, col, 0, 1, position, 'r', kingCaseUpper)
    check4 = checkHelper(row, col, 0, -1, position, 'r', kingCaseUpper)
    return check1 or check2 or check3 or check4

def bishopChecks(position, kingCaseUpper, row, col):
    check1 = checkHelper(row, col, 1, 1, position, 'b', kingCaseUpper)
    check2 = checkHelper(row, col, -1, -1, position, 'b', kingCaseUpper)
    check3 = checkHelper(row, col, -1, 1, position, 'b', kingCaseUpper)
    check4 = checkHelper(row, col, 1, -1, position, 'b', kingCaseUpper)
    return check1 or check2 or check3 or check4

def queenChecks(position, kingCaseUpper, row, col):
    check1 = checkHelper(row, col, 1, 0, position, 'q', kingCaseUpper)
    check2 = checkHelper(row, col, -1, 0, position, 'q', kingCaseUpper)
    check3 = checkHelper(row, col, 0, 1, position, 'q', kingCaseUpper)
    check4 = checkHelper(row, col, 0, -1, position, 'q', kingCaseUpper)
    check5 = checkHelper(row, col, 1, 1, position, 'q', kingCaseUpper)
    check6 = checkHelper(row, col, -1, -1, position, 'q', kingCaseUpper)
    check7 = checkHelper(row, col, -1, 1, position, 'q', kingCaseUpper)
    check8 = checkHelper(row, col, 1, -1, position, 'q', kingCaseUpper)
    return check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8

def isInRange(num):
    if num<0 or num>7:
        return False
    return True

def pieceCheckHelper(position, kingCaseUpper, row, col, c):
    if position[row][col] == '.' or position[row][col].lower() != c.lower():
        return False

    if (kingCaseUpper == True and position[row][col].islower()) or\
            (kingCaseUpper == False and position[row][col].isupper()):
        return True

    return False

def check(position, kingCaseUpper, currRow, currCol, c):
    if isInRange(currRow) and isInRange(currCol):
        return pieceCheckHelper(position, kingCaseUpper, currRow, currCol, c)
    return False

def knightChecks(position, kingCaseUpper, row, col):
    check1 = check(position, kingCaseUpper, row + 2, col + 1, 'n')
    check2 = check(position, kingCaseUpper, row + 2, col - 1, 'n')
    check3 = check(position, kingCaseUpper, row - 2, col + 1, 'n')
    check4 = check(position, kingCaseUpper, row - 2, col - 1, 'n')
    check5 = check(position, kingCaseUpper, row + 1, col + 2, 'n')
    check6 = check(position, kingCaseUpper, row + 1, col - 2, 'n')
    check7 = check(position, kingCaseUpper, row - 1, col + 2, 'n')
    check8 = check(position, kingCaseUpper, row - 1, col - 2, 'n')

    return check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8


def kingCheck(position, kingCaseUpper, row, col):
    check1 = check(position, kingCaseUpper, row + 1, col + 1, 'k')
    check2 = check(position, kingCaseUpper, row - 1, col + 1, 'k')
    check3 = check(position, kingCaseUpper, row, col + 1, 'k')
    check4 = check(position, kingCaseUpper, row + 1, col - 1, 'k')
    check5 = check(position, kingCaseUpper, row - 1, col - 1, 'k')
    check6 = check(position, kingCaseUpper, row, col - 1, 'k')
    check7 = check(position, kingCaseUpper, row + 1, col, 'k')
    check8 = check(position, kingCaseUpper, row - 1, col, 'k')

    return check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8

def pawnChecks(position, kingCaseUpper, row, col):
    rowInc = 1
    if kingCaseUpper == True:
        rowInc = -1
    if check(position, kingCaseUpper, row+rowInc, col-1, 'p') or check(position, kingCaseUpper, row+rowInc, col+1, 'p'):
        return True
    return False


def isKingChecked(position, whiteKing):
    kingCaseUpper = True
    if whiteKing == False:
        kingCaseUpper = False

    row = -1
    col = -1
    for i in range(0,8):
        for j in range(0,8):
            if kingCaseUpper == False and position[i][j] == 'k':
                row = i
                col = j
            elif kingCaseUpper == True and position[i][j] == 'K':
                row = i
                col = j

    if row == -1:
        return

    return pawnChecks(position, kingCaseUpper, row, col) or \
           knightChecks(position, kingCaseUpper, row, col) or \
           kingCheck(position, kingCaseUpper, row, col) or \
           queenChecks(position, kingCaseUpper, row, col) or \
           bishopChecks(position, kingCaseUpper, row, col) or \
           rookChecks(position, kingCaseUpper, row, col)


