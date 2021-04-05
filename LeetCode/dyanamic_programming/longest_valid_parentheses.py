class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, result = 0, 0, 0
        
        for char in s:
            if char == ')': 
                right+=1
                if right > left:
                    right, left = 0, 0
            else: 
                left+=1
                
            if right == left:
                result = max(result, right+left)
                
        right, left = 0, 0
        
        for char in s[::-1]:
            if char == ')': 
                right+=1
            else: 
                left+=1
                if left > right:
                    right, left = 0, 0
                    
            if right == left:
                result = max(result, right+left)
        return result