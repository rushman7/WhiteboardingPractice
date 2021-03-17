class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def valid_pal(s, l, r, errors):
            if l >= r:
                return True
            if s[l] == s[r]:
                return valid_pal(s, l+1, r-1, errors)
            errors+=1
            if errors == 2:
                return False
            return valid_pal(s, l+1, r, errors) or valid_pal(s, l, r-1, errors)
        
        return valid_pal(s, 0, len(s)-1, 0)
