def insertionSort(array):
	for i in range(len(array)):
		for j in range(i):
			if array[i] < array[j]:
				array[i], array[j] = array[j], array[i]
	
	return array
