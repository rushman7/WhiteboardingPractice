def kadanesAlgorithm(array):
    largest_sum = array[0]
	
    for i in range(1, len(array)):
      array[i] = array[i]+array[i-1] if array[i-1] > 0 else array[i]
      largest_sum = max(largest_sum, array[i])
      
    return largest_sum
