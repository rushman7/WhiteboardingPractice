# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    result = BST(preOrderTraversalValues[0])
	
    for val in range(1, len(preOrderTraversalValues)):
      curr = result
      while True:
        if curr.value <= preOrderTraversalValues[val]:
          if curr.right:
            curr = curr.right
          else:
            curr.right = BST(preOrderTraversalValues[val])
            break
        else:
          if curr.left:
            curr = curr.left
          else:
            curr.left = BST(preOrderTraversalValues[val])
            break
    return result
