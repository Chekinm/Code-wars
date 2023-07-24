import numpy as np
from copy import deepcopy


def check_row(sud, x, y):
    """check the row of the element sud[x][y] according sudoku rules, update set of possible number"""
    tmp_set = set(sud[x][i][0] for i in range(len(sud)))
    sud[x][y][1] -= tmp_set
    return sud

def check_column(sud, x ,y):
    """check the column of the element sud[x][y], according sudoku rules update set of possible number"""
    tmp_set = set(sud[i][y][0] for i in range(len(sud)))
    sud[x][y][1] -= tmp_set
    return sud

def check_square(sud, x, y):
    """check own local 3x3 square of the element, update set of possible number according sudoku rules"""
    tmp_set = set()
    for i in range(x//3 * 3, x//3 * 3 + 3):
        for j in range(y//3 * 3, y//3 * 3 + 3):
            tmp_set.add(sud[i][j][0])
    sud[x][y][1] -= tmp_set
    return sud

def sudoku_prepare(puzzle):
    """ solve the given sudoku according rules of the sudoku,
        it is supposed that every time we can find a cell with unique number allowed"""
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            puzzle[i][j] = [int(puzzle[i][j]), set(i for i in range(1, 10))]
    return np.array(puzzle)

def sudoku_deliver(sud):
    puzzle = np.zeros(9,9)
    np.count_nonzero
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            puzzle[i][j] = str(sud[i][j][0])
    return puzzle


def sudoku_try(sud):
    """ solve the given sudoku according rules of the sudoku,
        trying until too consecutive try is the same"""

    while 0 in sud:
        sud_prev = deepcopy(sud)
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if sud[i][j][0] == 0:
                    check_row(sud, i, j)
                    check_column(sud, i, j)
                    check_square(sud, i, j)
                    if len(sud[i][j][1]) == 1:
                        sud[i][j][0] = sud[i][j][1].pop()
        if sud == sud_prev:
            return sud, False

    return sud, True

def sudoku_guess(puzzle):
    pass
def main(puzzle):
    sud = sudoku_prepare(puzzle)
    sud, solved = sudoku_try(sud)
    if solved:
        return sudoku_prepare(sud)
    else:
        while not solved:
            for i in range(len(sud)):
                for j in range(len(sud)):
                    for guessed in sud[i][j][1]:
                        sud_g = deepcopy((sud)):
                        sud_g[i][j] = guessed
                        sud_g, flag = sudoku_try(sud_g)
                        if flag:
                            return sudoku_prepare(sud_g)






