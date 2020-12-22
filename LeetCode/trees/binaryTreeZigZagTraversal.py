# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root, ""]
        index = 0
        ans = [[]]
        direction = True
        
        while len(q) > 1:
            if direction:
                if q[0] == "":
                    index+=1
                    ans.append([])
                    direction = not direction
                else:
                    node = q.pop(0)
                    ans[index].append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            else:
                if q[-1] == "":
                    index+=1
                    ans.append([])
                    direction = not direction
                else:
                    node = q.pop()
                    ans[index].append(node.val)
                    if node.right:
                        q.insert(0, node.right)
                    if node.left:
                        q.insert(0, node.left)
        return ans