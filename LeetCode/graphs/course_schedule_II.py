class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, result, queue = defaultdict(list), [], deque()
        indegree = [0 for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
            
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.appendleft(i)
        
        while queue:
            vertex = queue.pop()
            result.append(vertex)
            for nei in graph[vertex]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.appendleft(nei)
                    
        return result if len(result) == numCourses else []