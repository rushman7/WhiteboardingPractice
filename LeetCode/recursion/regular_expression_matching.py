class Solution:
    def isMatch(self, s: str, p: str, sIdx=0, pIdx=0) -> bool:
        if pIdx >= len(p):
            return sIdx >= len(s)
        
        match = sIdx < len(s) and p[pIdx] in {s[sIdx], '.'}
        
        if pIdx < len(p)-1 and p[pIdx+1] == '*':
            return self.isMatch(s, p, sIdx, pIdx+2) or match and self.isMatch(s, p, sIdx+1, pIdx)
        else:
            return match and self.isMatch(s, p, sIdx+1, pIdx+1)
