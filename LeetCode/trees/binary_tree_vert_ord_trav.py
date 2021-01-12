# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples 1:

# Input: [3,9,20,null,null,15,7]

#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7 

# Output:

# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Examples 2:

# Input: [3,9,8,4,0,1,7]

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7 

# Output:

# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Examples 3:

# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2

# Output:

# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        hash_map = defaultdict(list)
        min_col, max_col = float('inf'), float('-inf')
        
        def dfs(node, col, depth):
            if not node:
                return None
            nonlocal min_col, max_col
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            hash_map[col].append((depth, node.val))
            dfs(node.left, col-1, depth+1)
            dfs(node.right, col+1, depth+1)

        dfs(root, 0, 0)
        res = []
        
        for n in range(min_col, max_col+1):
            ans = []
            hash_map[n].sort(key=lambda x: x[0])
            for d, v in hash_map[n]:
                ans.append(v)
            res.append(ans)
        
        return res