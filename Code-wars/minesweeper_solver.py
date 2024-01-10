from itertools import combinations

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


class Map:
    """all magic will occur inside the class map
    finnaly solution is not as clean as I supposed in the begining
    but it works, and no more ofre left to refactor may be later:)
    enjoy"""

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

        return list(to_check), list(to_check_surr_only)

    def check_consistency(self, unresolved):

        to_check, to_check_boarder_only = self.localize_problem_region(unresolved)

        for x, y, value in to_check:
            if isinstance(value, int) or value.isdigit():  
                # ok we have number here, let collect some 
                # information about surrounding
                value = int(value)
                mines = self.count_surrounding(x, y)[0]
                if mines != value:
                    return False
            elif value == '?':
                mines = self.count_surrounding(x, y)[0]
                if mines == 0:
                    return False

        return True

    def quantum_logic(self, border):
        """pure magic occures here
        we build spaces of probablilites, and try to find
        mines regions that non intersect"""
        quantum_mines_space = {}

        for x, y, value in border:
            if isinstance(value, int) or value.isdigit():
                (mines_coord,
                 quests_coord,
                 opens_coord) = self.count_quantum_surrounding(x, y)
                quests_coord = frozenset(quests_coord)
                left_mines = int(value) - len(mines_coord)
                quantum_mines_space[quests_coord] = left_mines

        sorted_regions = list(quantum_mines_space.keys())
        sorted_regions.sort(key=lambda x: len(x)/quantum_mines_space[x])
        localized_mines_regions = []
        if quantum_mines_space:
            localized_mines_regions.append(sorted_regions[0])

        i = 0
        while i < len(sorted_regions):
            if not any(bool(sorted_regions[i].intersection(st))
                       for st in localized_mines_regions):
                localized_mines_regions.append(sorted_regions[i])
            i += 1

        return ({region: quantum_mines_space[region]
                 for region in localized_mines_regions},
                quantum_mines_space,
                )

    def perform_quantum_magic(self):
        """something magic, reach me in lnkdin if you are interestined and need some explanation"""
        unresolved = self.get_unresolved()

        to_check, to_check_boarder_only = self.localize_problem_region(unresolved)

        non_intersect_regions, full_regions_dict = self.quantum_logic(to_check_boarder_only)

        non_intersect_regions_list = list(non_intersect_regions.keys())
        mines_in_nonintersect = sum(non_intersect_regions.values())
        
        fields_in_nonintersect = 0
        for s in non_intersect_regions_list:
            fields_in_nonintersect += len(s)

        if mines_in_nonintersect > self.mines:
            # defenetly not enough mines to fulfill all places
            print(f'{self.mines=},places={mines_in_nonintersect=}')
            return '?'
        
        elif mines_in_nonintersect < self.mines:
               
            print(f'quantum magic can\'t help, sorry too many mines {mines_in_nonintersect=}, {self.mines=}')
            print('will call another quntum magic trick')

            self.perform_another_quantum_magic(to_check_boarder_only,
                                               full_regions_dict,
                                               non_intersect_regions,
                                               )
            return

        elif mines_in_nonintersect == self.mines and len(unresolved) == fields_in_nonintersect:
            
            self.perform_another_quantum_magic(to_check_boarder_only,
                                               full_regions_dict,
                                               non_intersect_regions,
                                               )      
            return

        # number of places exactly equal to the
        # number of mines => we can open some fileds
        # lets do that
        dangerous = non_intersect_regions_list[0].union(*non_intersect_regions_list)
        non_dangerous = list(set(unresolved) - dangerous)

        for x, y in non_dangerous:
            self.set_field(x, y, str(open(x, y)))
        return True

    def perform_another_quantum_magic(self, border, full_regions_dict, non_intersect_regions):
        
        for x, y, value in border:
            #  find numbers in bordres
            if isinstance(value, int) or value.isdigit():

            #  2 collect all data
                (mines_coord,
                 quests_coord,
                 opens_coord) = self.count_quantum_surrounding(x, y)
                
                value = int(value)
                mines, quests, opens, total, surr = self.count_surrounding(x, y)

            # find if any of mines regions is the subset of quests_coords
                self.check_coords_aginst_dict(quests_coord,
                                              value - mines,
                                              full_regions_dict,
                                              )   

    def check_coords_aginst_dict(self,
                                 quests_coord,
                                 true_value,
                                 full_regions_dict,
                                 ):
        """find if any of mines regions is the subset of quests_coords
        check if we can do something more
        there is regression inside"""

        for mine_region, region_number_of_mines in full_regions_dict.items():
            if mine_region.issubset(quests_coord):
                diff = quests_coord - mine_region
                if len(diff):
                    if true_value - region_number_of_mines == 0:
                        for x1, y1 in diff:
                            print(f'magic works, found safe space at {x1}, {y1}')
                            self.set_field(x1, y1, str(open(x1, y1)))
                                    
                    elif len(diff) == true_value - region_number_of_mines:
                        for x1, y1 in diff:
                            print(f'magic works, found MINE at {x1}, {y1}')
                            self.set_field(x1, y1, 'x')
                            self.mines -= 1
                            
                    elif len(diff) > true_value - region_number_of_mines:
                        print(f'{diff=}, {true_value - region_number_of_mines=}')
                        self.check_coords_aginst_dict(
                                    diff,
                                    true_value - region_number_of_mines, 
                                    full_regions_dict,
                                    )
                
        
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
        # any other case,  not enough information, go backward, we reach leaf of our DFT
        return


def fight_with_problem_cells(m: Map):
    # most of the corner case will lead you here
    # like one cell, one mine etc
    
    # also brute fores algo performs here
    
    # let see what has left unresolved
    unresolved = m.get_unresolved()

    if len(unresolved) == m.mines:  # lucky we are, that is so simple
        for x, y in unresolved:
            m.set_field(x, y, 'x')
            m.mines -= 1
        return str(m)
    
    elif len(unresolved) == 2 or len(unresolved) > 20: # unlucky we are
        # 2 - means there are alwayes two solutions => unpredictable,
        # 20 means we are luck of resorcese, most probsably it is an efficency testcase,
        # which should return '?'
        # just drop it...
        return '?'

    else:
        # finnaly, looks like we only have less than 20 fileds.
        # think we can brute force it.
        # will check all combination of mines 
        
        variants = combinations(unresolved, m.mines)
        print(f'we have {len(unresolved)} cells with {m.mines} mines')

        valid_solutions = []
        possible_valid_mines = set()
        for variant in variants:
            # we will use temporary copy of the map, not to clean it up
            try_map = m.copy()

            for x, y in variant:
                try_map.set_field(x, y, 'x')
                try_map.mines -= 1

            if try_map.check_consistency(unresolved): 
                # found valid solution
                # save it
                valid_solutions.append(variant)
                possible_valid_mines.update(variant)

        if len(valid_solutions) == 0 or len(unresolved) == len(possible_valid_mines):
            # no valid solution,
            # or mines can be in every possible field in unresolved
            return '?'

        elif len(valid_solutions) == 1:
            # only one solution, great! we found it
            # lets return it
            for x, y in valid_solutions[0]:
                m.set_field(x, y, 'x')
                m.mines -= 1
            return str(map)

        elif len(valid_solutions) > 1:
            # well there are some place, in unresolved which can't hold the mine
            # we know as by task descritpion all zeros are already open
            # and we check it
            # so open all safe places and go back for anther round
            for x, y in unresolved:
                if (x, y) not in possible_valid_mines:
                    m.set_field(x, y, str(open(x, y)))
            return

        
def solve_mine(map, n):

    m = Map(map, n)
    # two trivial case
    if len(map) == 1:
        return str('x' if n else 0)

    while m.mines:  # until we have undiscovered mines

        str_m_old = str(m)  # will check dead loop with this 
                            # as we have three method we cannot do it in while above
    
        # first - simple regression logic, for simple problem
        for x in range(m.len_x):
            for y in range(m.len_y):
                m.open_around_field(x, y)
            
        if str(m) == str_m_old:  
            # we got stacked, no new moves was done using 
            # simple logic
            # hope it is not a lot of cell to resolve.
            # lets try to do something with it
            # firstly try some quantum magic

            print(f'==========before quantum=={m.mines=}=========')
            print(m)
            print('==========before quantum===========')
            m.perform_quantum_magic()

            if str(m) == str_m_old:  
                # looks like even quantum magic does't work, 
                # lets do smart brute force:)
                print(f'********before brute force=={m.mines=}********')
                print(m)
                print('********before bruteforce********')
                
                bf = fight_with_problem_cells(m)
                # fight_with_problem_cells return '?' if unresolvabel,
                # or do changes in map (m) in-place, so we will go futher
                if bf == '?':
                    # give up :(
                    return '?'
        else:
            str_m_old = str(m)
    else:
        # WOW, congrats! - we found all mines. 
        # Just need to do final cleaning, open the rest of the filed, as it is safe now.
        m.open_rest_of_the_solved()

    return str(m)


tests = []
tests.append((
"""1 x 1 0 1 1 1 0 1 x 2 x 1 0 0 0 1 x 1 0 0 0 0 0 0 1 1 1 0 0
1 1 1 0 1 x 2 2 3 2 2 1 1 0 0 0 1 1 2 1 1 0 0 0 0 1 x 1 0 0
0 0 0 1 2 2 2 x x 2 1 1 0 0 0 0 0 0 1 x 1 0 0 0 0 1 2 2 1 0
1 1 1 1 x 1 1 2 2 2 x 1 1 1 1 0 0 0 1 1 1 0 0 0 0 0 2 x 2 0
2 x 1 1 1 1 1 1 1 1 1 1 1 x 2 1 0 0 0 1 1 1 0 0 0 0 2 x 2 0
x 2 1 0 0 0 1 x 1 0 0 0 2 3 x 1 0 0 0 1 x 1 0 0 0 0 1 1 1 0
1 1 0 0 0 0 2 2 2 0 0 0 1 x 2 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0
0 0 0 0 0 0 1 x 1 0 0 0 2 2 2 0 1 1 1 0 0 0 1 1 1 1 x 1 0 0
0 0 0 0 1 1 2 1 1 0 0 0 1 x 1 0 1 x 1 1 1 2 2 x 1 1 1 1 0 0
0 0 0 0 1 x 1 0 0 0 0 0 1 1 1 0 2 2 2 2 x 3 x 2 1 0 0 0 1 1
0 0 0 0 1 1 1 0 0 0 0 1 1 1 0 0 1 x 1 2 x 4 2 2 0 1 1 1 1 x
0 1 1 1 0 0 0 0 0 0 0 1 x 1 0 0 1 2 2 2 1 2 x 1 0 1 x 1 1 1
0 1 x 2 1 2 1 1 0 0 0 1 1 1 0 0 0 1 x 1 0 1 2 2 1 1 1 1 0 0
0 1 1 2 x 2 x 3 2 1 0 1 2 2 1 0 0 1 2 2 1 0 1 x 1 0 0 0 0 0
1 1 0 1 1 2 2 x x 1 0 1 x x 1 0 0 0 1 x 1 0 1 2 2 1 0 0 0 0
x 1 0 0 0 0 2 3 3 1 0 1 2 2 1 0 0 0 1 1 1 0 0 2 x 2 0 0 0 0
1 1 0 0 0 0 1 x 1 0 0 0 0 1 1 1 0 0 0 0 0 0 0 2 x 3 1 0 0 0
0 0 0 0 0 0 1 1 1 0 0 0 0 1 x 1 0 0 0 1 1 1 0 1 2 x 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 2 x 2 0 1 2 2 1 0 0 0
1 2 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 x 2 0 1 x 1 0 1 1 1
1 x x 1 1 1 1 0 1 1 1 0 0 1 1 2 1 1 0 1 1 1 1 2 2 1 0 1 x 1
1 2 3 2 2 x 1 0 1 x 2 1 0 1 x 3 x 2 0 0 0 0 1 x 1 0 0 1 1 1
0 0 1 x 3 2 2 0 1 2 x 1 1 2 2 3 x 3 1 0 0 0 1 1 1 0 0 0 0 0
0 0 1 1 2 x 1 0 0 1 1 2 2 x 2 2 2 x 2 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 1 x 4 x 1 1 1 2 x 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 2 2 x 2 1 0 0 1 1 1 1 x 2 1 1 0 0 0 0
0 0 0 0 0 1 1 2 1 2 x 1 1 1 1 0 0 1 2 2 1 1 1 2 x 2 1 1 1 1
0 0 0 0 0 1 x 4 x 4 2 1 0 0 0 0 0 2 x x 2 2 2 2 3 x 2 1 x 1
0 0 0 0 0 1 2 x x x 1 0 0 0 0 0 0 2 x 3 2 x x 1 2 x 2 1 1 1""",
"""? ? ? 0 ? ? ? 0 ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? 0 0
? ? ? 0 ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0
0 0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? 0
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? 0 0
0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 ? ? ? ? ? ? 0 0
0 0 0 0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0
0 0 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? ? ? 0 0 0 ? ?
0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 ? ? ? ? ?
0 ? ? ? 0 0 0 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 ? ? ? ? ?
0 ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? 0 0
0 ? ? ? ? ? ? ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? 0 ? ? ? 0 0 0 0 0
? ? 0 ? ? ? ? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0 0
? ? 0 0 0 0 ? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0
? ? 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0
? ? ? ? 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? 0 ? ? ?
? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ? 0 ? ? ?
? ? ? ? ? ? ? 0 ? ? ? ? 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0 ? ? ?
0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0
0 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0
0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 0 0 0
0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?""",
87))

tests.append(("""0 0 0 0 0 0 0 1 1 1
1 1 1 1 1 1 0 2 x 2
1 x 2 2 x 1 0 2 x 2
1 1 2 x 2 1 0 1 1 1
0 0 2 2 2 1 1 1 0 0
0 0 1 x 1 1 x 2 1 1
0 0 1 1 2 2 2 3 x 2
0 0 0 0 1 x 1 2 x 2
0 0 0 0 1 1 1 1 1 1
0 0 0 1 2 2 1 0 0 0
0 0 0 1 x x 1 0 0 0
0 0 0 1 2 2 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 1 0 1 1 1 0 0 0 0
x 1 0 1 x 1 0 0 0 0
2 3 1 3 2 2 1 1 1 0
x 2 x 2 x 1 1 x 2 1
1 2 1 2 1 1 1 2 x 1
0 0 1 1 1 0 0 1 1 1
0 0 1 x 1 1 1 2 2 2
0 0 1 1 1 1 x 2 x x
0 0 0 0 0 1 1 2 2 2""",
"""0 0 0 0 0 0 0 ? ? ?
? ? ? ? ? ? 0 ? ? ?
? ? ? ? ? ? 0 ? ? ?
? ? ? ? ? ? 0 ? ? ?
0 0 ? ? ? ? ? ? 0 0
0 0 ? ? ? ? ? ? ? ?
0 0 ? ? ? ? ? ? ? ?
0 0 0 0 ? ? ? ? ? ?
0 0 0 0 ? ? ? ? ? ?
0 0 0 ? ? ? ? 0 0 0
0 0 0 ? ? ? ? 0 0 0
0 0 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
? ? 0 ? ? ? 0 0 0 0
? ? 0 ? ? ? 0 0 0 0
? ? ? ? ? ? ? ? ? 0
? ? ? ? ? ? ? ? ? ?
? ? ? ? ? ? ? ? ? ?
0 0 ? ? ? 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? ?
0 0 ? ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? ? ?""",
23))

tests.append((
"""2 x 1 0 0 0 0 0 0 0 0 1 x 1 0 0 0 0 0 0 1 1 1 1 x 1
1 x 2 1 0 0 0 0 0 0 0 0 1 1 1 0 0 0 1 1 1 1 x 1 1 1 1
1 2 2 1 0 0 1 1 1 0 0 0 0 0 0 0 0 0 1 x 2 2 1 1 0 0 0
0 1 x 2 1 2 2 x 2 1 0 0 0 0 0 0 0 0 1 3 x 3 1 1 0 0 0
0 1 1 2 x 2 x 3 x 1 0 0 0 0 0 0 0 0 0 2 x 3 x 1 0 0 0""",
"""? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ?
? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? ? ? ? ? ?
? ? ? ? 0 0 ? ? ? 0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0 0 0
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0 0 0
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0 ? ? ? ? ? 0 0 0""",
14,
))

tests.append((
"""0 0 0 0
0 0 1 1
0 0 1 x
0 0 1 1
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1 0
1 x 1 0
1 1 1 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 1 1
0 1 2 x
0 1 x 2
1 2 1 1
x 2 1 1
x 2 1 x
1 2 2 2
0 1 x 1""",
"""0 0 0 0
0 0 ? ?
0 0 ? ?
0 0 ? ?
0 0 0 0
0 0 0 0
0 0 0 0
? ? ? 0
? ? ? 0
? ? ? 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 ? ?
0 ? ? ?
0 ? ? ?
? ? ? ?
? ? ? ?
? ? ? ?
? ? ? ?
0 ? ? ?""",
8))

tests.append((
"""1 2 2 x 1 0 0 0
x 2 x 2 1 0 0 0
2 3 3 2 1 0 0 0
1 x 3 x 3 1 0 0
1 1 3 x x 1 0 0
0 0 1 2 2 1 0 0
1 1 1 0 0 0 0 0
1 x 1 0 0 0 0 0
1 1 1 0 0 0 0 0
0 0 0 0 1 1 2 1
0 0 0 0 1 x 3 x
1 1 1 0 1 2 x 2
1 x 1 0 0 1 1 1
1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0
1 x 1 0 0 0 0 0
1 1 1 0 0 0 0 0
1 1 0 0 0 0 0 0
x 1 0 0 0 0 0 0
1 1 1 1 2 2 2 1
0 0 2 x 4 x x 2
0 0 3 x 5 x 5 x
0 0 2 x 3 1 3 x
0 0 1 1 1 0 1 1""",
"""? ? ? ? ? 0 0 0
? ? ? ? ? 0 0 0
? ? ? ? ? 0 0 0
? ? ? ? ? ? 0 0
? ? ? ? ? ? 0 0
0 0 ? ? ? ? 0 0
? ? ? 0 0 0 0 0
? ? ? 0 0 0 0 0
? ? ? 0 0 0 0 0
0 0 0 0 ? ? ? ?
0 0 0 0 ? ? ? ?
? ? ? 0 ? ? ? ?
? ? ? 0 0 ? ? ?
? ? ? 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
? ? ? 0 0 0 0 0
? ? ? 0 0 0 0 0
? ? ? 0 0 0 0 0
? ? 0 0 0 0 0 0
? ? 0 0 0 0 0 0
? ? ? ? ? ? ? ?
0 0 ? ? ? ? ? ?
0 0 ? ? ? ? ? ?
0 0 ? ? ? ? ? ?
0 0 ? ? ? 0 ? ?""",
22))

tests.append((
"""0 2 x 3 1 1 0 1 1 2 x 2 x 1 0 0 0 0 0 0 1 1 2 2 2 1
1 3 x 3 x 1 0 1 x 2 1 2 1 2 1 1 0 0 0 0 1 x 2 x x 1
1 x 2 3 2 3 1 3 2 2 0 0 1 2 x 1 0 0 0 0 1 1 2 2 2 1
1 2 2 2 x 2 x 2 x 1 0 0 1 x 2 1 0 0 0 0 0 0 0 1 1 1
1 3 x 3 1 2 1 2 1 1 0 0 1 1 1 0 0 0 0 0 0 0 1 2 x 1
1 x x 2 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 x 2 1
1 2 2 2 1 2 x 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 x 2 1 0
1 1 0 1 x 3 3 2 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0
x 1 0 1 2 x 2 x 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0
2 2 1 1 2 2 2 1 1 1 2 2 2 1 1 1 x 1 1 1 1 0 0 0 0 0
1 x 1 1 x 1 0 0 0 1 x x 2 x 1 1 1 1 1 x 1 1 2 2 1 0
1 1 1 1 1 1 0 0 0 1 2 2 2 1 1 0 0 1 2 2 1 1 x x 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 2 2 x 2 1 2 2 2 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 x 3 x 3 3 x 1 0 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 x 3 2 x 3 2 2 1 2 x 1
0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 1 1 1 2 x 1 1 x 3 2 2
0 0 0 0 0 0 0 0 0 0 1 x 2 1 1 0 0 0 1 1 1 1 2 4 x 2
0 0 0 0 0 0 0 0 0 0 1 1 2 x 1 0 0 0 0 0 0 0 1 x x 3
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 1 1 1 0 2 4 x 2
0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 1 1 0 1 x 2 1 2 x 2 1
0 0 0 0 0 0 0 1 1 1 1 x 1 0 1 x 1 0 1 1 2 x 2 1 1 0
0 0 0 0 0 0 0 2 x 2 1 1 1 1 2 2 1 0 0 0 1 1 2 1 1 0
0 0 0 0 1 1 1 2 x 2 1 1 1 1 x 1 0 0 0 1 1 1 1 x 1 0
0 0 0 0 1 x 1 1 1 1 1 x 1 1 1 1 0 0 0 1 x 1 1 1 1 0""",
"""0 ? ? ? ? ? 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ?
? ? ? ? ? ? 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ? ? ?
? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? 0 0 0 0 ? ? ? ? ? ?
? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? 0 0 0 0 0 0 0 ? ? ?
? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? 0 0 0 0 0 0 0 ? ? ? ?
? ? ? ? 0 ? ? ? 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? ?
? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? 0
? ? 0 ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0
? ? 0 ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 0
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0
? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0
? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ? ? 0 ? ? ?
0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ?
0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? ?
0 0 0 0 0 0 0 0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ?
0 0 0 0 0 0 0 0 0 0 ? ? ? ? ? 0 0 0 0 0 0 0 ? ? ? ?
0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ?
0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? 0 ? ? ? ? ? ? ? ?
0 0 0 0 0 0 0 ? ? ? ? ? ? 0 ? ? ? 0 ? ? ? ? ? ? ? 0
0 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? 0
0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? 0
0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? 0""",
62))

for original, task, mines in tests:
    width = len(original.split('\n')[0].replace(' ',''))

    new = []
    for i in original:
        if i.isalnum():
            new.append(i)
    original = ''.join(new)

    def open(x, y):
        
        return (original[x*width + y])

    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    solution = solve_mine(task, mines)
    print(solution)
    print('++++++++++++++++++++++++++++++++++++++++++++++++')