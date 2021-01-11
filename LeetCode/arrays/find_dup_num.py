# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [1,1]
# Output: 1
# Example 4:

# Input: nums = [1,1,2]
# Output: 1

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            nums[abs(nums[i])]*=-1
            i+=1
        return -1
