# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    descendantOneDepth = getDepths(topAncestor, descendantOne)
    descendantTwoDepth = getDepths(topAncestor, descendantTwo)

	while descendantOneDepth != descendantTwoDepth:
		if descendantOneDepth > descendantTwoDepth:
			descendantOne = descendantOne.ancestor
			descendantOneDepth-=1
		else:
			descendantTwo = descendantTwo.ancestor
			descendantTwoDepth-=1
		if descendantOne == descendantTwo:
			return descendantOne
	
	while descendantOne.ancestor != descendantTwo.ancestor:
		descendantTwo = descendantTwo.ancestor
		descendantOne = descendantOne.ancestor
	
	return descendantOne.ancestor

def getDepths(node, val, depth=0):
	while node.name != val.name:
		val = val.ancestor
		depth+=1
	return depth