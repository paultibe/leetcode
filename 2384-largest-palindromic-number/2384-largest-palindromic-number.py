class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = Counter(num)
        DIGITS = "9876543210"
        frontArray = []
        # greedily try including largest
        for digit in DIGITS:            
            if digit == '0' and not frontArray:
                continue
            
            count = counts[digit]
            num_pairs = count // 2
            if num_pairs > 0:
                frontArray.append(digit * num_pairs)
                counts[digit] -= (num_pairs * 2)
            
        left_str = "".join(frontArray)
        
        middle = ""
        for digit in DIGITS:
            if counts[digit] > 0:
                middle = digit
                break
                
        if not left_str:
            if middle:
                return middle

        return left_str + middle + left_str[::-1]