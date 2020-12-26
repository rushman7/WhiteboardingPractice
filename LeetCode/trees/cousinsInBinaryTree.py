# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:



# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        d = 0
        q = [root, d]
        while len(q) > 1:
            node = q.pop()
            if type(node) == int:
                d+=1
                q.insert(0, d)
            else:
                l = node.left
                r = node.right
                if l and r:
                    if (l.val == x and r.val == y) or (l.val == y and r.val == x):
                        return False
                if l:
                    q.insert(0, l)
                if r:
                    q.insert(0, r)
                if node.val == x:
                    x = d
                if node.val == y:
                    y = d
        return x == y
                    
            