# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

def flatten(self, root: TreeNode) -> None:
    if not root:
        return None
    
    L = self.flatten(root.left)
    R = self.flatten(root.right)
    
    if L:
        root.right = L
        while L.right:
            L = L.right
        L.right = R
        root.left = None

    return root