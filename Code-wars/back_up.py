from preloaded import open

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
        
    def open_rest_of_the_solved(self):
        for x in range(self.len_x):
            for y in range(self.len_y):
                if self.get_field(x,y) == '?':
                    self.set_field(x, y, str(open(x,y)))

    def get_surrounding(self, x,y):
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
    
    
    def localize_problem_region(self, unresolved):
        to_check = set()
        for x, y in unresolved:
            for x1, y1, value in self.get_surrounding(x,y):
                to_check.add((x1, y1, value))
        #print( f'{unresolved=}\n surraunding ={list(to_check)}')
        return list(to_check)
    
    
    def check_consistency(self, unresolved):
        
        to_check = self.localize_problem_region(unresolved)
        
        for x, y, value in to_check:
            if type(value) == int or value.isdigit():  # ok we have number here, let collect some information about surrounding
                value = int(value)   
                mines, quests, opens, total, surr = self.count_surrounding(x,y)
                if mines != value:
                    return False
        return True


    def open_around_field(self, x, y):   
        """this finciton open solved cell using regression inside, kinda DTS"""
        
        value = self.get_field(x, y)

        if type(value) == int or value.isdigit():  # ok we have number here, let collect some information about surrounding

            value = int(value)   
            mines, quests, opens, total, surr = self.count_surrounding(x,y)
            
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
    unresolved = []
    for x in range(m.len_x):
        for y in range(m.len_y):
            if m.get_field(x,y) == '?':
                unresolved.append((x, y))

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
        print('='* 20)
        print(str(m))
        print('='* 20)
        
        valid_solutions = []
        for variant in variants:
            try_map = m.copy()

            for x, y  in variant:
                try_map.set_field(x, y, 'x')
                try_map.mines -= 1

            if try_map.check_consistency(unresolved): # found valid solution
                print('='* 20)
                print(try_map)
                print('='* 20)
                if valid_solutions: # more than one valid solutions, means uncertanaty
                    return '?'
                else:
                    valid_solutions.append(try_map)

        if valid_solutions: # wie have on good
            m = valid_solutions[0].copy()
            # open the rest cells using map method
            m.open_rest_of_the_solved()
            return str(m)
        else: # there is no one good solution
            return '?' 

    
def solve_mine(map, n):
    
     
    m = Map(map, n)
    
    # two trivial case
    if len(map) == 1:
        return str('x' if n else 0)
    
    
    while m.mines: # until we have undiscovered mines
        
        str_m_old = str(m) # will check dead loop with this 
        
        for x in range(m.len_x):
            for y in range(m.len_y):
                m.open_around_field(x,y)
                
                
        if str(m) == str_m_old:  # we got stacked, no new moves was done using simple logic
            #  hope it is not a lot of cell to resolve.
            # lets try to do something with it
            return fight_with_problem_cells(m)                 
        else:
            str_m_old = str(m)   
    
    else:
        # we found all mines, just need to open rest of the filed
        m.open_rest_of_the_solved()
        

    return str(m)