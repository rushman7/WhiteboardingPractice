def isMonotonic(array):
    if not array:
      return True
    non_incr = True if array[0] > array[-1] else False
	
    for i in range(len(array)-1):
      if non_incr and array[i+1] > array[i]:
        return False
      elif not non_incr and array[i+1] < array[i]:
        return False
    return True