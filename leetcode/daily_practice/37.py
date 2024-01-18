import numpy as np
from copy import deepcopy


class Solution(object):
    def solveSudoku(self, puzzle):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def check_row(sud, x, y):
            """check the row of the element sud[x][y] according sudoku rules, update set of possible number"""
            tmp_set = set(sud[x, :, 0])
            sud[x, y, 1] -= tmp_set
            return sud

        def check_column(sud, x, y):
            """check the column of the element sud[x][y], according sudoku rules update set of possible number"""
            tmp_set = set(sud[:, y, 0])
            sud[x, y, 1] -= tmp_set
            return sud

        def check_square(sud, x, y):
            """check own local 3x3 square of the element, update set of possible number according sudoku rules"""
            tmp_set = set()
            for i in range(x // 3 * 3, x // 3 * 3 + 3):
                for j in range(y // 3 * 3, y // 3 * 3 + 3):
                    tmp_set.add(sud[i, j, 0])
            sud[x, y, 1] -= tmp_set
            return sud

        def sudoku_prepare(puzzle):
            """ get sudoku in str format and transfer it to no with numbers an 0 on an empty place"""
            puzzle = np.array([[0 if cell == '.' else int(cell) for cell in row] for row in puzzle])
            sudoku = np.zeros((9, 9, 2), dtype=object)
            for i in range(len(puzzle)):
                for j in range(len(puzzle)):
                    sudoku[i, j] = [puzzle[i, j], set(i for i in range(1, 10))]
                    if puzzle[i, j] != 0:
                        sudoku[i, j, 1] = set()
            return sudoku

        def sudoku_deliver(sud, puzzle):
            """return solved in str format"""
            for i in range(len(sud)):
                for j in range(len(sud)):
                    puzzle[i][j] = str(sud[i, j, 0])

        def sudoku_try(sud):
            """ try to solve the given sudoku according to the rules of the sudoku,
                trying until two consecutive tries are the same"""
            while 0 in sud[:, :, 0]:
                counter_of_changes = 0
                for i in range(len(puzzle)):
                    for j in range(len(puzzle)):
                        if sud[i, j, 0] == 0:
                            check_row(sud, i, j)
                            check_column(sud, i, j)
                            check_square(sud, i, j)
                            if len(sud[i, j, 1]) == 1:
                                counter_of_changes += 1
                                sud[i, j, 0] = sud[i, j, 1].pop()

                if counter_of_changes == 0:
                    return sud, False

            return sud, True

        sud = sudoku_prepare(puzzle)
        sud, solved = sudoku_try(sud)

        if solved:
            sudoku_deliver(sud, puzzle)
        else:
            for i in range(len(sud)):
                for j in range(len(sud)):
                    for guessed in sud[i, j, 1]:
                        sud_g = deepcopy(sud)
                        sud_g[i, j, 0] = guessed
                        sud_g, solved = sudoku_try(sud_g)
                        if solved:
                            sudoku_deliver(sud_g, puzzle)
                            return
