# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        res, prev, curr, op = 0, 0, 0, '+'

        for c in s+'+':
            if c != ' ':
                if c.isdigit():
                    curr = 10 * curr + int(c)
                    continue
                if op == '+':
                    res+=prev
                    prev = curr
                elif op == '-':
                    res+=prev
                    prev = -curr
                elif op == '*':
                    prev *= curr
                elif op == '/':
                    prev = int(prev/curr)
                curr, op = 0, c
        
        return res + prev
         
