class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        hash_map = Counter(A)
        result = -1
        
        for key in hash_map:
            if hash_map[key] == 1:
                result = max(key, result)
        
        return result