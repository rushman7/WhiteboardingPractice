# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        prev = None
        curr = root
        
        while curr:
            if p.val >= curr.val:
                curr = curr.right
            else:
                prev = curr
                curr = curr.left
                
        return prev