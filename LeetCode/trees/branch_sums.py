# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#O(N) time, O(M) space, M being max depth of a tree for recursive call stack or total amount of leaf nodes.
def branchSums(root):
    # Write your code here.
    ans = []
    
    def dfs(node, curr_sum=0):
      if not node:
        return 0
      curr_sum+=node.value
      
      if not node.left and not node.right:
        ans.append(curr_sum)
        return
      
      dfs(node.left, curr_sum)
      dfs(node.right, curr_sum)
    
    dfs(root)
    
    return ans