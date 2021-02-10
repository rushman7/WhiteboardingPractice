class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float('-inf')
        def helper(node):
            if not node:
                return
            
            left_path_max = helper(node.left) if node.left else float('-inf')
            right_path_max = helper(node.right) if node.right else float('-inf')
            
            temp_left = left_path_max if left_path_max > 0 else 0
            temp_right = right_path_max if right_path_max > 0 else 0
            
            nonlocal max_path
            max_path = max(max_path, temp_left + temp_right + node.val)
            max_of_both_paths = max(right_path_max, left_path_max)
            if max_of_both_paths < 0:
                max_of_both_paths = 0
                
            return max_of_both_paths + node.val
        
        helper(root)
        return max_path