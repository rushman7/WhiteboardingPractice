# We are given a binary tree (with root node root), a target node, and an integer value K.

# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

# Output: [7,4,1]

# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.



# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
 

# Note:

# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        g = defaultdict(list)
        def dfs(node):
            if not node:
                return
            
            if node.left:
                g[node.val].append(node.left.val)
                g[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                g[node.val].append(node.right.val)
                g[node.right.val].append(node.val)
                dfs(node.right)
            
        dfs(root)
        
        q = deque([(target.val, 0)])
        ans = []
        seen = set()
        while q:
            node, d = q.popleft()
            seen.add(node)
            if d == K:
                ans.append(node)
                continue
            for nei in g[node]:
                if nei not in seen:
                    q.append((nei, d+1))
        
        return ans