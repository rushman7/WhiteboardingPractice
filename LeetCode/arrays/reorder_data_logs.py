class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_heap, numbers, result = [], [], []
        
        for log in logs:
            ident, rest = log.split(" ", maxsplit=1)
            if rest[0].isalpha():
                heapq.heappush(letter_heap, (rest, ident))
            else:
                numbers.append(log)
        
        while letter_heap:
            rest, ident = heapq.heappop(letter_heap)
            result.append(ident+' '+rest)
            
        return result+numbers
