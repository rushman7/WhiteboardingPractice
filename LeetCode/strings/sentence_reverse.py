def reverse_words(arr):
  for i in range(len(arr)//2):
    arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
  

  left = 0
  for i in range(len(arr)):
    if arr[i] == ' ' or i == len(arr)-1:
      right = i if i == len(arr)-1 else i-1

      while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
      left = i+1
    
  
  return arr
