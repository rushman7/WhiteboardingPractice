class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[n-1][m-1] = 1

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                R = dp[i][j+1] if j+1 < m else 0
                D = dp[i+1][j] if i+1 < n else 0
                dp[i][j] += (R + D)
                
        return dp[0][0]