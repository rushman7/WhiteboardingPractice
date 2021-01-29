class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        min_vert, max_vert = 0, 0
        hash_map = defaultdict(list)
        
        def dfs(node, x, y):
            if not node:
                return None
            nonlocal min_vert, max_vert
            
            min_vert = min(min_vert, x)
            max_vert = max(max_vert, x)
            hash_map[x].append((node.val, y))
            dfs(node.left, x-1, y-1)
            dfs(node.right, x+1, y-1)
        
        dfs(root, 0, 0)
        
        return self.build_result(min_vert, max_vert+1, hash_map)
    
    def build_result(self, min_vert, max_vert, hash_map):
        res = []
        for x in range(min_vert, max_vert):
            hash_map[x].sort(key=lambda x: (-x[1], x[0]))
            res.append([x[0] for x in hash_map[x]])
        return res