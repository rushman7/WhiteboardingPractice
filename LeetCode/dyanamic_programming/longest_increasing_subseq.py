class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] + [0 for _ in range(len(nums)-1)]
        result = 1
        
        for i in range(1, len(nums)):
            curr_max = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    curr_max = max(curr_max, dp[j])
                
            dp[i] = curr_max + 1
            result = max(result, dp[i])
        return result
