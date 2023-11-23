from random import randint

#################################################################################################
#################################################################################################
#################################################################################################
'''                            Hey stranger! Nice to meet you!                                '''
'''                       Byt the way I'm looking for a developer job                         '''     
'''                                                                                           '''
'''              Check my linkedIn  https://www.linkedin.com/in/mikhail-chekin/               '''
'''                                 if you can help me                                        '''
'''                                                                                           '''
'''                            or just enjoy the solution                                     '''                                    
#################################################################################################
#################################################################################################
#################################################################################################


class puzzle(list):
    """Class for the puzzle. just a list of lists
        plus 4 rotate methods and history list as attribute.
        history stores all rotation of the puzzle."""

    def __init__(self):
        self.history = []
        self.m = 0
        self.n = 0
        self.is_solved = False

    def __str__(self):
        return ("------------------------\n" +
                '\n'.join([str(_) for _ in self]) +
                "\n------------------------\n")

    def create_matrix(self, m, n):
        """ create matrix m x n, filled with number from 0 to m*n
            m - number of rows
            n - numer of columns
            set corresponding attributes m and n"""
        self.m = m
        self.n = n
        for i in range(m):
            self.append([])
            for k in range(n):
                self[i].append(i * self.n + k)

    def read_matrix(self, matrix):
        """be careful, this function clear original self
        content and rewrite it with new one"""
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.clear()
        for i in range(self.m):
            self.append([])
            for k in range(self.n):
                self[i].append(matrix[i][k])

    def left(self, row, repetition=1):
        """base method, rotate certain row of puzzle to the left.
        number of repetition = repetition
        log moves to history list"""
        for _ in range(repetition):
            self.history.append('L' + str(row))
            self[row].append(self[row][0])
            self[row].pop(0)

    def right(self, row, repetition=1):
        """base method, rotate certain row of puzzle to the right.
        number of repetition = repetition
        log moves to history list"""
        for _ in range(repetition):
            self.history.append('R' + str(row))
            self[row] = self[row][self.n-1:] + self[row][:self.n-1]

    def up(self, column, repetition=1):
        """base method, rotate certain column of the puzzle upward.
        number of repetition = repetition
        log moves to history list"""
        for _ in range(repetition):
            self.history.append('U' + str(column))
            tmp = self[0][column]
            for i in range(1, self.m):
                self[i-1][column] = self[i][column]
            self[self.m-1][column] = tmp

    def down(self, column, repetition=1):
        """base method, rotate certain column of the puzzle downward.
        number of repetition = repetition
        log moves to history list"""
        for _ in range(repetition):
            self.history.append('D' + str(column))
            tmp = self[self.m-1][column]
            for i in range(self.m-1, 0, -1):
                self[i][column] = self[i-1][column]
            self[0][column] = tmp

    def get_address(self, elem):
        """ find element elem in the puzzle, return address in matrix"""
        for i in range(self.m):
            if elem in self[i]:
                return (i, self[i].index(elem))

    def shuffle(self, n):
        """ make n random rotation of our puzzle"""
        for i in range(n):
            move_r_l = randint(0, self.m-1)
            move_u_d = randint(0, self.n-1)
            move = randint(0, 3)
            if move == 0:
                self.left(move_r_l)
            elif move == 1:
                self.right(move_r_l)
            elif move == 2:
                self.up(move_u_d)
            elif move == 3:
                self.down(move_u_d)

    def move_to_rb_corner(self, addr):
        """this function move elements with specified address
        to the right bottom corner"""
        self.right(addr[0], self.n - addr[1]-1)
        self.down(self.n-1, self.m - addr[0]-1)
        
        if addr[0] != self.m - 1:  # we need to fix line where the element
            # was, but not if it is in the bottom line
            self.right(addr[0], (addr[1]+1) % self.n)

    def solve_vertical_line(self, ref, column=0, rows=0):
        """find elements which need to be placed in certain
        column in first rows. rows=0 means we move 1 element
        (columns=2 row=3 func will process elements [0][2], [1][2], [2][2])"""
        for i in range(rows + 1):
            addr = self.get_address(ref[i][column])
            self.move_to_rb_corner(addr)
            # strange line, it does nothing, so put it in if incase it needed
            # for any reason 
            if rows + 2 != self.m:
                self.down(self.n-1, rows + 2)
            self.right(rows+1, column+1)
            self.up(column)

    def solve_horisontal_line(self, ref, row=1, columns=0):
        """find element which need to be placed in row in first columns places
        (row=1 columns=3 will process elements [2][0], [2][1], [2][2])"""
        for i in range(columns+1):
            addr = self.get_address(ref[row][i])
            self.move_to_rb_corner(addr)
            self.down(self.n-1, row + 2)
            self.right(row+1, columns+2)
            self.up(columns+1)
            self.left(row)

    def solve_last_vertical(self, ref):
        """place top n-2 elements in the left column,
        and we still need one place to solve bottom line"""
        for i in range(self.m-2):
            addr = self.get_address(ref[i][self.n-1])
            if addr[1] == self.n-1:
                self.down(self.n-1, self.m-addr[0]-1)
                self.left(self.m-1)
                self.up(self.n - 1, self.m - addr[0] - 1)
                self.right(self.m - 1)
                self.up(self.n-1)
            else:
                self.right(self.m - 1, self.n - addr[1] - 1)
                self.up(self.n - 1)

    def solve_last_horisontal(self, ref):
        """solve bottom line plus last elem in last vertical line
            sometimes it will not return unsolved puzzle """
        for i in range(self.n-1):  # check number
            addr = self.get_address(ref[self.m-1][i])
            if addr[1] == self.n-1:
                self.down(self.n-1, self.m - addr[0] - 1)
                self.left(self.m-1)
                self.up(self.n - 1, self.m - addr[0] - 1)
            else:
                self.right(self.m - 1, self.n - addr[1] - 1)
                self.up(self.n - 1)
                self.left(self.m - 1, self.n - addr[1] - 1)
                self.down(self.n - 1)
                self.left(self.m - 1)
        self.up(self.n - 1)
        if self[self.m - 1][self.n - 1] == ref[self.m - 1][self.n - 1]:
            self.is_solved = True

# # submited to codewars. class code is the same. only main function is
# # different.
# def loopover(mixed_up_board, solved_board):
#     problem = puzzle()  # create instance of class puzzle
#     ref_m = puzzle()   # create another one for solved pattern
#     problem.read_matrix(mixed_up_board)  # read input matrix and place
#                                          # it into our class
#     ref_m.read_matrix(solved_board)
#     n = problem.n
#     m = problem.m
#     while True:
#         for i in range(n - 1):
#             problem.solve_vertical_line(ref_m, i, m - 2)
#         problem.solve_last_vertical(ref_m)
#         problem.solve_last_horisontal(ref_m)
#         if problem.is_solved:  # only solve_last_horisontal can set
#                                # is_solved to True
#             break
#         else:
#             if problem.m * problem.n % 2 != 0:
#                 return None  # puzzle with uneven number of elements
#                   # and with two neighbor elements swapped can't be solved
#             problem.shuffle(5)  # oops, bad lack, but if number of element
#                              # is even. we can try to solve it again.
#                              # Let's shuflle and go
#     return problem.history


# standalone variant with autoproblem creation and shuffling.
# -------------- Create new puzzle and shaffle it -----------------------#

m = int(input('Enter number of rows: '))
n = int(input('Enter number of colums: '))

problem = puzzle()
problem.create_matrix(m, n)
problem.shuffle(5)
problem.history.clear()

# ------------------------------------------------------------------------#
ref_m = puzzle()
ref_m.create_matrix(m, n)

#  ref_m[m-1][n-1],ref_m[m-1][n-2] = ref_m[m-1][n-2],ref_m[m-1][n-1]
# print('-----------------------------------------')
# print(*ref_m, sep='\n')
# print('-----------------------------------------')
print("Original", ref_m, sep='\n')


# -------------------------START TO SOLVE --------------------------------#

print("Suffled", problem, sep='\n')
# print(*problem, sep='\n')

print('------------------------')

while True:
    for i in range(n-1):
        problem.solve_vertical_line(ref_m, i, m-2)

    problem.solve_last_vertical(ref_m)
    problem.solve_last_horisontal(ref_m)

    if problem.is_solved:
        break
    else:
        if problem.m * problem.n % 2 != 0:
            print('cannot solve this')
            break
        problem.shuffle(25)

print("solved", problem, sep='\n')
print('------------------------')
print(problem.history)
print('------------------------')
print('Numbers of steps = ' + str(len(problem.history)))
