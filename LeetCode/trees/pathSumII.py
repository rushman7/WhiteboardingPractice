# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def helper(node, total, curr):
            if not node:
                return 
            total+=node.val
            curr.append(node.val)
            if not node.left and not node.right and total == sum:
                ans.append(list(curr))
            else:
                helper(node.left, total, curr)
                helper(node.right, total, curr)
            curr.pop()
            
        ans = []
        helper(root, 0, [])
        return ans
