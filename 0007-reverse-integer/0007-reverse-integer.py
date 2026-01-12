class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        
        res_str = str(abs(x))[::-1]
        res_int = int(res_str) * sign
        
        if res_int < INT_MIN or res_int > INT_MAX:
            return 0
            
        return res_int