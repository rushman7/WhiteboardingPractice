class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited, result = set(), 0
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(vertex):
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            
        for vertex in range(n):
            if vertex not in visited:
                dfs(vertex)
                result+=1
                
        return result