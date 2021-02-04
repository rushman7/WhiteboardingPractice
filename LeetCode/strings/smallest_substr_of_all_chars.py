def get_shortest_unique_substring(arr, str):
  hash_map = {}
  for char in arr:
    hash_map[char] = -1

  for i in range(len(str)):
    if str[i] in hash_map:
      hash_map[str[i]] = i

  min_val = float('inf')
  max_val = float('-inf')
  
  for char in hash_map:
    if hash_map[char] == -1:
      return ""
    min_val = min(min_val, hash_map[char])
    max_val = max(max_val, hash_map[char])
  
  return str[min_val:max_val+1]