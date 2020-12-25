# Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        if t > m[-1][-1] or t < m[0][0]:
            return False
        r = len(m)-1
        c = 0
        while r < len(m) and c < len(m[0]):
            if t == m[r][c]:
                return True
            if t < m[r][c] and r > 0:
                r-=1
            else:
                c+=1
        return False