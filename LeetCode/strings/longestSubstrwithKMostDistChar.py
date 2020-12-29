# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.

from collections import OrderedDict
def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    if len(s) <= 1 or k == 0:
        return 1 if len(s) == 1 and k >= 1 else 0
    
    hashMap = OrderedDict()
    l,r,a = 0,1,0
    hashMap[s[0]] = 0
    while r < len(s):
        hashMap[s[r]] = r
        if len(hashMap) > k:
            l = hashMap.popitem(last=False)[1] + 1
        hashMap.move_to_end(s[r], last=True)
        r+=1
        a = max(a, r-l)
    return a