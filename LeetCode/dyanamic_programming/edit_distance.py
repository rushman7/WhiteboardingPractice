class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2) 
        dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]

        for i in range(len(dp)):
            dp[i][0] = i
        
        for j in range(len(dp[0])):
            dp[0][j] = j

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                left = dp[i-1][j] + 1
                top_left = dp[i-1][j-1]
                top = dp[i][j-1] + 1
                
                if word1[i-1] != word2[j-1]:
                    top_left += 1
                
                min_val = min(left, top_left, top)
                dp[i][j] = min_val
                 
        
        return dp[-1][-1]