class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.gen = self.flatten(nestedList)
        self.peek = None
           
    def next(self) -> int:
        if not self.hasNext(): 
            return None
        next_int, self.peek = self.peek, None
        return next_int
    
    def hasNext(self) -> bool:
        if self.peek is not None: return True
        try:
            self.peek = next(self.gen)
            return True
        except: 
            return False
    
    def flatten(self, nested_list):
        for nested in nested_list:
            if nested.isInteger(): 
                yield nested.getInteger()
            else: 
                yield from self.flatten(nested.getList())