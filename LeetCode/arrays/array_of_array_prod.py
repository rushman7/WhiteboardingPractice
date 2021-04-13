# def arrayOfProducts(array):
#     if len(array) <= 1:
#       return []
#     if len(array) == 2:
#       array[0], array[1] = array[1], array[0]
#       return array
#     length = len(array)
#     left_array = [1] * length
#     right_array = [1] * length
#     result = [1] * length
    
#     for i in range(1, length):
#       left_array[i] = left_array[i-1]*array[i-1]
#     for j in range(length-2, -1, -1):
#       right_array[j] = right_array[j+1]*array[j+1]
#     for k in range(length):
#       result[k] = right_array[k]*left_array[k]
    
#     return result

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1 for _ in range(n)]
        
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        
        right = nums[-1]
        
        for i in range(n-2, -1, -1):
            ans[i] *= right
            right *= nums[i]
        
        return ans

  
