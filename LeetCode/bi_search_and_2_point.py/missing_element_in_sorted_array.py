class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = lambda i: nums[i] - nums[0] - i
        n = len(nums)
        L, R = 0, n-1
        
        if k > missing(n-1):
            return nums[-1] + k - missing(n-1)
        while L < R:
            M = (L + R) // 2
            
            if missing(M) < k:
                L = M + 1
            else:
                R = M
                
        return nums[L-1] + k - missing(L-1)