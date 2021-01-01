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
    R = len(board)
    C = len(board[0])
    toCrush = {}
    
    for r in range(R):
        for c in range(C):
            if c+2 < len(board[r]): # check right
                if board[r][c] != 0 and board[r][c] == board[r][c+1] == board[r][c+2]:
                    toCrush[(f'{r},{c}')] = f'{r},{c}'
                    toCrush[(f'{r},{c+1}')] = f'{r},{c+1}'
                    toCrush[(f'{r},{c+2}')] = f'{r},{c+2}'
            if r+2 < len(board): # check down
                if board[r][c] != 0 and board[r][c] == board[r+1][c] == board[r+2][c]:
                    toCrush[(f'{r},{c}')] = f'{r},{c}'
                    toCrush[(f'{r+1},{c}')] = f'{r+1},{c}'
                    toCrush[(f'{r+2},{c}')] = f'{r+2},{c}'
    for x in toCrush: # convert crushes to 0
        split = x.index(',')
        r = int(x[:split])
        c = int(x[split+1:])
        board[r][c] = 0
        
    for c in range(C): # drop the board
        col_list = []
        for r in range(R):
            col_list.append(board[r][c])
        self.moveZeroesToFront(col_list)
        for i in range(len(col_list)):
            board[i][c] = col_list[i]
    return self.candyCrush(board) if len(toCrush) > 0 else board

def moveZeroesToFront(self, col_list):
    right = len(col_list)-1
    left = right - 1
    while left >= 0:
        if col_list[right] == 0:
            while left > 0 and col_list[left] == 0:
                left-=1
            col_list[left], col_list[right] = col_list[right], col_list[left]
        left-=1
        right-=1
    return col_list
                
            