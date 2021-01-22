def threeNumberSum(array, targetSum):
    array.sort()
    ans = []
    
    for i in range(1, len(array)):
      L, R = i-1, i+1
      
      while L >= 0 and R <= len(array)-1:
        if array[L]+array[i]+array[R] == targetSum:
          ans.append([array[L],array[i],array[R]])
          L-=1
          R+=1
        elif array[L]+array[i]+array[R] > targetSum:
          L-=1
        elif array[L]+array[i]+array[R] < targetSum:
          R+=1
    ans.sort()
    return ans
