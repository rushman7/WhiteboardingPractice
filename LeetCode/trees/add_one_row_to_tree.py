class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # BFS Solution O(N) time O(H) space
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        
        curr = root
        queue = deque()
        queue.appendleft((curr, None, True, 1))
        
        while queue:
            node, parent, is_left, depth = queue.pop()
            if depth == d:
                new_node = TreeNode(v)
                if is_left:
                    new_node.left = node if parent.left else None
                    parent.left = new_node
                else:
                    new_node.right = node if parent.right else None
                    parent.right = new_node
            elif node:
                queue.appendleft((node.left, node, True, depth+1))
                queue.appendleft((node.right, node, False, depth+1))
        return root
# DFS Solution O(N) time O(N) space        
        
#         def dfs(node, parent, is_left, depth):
#             if depth == d:
#                 new_node = TreeNode(v)
#                 if is_left:
#                     new_node.left = node if parent.left else None
#                     parent.left = new_node
#                 else:
#                     new_node.right = node if parent.right else None
#                     parent.right = new_node
#                 return
#             if node:
#                 dfs(node.left, node, True, depth+1)
#                 dfs(node.right, node, False, depth+1)
            
        
#         dfs(root, None, True, 1)
#         return root
