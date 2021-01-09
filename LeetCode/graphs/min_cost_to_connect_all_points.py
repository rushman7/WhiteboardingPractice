# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:



# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        L = len(points)
        edges = []
        for i in range(L):
            for j in range(i+1, L):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((w,i,j))
        edges.sort()

        roots = [i for i in range(L)]

        def find(v):
            if roots[v] != v:
                roots[v] = find(roots[v])
            return roots[v]
        
        def union(u,v):
            p1, p2 = find(u), find(v)
            if p1 != p2:
                roots[p2] = roots[p1]
                return True
            return False
        
        res = 0
        total = 0
        for d, u, v in edges:
            if union(u,v):
                res+=d
                total+=1
                if total == L-1:
                    break

        return res