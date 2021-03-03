class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] < n and i != nums[i]:
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
        for i in range(0, n):
            if i != nums[i]:
                return i
        return n
