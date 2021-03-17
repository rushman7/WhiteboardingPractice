class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        queue = deque()
        queue.appendleft(((0,0), (0,1), 0))
        seen = set()
        n = len(grid)

        while queue:
            tail, head, length = queue.pop()
            if head == (n-1,n-1) and tail == (n-1,n-2):
                return length
            if (tail, head) in seen:
                continue
            seen.add((tail, head))
            if self.check_valid(n, head, grid) and self.check_valid(n, tail, grid):
                hr, hc = head
                tr, tc = tail
                if self.check_valid(n, (hr, hc+1), grid) and self.check_valid(n, (tr, tc+1), grid):
                    queue.appendleft(((tr, tc+1), (hr, hc+1), length+1))
                    
                if self.check_valid(n, (hr+1, hc), grid) and self.check_valid(n, (tr+1, tc), grid):
                    queue.appendleft(((tr+1, tc), (hr+1, hc), length+1))
                if hr == tr:
                    if self.check_valid(n, (hr+1, hc-1), grid) and self.check_valid(n, (tr+1, tc+1), grid):
                        queue.appendleft(((tr, tc), (hr+1, hc-1), length+1))
                if hc == tc:
                    if self.check_valid(n, (hr-1, hc+1), grid) and self.check_valid(n, (tr+1, tc+1), grid):
                        queue.appendleft(((tr, tc), (hr-1, hc+1), length+1))
                
        return -1
                        
    def check_valid(self, n, pos, grid):
        r, c = pos
        if r < 0 or r >= n:
            return False
        if c < 0 or c >= n:
            return False
        if grid[r][c] == 1:
            return False
        return True