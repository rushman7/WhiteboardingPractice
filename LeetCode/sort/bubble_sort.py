def bubbleSort(array):
    for i in range(len(array)-1,-1,-1):
      for j in range(i):
        if array[j] > array[j+1]:
          array[j], array[j+1] = array[j+1], array[j]
    return array
        