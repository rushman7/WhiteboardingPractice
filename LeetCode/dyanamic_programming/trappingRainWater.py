# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 0 <= n <= 3 * 104
# 0 <= height[i] <= 105

def trap(self, height: List[int]) -> int:
    total_water = 0
    L = 0
    R = len(height)-1
    
    while L < R:
        if height[R] >= height[L]:
            L+=1
            h = min(height[L-1], height[R])-height[L]
            total_water+= h if h > 0 else 0
            height[L] = max(height[L], height[L-1])
        else:
            R-=1
            h = min(height[L], height[R+1])-height[R]
            total_water+= h if h > 0 else 0
            height[R] = max(height[R], height[R+1])
    return total_water
             