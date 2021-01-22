class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        
        i = j = 0
        edit = 1
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if edit == 0: return False
                edit-=1
                if len(t) > len(s): i-=1
                elif len(s) > len(t): j-=1
            i+=1
            j+=1
        return True
