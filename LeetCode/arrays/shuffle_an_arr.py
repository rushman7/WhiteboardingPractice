# Given an integer array nums, design an algorithm to randomly shuffle the array.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
 

# Example 1:

# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.default = list(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.default)
        return self.nums
        
    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            rand_idx = randrange(i, len(self.nums))
            self.nums[i], self.nums[rand_idx] = self.nums[rand_idx], self.nums[i]
        
        return self.nums