# O(N^2), O(1)

def longestPalindrome(self, s: str) -> str:
    start, end = 0, 0
    
    for i in range(len(s)-1):
        odd_len = self.expand(s, i, i)
        even_len = self.expand(s, i, i+1)

        max_len = max(odd_len, even_len)
        
        if max_len > end-start:
            end = i + (max_len+1)//2
            start = i - max_len//2
    
    return s[start:end+1]
        
        
def expand(self, s, l, r):
    if s[r] != s[l]:
        return 0
    
    while (l > 0 and r < len(s)-1) and s[l-1] == s[r+1]:
        l-=1
        r+=1
    
    return r-l if s[r]==s[l] else r-l-1