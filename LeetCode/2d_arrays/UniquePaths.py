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
