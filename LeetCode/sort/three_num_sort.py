def threeNumberSort(array, order):
    i = 0
	
    for num in order:
      j = i + 1
      while j < len(array):
        if array[i] != num:
          while j < len(array) and array[j] != num:
            j+=1
          if j == len(array):
            break
          array[i], array[j] = array[j], array[i]
        i+=1
        j+=1
    return array
