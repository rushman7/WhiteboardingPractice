# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return root
        q = []
        q.insert(0, root)
        q.insert(0, "")
        ans = []
        while len(q) > 0:
            if len(q) == 1: 
                break
            node = q.pop()
            if node.left: 
                q.insert(0, node.left)
            if node.right: 
                q.insert(0, node.right)
            if q[-1] == "":
                ans.append(node.val)
                q.insert(0, q.pop())
        return ans