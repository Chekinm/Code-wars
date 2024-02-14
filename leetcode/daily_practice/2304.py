class Solution:
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * (n) for i in range(m)]
        dp[0] = [grid[0][i] for i in range(n)]

        for i in range(1, m):
            for j in range(n):
                variants = [dp[i-1][k] + moveCost[grid[i-1][k]][j] for k in range(n)] 
                dp[i][j] = grid[i][j] + min(variants)

        return min(dp[m-1])
    
s = Solution()

print(s.minPathCost([[5,3],[4,0],[2,1]], [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]))