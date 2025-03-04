# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # target = isBadVersion(i) (not a number)
        # 0, 1, 2, 3, 4, 5
        left, right = 0, n
        while left <= right:
            mid = left + ((right - left) // 2)
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        