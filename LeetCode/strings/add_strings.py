class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_idx, num2_idx, carry = len(num1)-1, len(num2)-1, 0
        result = ""
        
        while num1_idx >= 0 or num2_idx >= 0:
            num1_digi = int(num1[num1_idx]) if num1_idx >= 0 else 0
            num2_digi = int(num2[num2_idx]) if num2_idx >= 0 else 0
            
            new_val = num1_digi + num2_digi + carry
            if new_val > 9:
                carry = 1
                new_val-=10
            else:
                carry = 0
            
            result = str(new_val) + result
            num1_idx-=1
            num2_idx-=1
        if carry:
            result = "1" + result
        
        return result
