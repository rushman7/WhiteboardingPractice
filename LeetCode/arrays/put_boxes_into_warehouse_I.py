class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        last_box_placed = len(warehouse)
        result = 0
        
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i-1], warehouse[i])
        
        for box in boxes:
            i = last_box_placed - 1
            
            while i >= 0:
                if box > warehouse[i]:
                    i-=1
                else:
                    result+=1
                    last_box_placed = i
                    break
        
        return result