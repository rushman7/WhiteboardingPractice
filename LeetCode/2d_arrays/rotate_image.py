class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)-1

        for i in range(n):
            for j in range(i, n-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = temp
                
        return matrix

