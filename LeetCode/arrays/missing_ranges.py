class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result, curr = [], lower
        
        for num in nums:
            if num == curr: 
                curr+=1
            else:
                result.append(self.get_range(curr, num-1))
                curr = num + 1

        if curr <= upper:
            result.append(self.get_range(curr, upper))

        return result

    def get_range(self, lower, upper):
        return str(lower) if upper == lower else str(lower) + '->' + str(upper)