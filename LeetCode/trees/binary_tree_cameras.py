class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        result = 0
        def DFS(node):
            nonlocal result
            if not node:
                return 0
            left = DFS(node.left)
            right = DFS(node.right)
            
            if left == 1 or right == 1:
                result += 1
                return 2
            if left == 2 or right == 2:
                return 0
            
            if node != root:
                return 1
            
            result += 1
        
        DFS(root)
        
        return result