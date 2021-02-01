def riverSizes(matrix):
	res = []
	
	def dfs(i, j):
		if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) or matrix[i][j] == 0:
			return 0
		matrix[i][j] = 0
		return 1 + dfs(i-1, j) + dfs(i, j+1) + dfs(i+1,j) + dfs(i, j-1)

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == 1:
				size = dfs(i, j)
				res.append(size)
	
	return res
