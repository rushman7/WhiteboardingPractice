import heapq

def sort_k_messed_array(arr, k):
  if k == 0:
    return arr
  heap, index = [], 0
  while len(heap) <= k:
    heapq.heappush(heap, arr[index])
    index+=1
  
  for i in range(len(arr)):
    arr[i] = heapq.heappop(heap)
    if i+k+1 < len(arr):
      heapq.heappush(heap, arr[i+k+1])
      
  return arr