from itertools import combinations

class Map:
    def __init__(self, task: str, mines: int) -> None:
        self.matrix = [row.split() for row in task.split('\n')]
        self.len_x = len(self.matrix)
        self.len_y = len(self.matrix[0])
        self.mines = mines

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.matrix])

    def get_field(self, x, y):
        return self.matrix[x][y]

    def set_field(self, x, y, value):
        self.matrix[x][y] = value

    def copy(self):
        return Map(str(self), self.mines)
    
    def get_unresolved(self):
        unresolved = []
        for x in range(self.len_x):
            for y in range(self.len_y):
                if self.get_field(x, y) == '?':
                    unresolved.append((x, y))
        return unresolved

    def open_rest_of_the_solved(self):
        for x in range(self.len_x):
            for y in range(self.len_y):
                if self.get_field(x, y) == '?':
                    self.set_field(x, y, str(open(x, y)))

    def get_surrounding(self, x, y):
        return [(x+i, y+j, self.matrix[x+i][y+j])
                for i in range(-1, 2)
                for j in range(-1, 2)
                if (0 <= x+i < self.len_x and
                    0 <= y+j < self.len_y and
                    not (i == 0 and j == 0))]

    def count_surrounding(self, x, y):
        mines = 0
        quests = 0
        opens = 0
        surr = self.get_surrounding(x, y)
        for x, y, value in surr:
            val = self.get_field(x, y)
            if val == 'x':
                mines += 1
            elif val == '?':
                quests += 1
            else:
                opens += 1

        return (mines, quests, opens, len(surr), surr)

    def count_quantum_surrounding(self, x, y):
        mines = 0
        mines_coord = set()
        quests = 0
        quests_coord = set()
        opens = 0
        opens_coord = set()
        surr = self.get_surrounding(x, y)
        for x, y, value in surr:
            val = self.get_field(x, y)
            if val == 'x':
                mines += 1
                mines_coord.add((x, y))
            elif val == '?':
                quests += 1
                quests_coord.add((x, y))
            else:
                opens += 1
                opens_coord.add((x, y))

        return (mines_coord, quests_coord, opens_coord)

    def localize_problem_region(self, unresolved):
        to_check = set()
        to_check_surr_only = set()
        for x, y in unresolved:
            for x1, y1, value in self.get_surrounding(x, y):
                to_check.add((x1, y1, value))
                # also create set with only border cell
                if (x1, y1) not in unresolved:
                    to_check_surr_only.add((x1, y1, value))

        # print( f'{unresolved=}\n surraunding ={list(to_check)}')
        # print(f'to_check={list(to_check)}')
        # print(f'surr_to_check {list(to_check_surr_only)}')

        return list(to_check), list(to_check_surr_only)

    def check_consistency(self, unresolved):

        to_check, to_check_boarder_only = self.localize_problem_region(unresolved)

        for x, y, value in to_check:
            if isinstance(value, int) or value.isdigit():  # ok we have number here, let collect some information about surrounding
                value = int(value)
                mines, quests, opens, total, surr = self.count_surrounding(x, y)
                if mines != value:
                    return False
        return True

    def quantum_logic(self, border):
        """pure magic occures here
        we build spaces of probablilites, and try to find
        mines regions that non intersect"""
        quantum_mines_space = []

        for x, y, value in border:
            if isinstance(value, int) or value.isdigit():
                (mines_coord, 
                 quests_coord, 
                 opens_coord) = self.count_quantum_surrounding(x, y)
                quantum_mines_space.append(quests_coord)

        quantum_mines_space.sort(key=len)

        localized_mines_regions = []
        if quantum_mines_space:
            localized_mines_regions.append(quantum_mines_space[0])

        i = 0
        while i < len(quantum_mines_space):
            if not any(bool(quantum_mines_space[i].intersection(st))
                       for st in localized_mines_regions):
                localized_mines_regions.append(quantum_mines_space[i])
            i += 1

        return localized_mines_regions
    
    def perform_quantum_magic(self):
        # let see what has left unresolved
        unresolved = self.get_unresolved()

        to_check, to_check_boarder_only = self.localize_problem_region(unresolved)

        response_from_quantum_universe = self.quantum_logic(to_check_boarder_only)
        
        print(f'{response_from_quantum_universe=}')
        if len(response_from_quantum_universe) > self.mines:
            # defenetly not enough mines to fulfill all places
            print(f'{self.mines=},places={len(response_from_quantum_universe)=}')
            return '?'
        elif len(response_from_quantum_universe) < self.mines:
            print(f'quantum magic can\'t help, sorry too many mines places={len(response_from_quantum_universe)}, {self.mines=}')
            print('will call quntum another quntum magic trick')
            
            # self.perform_another_quantum_magic(to_check_boarder_only,
            #                                    response_from_quantum_universe,
            #                                    )
            
            return False

            
        # number of places exactly equal to the 
        # number of mines => we can open some fileds
        # lets do that
        dangerous = response_from_quantum_universe[0].union(*response_from_quantum_universe)
        non_dangerous = list(set(unresolved) - dangerous)
        for x, y in non_dangerous:
            self.set_field(x, y, open(x, y))
        return True
    
    # def perform_another_quantum_magic(self, border, localized_mines_spaces):
        
        
    #     for x, y, value in border:
    #         #  find numbers in bordres
    #         if isinstance(value, int) or value.isdigit():

    #         #  2 collect all data
    #             (mines_coord, 
    #              quests_coord, 
    #              opens_coord) = self.count_quantum_surrounding(x, y)
    #             value = int(value)
    #             mines, quests, opens, total, surr = self.count_surrounding(x, y)

    #         # find if any of mines regions a subset of quests_coords 
    #             for mine_region in localized_mines_spaces:
    #                 if mine_region.issubset(quests_coord):

                    



            





    def open_around_field(self, x, y):   
        """this finciton open solved cell using regression inside, kinda DTS"""

        value = self.get_field(x, y)

        if isinstance(value, int) or value.isdigit():  # ok we have number here, let collect some information about surrounding

            value = int(value)
            mines, quests, opens, total, surr = self.count_surrounding(x, y)

            if quests == 0:  # we know everything around this fild, cannot do nothing 
                return

            if value == mines:  # we know where all the mines is. others are clear, can dive depper
                for x1, y1, value in surr:
                    if value == '?':
                        new_value = str(open(x1, y1))
                        self.set_field(x1, y1, new_value)
                        self.open_around_field(x1,y1) # here regresion magic occurs
    
            elif quests <= (value - mines):  # '?' around equal to value- already open mines => all of them are mines
                for x2, y2, value2 in surr:
                    if value2 == '?':
                        self.set_field(x2, y2, 'x')
                        self.mines -= 1

        # any other case,  not enough information, go backward, we reach leaf our searh tree
        return


def fight_with_problem_cells(m: Map):

    # let see what has left unresolved
    unresolved = m.get_unresolved()

    if len(unresolved) == m.mines:  # thanks god, we know what to do
        for x, y in unresolved:
            m.set_field(x, y, 'x')
        return str(m)
    elif len(unresolved) == 2 or len(unresolved) > 20:
        # 2 - means there are lwayes two solution, unpredictable,
        # 20 means we are in efficency testcase, just drop it...
        return '?'

    else:
        # looks like we only have less than 20 fileds.
        # think we can broot force it.
        variants = combinations(unresolved, m.mines)
        print(f'we will try {len(unresolved)} cells with {m.mines} mines')
        print('=' * 20)
        print(str(m))
        print('=' * 20)

        valid_solutions = []
        for variant in variants:
            try_map = m.copy()

            for x, y in variant:
                try_map.set_field(x, y, 'x')
                try_map.mines -= 1

            if try_map.check_consistency(unresolved): # found valid solution
                # print('='* 20)
                # print(try_map)
                # print('='* 20)
                if valid_solutions:  # more than one valid solutions, means uncertanaty
                    return '?'
                else:
                    valid_solutions.append(try_map)

        if valid_solutions:  # we have on good
            m = valid_solutions[0].copy()
            # open the rest cells using map method
            m.open_rest_of_the_solved()
            return str(m)
        else:  # there is no one good solution
            return '?'


def solve_mine(map, n):

    m = Map(map, n)
    # two trivial case
    if len(map) == 1:
        return str('x' if n else 0)

    while m.mines:  # until we have undiscovered mines

        str_m_old = str(m)  # will check dead loop with this 

        for x in range(m.len_x):
            for y in range(m.len_y):
                m.open_around_field(x, y)

        if str(m) == str_m_old:  # we got stacked, no new moves was done using 
            # simple logic
            #  hope it is not a lot of cell to resolve.
            # lets try to do something with it
            # firstly try quantum magic
            print(m.mines)
            m.perform_quantum_magic()

            if str(m) == str_m_old: # if magic not working, do brute force:)
                return fight_with_problem_cells(m)
        else:
            str_m_old = str(m)

    else:
        # we found all mines, just need to open rest of the filed
        m.open_rest_of_the_solved()

    return str(m)

task="""0 0 0 ? ? ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? ? ?
? ? 0 ? ? ? ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
? ? ? ? 0 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? 0 ? ? ? ? ? ?
? ? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 ? ? ? ? ? ?
0 ? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ?
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? 0"""


original="""0 0 0 1 x 1 1 x 1 0 0 0 0 0 1 1 1 0 0 1 x 3 x 3 1 2 1
1 1 0 1 1 1 1 1 1 0 0 0 0 0 1 x 1 1 1 2 1 3 x 3 x 2 x
x 2 1 1 0 0 0 0 0 0 1 1 1 0 1 1 1 1 x 1 0 2 2 3 1 3 2
1 2 x 1 0 0 0 0 0 0 1 x 1 0 0 0 0 1 1 1 0 1 x 2 1 2 x
0 1 1 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 1 2 3 x 2 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 x 2 1 0"""


# task = '''0 0 0 0 ? ? ? ? ? ?
# 0 0 0 ? ? ? ? ? ? ?
# 0 ? ? ? ? ? ? ? ? ?
# ? ? ? ? ? ? ? ? ? 0
# ? ? ? ? 0 0 0 0 0 0
# ? ? ? 0 0 0 0 0 0 0'''


# original = '''0 0 0 0 1 1 1 1 1 1
# 0 0 0 1 2 x 2 2 x 1
# 0 1 1 2 x 2 2 x 2 1
# 1 2 x 2 1 1 1 1 1 0
# 1 x 2 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0 0'''

new = []
for i in original:
    if i.isalnum():
        new.append(i)
original = ''.join(new)

expected = '''0 0 0 0 1 1 1 1 1 1
0 0 0 1 2 x 2 2 x 1
0 1 1 2 x 2 2 x 2 1
1 2 x 2 1 1 1 1 1 0
1 x 2 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0'''

mines = 6


def open(x, y):
    return (original[x*27 + y])


solution = solve_mine(task, 16)
print(solution)
