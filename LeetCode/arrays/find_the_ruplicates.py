def find_duplicates(arr1, arr2):
  hash_set = set()
  ans = []
  for num in arr1:
    hash_set.add(num)
    
  for num in arr2:
    if num in hash_set:
      ans.append(num)

  return ans
