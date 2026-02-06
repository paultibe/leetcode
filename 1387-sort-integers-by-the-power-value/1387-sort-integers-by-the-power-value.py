class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache
        def getPowerValue(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return 1 + getPowerValue(num // 2)
            else:
                return 1 + getPowerValue(3 * num + 1)

        power_list = [(getPowerValue(i), i) for i in range(lo, hi + 1)]

        power_list.sort()
        
        return power_list[k-1][1]