def runLengthEncoding(string):
  ans = ''
  i = 0

  while i < len(string):
    count = 1
    curr_str = string[i]
    
    while i+1 < len(string) and curr_str == string[i+1]:
      count+=1
      i+=1
      
    while count > 9:
      ans = ans + '9' + curr_str
      count-=9
    
    ans = ans + f'{count}' + curr_str
      
    i+=1
    
  return ans