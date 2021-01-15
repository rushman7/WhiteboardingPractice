# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
# Example 4:

# Input: s = "  Bob    Loves  Alice   "
# Output: "Alice Loves Bob"
# Example 5:

# Input: s = "Alice does not even like bob"
# Output: "bob like even not does Alice"
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        split = s.split(' ')
        
        for i in range(len(split)-1, -1,-1):
            if len(split[i]) > 0:
                res.append(split[i])
                
        return " ".join(res)