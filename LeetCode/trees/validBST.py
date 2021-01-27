class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, tree_min=float('-inf'), tree_max=float('inf')):
	if not tree:
		return True
	if tree.value < tree_min or tree.value >= tree_max:
		return False

	return validateBst(tree.left, tree_min, tree.value) and validateBst(tree.right, tree.value, tree_max)