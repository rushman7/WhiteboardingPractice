class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        hash_map = {k:i for i, k in enumerate(inorder)}
        preIdx = 0
        
        def helper(left_bound, right_bound):
            if right_bound < left_bound:
                return None
            
            nonlocal preIdx
            result = TreeNode(preorder[preIdx])
            inIdx = hash_map[preorder[preIdx]]
            preIdx+=1
            
            if left_bound == right_bound:
                return result
            
            result.left = helper(left_bound, inIdx-1)
            result.right = helper(inIdx+1, right_bound)
            
            return result
        
        return helper(0, len(preorder)-1)