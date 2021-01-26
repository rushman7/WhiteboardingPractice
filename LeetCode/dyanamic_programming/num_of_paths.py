def num_of_paths_to_dest(n):
  memo = [[0 for _ in range(n)] for _ in range(n-1)] + [[1 for _ in range(n)]]

  for i in range(n-2, -1,-1):
    for j in range(i, -1,-1):
      memo[i][j] = memo[i+1][j] + memo[i][j+1]

  return memo[0][0]