# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Follow up: Could you implement the O(n) solution? 

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1
        curr = 1
        nums.sort()
        i = 0 
        while i < len(nums)-1:
            while nums[i] == nums[i+1]:
                i+=1
                if i == len(nums)-1:
                    break
            if i == len(nums)-1:
                    break
            if nums[i]+1 == nums[i+1]:
                curr+=1
                ans = max(ans, curr)
            else:
                curr = 1
            i+=1
        return ans