class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)
        
        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= stack[-1][0]:
                stack.pop()
            if not stack:
                result[i] = 0
            else:
                result[i] = stack[-1][1] - i
            stack.append((T[i], i))
            
        return result