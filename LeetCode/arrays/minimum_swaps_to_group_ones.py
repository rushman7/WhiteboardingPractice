class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = 0
        for num in data:
            if num == 1:
                ones+=1
                
        if ones <= 1:
            return 0
                
        curr_ones = 0
        swaps = float('inf')
        L, R = 0, 0
        
        while R < len(data):
            if data[R] == 1:
                curr_ones+=1
            swaps = min(swaps, ones-curr_ones)
            if R == L + ones - 1:
                if data[L] == 1:
                    curr_ones-=1
                L+=1
            R+=1
            
            
        return swaps