# This question is about implementing a basic elimination algorithm for Candy Crush.

# Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

# If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
# After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
# After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the current board.

 

# Example:

# Input:
# board =
# [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

# Output:
# [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]

def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
    to_crush = set()
        
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                if j < len(board[i])-2 and board[i][j] == board[i][j+1] == board[i][j+2]:
                    to_crush.update([(i,j),(i,j+1),(i,j+2)])
                if i < len(board)-2 and board[i][j] == board[i+1][j] == board[i+2][j]:
                    to_crush.update([(i,j),(i+1,j),(i+2,j)])

    for i, j in to_crush:
        board[i][j] = 0
    
    if to_crush:
        for col in range(len(board[0])):
            right = len(board)-1
            left = right-1

            while left >= 0:
                if board[right][col] == 0:
                    while left > 0 and board[left][col] == 0:
                        left-=1
                    board[left][col], board[right][col] = board[right][col], board[left][col]
                left-=1
                right-=1

    return board if not to_crush else self.candyCrush(board)