# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
      ans = []
      def dfs(vert):
        if not vert:
          return None
        ans.append(vert.name)
        for nei in vert.children:
          dfs(nei)
      
      dfs(self)
      return ans
