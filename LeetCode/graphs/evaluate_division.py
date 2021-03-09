class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        result = []
        for i, vals in enumerate(equations): # time: O(N) space: O(N)
            graph[vals[0]].append((vals[1], values[i]))
            graph[vals[1]].append((vals[0], 1/values[i]))

        def dfs(vertex, curr_val, target, visited):
            if vertex == target:
                if vertex in graph:
                    result.append(curr_val)
                else:
                    result.append(-1.00000)
                return True
            for v, val in graph[vertex]:
                if v not in visited:
                    visited[v] = 1
                    if dfs(v, curr_val * val, target, visited):
                        return True
                    del visited[v]
                
            return False
        
        for v, n in queries: # time: O(M)
            if not dfs(v, 1, n, {v:1}): # time: O(N) space: O(N) - recursive call stack +  visited set O(N)
                result.append(-1.00000)
                
        return result