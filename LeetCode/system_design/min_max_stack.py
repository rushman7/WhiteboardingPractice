class MinMaxStack:
  def __init__(self):
      self.stack = []
      self.minMaxStack = []
      
  def peek(self):
      return self.stack[-1]

  def pop(self):
    self.minMaxStack.pop()
    return self.stack.pop()

  def push(self, number):
      self.stack.append(number)
      stack_min = min(self.minMaxStack[-1][0], number) if self.minMaxStack else number
      stack_max = max(self.minMaxStack[-1][1], number) if self.minMaxStack else number
      self.minMaxStack.append((stack_min, stack_max))

  def getMin(self):
      return self.minMaxStack[-1][0]

  def getMax(self):
      return self.minMaxStack[-1][1]