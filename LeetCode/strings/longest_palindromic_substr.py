# O(N^2), O(1)

def longestPalindrome(self, s: str) -> str:
    if len(s) <= 2:
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]
        return s

    max_str = s[0]
    max_size = 1

    for i in range(len(s)):
        if i < len(s)-1 and s[i] == s[i+1]:
            max_size, max_str = self.expandFromMiddle(i, i+1, s, max_size, max_str)
        if i > 0 and i < len(s)-1 and s[i-1] == s[i+1]:
            max_size, max_str = self.expandFromMiddle(i-1, i+1, s, max_size, max_str)
    return max_str


def expandFromMiddle(self, left, right, s, max_size, max_str):
    while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
        left-=1
        right+=1
    if right-left+1 > max_size:
        max_size = right-left+1
        max_str = s[left:right+1]
    return max_size, max_str