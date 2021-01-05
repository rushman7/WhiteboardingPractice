# You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

def search(self, nums: List[int], target: int) -> int:
    L, R = 0, len(nums)-1
    
    while L <= R:
        mid = floor((L+R)/2)
        
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[L]:
            if target >= nums[L] and target < nums[mid]:
                R = mid-1
            else:
                L = mid+1
        else:
            if target <= nums[R] and target > nums[mid]:
                L = mid+1
            else:
                R = mid-1
    return -1