# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0

def maximalSquare(self, matrix: List[List[str]]) -> int:
    max_square = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '1':
                # pre-assign max_square in case list len is 1
                max_square = max(max_square, int(matrix[i][j]))
                # check that we can look at 3 areas
                if i > 0 and j > 0:
                    # look top, left and topleft
                    top = int(matrix[i][j-1])
                    left = int(matrix[i-1][j])
                    topleft = int(matrix[i-1][j-1])
                    # check if all are greater than 1
                    if top >= 1 and left >= 1 and topleft >= 1:
                        # set matrix to be min val of all 3 + 1
                        matrix[i][j] = str(min(top,left,topleft)+1)
                        # set max to be curr max or i*i max
                        max_square = max(max_square, int(matrix[i][j])*int(matrix[i][j]))
    # time is O(M*N)
    # space is O(1)
    return max_square