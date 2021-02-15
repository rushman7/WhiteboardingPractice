class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        max_gaps = 0
        gaps = defaultdict(int)
        for row in wall:
            w = 0
            for brick in row[:-1]:
                w+=brick
                gaps[w]+=1
                max_gaps = max(max_gaps, gaps[w])

        return len(wall)-max_gaps