class Solution:
    def convertBST(self, root) -> TreeNode:
        def helper(node, tree_sum):
            if not node:
                return 0
            if node.right:
                tree_sum = helper(node.right, tree_sum)
            tree_sum += node.val
            node.val = tree_sum
            if node.left:
                tree_sum = helper(node.left, tree_sum)
            return tree_sum
        helper(root, 0)
        return root