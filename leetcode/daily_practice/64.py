from math import inf
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(len(dp[0])):
            dp[0][i] = inf
        for i in range(len(dp)):
            dp[i][0] = inf
        dp[0][1] = 0
        

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
                     
        return dp[n][m]
        

s = Solution()

print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))