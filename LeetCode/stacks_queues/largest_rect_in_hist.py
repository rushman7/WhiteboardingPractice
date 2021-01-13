# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


# The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10
 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stack = [-1]
        max_area = 0
        L = len(h)
        for i in range(L):
            while stack[-1] != -1 and h[i] <= h[stack[-1]]:
                height = stack.pop()
                max_area = max(max_area, h[height]*(i-stack[-1]-1))
            stack.append(i)
        
        while stack[-1] != -1:
            height = stack.pop()
            max_area = max(max_area, h[height]*(L-stack[-1]-1))

        return max_area