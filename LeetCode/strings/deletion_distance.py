from collections import Counter

def deletion_distance(str1, str2):
  if not str1 or not str2:
    return len(str1) if str1 else len(str2)
  if str1 == str2[::-1]:
    return (len(str1)-1)*2
  
  word1, word2 = Counter(str1), Counter(str2)
  result = 0
  
  for char in word1:
    if char in word2:
      min_val = min(word2[char], word1[char])
      word2[char]-=min_val
      word1[char]-=min_val
    result+=word1[char]
  
  for char in word2:
    result+=word2[char]
    
  return result