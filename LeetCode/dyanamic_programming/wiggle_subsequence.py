class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n, up_bool, down_bool, up, down = len(nums), True, True, 1, 1
        if n < 2: 
            return n
        
        def adjust_vals(bool_, prev, curr, is_up, val):
            if is_up:
                u = 1 if bool_ and curr > prev else 0
                d = 1 if not bool_ and curr < prev else 0
            else:
                u = 1 if bool_ and curr < prev else 0
                d = 1 if not bool_ and curr > prev else 0
            return val+u+d, not bool_ if u or d else bool_
        
        for i in range(1, n):
            up, up_bool = adjust_vals(up_bool, nums[i-1], nums[i], True, up) 
            down, down_bool = adjust_vals(down_bool, nums[i-1], nums[i], False, down) 
            
        return max(down, up)