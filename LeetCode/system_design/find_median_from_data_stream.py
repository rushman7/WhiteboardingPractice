class MedianFinder:
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        val = heapq.heappushpop(self.lo, -num)
        heapq.heappush(self.hi, -val)
        
        while len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
            

    def findMedian(self) -> float:
        return -self.lo[0] if len(self.lo) != len(self.hi) else (-self.lo[0] + self.hi[0]) / 2