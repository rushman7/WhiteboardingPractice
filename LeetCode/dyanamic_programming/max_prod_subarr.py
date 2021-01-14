# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        res = nums[0]
        min_ = nums[0]
        max_ = nums[0]
        
        for i in range(1, len(nums)):
            temp_min = min_
            min_ = min(nums[i], min_*nums[i], max_*nums[i])
            max_ = max(nums[i], temp_min*nums[i], max_*nums[i])
            res = max(res, max_)
            
        return res