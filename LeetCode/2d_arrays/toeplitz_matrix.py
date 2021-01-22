def isToeplitz(arr):
  for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
      curr = arr[i][j]

      if curr != arr[i-1][j-1]:
        return False

      if i < len(arr)-1 and j < len(arr[i])-1 and curr != arr[i+1][j+1]:
        return False

  return True