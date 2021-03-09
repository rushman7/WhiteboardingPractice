"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)-1
        result = self.same((0,0), (n,n), grid)
        return result if type(result) != bool else Node(1 if result else 0, 1)
    

    def same(self, s, e, grid):
        if s == e:
            return grid[e[0]][e[1]] == 1
        
        result = Node(1, 0)
        x = (s[0] + e[0]) // 2
        y = (s[1] + e[1]) // 2

        tl = self.same(s, (x, y), grid)
        tr = self.same((s[0], y+1), (x, e[1]), grid)
        bl = self.same((x+1, s[1]), (e[0], y), grid)
        br = self.same((x+1, y+1), e, grid)
        
        if tl == tr == bl == br:
            return tl
        else:
            result.topLeft = Node(1 if tl else 0, 1) if type(tl) == bool else tl
            result.topRight = Node(1 if tr else 0, 1) if type(tr) == bool else tr
            result.bottomLeft = Node(1 if bl else 0, 1) if type(bl) == bool else bl
            result.bottomRight = Node(1 if br else 0, 1) if type(br) == bool else br
        return result
