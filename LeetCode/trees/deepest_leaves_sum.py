# Given a binary tree, return the sum of values of its deepest leaves.
 

# Example 1:



# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
 

# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.

def deepestLeavesSum(self, root: TreeNode) -> int:
        self.max_depth = 0
        hashMap = {}
        
        def dfs(node, depth):
            if not node:
                return None
            
            self.max_depth = max(self.max_depth, depth)
            if not node.left and not node.right:
                if depth in hashMap:
                    hashMap[depth] += node.val
                else:
                    hashMap[depth] = node.val
                
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)

        return hashMap[self.max_depth]