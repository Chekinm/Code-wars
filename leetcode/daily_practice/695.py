class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        islands = []

        def check_neighbors(x, y, island=None):
            if island == None:
                island = set() 
            island.add((x, y))
            seen.add((x, y))   
            for i in range(-1, 2, 2):
                if (0 <= x + i < m and 
                        grid[x + i][y] == 1 and 
                        (x+i, y) not in seen and 
                        (x+i, y) not in island):
                    check_neighbors(x+i, y, island)
                if (0 <= y + i < n and 
                        grid[x][y + i] == 1 and 
                        (x, y + i) not in seen and
                        (x, y + i) not in island):
                    check_neighbors(x, y + i, island) 
            return island

        for x in range(m):
            for y in range(n):
                if (x, y) not in seen and grid[x][y] == 1:
                    islands.append(check_neighbors(x, y))
        return max(islands, key=len)
    
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

grid = [[1,1]]

s = Solution()
print(s.maxAreaOfIsland(grid))
