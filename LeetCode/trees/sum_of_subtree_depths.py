class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_subtree_depths(root):
  if not root:
    return 0
  
  if not root.left and not root.right:
    return 1
  
  L = sum_of_subtree_depths(root.left)
  R = sum_of_subtree_depths(root.right)


  return L + R


#       1/10
#      /   \
#     2/2  3/2
#    / \   / \
#   4   5 6   7    



#  / \  
# 8   9         




tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.left.left.left = TreeNode(8)
tree.left.left.right = TreeNode(9)
tree.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)

sum_of_subtree_depths(tree)


