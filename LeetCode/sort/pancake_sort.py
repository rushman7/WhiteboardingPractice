def pancake_sort(arr):
  tracker, n = 0, len(arr)
  def flip(arr, k):
    for i in range(k//2):
      arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
      
  for i in range(n-1, -1, -1):
    largest_index = i
    
    for j in range(0, i+1):
      if arr[j] > arr[largest_index]:
        largest_index = j
    
    if largest_index != n-tracker-1:
      flip(arr, largest_index+1)
      flip(arr, n-tracker)
    tracker+=1
    
  return arr
