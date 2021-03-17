class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, profit = prices[0], 0
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy + fee:
                profit += prices[i] - buy - fee
                buy = prices[i] - fee
        return profit
