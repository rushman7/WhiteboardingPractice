class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    ans = 0
    
    def dfs(node):
      if not node:
        return 0
      
      L = dfs(node.left)
      R = dfs(node.right)
      nonlocal ans
      ans = max(ans, L+R)
      return 1 + max(L, R)
    
    dfs(tree)
    return ans