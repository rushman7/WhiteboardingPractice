# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    sum = 0
    hashMap = {0:1}
    
    for num in nums:
        sum+=num
        if sum-k in hashMap:
            count+=hashMap[sum-k]
        hashMap[sum] = (hashMap.get(sum) if hashMap.get(sum) else 0) + 1
    return count