def reverseWordsInString(string):
  result, n, left = [], len(string), 0
  for s in string:
    result.append(s)
  swap(result, 0, n-1)
  for right in range(n):
    if result[right] == ' ':
      swap(result, left, right-1)
      left = right+1
      
  swap(result, left, n-1)
      
  return "".join(result)

def swap(result, left, right):
  while left <= right:
    result[left], result[right] = result[right], result[left]
    left+=1
    right-=1