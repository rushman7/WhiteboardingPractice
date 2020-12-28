# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        
        for x in nums:
            if not hashMap.get(x):
                hashMap[x] = 1
            else:
                del hashMap[x]
        return list(hashMap.keys())[0]
        