# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

# After this process, we have some array B.

# Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

# Example 1:

# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
# Example 2:

# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
# Example 3:

# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]

class Solution(object):
    def smallestRangeII(self, A, K):
        A.sort()
        min_A = A[0]
        max_A = A[-1]
        diff = max_A - min_A
        for i in range(len(A)-1):
            a,b = A[i], A[i+1]
            diff = min(diff, max(max_A-K, a+K) - min(min_A+K, b-K))
            
        return diff
        
            