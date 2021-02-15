class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, words = len(s), set(wordDict)
        dp = [True] + [False] * n
        
        for i in range(n):
            curr_str = ""
            for j in range(i, n):
                curr_str+=s[j]
                if curr_str in words and dp[i]:
                    dp[j+1] = True
        return dp[-1]