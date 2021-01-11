# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

 

# Example 1:

# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:

# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
# Example 4:

# Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# Output: 2
# Example 5:

# Input: nums = [-1,-2,-3], k = 1
# Output: 2

# Solution 1: O(NlogN) time, O(1) space
def findPairs(self, nums: List[int], k: int) -> int:
    nums.sort()
    pairs = 0
    i, j = 0, 1
    L = len(nums)
    while j < L:
        while j < L and abs(nums[i]-nums[j]) < k:
            j+=1
        if j < L and abs(nums[i]-nums[j]) == k:
            pairs+=1
        while i < L-1 and nums[i] == nums[i+1]:
            i+=1
        i+=1
        j=i+1
    return pairs

# Solution 1: O(N) time, O(N) space
def findPairs(self, nums: List[int], k: int) -> int:
    pairs = 0
    hash_set = set()
    pair_sets = set()
    
    for num in nums:
        if num not in hash_set:
            if num+k in hash_set and (num, num+k) not in pair_sets and (num+k, num) not in pair_sets:
                pairs+=1
                pair_sets.add((num, num+k))
            if num-k in hash_set and (num, num-k) not in pair_sets and (num-k, num) not in pair_sets:
                pairs+=1
                pair_sets.add((num, num-k))
            hash_set.add(num)
        elif k == 0 and (num, num) not in pair_sets:
            pairs+=1
            pair_sets.add((num, num))
                
    return pairs