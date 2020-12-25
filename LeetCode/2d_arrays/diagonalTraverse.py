# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

# Example:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# Output:  [1,2,4,7,5,3,6,8,9]

# Explanation:

 

# Note:

# The total number of elements of the given matrix will not exceed 10,000.

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        up = True
        ans = []
        i = 0
        j = 0
        
        while i < len(matrix) and j < len(matrix[0]):
            ans.append(matrix[i][j])
            if up:
                if i == 0:
                    if j == len(matrix[0])-1:
                        i+=1
                    else:
                        j+=1
                    up = False
                elif j == len(matrix[0])-1:
                    i+=1
                    up = False
                else:
                    i-=1
                    j+=1
            else:
                if j == 0:
                    if i == len(matrix)-1:
                        j+=1
                    else:
                        i+=1
                    up = True
                elif i == len(matrix)-1:
                    j+=1
                    up = True
                else:
                    i+=1
                    j-=1
        return ans