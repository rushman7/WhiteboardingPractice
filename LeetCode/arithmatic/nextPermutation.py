# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:

# Input: nums = [1]
# Output: [1]

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        swapped = False
        while i > 0:
            if nums[i-1] < nums[i]:
                cand = i
                curr = i+1
                swapped = True
                while curr < len(nums):
                    diff_curr = nums[curr] - nums[i-1]
                    diff_cand = nums[cand] - nums[i-1]
                    if diff_cand > diff_curr and diff_curr >= 1:
                        cand = curr
                    curr += 1
                nums[i-1], nums[cand] = nums[cand], nums[i-1]
                break
            i-=1
        nums[i:] = sorted(nums[i:])
        if not swapped:
            nums.sort()
        