class Solution1:      
    """backtracking solution"""
    def __init__(self):
        self.variants = 0

    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        def _bt(x, y):

            if x > n - 1 or y > m - 1 or obstacleGrid[x][y] == 1:
                return 
            if x == n - 1 and y == m - 1:
                self.variants += 1
                return
             
            _bt(x + 1, y)
            _bt(x, y + 1)

            return 



        _bt(0, 0)

        return self.variants


class Solution2:      
    """dp solution"""

    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0][1] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[n][m]
        


        return self.variants


s = Solution2()




print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))