def searchInSortedMatrix(matrix, target):
    i, j = len(matrix)-1, 0
	
    while i >= 0 and j < len(matrix[0]):
      if target < matrix[i][j]:
        i-=1
      elif target > matrix[i][j]:
        j+=1
      else:
        return [i,j]
      
    return [-1,-1]