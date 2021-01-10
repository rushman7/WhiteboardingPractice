# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

# Example 1:

# Input: n = 12
# Output: 21
# Example 2:

# Input: n = 21
# Output: -1
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        m = [x for x in str(n)]
        i = len(m)-1
        while i > 0:
            if m[i-1] < m[i]:
                cand = i
                curr = i+1
                while curr < len(m):
                    diff_curr = int(m[curr]) - int(m[i-1])
                    diff_cand = int(m[cand]) - int(m[i-1])
                    if diff_cand > diff_curr and diff_curr >= 1:
                        cand = curr
  
                    curr += 1
                m[i-1], m[cand] = m[cand], m[i-1]
                break
            i-=1
        j = len(m)-1
        while i < j:
            if m[i] < m[j]:
                break
            m[i], m[j] = m[j], m[i]
            i+=1
            j-=1
        return int("".join(m)) if int("".join(m)) > n and int("".join(m)) < 2**31 else -1
        
        
