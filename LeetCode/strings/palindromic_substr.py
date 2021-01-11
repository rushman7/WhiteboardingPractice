# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:

# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
 

# Example 2:

# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Note:

# The input string length won't exceed 1000.


# def countSubstrings(self, s: str) -> int:
    # total = 0
    # hash_pairs = set()
    
    # def reverse(s):
    #     return s[::-1]

    # def helper(i,j):
    #     if i == j:
    #         return
    #     if s[i:j+1] == reverse(s[i:j+1]) and (i,j) not in hash_pairs:
    #         nonlocal total
    #         total+=1

    #     hash_pairs.add((i,j))
    #     if (i+1,j) not in hash_pairs:
    #         helper(i+1, j)
    #     if (i,j-1) not in hash_pairs:
    #         helper(i, j-1)

    # helper(0, len(s)-1)
    # return total + len(s)

def countSubstrings(self, s: str) -> int:
    n = len(s)
    res = 0
    dp = [[0]*(n) for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]):
                dp[i][j] = 1
            else:
                dp[i][j] = 0
                
            if dp[i][j]:
                res+=1
    return res 