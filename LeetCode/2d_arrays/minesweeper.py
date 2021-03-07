class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        visited = set()
        queue = deque()
        queue.appendleft(click)
        directions = [[0,1],[1,0],[1,1],[-1,-1],[-1,0],[0,-1],[1, -1],[-1, 1]]
        
        while queue:
            curr_i, curr_j = queue.pop()
            curr_mines = 0
            if (curr_i, curr_j) in visited:
                continue
            else:
                visited.add((curr_i, curr_j))
            for i, j in directions:
                temp_i = curr_i + i
                temp_j = curr_j + j
                if temp_i >= len(board) or temp_i < 0 or temp_j < 0 or temp_j >= len(board[0]):
                    continue
                
                if board[temp_i][temp_j] == 'M':
                    curr_mines+=1
            if curr_mines == 0:
                for i, j in directions:
                    temp_i = curr_i + i
                    temp_j = curr_j + j
                    if temp_i >= len(board) or temp_i < 0 or temp_j < 0 or temp_j >= len(board[0]):
                        continue

                    if (temp_i, temp_j) not in visited:
                        queue.appendleft([temp_i, temp_j])
                board[curr_i][curr_j] = 'B'
            else:
                board[curr_i][curr_j] = str(curr_mines)
    
        return board