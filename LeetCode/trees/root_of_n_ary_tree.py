# You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

# Return the root of the N-ary tree.

# Custom testing:

# An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the null value (see examples).



# For example, the above tree is serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

# The testing will be done in the following way:

# The input data should be provided as a serialization of the tree.
# The driver code will construct the tree from the serialized input data and put each Node object into an array in an arbitrary order.
# The driver code will pass the array to findRoot, and your function should find and return the root Node object in the array.
# The driver code will take the returned Node object and serialize it. If the serialized value and the input data are the same, the test passes.

def findRoot(self, tree: List['Node']) -> 'Node':
    if len(tree) <= 1:
        return tree[0]
    
    g = {}
    visited = set()
    self.root_val = None
    for node in tree:
        for child in node.children:
            if child not in g:
                g[child] = set()
            g[child].add(node)
            
    def dfs(vertex):
        if vertex not in g:
            self.root_val = vertex
            return vertex
        
        visited.add(vertex)
        for neighbor in g[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
                
    dfs(tree[0])
    return self.root_val