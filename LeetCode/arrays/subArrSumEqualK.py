# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        sum = nums[i]
        if sum == k:
            count+=1
        for j in range(i+1, len(nums)):
            sum+=nums[j]
            if sum == k:
                count+=1
    return count