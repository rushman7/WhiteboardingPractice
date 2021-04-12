class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        result = 1
        graph = defaultdict(set)
        indegree = defaultdict(int)
        directions = [(-1,0), (1,0), (0,-1), (0, 1)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                indegree[(i,j)]

                for x, y in directions:
                    if i+x < 0 or j+y < 0 or i+x > len(matrix)-1 or j+y > len(matrix[0])-1:
                        continue
                        
                    if matrix[i][j] > matrix[i+x][j+y]:
                        graph[(i+x,j+y)].add((i,j))
                        indegree[(i,j)]+=1

        queue = deque()
        
        for coord in graph:
            if indegree[coord] == 0:
                queue.append(coord)
                
        while queue:
            k = len(queue)
            while k:
                vertex = queue.popleft()
                for nei in graph[vertex]:
                    indegree[nei]-=1
                    
                    if indegree[nei] == 0:
                        queue.append(nei)
                k-=1
            if queue:
                result+=1
        return result
