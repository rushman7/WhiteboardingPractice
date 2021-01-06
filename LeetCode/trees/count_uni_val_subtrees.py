# Given the root of a binary tree, return the number of uni-value subtrees.

# A uni-value subtree means all nodes of the subtree have the same value.

 

# Example 1:


# Input: root = [5,1,5,5,5,null,5]
# Output: 4
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [5,5,5,5,5,null,5]
# Output: 6

def countUnivalSubtrees(self, root: TreeNode) -> int:
    self.total = 0
    
    def dfs(node, val):
        if not node:
            return True

        if not all([dfs(node.left, node.val),dfs(node.right, node.val)]):
            return False
        
        self.total+=1
        
        return node.val == val
    
    dfs(root, 0)

    return self.total