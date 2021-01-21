def selectionSort(array):
	for i in range(len(array)):
		min_j = i
		for j in range(i, len(array)):
			if array[j] < array[min_j]:
				min_j = j
		array[i], array[min_j] = array[min_j], array[i]
		
	
	return array
