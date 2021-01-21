def findThreeLargestNumbers(array):
    ans = [float('-inf') for _ in range(3)] 
	
    for num in array:
      if num > ans[0]:
        ans[0] = num
        for i in range(2):
          if ans[i] > ans[i+1]:
            ans[i], ans[i+1] = ans[i+1], ans[i]
            
    return ans