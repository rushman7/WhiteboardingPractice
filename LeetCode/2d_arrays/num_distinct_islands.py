class Solution:
    def numDistinctIslands(self, grid):
        n, m = len(grid), len(grid[0])
        result = 0
        islands = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island = []
                    self.dfs(grid, i, j, island)
                    islands.append(island)
        for i in range(len(islands)):
            distinct = True
            for j in range(i+1, len(islands)):
                if len(islands[i]) == len(islands[j]):
                    x,y = abs(islands[i][0][0]-islands[j][0][0]), abs(islands[i][0][1]-islands[j][0][1])
                    for k in range(len(islands[j])):
                        if abs(islands[i][k][0]-islands[j][k][0]) != x or abs(islands[i][k][1]-islands[j][k][1]) != y:
                            break
                        if k == len(islands[j])-1:
                            distinct = False
            if distinct:
                result+=1
        
        return result

    def dfs(self, grid, i, j, island):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        
        grid[i][j] = 0
        island.append((i, j))
        
        self.dfs(grid, i-1, j, island)
        self.dfs(grid, i, j+1, island)
        self.dfs(grid, i+1, j, island)
        self.dfs(grid, i, j-1, island)

'''
Optimized solution:

class Solution:
    def numDistinctIslands(self, grid):
        n, m = len(grid), len(grid[0])
        islands = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island = []
                    self.dfs(grid, i, j, island, 'O')
                    islands.add("".join(island))

        return len(islands)

    def dfs(self, grid, i, j, island, direction):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        
        grid[i][j] = 0
        island.append(direction)
        
        self.dfs(grid, i-1, j, island, 'U')
        self.dfs(grid, i, j+1, island, 'R')
        self.dfs(grid, i+1, j, island, 'D')
        self.dfs(grid, i, j-1, island, 'L')
        island.append(direction)


'''