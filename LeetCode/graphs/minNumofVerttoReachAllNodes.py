# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.

 

# Example 1:



# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
# Example 2:



# Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
# Output: [0,2,3]
# Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.

# optimal solution:
def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    ans = set(range(n))
    for u,v in edges:
        if v in ans:
            ans.discard(v)
    return ans

# slow solution:
from collections import deque
def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    g = {}
    for u,v in edges:
        if u not in g:
            g[u] = set()
        g[u].add(v)
    q = deque()
    ans = set()
    visited = set()
    for v in range(n):
        if v not in visited:
            q.appendleft(v)
            ans.add(v)
        while len(q) > 0:
            v = q.pop()
            if v not in visited:
                visited.add(v)
                if v in g:
                    for neighbor in g[v]:
                        if neighbor in ans:
                            ans.remove(neighbor)
                        if neighbor not in visited:
                            q.appendleft(neighbor)
    return ans
                    