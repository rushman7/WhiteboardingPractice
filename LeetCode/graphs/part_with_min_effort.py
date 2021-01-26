class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.ans = float(inf)
        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(i, j, curr_max, curr_path, prev=None):
            if i < 0 or j < 0 or i == len(heights) or j == len(heights[0]):
                return
            if prev:
                curr_max = max(abs(heights[i][j]-prev), curr_max)

                if i == len(heights)-1 and j == len(heights[i])-1:
                    # print(i, j, curr_max, curr_path, prev)
                    self.ans = min(self.ans, curr_max)
                    return

            for move in moves:
                x,y = move
                if (i+x,j+y) not in curr_path:
                    curr_path.add((i+x,j+y))
                    dfs(i+x,j+y, curr_max, curr_path, heights[i][j])
                    curr_path.remove((i+x,j+y))
                             
        dfs(0,0,float(-inf), set((0,0)))
        return self.ans if self.ans != inf else 0
