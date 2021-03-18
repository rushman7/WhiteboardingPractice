class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        prio_queue = []
        for slot in slots1:
            if slot[1] - slot[0] >= duration:
                heapq.heappush(prio_queue, slot)
        for slot in slots2:
            if slot[1] - slot[0] >= duration:
                heapq.heappush(prio_queue, slot)
        
        while prio_queue:
            a = heapq.heappop(prio_queue)
            if not prio_queue:
                break
            b = prio_queue[0]
            
            if a[1] - b[0] >= duration:
                return [b[0], b[0]+duration]
        return []