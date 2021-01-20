class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [
            (1,2),
            (2,1),
            (2,-1),
            (1,-2),
            (-1,-2),
            (-2,-1),
            (-2,1),
            (-1,2)
        ]
        

        q = deque()
        
        q.appendleft((0,0,0))
        seen = set()
        while q:
            c_x, c_y, c_m = q.pop()
            if c_x == x and c_y == y:
                return c_m
            for move in moves:
                x_c, y_c = move
                x_c += c_x
                y_c += c_y
                m = c_m+1
                if x == x_c and y == y_c:
                    return m
                if (x_c,y_c) not in seen:
                    seen.add((x_c,y_c))
                    q.appendleft((x_c,y_c,m))