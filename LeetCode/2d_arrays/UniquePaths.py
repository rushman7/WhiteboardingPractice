# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# Example 3:

# Input: m = 7, n = 3
# Output: 28
# Example 4:

# Input: m = 3, n = 3
# Output: 6

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(i,j):
            if i > m or j > n:
                return 0
            if i == m and j == n:
                return 1
        
            if (i,j) in cache:
                return cache[(i,j)]
        
            cache[(i,j)] = (dfs(i,j+1) or 0) + (dfs(i+1,j) or 0)
            return dfs(i,j+1) + dfs(i+1,j)
        dfs(1,1)
        return 1 if m == 1 and n == 1 else cache[(1,1)] 


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m= len(obstacleGrid[0]), len(obstacleGrid)
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        
        for i in range(m-1, -1, -1): 
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if obstacleGrid[i][j] == 0:
                    right = dp[i][j+1] if j+1 < n else 0
                    down = dp[i+1][j] if i+1 < m else 0
                    dp[i][j] = right + down
                    
        return dp[0][0]
