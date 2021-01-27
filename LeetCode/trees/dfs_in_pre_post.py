def inOrderTraverse(tree, array):
    ans = []
    def dfs(node):
      if not node:
        return None
      dfs(node.left)
      ans.append(node.value)
      dfs(node.right)
      
      dfs(tree)
    return ans


def preOrderTraverse(tree, array):
    ans = []
    def dfs(node):
      if not node:
        return None
      ans.append(node.value)
      dfs(node.left)
      dfs(node.right)
      
      dfs(tree)
    return ans


def postOrderTraverse(tree, array):
    ans = []
    def dfs(node):
      if not node:
        return None
      dfs(node.left)
      dfs(node.right)
      ans.append(node.value)
      
      dfs(tree)
    return ans
