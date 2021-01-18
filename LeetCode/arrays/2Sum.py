# O(N), O(N)

def twoNumberSum(array, targetSum):
    # Write your code here.
    hashMap = {}
	
    for i, val in enumerate(array):
      hashMap[targetSum-val] = i
    
    for i, val in enumerate(array):
      if val in hashMap and i != hashMap[val]:
        return [val, array[hashMap[val]]]
    
    return []

# O(N^2), O(1)
def twoNumberSum(array, targetSum):
    # Write your code here.

    for i in range(len(array)):
      for j in range(len(array)):
        if i != j and array[i] + array[j] == targetSum:
          return [array[i], array[j]]
    return []
