from typing import List

class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        max_side = 0
        n = len(bottomLeft)

        for i in range(n):
            for j in range(i + 1, n):
                w = min(topRight[i][0], topRight[j][0]) - max(bottomLeft[i][0], bottomLeft[j][0])
                
                h = min(topRight[i][1], topRight[j][1]) - max(bottomLeft[i][1], bottomLeft[j][1])

                max_side = max(max_side, min(w, h))

        return max_side * max_side