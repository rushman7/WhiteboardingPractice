# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L = len(nums)
        res = [0] * L
        l, r, p = 0, L-1, L-1
        
        while p >= 0:
            if abs(nums[l]) > abs(nums[r]):
                res[p] = nums[l]**2
                l+=1
            else:
                res[p] = nums[r]**2
                r-=1
            p-=1
            
        return res