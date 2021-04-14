class Solution:
    def rob(self, nums: List[int]) -> int:
        one_back, two_back = nums[0], 0

        for i in range(1, len(nums)):
            current = max(two_back + nums[i], one_back)
            two_back = one_back
            one_back = current
        
        return one_back
