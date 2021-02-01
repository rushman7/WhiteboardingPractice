def removeIslands(matrix):
    W = len(matrix[0])
    H = len(matrix)
    seen = [[False for _ in range(W)] for _ in range(H)]
    
    def dfs(i, j, to_delete):
      if matrix[i][j] == 0 or seen[i][j]:
        return True
      if i == 0 or j == 0 or i == H-1 or j == W-1: 
        return False
      seen[i][j] = True
      to_delete.add((i,j))

      return dfs(i-1, j, to_delete) and dfs(i+1, j, to_delete) and dfs(i, j+1, to_delete) and dfs(i, j-1, to_delete)

    for i in range(1, H-1):
      for j in range(1, W-1):
        if matrix[i][j] == 1:
          to_delete = set()
          can_delete = dfs(i, j, to_delete)
          if can_delete:
            for i, j in to_delete:
              matrix[i][j] = 0
    return matrix