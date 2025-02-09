class Solution:
    def countBits(self, n: int) -> List[int]:
        # n = 3
        # [0, 1, 1, 2]
        # 0, 1, 10, 11
        # count ones for each value in range 0 to n (inclusive)
        result = []
        for i in range(n + 1):
            num = i
            count = 0
            while (num):
                # check if odd (least significant bit is 1)
                if num % 2 == 1:
                    count += 1
                num = num >> 1 # or divide num by two
            result.append(count)
        
        return result
