def cycleInGraph(edges):
	colors = [0 for _ in range(len(edges))]
	
	def dfs(vertex):
		colors[vertex] = 1
		for nei in edges[vertex]:
			if colors[nei] == 1:
				return True
			if colors[nei] != 2 and dfs(nei):
				return True
			
		colors[vertex] = 2
		return False
	
	for i in range(len(edges)):
		if dfs(i):
			return True
	return False