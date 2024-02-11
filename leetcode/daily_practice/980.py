class Solution:
    def __init__(self):
        self.variants = 0
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        
        def _bt(x, y, steps):
            for row in grid:
                print(row)
            print()
            if  x < 0 or x > n - 1 or y < 0 or y > m - 1 or grid[x][y] < 0:
                return 
            
            if grid[x][y] == 2:
                if steps == 1:
                    self.variants += 1
                    return 
                return 
            
            cell_val_backup = grid[x][y]
            grid[x][y] = -1
            steps -= 1
            _bt(x+1, y, steps)
            _bt(x-1, y, steps)
            _bt(x, y+1, steps)
            _bt(x, y-1, steps)

            steps += 1
            grid[x][y] = cell_val_backup
            return

        
        n = len(grid)
        m = len(grid[0])
        steps = 0
        variants = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start_x = i
                    start_y = j
                if grid[i][j] >= 0:
                    steps += 1
        
        _bt(start_x, start_y, steps)

        return self.variants


s = Solution()

print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))