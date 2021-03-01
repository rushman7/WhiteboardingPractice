class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, isLeft=False) -> int:
        if not root:
            return 0
        total = 0
        total += self.sumOfLeftLeaves(root.left, True)
        if isLeft and not root.right and not root.left:
            total += root.val
        else:
            total += self.sumOfLeftLeaves(root.right, False)
        return total