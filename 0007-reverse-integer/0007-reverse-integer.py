class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1 # 2147483647, -2147483648
        
        sign = -1 if x < 0 else 1
        remaining_digits = abs(x)
        reversed_val = 0
        
        while remaining_digits:
            if reversed_val > MAX_INT // 10:
                return 0
            
            # if they are equal, check if the last digit pushes it over
            if reversed_val == MAX_INT // 10:
                pop = remaining_digits % 10
                if sign == 1 and pop > 7: return 0
                if sign == -1 and pop > 8: return 0

            reversed_val = (reversed_val * 10) + (remaining_digits % 10)
            remaining_digits //= 10
            
        return sign * reversed_val