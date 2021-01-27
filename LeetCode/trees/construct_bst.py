class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
      if value < self.value:
        if self.left:
          self.left.insert(value)
        else:
          self.left = BST(value)
      else:
        if self.right:
          self.right.insert(value)
        else:
          self.right = BST(value)
          return self

    def contains(self, value):
        if value < self.value:
          if self.left:
            return self.left.contains(value)
          else:
            return False
        elif value > self.value:
          if self.right:
            return self.right.contains(value)
          else:
            return False
        else:
          return True

    def remove(self, value, parent=None):
        if value < self.value:
          if self.left:
            self.left.remove(value, self)
        elif value > self.value:
          if self.right:
            self.right.remove(value, self)
        else:
          if self.left and self.right:
            self.value = self.right.getMinValue()
            self.right.remove(self.value, self)
          elif not parent:
            if self.left:
              self.value = self.left.value
              self.right = self.left.right
              self.left = self.left.left
            elif self.right:
              self.value = self.right.value
              self.left = self.right.left
              self.right = self.right.right
          elif parent.left == self:
            parent.left = self.left if self.left else self.right
          elif parent.right == self:
            parent.right = self.left if self.left else self.right
        return self
	
    def getMinValue(self):
        if self.left:
          return self.left.getMinValue()
        else:
          return self.value