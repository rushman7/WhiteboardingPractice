# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

# Example 1:


# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.

# O(M*N) extra memory, O(M*N) time complexity

def gameOfLife(self, board: List[List[int]]) -> None:
    toChange = {}
    changes = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            ones = 0
            if i > 0 and j > 0 and board[i-1][j-1] == 1: # top left
                ones+=1
            if i > 0 and board[i-1][j] == 1: # top
                ones+=1
            if i > 0 and j < len(board[i])-1 and board[i-1][j+1] == 1: # top right
                ones+=1
            if j > 0 and board[i][j-1] == 1: # left
                ones+=1
            if j < len(board[i])-1 and board[i][j+1] == 1: # right
                ones+=1
            if i < len(board)-1 and j > 0 and board[i+1][j-1] == 1: # bottom left
                ones+=1
            if i < len(board)-1 and board[i+1][j] == 1: # bottom
                ones+=1
            if i < len(board)-1 and j < len(board[i])-1 and board[i+1][j+1] == 1: # bottom right
                ones+=1
            if board[i][j] == 0 and ones == 3:
                changes+=1
                toChange[changes] = (i, j, 1)
            elif board[i][j] == 1 and ones not in (2, 3):
                changes+=1
                toChange[changes] = (i, j, 0)
    for val in toChange.values():
        board[val[0]][val[1]] = val[2]

# O(1) extra memory, O(M*N) time complexity

def gameOfLife(self, board: List[List[int]]) -> None:
    for i in range(len(board)):
        for j in range(len(board[i])):
            ones = 0
            if i > 0 and j > 0 and (board[i-1][j-1] == 1 or board[i-1][j-1] == -1): # top left
                ones+=1
            if i > 0 and (board[i-1][j] == 1 or board[i-1][j] == -1): # top
                ones+=1
            if i > 0 and j < len(board[i])-1 and abs(board[i-1][j+1]) == 1: # top right
                ones+=1
            if j > 0 and abs(board[i][j-1]) == 1: # left
                ones+=1
            if j < len(board[i])-1 and abs(board[i][j+1]) == 1: # right
                ones+=1
            if i < len(board)-1 and j > 0 and abs(board[i+1][j-1]) == 1: # bottom left
                ones+=1
            if i < len(board)-1 and abs(board[i+1][j]) == 1: # bottom
                ones+=1
            if i < len(board)-1 and j < len(board[i])-1 and abs(board[i+1][j+1]) == 1: # bottom right
                ones+=1
            if (board[i][j] == 0 or board[i][j] == 2) and ones == 3:
                board[i][j] = 2
            elif (board[i][j] == 1 or board[i][j] == -1) and ones not in (2, 3):
                board[i][j] = -1
            
            if i > 0 and j > 0 and (board[i-1][j-1] == 2 or board[i-1][j-1] == -1):
                board[i-1][j-1] = 1 if board[i-1][j-1] == 2 else 0
            if j == len(board[i])-1 and (board[i-1][j] == 2 or board[i-1][j] == -1):
                board[i-1][j] = 1 if board[i-1][j] == 2 else 0
            if i == len(board)-1 and (board[i][j-1] == 2 or board[i][j-1] == -1):
                board[i][j-1] = 1 if board[i][j-1] == 2 else 0
            if board[len(board)-1][len(board[0])-1] == 2 or board[len(board)-1][len(board[0])-1] == -1:
                board[len(board)-1][len(board[0])-1] = 1 if board[len(board)-1][len(board[0])-1] == 2 else 0