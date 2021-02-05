class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1_len, text2_len = len(text1), len(text2)
        dp = [[0 for _ in range(text1_len+1)] for _ in range(text2_len+1)]
        
        for i in range(1, text2_len+1):
            for j in range(1, text1_len+1):
                dp[i][j] = dp[i-1][j-1] + 1 if text2[i-1] == text1[j-1] else max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]