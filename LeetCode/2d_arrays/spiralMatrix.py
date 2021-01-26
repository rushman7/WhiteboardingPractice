# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralTraverse(array):
	startRow = startCol = 0
	endRow, endCol = len(array)-1, len(array[0])-1
	ans = []
	while startRow <= endRow and startCol <= endCol:
		for col in range(startCol, endCol+1):
			ans.append(array[startRow][col])
		startRow+=1
		for row in range(startRow, endRow+1):
			ans.append(array[row][endCol])
		endCol-=1
		for col in reversed(range(startCol, endCol+1)):
			if startRow > endRow:
				break
			ans.append(array[endRow][col])
		endRow-=1 
		for row in reversed(range(startRow, endRow+1)):
			if startCol > endCol:
				break
			ans.append(array[row][startCol])
		startCol+=1

	return ans
