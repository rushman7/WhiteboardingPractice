def array_of_array_products(arr):
  if len(arr) <= 1:
    return []
  if len(arr) == 2:
    arr[0], arr[1] = arr[1], arr[0]
    return arr
  L = [1] * len(arr)
  R = [1] * len(arr)
  ans = [1] * len(arr)

  for i in range(1, len(arr)):
    L[i] = L[i-1]*arr[i-1]
  for i in range(len(arr)-2, -1,-1):
    R[i] = R[i+1]*arr[i+1]
    
  for i in range(len(ans)):
    ans[i] = R[i]*L[i]
   
  return ans
