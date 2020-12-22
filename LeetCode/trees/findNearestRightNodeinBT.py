# Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.

 

# Example 1:



# Input: root = [1,2,3,null,4,5,6], u = 4
# Output: 5
# Explanation: The nearest node on the same level to the right of node 4 is node 5.
# Example 2:



# Input: root = [3,null,4,2], u = 2
# Output: null
# Explanation: There are no nodes to the right of 2.
# Example 3:

# Input: root = [1], u = 1
# Output: null

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if not root: return root
        queue = Queue(maxsize=0)
        queue.put(root)
        queue.put("")
        while queue.qsize() > 0:
            if queue.qsize() == 1: return None
            node = queue.get()
            if node == u:
                ans = queue.get()
                if ans == "": return None
                return ans
            if node == "": queue.put("")
            else:
                if node.left: queue.put(node.left)
                if node.right: queue.put(node.right)