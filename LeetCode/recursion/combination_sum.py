class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(combo, index, _sum):
            if _sum == target:
                return result.append(list(combo))

            for i in range(index, len(candidates)):
                combo.append(candidates[i])
                if _sum+candidates[i] <= target:
                    backtrack(combo, i, _sum+candidates[i])
                combo.pop()
                
        backtrack([], 0, 0)
        return result