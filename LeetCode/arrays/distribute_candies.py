class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        result = len(set(candyType))
        candies = len(candyType) // 2
        return result if result <= candies else candies