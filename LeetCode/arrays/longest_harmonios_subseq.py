class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hash_map = Counter(nums)
        result = 0
        for num in nums:
            if num+1 in hash_map:
                result = max(result, hash_map[num]+hash_map[num+1])
        return result