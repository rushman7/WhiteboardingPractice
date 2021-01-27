class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minHeightBst(array):
	def build_tree(start, end):
		if end < start:
			return None
		
		mid = (start+end)//2
		tree = BST(array[mid])
		tree.left = build_tree(start, mid-1)
		tree.right = build_tree(mid+1, end)
		
		return tree
		
	return build_tree(0, len(array)-1)
