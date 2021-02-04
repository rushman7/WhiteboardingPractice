def getPermutations(array):
	def helper(i, result):
		if i == len(array)-1:
			result.append(list(array))
		for j in range(i, len(array)):
			array[j], array[i] = array[i], array[j]
			helper(i+1, result)
			array[j], array[i] = array[i], array[j]
		return result

	return helper(0, [])
