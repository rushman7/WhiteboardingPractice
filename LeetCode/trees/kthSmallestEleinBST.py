# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

def kthSmallest(self, root: TreeNode, k: int) -> int:
    if not root:
        return None
    ans = []
    heapq.heapify(ans)
    
    def dfs(node):
        if not node:
            return None
        heapq.heappush(ans, node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    
    return heapq.nsmallest(k, ans)[-1]