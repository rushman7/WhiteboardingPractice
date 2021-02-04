def powerset(array):
	added = set()
	result = []
	def helper(arr):
		added.add(tuple(arr))
		result.append(arr)
		for i in range(len(arr)):
			split = tuple(arr[:i]+arr[i+1:])
			if split not in added:
				helper(arr[:i]+arr[i+1:])
				
	helper(array)
	return result