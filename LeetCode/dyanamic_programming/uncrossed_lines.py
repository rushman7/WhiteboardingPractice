class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        a, b = len(A), len(B)
        dp = [[0 for _ in range(b+1)] for _ in range(a+1)]
        
        for i in range(1, a+1):
            for j in range(1, b+1):
                dp[i][j] = 1 + dp[i-1][j-1] if A[i-1] == B[j-1] else max(dp[i-1][j], dp[i][j-1])
                
        return dp[-1][-1]