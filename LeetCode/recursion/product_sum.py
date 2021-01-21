def productSum(array, depth=1, total=0):
	if not array: return 0

	for val in array:
		if type(val) != int:
			val = (depth+1) * productSum(val, depth+1)
		total+=val
		
	return total
