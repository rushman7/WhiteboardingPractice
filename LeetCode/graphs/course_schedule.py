class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        
        for preq in prerequisites:
            graph[preq[1]].append(preq[0])

        def dfs(course):
            visited[course] = 1
            for nei in graph[course]:
                if visited[nei] == 1:
                    return True
                if visited[nei] != 2 and dfs(nei):
                    return True
            visited[course] = 2
            return False

        for course in range(numCourses):
            if visited[course] == 0:
                if dfs(course):
                    return False
        
        return True
