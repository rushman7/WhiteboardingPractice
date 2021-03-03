class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = {'N': (0, 1),'E': (1, 0),'S': (0,-1),'W': (-1,0)}
        left = {'N': 'W','E': 'N','S': 'E','W': 'S'}
        right = {'N': 'E','E': 'S','S': 'W','W': 'N'}
        x, y = 0, 0
        curr_direction = 'N'
       
        for instruct in instructions:
            if instruct == 'L':
                curr_direction = left[curr_direction]
            elif instruct =='R':
                curr_direction = right[curr_direction]
            else:
                x += directions[curr_direction][0]
                y += directions[curr_direction][1]
            
        return True if x == 0 and y == 0 else False