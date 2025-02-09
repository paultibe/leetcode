class Solution:
    def countBits(self, n: int) -> List[int]:
        # n = 3
        # [0, 1, 1, 2]
        # 0, 1, 10, 11
        # count ones for each value in range 0 to n (inclusive)

        # 111
        # 110
        result = []
        for i in range(n + 1):
            result.append(bin(i).count("1"))
        return result
        
