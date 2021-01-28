class Node:
  def __init__(self, key):
      self.key = key
      self.left = None
      self.right = None
      self.parent = None

class BinarySearchTree:
  def __init__(self):
      self.root = None

  def find_largest_smaller_key_(self, node, num):
      if num <= node.key:
        if not node.left:
          return node.parent.key if node.parent and node.parent.key < num else -1

        return self.find_largest_smaller_key_(node.left, num)
      if num > node.key:
        if not node.right:
          return node.key

        return self.find_largest_smaller_key_(node.right, num) 
      
  def find_largest_smaller_key(self, num):
    return self.find_largest_smaller_key_(self.root, num)

  
  def insert(self, key):
      if (self.root is None):
          self.root = Node(key)
          return

      currentNode = self.root
      newNode = Node(key)

      while(currentNode is not None):
        if(key < currentNode.key):
          if(currentNode.left is None):
            currentNode.left = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.left
        else:
          if(currentNode.right is None):
            currentNode.right = newNode
            newNode.parent = currentNode
            break
          else:
            currentNode = currentNode.right


bst  = BinarySearchTree()
 
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14) 

result = bst.find_largest_smaller_key(17)

print ("Largest smaller number is %d " %(result))
