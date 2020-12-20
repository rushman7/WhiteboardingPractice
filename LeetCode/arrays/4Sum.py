# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Notice that the solution set must not contain duplicate quadruplets.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [], target = 0
# Output: []

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums)-3): 
            for j in range(i+1, len(nums)-2):
                self.checkSum(i,j,j+1,len(nums)-1, nums, res, target)
                
        return res
    def checkSum(self, i,j,lo, hi, nums, res, target):
        while lo < hi:
            sum = nums[i]+nums[j]+nums[lo]+nums[hi]
            if sum < target: lo+=1
            elif sum > target: hi-=1
            else:
                if [nums[i],nums[j],nums[lo],nums[hi]] not in res:
                    res.append([nums[i],nums[j],nums[lo],nums[hi]])
                while lo < hi and nums[lo] == nums[lo+1]: lo+=1
                while lo < hi and nums[hi] == nums[hi-1]: hi-=1
                lo+=1
                hi-=1
                