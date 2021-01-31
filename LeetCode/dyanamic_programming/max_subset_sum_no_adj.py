def maxSubsetSumNoAdjacent(array):
	if not array:
		return 0
	for i in range(2, len(array)):
		third_val = array[i-3] if i >= 3 else 0
		array[i] = max(array[i]+array[i-2], array[i-1], third_val+array[i])

	return array[-1]
