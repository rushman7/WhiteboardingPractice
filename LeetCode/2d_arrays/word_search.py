# Given an m x n board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 200
# 1 <= word.length <= 103
# board and word consists only of lowercase and uppercase English letters.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:  
        def search(i, j, wi, visited=set()):
            print(visited)
            if wi == len(word):
                return True
            
            if i < 0 or j < 0 or i == len(board) or j == len(board[i]) or word[wi] != board[i][j]:
                return False
            
            visited.add((i,j))
            for ic, jc in [(0,1),(1,0),(0,-1),(-1,0)]:
                if (i+ic, j+jc) not in visited:
                    if search(i+ic, j+jc, wi+1):
                        return True
            visited.remove((i,j))
            
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if search(i, j, 0):
                    return True

        return False
            