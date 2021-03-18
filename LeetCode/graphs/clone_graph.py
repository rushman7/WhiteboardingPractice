"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hash_map={}
        
        def dfs(node):
            if not node:
                return None
            if node.val in hash_map:
                return hash_map[node.val]

            new_node = Node(node.val)
            hash_map[new_node.val] = new_node

            new_node.neighbors = [dfs(nei) for nei in node.neighbors]

            return new_node
    
        return dfs(node)