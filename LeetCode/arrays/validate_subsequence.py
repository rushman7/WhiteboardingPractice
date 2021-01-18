# O(N), O(1)

def isValidSubsequence(array, sequence):
	i = 0
	for j in range(len(array)):
		if array[j] == sequence[i]:
			i+=1
		if i == len(sequence):
			return True
			
	return False


