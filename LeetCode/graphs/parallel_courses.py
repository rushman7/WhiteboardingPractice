class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegree = [0 for _ in range(n)]
        graph = defaultdict(list)
        queue = deque()
        result, visited = 0, 0
        
        for a, b in relations:
            graph[a].append(b)
            indegree[b-1]+=1
            
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.appendleft(i+1)
        
        while queue:
            result+=1
            queue, visited = self.empty_queue(queue, visited, indegree, graph)

        return -1 if visited != n else result
    
    def empty_queue(self, queue, visited, indegree, graph):
        new_queue = deque()
        while queue:
            vertex = queue.pop()
            visited+=1
            for nei in graph[vertex]:
                indegree[nei-1]-=1

                if indegree[nei-1] == 0:
                    new_queue.appendleft(nei)
        return new_queue, visited