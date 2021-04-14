class Solution:
    def calculate(self, s: str) -> int:
        return self.compute(s, 0)[0]
    
    def compute(self, s, i):
        ans = 0
        num = 0
        positive = True
        
        if s[i] == '-':
            positive = False
            i += 1
        
        while i < len(s):
            if s[i] == '(':
                num, i = self.compute(s, i+1)
            elif s[i].isnumeric():
                num = num * 10 + int(s[i])
            elif s[i] == ')':
                return ans+num if positive else ans-num, i
            elif s[i] in {'+', '-'}:
                ans += num if positive else -num
                num = 0
                positive = True if s[i] == '+' else False
            i+=1
        
        ans += num if positive else -num
        
        return ans, i