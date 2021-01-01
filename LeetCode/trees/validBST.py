def isValidBST(self, root: TreeNode, min=None, max=None) -> bool:
    if not root:
        return True
    if (min != None and root.val <= min) or (max != None and root.val >= max):
        return False
    
    return self.isValidBST(root.right, root.val, max) and self.isValidBST(root.left, min, root.val)