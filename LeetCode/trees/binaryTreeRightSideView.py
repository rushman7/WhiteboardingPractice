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
        if not root: 
            return None
        
        ans = []
        
        def dfs(node,i):
            if not node:
                return
            
            if i < len(ans):
                ans[i] = node.val
            else:
                ans.append(node.val)
            
            if node.left:
                dfs(node.left,i+1)
            if node.right:
                dfs(node.right,i+1)
                
        dfs(root,0)
        
        return ans