# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

def numIslands(self, grid: List[List[str]]) -> int:
    total_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                total_islands+=1
                self.deleteIsland(i, j, grid)
    
    return total_islands

def deleteIsland(self, i, j, grid):
    grid[i][j] = '0'
    
    # check top
    if i > 0 and grid[i-1][j] == '1':
        self.deleteIsland(i-1, j, grid)
    # check bot
    if i < len(grid)-1 and grid[i+1][j] == '1':
        self.deleteIsland(i+1, j, grid)
    # check left
    if j > 0 and grid[i][j-1] == '1':
        self.deleteIsland(i, j-1, grid)
    # check right
    if j < len(grid[i])-1 and grid[i][j+1] == '1':
        self.deleteIsland(i, j+1, grid)