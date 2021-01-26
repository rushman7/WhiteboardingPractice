def moveElementToEnd(array, toMove):
    left, right = 0, len(array)-1
	
    while left < right:
      while left < right and array[right] == toMove:
        right-=1
      while left < right and array[left] != toMove:
        left+=1
      array[right], array[left] = array[left], array[right]
    return array